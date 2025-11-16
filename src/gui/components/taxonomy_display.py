"""Taxonomy code display component."""

import tkinter as tk
from tkinter import ttk
from typing import List
from ...mapping.cpt_mapper import ProcedureSpecialtyMapper


class TaxonomyDisplay:
    """Display component for taxonomy codes mapped from CPT."""
    
    def __init__(self, parent):
        """Initialize the taxonomy display.
        
        Args:
            parent: Parent widget
        """
        self.parent = parent
        self.mapper = ProcedureSpecialtyMapper()
        
        # Create frame
        self.frame = ttk.Frame(parent)
        
        self.label = ttk.Label(self.frame, text="Mapped Taxonomy:")
        self.label.grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        
        self.taxonomy_text = tk.Text(
            self.frame,
            height=4,
            wrap=tk.WORD,
            state=tk.DISABLED,
            font=("TkDefaultFont", 9)
        )
        self.taxonomy_text.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
        scrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.taxonomy_text.yview)
        scrollbar.grid(row=1, column=1, sticky=(tk.N, tk.S))
        self.taxonomy_text.config(yscrollcommand=scrollbar.set)
        
        self.frame.columnconfigure(0, weight=1)
    
    def update_from_cpt(self, cpt_code: str):
        """Update display based on CPT code.
        
        Args:
            cpt_code: CPT procedure code
        """
        taxonomy_codes = self.mapper.map(cpt_code)
        
        self.taxonomy_text.config(state=tk.NORMAL)
        self.taxonomy_text.delete(1.0, tk.END)
        
        if taxonomy_codes:
            lines = []
            for tax_code in taxonomy_codes:
                specialty_name = self.mapper.get_taxonomy_name(tax_code)
                lines.append(f"• {specialty_name} ({tax_code})")
            self.taxonomy_text.insert(1.0, "\n".join(lines))
        else:
            self.taxonomy_text.insert(1.0, "No taxonomy codes found")
        
        self.taxonomy_text.config(state=tk.DISABLED)
    
    def clear(self):
        """Clear the display."""
        self.taxonomy_text.config(state=tk.NORMAL)
        self.taxonomy_text.delete(1.0, tk.END)
        self.taxonomy_text.config(state=tk.DISABLED)
    
    def grid(self, **kwargs):
        """Grid the component frame."""
        self.frame.grid(**kwargs)

