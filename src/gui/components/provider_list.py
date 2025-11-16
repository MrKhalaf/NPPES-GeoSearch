"""Provider results list component."""

import tkinter as tk
from tkinter import ttk
from typing import List, Optional
from ...nppes.models import Provider


class ProviderList:
    """Table/list component for displaying provider search results."""
    
    def __init__(self, parent, filter_physicians: bool = True):
        """Initialize the provider list.
        
        Args:
            parent: Parent widget
            filter_physicians: If True, filter to show only physicians (Individual entity type)
        """
        self.parent = parent
        self.filter_physicians = filter_physicians
        self.providers: List[Provider] = []
        
        # Create frame
        self.frame = ttk.Frame(parent)
        
        # Header with count
        header_frame = ttk.Frame(self.frame)
        header_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 5))
        header_frame.columnconfigure(1, weight=1)
        
        self.count_label = ttk.Label(header_frame, text="No results", font=("TkDefaultFont", 9, "bold"))
        self.count_label.grid(row=0, column=0, sticky=tk.W)
        
        self.filter_var = tk.BooleanVar(value=filter_physicians)
        self.filter_check = ttk.Checkbutton(
            header_frame,
            text="Physicians Only",
            variable=self.filter_var,
            command=self._on_filter_toggle
        )
        self.filter_check.grid(row=0, column=1, sticky=tk.E)
        
        # Treeview for results
        columns = ("NPI", "Name", "Specialty", "Taxonomy", "Phone", "ZIP")
        self.tree = ttk.Treeview(self.frame, columns=columns, show="headings", height=15)
        
        # Configure columns
        self.tree.heading("NPI", text="NPI")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Specialty", text="Specialty")
        self.tree.heading("Taxonomy", text="Taxonomy")
        self.tree.heading("Phone", text="Phone")
        self.tree.heading("ZIP", text="ZIP")
        
        self.tree.column("NPI", width=100)
        self.tree.column("Name", width=200)
        self.tree.column("Specialty", width=150)
        self.tree.column("Taxonomy", width=120)
        self.tree.column("Phone", width=120)
        self.tree.column("ZIP", width=80)
        
        # Scrollbars
        v_scrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.tree.yview)
        h_scrollbar = ttk.Scrollbar(self.frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        self.tree.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        v_scrollbar.grid(row=1, column=1, sticky=(tk.N, tk.S))
        h_scrollbar.grid(row=2, column=0, sticky=(tk.W, tk.E))
        
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
    
    def _on_filter_toggle(self):
        """Handle filter toggle."""
        self.filter_physicians = self.filter_var.get()
        self._refresh_display()
    
    def set_providers(self, providers: List[Provider]):
        """Set the providers to display.
        
        Args:
            providers: List of Provider objects
        """
        self.providers = providers
        self._refresh_display()
    
    def add_providers(self, providers: List[Provider]):
        """Add providers to the existing list (deduplicated by NPI).
        
        Args:
            providers: List of Provider objects to add
        """
        existing_npis = {p.npi for p in self.providers}
        new_providers = [p for p in providers if p.npi not in existing_npis]
        self.providers.extend(new_providers)
        self._refresh_display()
    
    def _refresh_display(self):
        """Refresh the treeview display."""
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Filter providers
        display_providers = self.providers
        if self.filter_physicians:
            display_providers = [p for p in self.providers if p.entity_type == "Individual"]
        
        # Add to treeview
        for provider in display_providers:
            self.tree.insert("", tk.END, values=(
                provider.npi,
                provider.name[:50] if provider.name else "",
                provider.specialty[:30] if provider.specialty else "",
                provider.taxonomy_code or "",
                provider.phone or "",
                provider.zip_code or ""
            ))
        
        # Update count
        total = len(self.providers)
        displayed = len(display_providers)
        if total == displayed:
            self.count_label.config(text=f"{displayed} result{'s' if displayed != 1 else ''}")
        else:
            self.count_label.config(text=f"{displayed} of {total} result{'s' if total != 1 else ''}")
    
    def clear(self):
        """Clear all providers."""
        self.providers = []
        self._refresh_display()
    
    def grid(self, **kwargs):
        """Grid the component frame."""
        self.frame.grid(**kwargs)

