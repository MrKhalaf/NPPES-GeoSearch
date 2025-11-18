"""CPT code selector dropdown component using PyQt6."""

from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QComboBox
from PyQt6.QtCore import Qt, pyqtSignal
from typing import Optional, Callable
from ...mapping.cpt_mapper import ProcedureSpecialtyMapper
from ..theme import MacOSTheme


class CPTSelector(QWidget):
    """Searchable dropdown for selecting CPT codes."""
    
    cpt_changed = pyqtSignal(str)
    
    def __init__(self, parent=None, on_change: Optional[Callable] = None):
        """Initialize the CPT selector.
        
        Args:
            parent: Parent widget
            on_change: Optional callback when CPT code changes
        """
        super().__init__(parent)
        self.on_change = on_change
        self.mapper = ProcedureSpecialtyMapper()
        self.cpt_codes = self.mapper.get_all_cpt_codes()
        self._last_selected_cpt = None  # Track last selected CPT to avoid duplicate updates
        
        # Main layout
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(MacOSTheme.SPACING['md'])
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)  # Left align contents
        
        # Label
        self.label = QLabel("CPT Code")
        self.label.setFont(MacOSTheme.get_font('field_label'))
        self.label.setStyleSheet(f"""
            color: {MacOSTheme.COLORS['text_primary']};
            background-color: {MacOSTheme.COLORS['surface']};
        """)
        layout.addWidget(self.label)
        
        # Combobox
        self.combo = QComboBox()
        self.combo.setEditable(True)
        self.combo.setMaximumWidth(400)  # Limit horizontal space
        # Style the combobox dropdown items for readability
        self.combo.setStyleSheet(f"""
            QComboBox {{
                background-color: {MacOSTheme.COLORS['input_bg']};
                border: 1px solid {MacOSTheme.COLORS['input_border']};
                border-radius: 8px;
                padding: 10px 14px;
                font-size: 14px;
                color: {MacOSTheme.COLORS['text_primary']};
            }}
            QComboBox:hover {{
                border: 1px solid {MacOSTheme.COLORS['accent']};
            }}
            QComboBox:focus {{
                border: 2px solid {MacOSTheme.COLORS['accent']};
                padding: 9px 13px;
            }}
            QComboBox QAbstractItemView {{
                background-color: {MacOSTheme.COLORS['surface']};
                border: 1px solid {MacOSTheme.COLORS['border']};
                border-radius: 8px;
                selection-background-color: {MacOSTheme.COLORS['accent_light']};
                selection-color: {MacOSTheme.COLORS['text_primary']};
                color: {MacOSTheme.COLORS['text_primary']};
                padding: 4px;
            }}
            QComboBox QAbstractItemView::item {{
                color: {MacOSTheme.COLORS['text_primary']};
                padding: 6px;
                min-height: 20px;
            }}
            QComboBox QAbstractItemView::item:selected {{
                background-color: {MacOSTheme.COLORS['accent_light']};
                color: {MacOSTheme.COLORS['text_primary']};
            }}
        """)
        line_edit = self.combo.lineEdit()
        line_edit.setPlaceholderText("Select or search for a CPT code...")
        line_edit.setReadOnly(False)
        
        # Add items
        for code, desc in self.cpt_codes.items():
            self.combo.addItem(f"{code} - {desc}", code)
        
        # Store all items for filtering
        self.all_items = [(f"{code} - {desc}", code) for code, desc in self.cpt_codes.items()]
        
        # Enable search filtering
        line_edit.textChanged.connect(self._filter_items)
        # Use activated signal (fires when user selects from dropdown)
        self.combo.activated.connect(self._on_selection_change)
        # Also connect currentIndexChanged for programmatic changes
        self.combo.currentIndexChanged.connect(self._on_selection_change)
        # Connect text editing finished to handle when user completes typing
        line_edit.editingFinished.connect(self._on_editing_finished)
        
        layout.addWidget(self.combo)
        layout.addStretch()  # Push everything to the left
    
    def _filter_items(self, text: str):
        """Filter combobox items based on search text."""
        # Don't filter if user is typing a selection (contains " - ")
        if " - " in text:
            # Check if this is a complete selection - if so, trigger selection change
            for item_text, code in self.all_items:
                if text == item_text:
                    # User selected this item, trigger selection change
                    self.combo.blockSignals(True)
                    # Find the item in the current combobox and set it
                    for i in range(self.combo.count()):
                        if self.combo.itemText(i) == item_text:
                            self.combo.setCurrentIndex(i)
                            break
                    else:
                        # Item not in current list, add it and select it
                        self.combo.addItem(item_text, code)
                        self.combo.setCurrentIndex(self.combo.count() - 1)
                    self.combo.blockSignals(False)
                    # Trigger selection change manually
                    self._on_selection_change(self.combo.currentIndex())
                    return
            return
        
        # Don't filter if text matches a complete item (user selected from dropdown)
        for item_text, code in self.all_items:
            if text == item_text:
                # User selected this item, don't filter
                return
        
        # Clear and repopulate with filtered items
        self.combo.blockSignals(True)
        current_text = self.combo.currentText()
        self.combo.clear()
        
        if not text:
            # Show all items
            for item_text, code in self.all_items:
                self.combo.addItem(item_text, code)
        else:
            # Filter items
            text_lower = text.lower()
            for item_text, code in self.all_items:
                if text_lower in item_text.lower():
                    self.combo.addItem(item_text, code)
        
        self.combo.blockSignals(False)
        
        # Show popup if there are items and user is typing
        if self.combo.count() > 0 and text:
            self.combo.showPopup()
    
    def _on_editing_finished(self):
        """Handle when user finishes editing the combobox text."""
        text = self.combo.currentText().strip()
        if not text:
            return
            
        # Check if the text matches a complete item
        for item_text, code in self.all_items:
            if text == item_text:
                # Find the item in the combobox and select it
                for i in range(self.combo.count()):
                    if self.combo.itemText(i) == item_text:
                        self.combo.setCurrentIndex(i)
                        self._on_selection_change(i)
                        return
                # If not found, add it and select it
                self.combo.addItem(item_text, code)
                self.combo.setCurrentIndex(self.combo.count() - 1)
                self._on_selection_change(self.combo.count() - 1)
                return
        
        # Check if text is just a CPT code (e.g., "99213")
        for item_text, code in self.all_items:
            if text == code:
                # Find the item in the combobox and select it
                for i in range(self.combo.count()):
                    if self.combo.itemData(i) == code:
                        self.combo.setCurrentIndex(i)
                        self._on_selection_change(i)
                        return
                # If not found, add it and select it
                self.combo.addItem(item_text, code)
                self.combo.setCurrentIndex(self.combo.count() - 1)
                self._on_selection_change(self.combo.count() - 1)
                return
    
    def _on_selection_change(self, index: int):
        """Handle CPT code selection change."""
        if index < 0:
            return
            
        # Try to get CPT code from itemData first
        cpt_code = self.combo.itemData(index)
        
        # If no itemData, try to extract from text
        if not cpt_code:
            text = self.combo.currentText()
            if " - " in text:
                cpt_code = text.split(" - ")[0].strip()
        
        if cpt_code and cpt_code != self._last_selected_cpt:
            self._last_selected_cpt = cpt_code
            # Make line edit read-only after selection to show selected value
            line_edit = self.combo.lineEdit()
            line_edit.setReadOnly(True)
            # Set cursor to beginning to show first characters of the text
            line_edit.setCursorPosition(0)
            # Emit signal and call callback to update taxonomy display
            self.cpt_changed.emit(cpt_code)
            if self.on_change:
                self.on_change(cpt_code)
    
    def get_selected_cpt(self) -> Optional[str]:
        """Get the currently selected CPT code.
        
        Returns:
            CPT code string or None if nothing selected
        """
        index = self.combo.currentIndex()
        if index >= 0:
            return self.combo.itemData(index)
        return None
