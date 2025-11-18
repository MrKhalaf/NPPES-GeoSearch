"""Main GUI window for NPPES GeoSearch application using PyQt6."""

from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QFrame, QPushButton, QHBoxLayout
from PyQt6.QtCore import Qt
from .theme import MacOSTheme


class MainWindow(QMainWindow):
    """Main application window with modern macOS design."""
    
    def __init__(self):
        """Initialize the main window."""
        super().__init__()
        self.setWindowTitle("NPPES GeoSearch")
        self.setGeometry(100, 100, 1400, 900)
        
        # Apply modern theme
        self.setStyleSheet(MacOSTheme.apply_style_sheet())
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setStyleSheet(f"background-color: {MacOSTheme.COLORS['background']};")
        
        # Main layout with generous padding
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(
            MacOSTheme.SPACING['xl'],
            MacOSTheme.SPACING['xl'],
            MacOSTheme.SPACING['xl'],
            MacOSTheme.SPACING['xl']
        )
        main_layout.setSpacing(MacOSTheme.SPACING['lg'])
        
        # Title section
        title_label = QLabel("NPPES GeoSearch")
        title_label.setProperty("class", "title")
        title_label.setFont(MacOSTheme.get_font('title'))
        title_label.setStyleSheet(f"""
            color: {MacOSTheme.COLORS['text_primary']};
            background-color: {MacOSTheme.COLORS['background']};
        """)
        main_layout.addWidget(title_label)
        
        subtitle_label = QLabel("Find healthcare providers by location and specialty")
        subtitle_label.setProperty("class", "caption")
        subtitle_label.setFont(MacOSTheme.get_font('caption'))
        subtitle_label.setStyleSheet(f"""
            color: {MacOSTheme.COLORS['text_secondary']};
            background-color: {MacOSTheme.COLORS['background']};
        """)
        main_layout.addWidget(subtitle_label)
        
        main_layout.addSpacing(MacOSTheme.SPACING['xxl'])
        
        # Search configuration section - modern card (white background)
        self.config_frame = QFrame()
        self.config_frame.setProperty("class", "card")
        self.config_frame.setStyleSheet(f"""
            QFrame[class="card"] {{
                background-color: {MacOSTheme.COLORS['surface']};
                border: 1px solid {MacOSTheme.COLORS['border_light']};
                border-radius: {MacOSTheme.RADIUS}px;
            }}
        """)
        
        config_layout = QVBoxLayout(self.config_frame)
        config_layout.setContentsMargins(
            MacOSTheme.SPACING['xl'],
            MacOSTheme.SPACING['xl'],
            MacOSTheme.SPACING['xl'],
            MacOSTheme.SPACING['xl']
        )
        config_layout.setSpacing(MacOSTheme.SPACING['lg'])
        
        # Header with title and toggle button
        header_layout = QHBoxLayout()
        
        # Toggle button - dark blue
        self.config_toggle_button = QPushButton("▼ Search Configuration")
        self.config_toggle_button.setFont(MacOSTheme.get_font('heading'))
        self.config_toggle_button.setStyleSheet(f"""
            QPushButton {{
                background-color: {MacOSTheme.COLORS['accent']};
                color: white;
                border: none;
                border-radius: {MacOSTheme.RADIUS}px;
                padding: 8px 16px;
                font-weight: 600;
            }}
            QPushButton:hover {{
                background-color: {MacOSTheme.COLORS['accent_hover']};
            }}
        """)
        self.config_toggle_button.clicked.connect(self._toggle_config)
        header_layout.addWidget(self.config_toggle_button)
        header_layout.addStretch()
        
        config_layout.addLayout(header_layout)
        
        # Content container for collapsible content
        self.config_content_widget = QWidget()
        self.config_content_widget.setStyleSheet(f"background-color: {MacOSTheme.COLORS['surface']};")
        self.config_content_layout = QVBoxLayout(self.config_content_widget)
        self.config_content_layout.setContentsMargins(0, 0, 0, 0)
        self.config_content_layout.setSpacing(MacOSTheme.SPACING['lg'])
        
        # Store inner layout for component placement
        self.config_layout = self.config_content_layout
        
        config_layout.addWidget(self.config_content_widget)
        
        # Track expansion state
        self.config_expanded = True
        
        main_layout.addWidget(self.config_frame)
        
        # Results section - modern card
        self.results_frame = QFrame()
        self.results_frame.setProperty("class", "card")
        self.results_frame.setStyleSheet(f"""
            QFrame[class="card"] {{
                background-color: {MacOSTheme.COLORS['surface']};
                border: 1px solid {MacOSTheme.COLORS['border_light']};
                border-radius: {MacOSTheme.RADIUS}px;
            }}
        """)
        
        results_layout = QVBoxLayout(self.results_frame)
        results_layout.setContentsMargins(
            MacOSTheme.SPACING['xl'],
            MacOSTheme.SPACING['xl'],
            MacOSTheme.SPACING['xl'],
            MacOSTheme.SPACING['xl']
        )
        results_layout.setSpacing(MacOSTheme.SPACING['lg'])
        
        results_title = QLabel("Provider Results")
        results_title.setFont(MacOSTheme.get_font('heading'))
        results_title.setStyleSheet(f"""
            color: {MacOSTheme.COLORS['text_primary']};
            background-color: {MacOSTheme.COLORS['surface']};
        """)
        results_layout.addWidget(results_title)
        
        self.results_layout = results_layout
        
        main_layout.addWidget(self.results_frame, stretch=1)
        
        # Logs section - modern card (grey background)
        self.logs_frame = QFrame()
        self.logs_frame.setProperty("class", "card")
        self.logs_frame.setStyleSheet(f"""
            QFrame[class="card"] {{
                background-color: {MacOSTheme.COLORS['background']};
                border: 1px solid {MacOSTheme.COLORS['border_light']};
                border-radius: {MacOSTheme.RADIUS}px;
            }}
        """)
        
        main_layout.addWidget(self.logs_frame)
        
        # Placeholder for components (will be set by application)
        self.cpt_selector = None
        self.zip_input = None
        self.taxonomy_display = None
        self.provider_list = None
    
    def _toggle_config(self):
        """Toggle the visibility of the config content."""
        self.config_expanded = not self.config_expanded
        
        if self.config_expanded:
            self.config_content_widget.show()
            self.config_toggle_button.setText("▼ Search Configuration")
        else:
            self.config_content_widget.hide()
            self.config_toggle_button.setText("▶ Search Configuration")
    
    def collapse_config(self):
        """Collapse the config section."""
        if self.config_expanded:
            self._toggle_config()
    
    def expand_config(self):
        """Expand the config section."""
        if not self.config_expanded:
            self._toggle_config()
    
    def set_cpt_selector(self, widget):
        """Set the CPT selector component."""
        self.cpt_selector = widget
    
    def set_zip_input(self, widget):
        """Set the ZIP input component."""
        self.zip_input = widget
    
    def set_taxonomy_display(self, widget):
        """Set the taxonomy display component."""
        self.taxonomy_display = widget
    
    def set_provider_list(self, widget):
        """Set the provider list component."""
        self.provider_list = widget
