"""ZIP code input component with neighbors display."""

import tkinter as tk
from tkinter import ttk
from typing import Optional, Callable, List
from ...geo.zip_neighbors import load_zip_neighbors, get_search_set


class ZIPInput:
    """ZIP code input with neighbors display."""
    
    def __init__(self, parent, on_change: Optional[Callable] = None):
        """Initialize the ZIP input component.
        
        Args:
            parent: Parent widget
            on_change: Optional callback when ZIP code changes
        """
        self.parent = parent
        self.on_change = on_change
        self.neighbors_data = {}
        self.include_neighbors = True
        
        # Load neighbors data
        try:
            self.neighbors_data = load_zip_neighbors()
        except FileNotFoundError as e:
            # If file not found, use empty dict
            print(f"Warning: ZIP neighbors file not found: {e}")
            print("  Neighbor search will be limited. Place zip_neighbors_20mi.json in data/ directory.")
        except Exception as e:
            print(f"Warning: Error loading ZIP neighbors: {e}")
            self.neighbors_data = {}
        
        # Create frame
        self.frame = ttk.Frame(parent)
        
        # ZIP input row
        input_frame = ttk.Frame(self.frame)
        input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 5))
        input_frame.columnconfigure(1, weight=1)
        
        self.label = ttk.Label(input_frame, text="ZIP Code:")
        self.label.grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
        
        self.zip_var = tk.StringVar()
        self.zip_entry = ttk.Entry(input_frame, textvariable=self.zip_var, width=15)
        self.zip_entry.grid(row=0, column=1, sticky=tk.W, padx=(0, 10))
        self.zip_entry.bind("<KeyRelease>", self._on_zip_change)
        
        self.neighbors_var = tk.BooleanVar(value=True)
        self.neighbors_check = ttk.Checkbutton(
            input_frame,
            text="Include Neighbors",
            variable=self.neighbors_var,
            command=self._on_neighbors_toggle
        )
        self.neighbors_check.grid(row=0, column=2, sticky=tk.W)
        
        # Update include_neighbors from checkbox state
        self.include_neighbors = self.neighbors_var.get()
        
        # Neighbors display
        self.neighbors_label = ttk.Label(
            self.frame,
            text="Enter a ZIP code to see neighbors",
            foreground="gray"
        )
        self.neighbors_label.grid(row=1, column=0, sticky=tk.W, pady=(5, 0))
        
        self.frame.columnconfigure(0, weight=1)
    
    def _on_zip_change(self, event=None):
        """Handle ZIP code input change."""
        zip_code = self.zip_var.get().strip()
        self._update_neighbors_display(zip_code)
        if self.on_change:
            self.on_change(zip_code)
    
    def _on_neighbors_toggle(self):
        """Handle neighbors checkbox toggle."""
        self.include_neighbors = self.neighbors_var.get()
        zip_code = self.zip_var.get().strip()
        self._update_neighbors_display(zip_code)
    
    def _update_neighbors_display(self, zip_code: str):
        """Update the neighbors display label."""
        if not zip_code or len(zip_code) < 5:
            self.neighbors_label.config(text="Enter a ZIP code to see neighbors", foreground="gray")
            return
        
        zip_code = zip_code[:5]  # Take first 5 digits
        
        try:
            search_set = get_search_set(zip_code, self.neighbors_data, self.include_neighbors)
            origin = search_set[0] if search_set else zip_code
            neighbors = search_set[1:] if len(search_set) > 1 else []
            
            if neighbors:
                neighbors_str = ", ".join(neighbors[:10])
                if len(neighbors) > 10:
                    neighbors_str += f", ... (+{len(neighbors) - 10} more)"
                text = f"Origin: {origin} | Neighbors: {neighbors_str} | Total: {len(search_set)} ZIP codes"
            else:
                text = f"Origin: {origin} | No neighbors found | Total: 1 ZIP code"
            
            self.neighbors_label.config(text=text, foreground="black")
        except Exception:
            self.neighbors_label.config(
                text=f"Origin: {zip_code} | Neighbors: (error loading)",
                foreground="orange"
            )
    
    def get_zip_code(self) -> Optional[str]:
        """Get the entered ZIP code.
        
        Returns:
            5-digit ZIP code string or None if invalid
        """
        zip_code = self.zip_var.get().strip()[:5]
        if len(zip_code) == 5 and zip_code.isdigit():
            return zip_code
        return None
    
    def get_search_set(self) -> List[str]:
        """Get the list of ZIP codes to search.
        
        Returns:
            List of ZIP codes (origin first, then neighbors)
        """
        zip_code = self.get_zip_code()
        if not zip_code:
            return []
        
        # Ensure checkbox state is synced
        self.include_neighbors = self.neighbors_var.get()
        
        search_set = get_search_set(zip_code, self.neighbors_data, self.include_neighbors)
        neighbors_found = len(search_set) - 1  # Subtract 1 for origin ZIP
        
        if self.include_neighbors and neighbors_found == 0 and zip_code not in self.neighbors_data:
            print(f"WARNING: No neighbor data found for ZIP {zip_code} in neighbors file")
            print(f"  Only searching origin ZIP. Add neighbor data to data/zip_neighbors_20mi.json")
        
        print(f"DEBUG ZIPInput: ZIP {zip_code}, include_neighbors={self.include_neighbors}, neighbors_found={neighbors_found}")
        print(f"DEBUG ZIPInput: Search set: {search_set}")
        return search_set
    
    def grid(self, **kwargs):
        """Grid the component frame."""
        self.frame.grid(**kwargs)

