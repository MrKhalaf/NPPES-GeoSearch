"""Main entry point for NPPES GeoSearch application."""

import sys
from PyQt6.QtWidgets import QApplication, QMessageBox, QHBoxLayout, QPushButton, QLabel, QVBoxLayout
from PyQt6.QtCore import QThread, pyqtSignal
from typing import List, Set

from .gui.main_window import MainWindow
from .gui.components.cpt_selector import CPTSelector
from .gui.components.zip_input import ZIPInput
from .gui.components.taxonomy_display import TaxonomyDisplay
from .gui.components.provider_list import ProviderList
from .gui.components.logs_view import LogsView
from .gui.theme import MacOSTheme
from .nppes.client import NPPESClient
from .nppes.models import Provider
from .mapping.cpt_mapper import ProcedureSpecialtyMapper
from .utils.progress import ProgressBar, print_step


class SearchThread(QThread):
    """Thread for performing NPPES search without blocking UI."""
    
    search_complete = pyqtSignal(list)
    search_error = pyqtSignal(str)
    progress_update = pyqtSignal(str)
    log_message = pyqtSignal(str, str)  # message, level
    providers_update = pyqtSignal(list)
    
    def __init__(self, cpt_code: str, zip_codes: List[str], nppes_client: NPPESClient, cpt_mapper: ProcedureSpecialtyMapper):
        """Initialize search thread.
        
        Args:
            cpt_code: CPT procedure code
            zip_codes: List of ZIP codes to search
            nppes_client: NPPES client instance
            cpt_mapper: CPT mapper instance
        """
        super().__init__()
        self.cpt_code = cpt_code
        self.zip_codes = zip_codes
        self.nppes_client = nppes_client
        self.cpt_mapper = cpt_mapper
    
    def run(self):
        """Perform the search."""
        try:
            # Print initial step
            print_step("Starting search", f"CPT: {self.cpt_code}, ZIP codes: {len(self.zip_codes)}")
            
            # Get taxonomy codes for CPT
            taxonomy_codes = self.cpt_mapper.map(self.cpt_code)
            taxonomy_descriptions = self.cpt_mapper.get_taxonomy_descriptions(taxonomy_codes) if taxonomy_codes else []
            print_step("Mapped taxonomy codes", f"Found {len(taxonomy_codes)} taxonomy code(s)")
            
            # Log to GUI
            self.log_message.emit(
                f"Starting search: CPT {self.cpt_code}, {len(self.zip_codes)} ZIP code(s), {len(taxonomy_codes)} taxonomy(ies)",
                "INFO"
            )
            
            all_providers: List[Provider] = []
            seen_npis: Set[str] = set()
            
            total_zips = len(self.zip_codes)
            total_taxonomies = len(taxonomy_codes) if taxonomy_codes else 1
            total_searches = total_zips * total_taxonomies
            
            # Create progress bar
            progress = ProgressBar(total_searches, desc="Searching providers")
            
            # Search each ZIP code
            for zip_idx, zip_code in enumerate(self.zip_codes):
                # Update GUI progress
                progress_text = f"Searching ZIP {zip_idx + 1}/{total_zips}: {zip_code}"
                self.progress_update.emit(progress_text)
                
                # Search with each taxonomy description (API-accepted format)
                search_taxonomies = taxonomy_descriptions if taxonomy_descriptions else [None]
                for tax_idx, taxonomy_description in enumerate(search_taxonomies):
                    tax_display = taxonomy_description or "all taxonomies"
                    progress.update(1, f"ZIP {zip_code} ({tax_display})")
                    
                    try:
                        providers = self.nppes_client.search_providers(
                            zip_code=zip_code,
                            taxonomy_description=taxonomy_description,  # Use taxonomy_description parameter
                            limit=100,
                            entity_type="1",  # Individuals only
                            log_callback=lambda m: self.log_message.emit(m, "INFO")
                        )
                        
                        new_count = 0
                        # Deduplicate by NPI
                        for provider in providers:
                            if provider.npi not in seen_npis:
                                seen_npis.add(provider.npi)
                                all_providers.append(provider)
                                new_count += 1
                        
                        if new_count > 0:
                            print(f"  Found {len(providers)} providers ({new_count} new)")
                            self.log_message.emit(
                                f"ZIP {zip_code} ({tax_display}): Found {new_count} new providers",
                                "SUCCESS"
                            )
                        
                    except Exception as e:
                        # Log error but continue searching
                        tax_display_name = taxonomy_description or "all taxonomies"
                        error_msg = f"Error searching {zip_code} with taxonomy {taxonomy_description} ({tax_display_name}): {e}"
                        print(f"  {error_msg}")
                        self.log_message.emit(error_msg, "ERROR")
                
                # Update results incrementally
                self.providers_update.emit(all_providers.copy())
            
            # Finish progress bar
            progress.finish(f"Complete - Found {len(all_providers)} total providers")
            print_step("Search complete", f"Total unique providers: {len(all_providers)}")
            
            # Log final count
            self.log_message.emit(
                f"Search complete: {len(all_providers)} total unique providers",
                "SUCCESS"
            )
            
            # Emit final results
            self.search_complete.emit(all_providers)
            
        except Exception as e:
            error_msg = f"Search failed: {str(e)}"
            print(f"ERROR: {error_msg}")
            self.search_error.emit(error_msg)


