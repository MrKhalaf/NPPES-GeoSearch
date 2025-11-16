"""CPT code selector dropdown component."""

import tkinter as tk
from tkinter import ttk
from typing import Optional, Callable
from ...mapping.cpt_mapper import ProcedureSpecialtyMapper


class CPTSelector:
    """Searchable dropdown for selecting CPT codes."""
    
    def __init__(self, parent, on_change: Optional[Callable] = None):
        """Initialize the CPT selector.
        
        Args:
            parent: Parent widget
            on_change: Optional callback when CPT code changes
        """
        self.parent = parent
        self.on_change = on_change
        self.mapper = ProcedureSpecialtyMapper()
        self.cpt_codes = self.mapper.get_all_cpt_codes()
        
        # Create frame
        self.frame = ttk.Frame(parent)
        
        # Label
        self.label = ttk.Label(self.frame, text="CPT Code:")
        self.label.grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
        
        # Combobox with search
        self.selected_cpt = tk.StringVar()
        self.combo = ttk.Combobox(
            self.frame,
            textvariable=self.selected_cpt,
            values=[f"{code} - {desc}" for code, desc in self.cpt_codes.items()],
            state="readonly",
            width=60
        )
        self.combo.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 5))
        self.combo.bind("<<ComboboxSelected>>", self._on_selection_change)
        
        # Selected value display
        self.value_label = ttk.Label(self.frame, text="", font=("TkDefaultFont", 9, "bold"))
        self.value_label.grid(row=1, column=1, sticky=tk.W, pady=(5, 0))
        
        self.frame.columnconfigure(1, weight=1)
    
    def _on_selection_change(self, event=None):
        """Handle CPT code selection change."""
        selection = self.combo.get()
        if selection and " - " in selection:
            cpt_code = selection.split(" - ")[0]
            self.value_label.config(text=f"Selected: {cpt_code}")
            if self.on_change:
                self.on_change(cpt_code)
    
    def get_selected_cpt(self) -> Optional[str]:
        """Get the currently selected CPT code.
        
        Returns:
            CPT code string or None if nothing selected
        """
        selection = self.combo.get()
        if selection and " - " in selection:
            return selection.split(" - ")[0]
        return None
    
    def grid(self, **kwargs):
        """Grid the component frame."""
        self.frame.grid(**kwargs)

