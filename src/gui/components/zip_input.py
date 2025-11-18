"""ZIP code input component with neighbors display using PyQt6."""

from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QCheckBox
from PyQt6.QtCore import Qt, pyqtSignal
from typing import Optional, Callable, List
from ...geo.zip_neighbors import get_search_set
from ..theme import MacOSTheme


class ZIPInput(QWidget):
    """ZIP code input with neighbors display."""
    
    zip_changed = pyqtSignal(str)
    
    def __init__(self, parent=None, on_change: Optional[Callable] = None):
        """Initialize the ZIP input component.
        
        Args:
            parent: Parent widget
            on_change: Optional callback when ZIP code changes
        """
        super().__init__(parent)
        self.on_change = on_change
        self.include_neighbors = True
        
        # Main layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(MacOSTheme.SPACING['sm'])
        
        # Input row
        input_layout = QHBoxLayout()
        input_layout.setSpacing(MacOSTheme.SPACING['md'])
        
        # Label
        self.label = QLabel("ZIP Code")
        self.label.setFont(MacOSTheme.get_font('field_label'))
        self.label.setStyleSheet(f"""
            color: {MacOSTheme.COLORS['text_primary']};
            background-color: {MacOSTheme.COLORS['surface']};
        """)
        input_layout.addWidget(self.label)
        
        # ZIP input
        self.zip_entry = QLineEdit()
        self.zip_entry.setPlaceholderText("Enter 5-digit ZIP code")
        self.zip_entry.setMaxLength(5)
        self.zip_entry.setFixedWidth(120)
        self.zip_entry.textChanged.connect(self._on_zip_change)
        input_layout.addWidget(self.zip_entry)
        
        # Neighbors checkbox
        self.neighbors_check = QCheckBox("Include Neighbors")
        self.neighbors_check.setChecked(True)
        self.neighbors_check.toggled.connect(self._on_neighbors_toggle)
        input_layout.addWidget(self.neighbors_check)
        
        input_layout.addStretch()
        layout.addLayout(input_layout)
        
        # Neighbors display
        self.neighbors_label = QLabel("Enter a ZIP code to see neighbors")
        self.neighbors_label.setProperty("class", "caption")
        self.neighbors_label.setFont(MacOSTheme.get_font('caption'))
        self.neighbors_label.setStyleSheet(f"""
            color: {MacOSTheme.COLORS['text_secondary']};
            background-color: {MacOSTheme.COLORS['surface']};
        """)
        layout.addWidget(self.neighbors_label)
    
    def _on_zip_change(self, text: str):
        """Handle ZIP code input change."""
        zip_code = text.strip()
        self._update_neighbors_display(zip_code)
        self.zip_changed.emit(zip_code)
        if self.on_change:
            self.on_change(zip_code)
    
    def _on_neighbors_toggle(self, checked: bool):
        """Handle neighbors checkbox toggle."""
        self.include_neighbors = checked
        zip_code = self.zip_entry.text().strip()
        self._update_neighbors_display(zip_code)
    
    def _update_neighbors_display(self, zip_code: str):
        """Update the neighbors display label."""
        if not zip_code or len(zip_code) < 5:
            self.neighbors_label.setText("Enter a ZIP code to see neighbors")
            self.neighbors_label.setStyleSheet(f"color: {MacOSTheme.COLORS['text_secondary']};")
            return
        
        zip_code = zip_code[:5]  # Take first 5 digits
        
        try:
            # Limit to 30 neighbors to avoid too many API calls
            search_set = get_search_set(zip_code, self.include_neighbors, radius_miles=20.0, max_neighbors=30)
            origin = search_set[0] if search_set else zip_code
            neighbors = search_set[1:] if len(search_set) > 1 else []
            
            if neighbors:
                neighbors_str = ", ".join(neighbors[:10])
                if len(neighbors) > 10:
                    neighbors_str += f", ... (+{len(neighbors) - 10} more)"
                text = f"Origin: {origin} • Neighbors: {neighbors_str} • Total: {len(search_set)} ZIP codes"
            else:
                if self.include_neighbors:
                    text = f"Origin: {origin} • Searching for neighbors... • Total: 1 ZIP code"
                else:
                    text = f"Origin: {origin} • Neighbors disabled • Total: 1 ZIP code"
            
            self.neighbors_label.setText(text)
            self.neighbors_label.setStyleSheet(f"color: {MacOSTheme.COLORS['text_primary']};")
        except Exception as e:
            self.neighbors_label.setText(
                f"Origin: {zip_code} • Error loading neighbors: {str(e)[:50]}"
            )
            self.neighbors_label.setStyleSheet(f"color: {MacOSTheme.COLORS['warning']};")
    
    def get_zip_code(self) -> Optional[str]:
        """Get the entered ZIP code.
        
        Returns:
            5-digit ZIP code string or None if invalid
        """
        zip_code = self.zip_entry.text().strip()[:5]
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
        self.include_neighbors = self.neighbors_check.isChecked()
        
        # Limit to 30 neighbors to avoid too many API calls
        search_set = get_search_set(zip_code, self.include_neighbors, radius_miles=20.0, max_neighbors=30)
        return search_set