class NPPESGeoSearchApp:
    """Main application class."""
    
    def __init__(self):
        """Initialize the application.""" 
        self.app = QApplication(sys.argv)
        
        # Set application style
        self.app.setStyle('Fusion')  # Use Fusion style for better cross-platform look
        
        # Create main window
        self.main_window = MainWindow()
        
        # Initialize components in config section
        self.cpt_selector = CPTSelector(on_change=self._on_cpt_change)
        self.main_window.config_layout.addWidget(self.cpt_selector)
        
        self.zip_input = ZIPInput(on_change=self._on_zip_change)
        self.main_window.config_layout.addWidget(self.zip_input)
        
        self.taxonomy_display = TaxonomyDisplay()
        self.main_window.config_layout.addWidget(self.taxonomy_display)
        
        # Search controls
        controls_layout = self.main_window.config_layout
        
        button_layout = QHBoxLayout()
        
        # Primary search button - dark blue
        self.search_button = QPushButton("Search Providers")
        self.search_button.setFont(MacOSTheme.get_font('body_bold'))
        self.search_button.setStyleSheet(f"""
            QPushButton {{
                background-color: {MacOSTheme.COLORS['accent']};
                color: white;
                border: none;
                border-radius: {MacOSTheme.RADIUS}px;
                padding: 12px 24px;
                font-weight: 600;
                font-size: 14px;
            }}
            QPushButton:hover {{
                background-color: {MacOSTheme.COLORS['accent_hover']};
            }}
            QPushButton:pressed {{
                background-color: {MacOSTheme.COLORS['accent_hover']};
            }}
            QPushButton:disabled {{
                background-color: #999999;
                color: white;
            }}
        """)
        self.search_button.clicked.connect(self._on_search_clicked)
        button_layout.addWidget(self.search_button)
        
        # Clear button - de-emphasized style
        self.clear_button = QPushButton("Clear Results")
        self.clear_button.setFont(MacOSTheme.get_font('body'))
        self.clear_button.setStyleSheet(f"""
            QPushButton {{
                background-color: {MacOSTheme.COLORS['surface']};
                color: {MacOSTheme.COLORS['text_secondary']};
                border: 1px solid {MacOSTheme.COLORS['border_light']};
                border-radius: {MacOSTheme.RADIUS}px;
                padding: 12px 24px;
                font-weight: 500;
                font-size: 14px;
            }}
            QPushButton:hover {{
                background-color: {MacOSTheme.COLORS['hover']};
                color: {MacOSTheme.COLORS['text_primary']};
            }}
            QPushButton:pressed {{
                background-color: {MacOSTheme.COLORS['border_light']};
            }}
        """)
        self.clear_button.clicked.connect(self._on_clear_clicked)
        button_layout.addWidget(self.clear_button)
        
        button_layout.addStretch()
        
        # Progress label
        self.progress_label = QLabel("")
        self.progress_label.setProperty("class", "caption")
        self.progress_label.setFont(MacOSTheme.get_font('caption'))
        self.progress_label.setStyleSheet(f"""
            color: {MacOSTheme.COLORS['text_secondary']};
            background-color: {MacOSTheme.COLORS['surface']};
        """)
        button_layout.addWidget(self.progress_label)
        
        controls_layout.addLayout(button_layout)
        
        # Provider list in results section
        self.provider_list = ProviderList()
        self.main_window.results_layout.addWidget(self.provider_list, stretch=1)
        
        # Logs view
        logs_layout = QVBoxLayout()
        logs_layout.setContentsMargins(0, 0, 0, 0)
        self.logs_view = LogsView()
        logs_layout.addWidget(self.logs_view)
        self.main_window.logs_frame.setLayout(logs_layout)
        
        # Initialize services
        self.nppes_client = NPPESClient()
        self.cpt_mapper = ProcedureSpecialtyMapper()
        
        # Search state
        self.is_searching = False
        self.search_thread = None
    
    def _on_cpt_change(self, cpt_code: str):
        """Handle CPT code selection change.
        
        Args:
            cpt_code: Selected CPT code
        """
        if cpt_code:
            self.taxonomy_display.update_from_cpt(cpt_code)
    
    def _on_zip_change(self, zip_code: str):
        """Handle ZIP code input change.
        
        Args:
            zip_code: Entered ZIP code
        """
        # ZIP input component handles its own display updates
        pass
    
    def _on_search_clicked(self):
        """Handle search button click."""
        if self.is_searching:
            QMessageBox.warning(self.main_window, "Search in Progress", "A search is already in progress.")
            return
        
        cpt_code = self.cpt_selector.get_selected_cpt()
        if not cpt_code:
            QMessageBox.warning(self.main_window, "Missing CPT Code", "Please select a CPT code.")
            return
        
        zip_codes = self.zip_input.get_search_set()
        if not zip_codes:
            QMessageBox.warning(self.main_window, "Invalid ZIP Code", "Please enter a valid 5-digit ZIP code.")
            return
        
        # Collapse config section immediately to give more space to results
        self.main_window.collapse_config()
        
        # Start search in background thread
        self.is_searching = True
        self.search_button.setEnabled(False)
        self.progress_label.setText("Searching...")
        
        # Clear previous results
        self.provider_list.clear()
        
        # Create and start search thread
        self.search_thread = SearchThread(
            cpt_code,
            zip_codes,
            self.nppes_client,
            self.cpt_mapper
        )
        self.search_thread.search_complete.connect(self._search_complete)
        self.search_thread.search_error.connect(self._search_error)
        self.search_thread.progress_update.connect(self._update_progress)
        self.search_thread.log_message.connect(self._on_log_message)
        self.search_thread.providers_update.connect(self._update_provider_list)
        self.search_thread.start()
    
    def _update_progress(self, text: str):
        """Update progress label.
        
        Args:
            text: Progress text
        """
        self.progress_label.setText(text)
    
    def _on_log_message(self, message: str, level: str):
        """Handle log message from search thread.
        
        Args:
            message: Log message
            level: Log level
        """
        self.logs_view.log(message, level)
    
    def _search_complete(self, providers: List[Provider]):
        """Handle search completion.
        
        Args:
            providers: List of found providers
        """
        self.is_searching = False
        self.search_button.setEnabled(True)
        self.progress_label.setText(f"Search complete. Found {len(providers)} providers.")
        
        # Collapse the config section to give more space to results
        self.main_window.collapse_config()
        
        if not providers:
            QMessageBox.information(self.main_window, "No Results", "No providers found matching the search criteria.")
    
    def _search_error(self, error_msg: str):
        """Handle search error.
        
        Args:
            error_msg: Error message
        """
        self.is_searching = False
        self.search_button.setEnabled(True)
        self.progress_label.setText("Search failed")
        QMessageBox.critical(self.main_window, "Search Error", error_msg)
    
    def _update_provider_list(self, providers: List[Provider]):
        """Update the provider list (called from search thread).
        
        Args:
            providers: List of Provider objects to display
        """
        self.provider_list.set_providers(providers)
    
    def _on_clear_clicked(self):
        """Handle clear button click."""
        self.provider_list.clear()
        self.progress_label.setText("")
        # Expand config section so user can reconfigure search
        self.main_window.expand_config()
    
    def run(self):
        """Run the application."""
        self.main_window.show()
        sys.exit(self.app.exec())
    
    def cleanup(self):
        """Cleanup resources."""
        if self.nppes_client:
            self.nppes_client.close()


def main():
    """Main entry point."""
    print("Starting NPPES GeoSearch application...")
    print("Loading GUI components...")
    
    app = NPPESGeoSearchApp()
    
    print("Application ready! GUI window should be visible.")
    print("Select a CPT code, enter a ZIP code, and click 'Search Providers' to begin.")
    
    try:
        app.run()
    except KeyboardInterrupt:
        print("\nApplication interrupted by user.")
    except Exception as e:
        print(f"\nERROR: Application crashed: {e}")
        import traceback
        traceback.print_exc()
    finally:
        print("Cleaning up...")
        app.cleanup()
        print("Application closed.")


if __name__ == "__main__":
    main()
