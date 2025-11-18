"""Taxonomy code display component using PyQt6."""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit
from typing import List
from ...mapping.cpt_mapper import ProcedureSpecialtyMapper
from ..theme import MacOSTheme


class TaxonomyDisplay(QWidget):
    """Display component for taxonomy codes mapped from CPT."""
    
    def __init__(self, parent=None):
        """Initialize the taxonomy display.
        
        Args:
            parent: Parent widget
        """
        super().__init__(parent)
        self.mapper = ProcedureSpecialtyMapper()
        
        # Main layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(MacOSTheme.SPACING['sm'])
        
        # Label
        self.label = QLabel("Mapped Taxonomy")
        self.label.setFont(MacOSTheme.get_font('field_label'))
        self.label.setStyleSheet(f"""
            color: {MacOSTheme.COLORS['text_primary']};
            background-color: {MacOSTheme.COLORS['surface']};
        """)
        layout.addWidget(self.label)
        
        # Text widget
        self.taxonomy_text = QTextEdit()
        self.taxonomy_text.setReadOnly(True)
        self.taxonomy_text.setMinimumHeight(100)
        self.taxonomy_text.setMaximumHeight(150)
        self.taxonomy_text.setPlaceholderText("Select a CPT code to see mapped taxonomy codes")
        # Ensure text is visible - use explicit colors
        self.taxonomy_text.setStyleSheet(f"""
            QTextEdit {{
                color: {MacOSTheme.COLORS['text_primary']} !important;
                background-color: {MacOSTheme.COLORS['input_bg']} !important;
                border: 1px solid {MacOSTheme.COLORS['input_border']};
                border-radius: 8px;
                padding: 10px;
            }}
        """)
        layout.addWidget(self.taxonomy_text)
    
    def update_from_cpt(self, cpt_code: str):
        """Update display based on CPT code.
        
        Args:
            cpt_code: CPT procedure code
        """
        if not cpt_code:
            self.taxonomy_text.clear()
            self.taxonomy_text.setPlaceholderText("Select a CPT code to see mapped taxonomy codes")
            return
            
        taxonomy_codes = self.mapper.map(cpt_code)
        self.taxonomy_text.clear()
        
        if taxonomy_codes:
            lines = []
            for tax_code in taxonomy_codes:
                specialty_name = self.mapper.get_taxonomy_name(tax_code)
                line = f"• {specialty_name} ({tax_code})"
                lines.append(line)
            text_content = "\n".join(lines)
            
            # Temporarily enable to set text, then disable again
            self.taxonomy_text.setReadOnly(False)
            self.taxonomy_text.setPlainText(text_content)
            self.taxonomy_text.setReadOnly(True)
            
            # Force update to ensure text is visible
            self.taxonomy_text.update()
            self.taxonomy_text.repaint()
            
            # Ensure text color is set
            self.taxonomy_text.setStyleSheet(f"""
                QTextEdit {{
                    color: {MacOSTheme.COLORS['text_primary']};
                    background-color: {MacOSTheme.COLORS['input_bg']};
                }}
            """)
        else:
            self.taxonomy_text.setPlainText("No taxonomy codes found")
            self.taxonomy_text.setStyleSheet(f"""
                QTextEdit {{
                    color: {MacOSTheme.COLORS['text_secondary']};
                    background-color: {MacOSTheme.COLORS['input_bg']};
                }}
            """)
    
    def clear(self):
        """Clear the display."""
        self.taxonomy_text.clear()
