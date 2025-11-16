"""Main GUI window for NPPES GeoSearch application."""

import tkinter as tk
from tkinter import ttk
from typing import Optional


class MainWindow:
    """Main application window."""
    
    def __init__(self, root: tk.Tk):
        """Initialize the main window.
        
        Args:
            root: Tkinter root window
        """
        self.root = root
        self.root.title("NPPES GeoSearch")
        self.root.geometry("1000x700")
        
        # Create main container
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(2, weight=1)
        
        # Search configuration section
        self.config_frame = ttk.LabelFrame(self.main_frame, text="Search Configuration", padding="10")
        self.config_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        self.config_frame.columnconfigure(1, weight=1)
        
        # Results section
        self.results_frame = ttk.LabelFrame(self.main_frame, text="Provider Results", padding="10")
        self.results_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.results_frame.columnconfigure(0, weight=1)
        self.results_frame.rowconfigure(1, weight=1)
        
        # Placeholder for components (will be set by application)
        self.cpt_selector = None
        self.zip_input = None
        self.taxonomy_display = None
        self.provider_list = None
    
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

