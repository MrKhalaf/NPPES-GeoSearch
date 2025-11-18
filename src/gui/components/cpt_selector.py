"""CPT code selector dropdown component using PyQt6."""

from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QComboBox
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFocusEvent, QKeyEvent
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
        # Disable built-in completer to prevent interference with custom filtering
        self.combo.setCompleter(None)
        # Set insert policy to prevent Qt from auto-inserting/matching items
        self.combo.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
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
        
        # Store reference to line edit for signal management
        self.line_edit = line_edit
        
        # Enable search filtering - connect before other signals
        line_edit.textChanged.connect(self._filter_items)
        # Use activated signal (fires when user selects from dropdown)
        self.combo.activated.connect(self._on_selection_change)
        # Also connect currentIndexChanged for programmatic changes
        self.combo.currentIndexChanged.connect(self._on_selection_change)
        # Connect text editing finished to handle when user completes typing
        line_edit.editingFinished.connect(self._on_editing_finished)
        
        # Install event filter on line edit to catch key presses and focus events
        line_edit.installEventFilter(self)
        
        layout.addWidget(self.combo)
        layout.addStretch()  # Push everything to the left
    
    def eventFilter(self, obj, event):
        """Event filter to handle focus and key press events."""
        # Handle focus events on line edit (when user clicks directly on the text field)
        if obj == self.combo.lineEdit():
            if event.type() == event.Type.FocusIn:
                # Select all text when line edit receives focus so user can immediately type
                # Use QTimer to do this after the focus event completes
                from PyQt6.QtCore import QTimer
                QTimer.singleShot(0, lambda: self.combo.lineEdit().selectAll())
                
                # Ensure all items are available for filtering
                # Only repopulate if combobox is empty
                if self.combo.count() == 0:
                    self.combo.blockSignals(True)
                    for item_text, code in self.all_items:
                        self.combo.addItem(item_text, code)
                    self.combo.blockSignals(False)
                
                # Don't force show popup - let user click dropdown arrow if they want
                # The filtering will show popup automatically when they type
                return False
            
            if event.type() == event.Type.KeyPress:
                # Show popup immediately on first keystroke (if not already visible)
                if not self.combo.view().isVisible():
                    # Ensure all items are loaded before showing popup
                    if self.combo.count() == 0:
                        # Repopulate with all items if empty
                        self.combo.blockSignals(True)
                        for item_text, code in self.all_items:
                            self.combo.addItem(item_text, code)
                        self.combo.blockSignals(False)
                    if self.combo.count() > 0:
                        self.combo.showPopup()
                # Ensure currentIndex is -1 so Qt doesn't auto-match text to items
                # This must be done after the key press updates the text
                from PyQt6.QtCore import QTimer
                QTimer.singleShot(0, lambda: self.combo.setCurrentIndex(-1) if self.combo.currentIndex() >= 0 else None)
                # Don't return False - let the key press go through to update text
        
        return super().eventFilter(obj, event)
    
    def _filter_items(self, text: str):
        """Filter combobox items based on search text (substring search)."""
        # Ensure line edit is editable for searching
        line_edit = self.combo.lineEdit()
        line_edit.setReadOnly(False)
        
        # Use the text parameter (the new text from textChanged signal)
        # This is the text the user just typed, which is what we want to filter on
        user_text = text.strip() if text else ""
        
        # If text contains " - " and matches a complete item exactly, user selected it
        if " - " in user_text:
            for item_text, code in self.all_items:
                if user_text == item_text:
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
        
        # Temporarily disconnect textChanged to prevent recursion during filtering
        self.line_edit.textChanged.disconnect(self._filter_items)
        
        # Clear and repopulate with filtered items
        self.combo.blockSignals(True)
        self.combo.clear()
        
        # Now filter based on user's text
        if not user_text:
            # Show all items when search is empty
            for item_text, code in self.all_items:
                self.combo.addItem(item_text, code)
        else:
            # Filter items using case-insensitive substring search
            # Search in both the CPT code and description
            text_lower = user_text.lower()
            matched_count = 0
            for item_text, code in self.all_items:
                # Check if search text appears ANYWHERE in the full item text (code or description)
                # This is a true substring search - not prefix-only
                item_lower = item_text.lower()
                if text_lower in item_lower:
                    self.combo.addItem(item_text, code)
                    matched_count += 1
        
        # Set current index to -1 FIRST to prevent Qt from matching text to items
        # This must be done before setting the text
        self.combo.setCurrentIndex(-1)
        
        # Restore the exact text the user typed (clear() cleared it)
        line_edit.setText(user_text)
        
        # Move cursor to end so user can continue typing
        line_edit.setCursorPosition(len(user_text))
        
        # Reconnect the signal AFTER setting text to avoid triggering filter again
        self.line_edit.textChanged.connect(self._filter_items)
        
        self.combo.blockSignals(False)
        
        # Show popup only when user has typed something AND there are matching items
        # Don't show popup if text is empty (user cleared it)
        if user_text and self.combo.count() > 0:
            # Show popup when there are filtered results
            self.combo.showPopup()
        else:
            # Hide popup if no text or no matches
            self.combo.hidePopup()
    
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
            # Keep line edit editable so user can continue searching
            # Set cursor to beginning to show first characters of the text
            line_edit = self.combo.lineEdit()
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
