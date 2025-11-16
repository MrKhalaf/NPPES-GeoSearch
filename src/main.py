"""Main entry point for NPPES GeoSearch application."""

import tkinter as tk
from tkinter import ttk, messagebox
import threading
from typing import List, Set

from .gui.main_window import MainWindow
from .gui.components.cpt_selector import CPTSelector
from .gui.components.zip_input import ZIPInput
from .gui.components.taxonomy_display import TaxonomyDisplay
from .gui.components.provider_list import ProviderList
from .gui.components.logs_view import LogsView
from .nppes.client import NPPESClient
from .nppes.models import Provider
from .mapping.cpt_mapper import ProcedureSpecialtyMapper
from .utils.progress import ProgressBar, print_step


class NPPESGeoSearchApp:
    """Main application class."""
    
    def __init__(self, root: tk.Tk):
        """Initialize the application.
        
        Args:
            root: Tkinter root window
        """
        self.root = root
        self.main_window = MainWindow(root)
        
        # Initialize components
        self.cpt_selector = CPTSelector(
            self.main_window.config_frame,
            on_change=self._on_cpt_change
        )
        self.cpt_selector.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.zip_input = ZIPInput(
            self.main_window.config_frame,
            on_change=self._on_zip_change
        )
        self.zip_input.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.taxonomy_display = TaxonomyDisplay(self.main_window.config_frame)
        self.taxonomy_display.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Search controls
        self.controls_frame = ttk.Frame(self.main_window.config_frame)
        self.controls_frame.grid(row=3, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.search_button = ttk.Button(
            self.controls_frame,
            text="Search Providers",
            command=self._on_search_clicked
        )
        self.search_button.grid(row=0, column=0, padx=(0, 5))
        
        self.clear_button = ttk.Button(
            self.controls_frame,
            text="Clear Results",
            command=self._on_clear_clicked
        )
        self.clear_button.grid(row=0, column=1, padx=(0, 5))
        
        self.progress_label = ttk.Label(self.controls_frame, text="")
        self.progress_label.grid(row=0, column=2, padx=(10, 0))
        
        # Provider list
        self.provider_list = ProviderList(self.main_window.results_frame)
        self.provider_list.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Logs view
        self.logs_view = LogsView(self.main_window.logs_frame)
        self.logs_view.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.main_window.logs_frame.rowconfigure(0, weight=1)
        
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
            messagebox.showwarning("Search in Progress", "A search is already in progress.")
            return
        
        cpt_code = self.cpt_selector.get_selected_cpt()
        if not cpt_code:
            messagebox.showwarning("Missing CPT Code", "Please select a CPT code.")
            return
        
        zip_codes = self.zip_input.get_search_set()
        if not zip_codes:
            messagebox.showwarning("Invalid ZIP Code", "Please enter a valid 5-digit ZIP code.")
            return
        
        # Start search in background thread
        self.is_searching = True
        self.search_button.config(state=tk.DISABLED)
        self.progress_label.config(text="Searching...")
        
        self.search_thread = threading.Thread(
            target=self._perform_search,
            args=(cpt_code, zip_codes),
            daemon=True
        )
        self.search_thread.start()
    
    def _perform_search(self, cpt_code: str, zip_codes: List[str]):
        """Perform the NPPES search.
        
        Args:
            cpt_code: CPT procedure code
            zip_codes: List of ZIP codes to search
        """
        try:
            # Print initial step
            print_step("Starting search", f"CPT: {cpt_code}, ZIP codes: {len(zip_codes)}")
            
            # Get taxonomy codes for CPT and convert to descriptions
            taxonomy_codes = self.cpt_mapper.map(cpt_code)
            taxonomy_descriptions = self.cpt_mapper.get_taxonomy_descriptions(taxonomy_codes) if taxonomy_codes else []
            print_step("Mapped taxonomy codes", f"Found {len(taxonomy_codes)} taxonomy code(s)")
            
            # Log to GUI
            self.root.after(0, lambda: self.logs_view.log(f"Starting search: CPT {cpt_code}, {len(zip_codes)} ZIP code(s), {len(taxonomy_descriptions)} taxonomy(ies)"))
            
            # Clear previous results
            self.root.after(0, self.provider_list.clear)
            
            all_providers: List[Provider] = []
            seen_npis: Set[str] = set()
            
            total_zips = len(zip_codes)
            total_taxonomies = len(taxonomy_descriptions) if taxonomy_descriptions else 1
            total_searches = total_zips * total_taxonomies
            
            # Create progress bar
            progress = ProgressBar(total_searches, desc="Searching providers")
            
            # Log callback function
            def log_callback(message: str):
                self.root.after(0, lambda m=message: self.logs_view.log(m))
            
            # Search each ZIP code
            for zip_idx, zip_code in enumerate(zip_codes):
                # Update GUI progress
                progress_text = f"Searching ZIP {zip_idx + 1}/{total_zips}: {zip_code}"
                self.root.after(0, lambda t=progress_text: self.progress_label.config(text=t))
                
                # Search with each taxonomy description
                search_taxonomies = taxonomy_descriptions if taxonomy_descriptions else [None]
                for tax_idx, taxonomy_description in enumerate(search_taxonomies):
                    tax_display = taxonomy_description or "all taxonomies"
                    progress.update(1, f"ZIP {zip_code} ({tax_display})")
                    
                    try:
                        providers = self.nppes_client.search_providers(
                            zip_code=zip_code,
                            taxonomy_description=taxonomy_description,
                            limit=20,
                            entity_type="1",  # Individuals only
                            log_callback=log_callback
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
                            self.root.after(0, lambda z=zip_code, t=tax_display, c=new_count: 
                                          self.logs_view.log(f"ZIP {z} ({t}): Found {c} new providers", "SUCCESS"))
                        
                    except Exception as e:
                        # Log error but continue searching
                        error_msg = f"Error searching {zip_code} with taxonomy {taxonomy_description}: {e}"
                        print(f"  {error_msg}")
                        self.root.after(0, lambda m=error_msg: self.logs_view.log(m, "ERROR"))
                
                # Update results incrementally
                self.root.after(0, lambda p=all_providers.copy(): self.provider_list.set_providers(p))
            
            # Finish progress bar
            progress.finish(f"Complete - Found {len(all_providers)} total providers")
            print_step("Search complete", f"Total unique providers: {len(all_providers)}")
            
            # Final update
            self.root.after(0, lambda: self._search_complete(all_providers))
            
        except Exception as e:
            error_msg = f"Search failed: {str(e)}"
            print(f"ERROR: {error_msg}")
            self.root.after(0, lambda: self._search_error(error_msg))
    
    def _search_complete(self, providers: List[Provider]):
        """Handle search completion.
        
        Args:
            providers: List of found providers
        """
        self.is_searching = False
        self.search_button.config(state=tk.NORMAL)
        self.progress_label.config(text=f"Search complete. Found {len(providers)} providers.")
        
        if not providers:
            messagebox.showinfo("No Results", "No providers found matching the search criteria.")
    
    def _search_error(self, error_msg: str):
        """Handle search error.
        
        Args:
            error_msg: Error message
        """
        self.is_searching = False
        self.search_button.config(state=tk.NORMAL)
        self.progress_label.config(text="Search failed")
        messagebox.showerror("Search Error", error_msg)
    
    def _on_clear_clicked(self):
        """Handle clear button click."""
        self.provider_list.clear()
        self.progress_label.config(text="")
    
    def run(self):
        """Run the application."""
        self.root.mainloop()
    
    def cleanup(self):
        """Cleanup resources."""
        if self.nppes_client:
            self.nppes_client.close()


def main():
    """Main entry point."""
    print("Starting NPPES GeoSearch application...")
    print("Loading GUI components...")
    
    root = tk.Tk()
    
    # Bring window to front
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)
    
    print("Initializing application...")
    app = NPPESGeoSearchApp(root)
    
    # Force window to render immediately
    root.update_idletasks()
    root.update()
    
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

