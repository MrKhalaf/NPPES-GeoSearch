"""API logs view component using PyQt6."""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QPushButton
from PyQt6.QtGui import QTextCursor
from PyQt6.QtCore import Qt
from datetime import datetime
from typing import Optional
from ..theme import MacOSTheme


class LogsView(QWidget):
    """Component for displaying API call logs with toggleable visibility."""
    
    def __init__(self, parent=None):
        """Initialize the logs view.
        
        Args:
            parent: Parent widget
        """
        super().__init__(parent)
        self.is_expanded = False  # Start collapsed
        
        # Set grey background to match logs_frame
        self.setStyleSheet(f"background-color: {MacOSTheme.COLORS['background']};")
        
        # Main layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(
            MacOSTheme.SPACING['xl'],
            MacOSTheme.SPACING['lg'],
            MacOSTheme.SPACING['xl'],
            MacOSTheme.SPACING['lg']
        )
        layout.setSpacing(MacOSTheme.SPACING['md'])
        
        # Header with title, toggle button, and clear button
        header_layout = QHBoxLayout()
        
        # Toggle button - dark blue
        self.toggle_button = QPushButton("▶ API Logs")
        self.toggle_button.setFont(MacOSTheme.get_font('heading'))
        self.toggle_button.setStyleSheet(f"""
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
        self.toggle_button.clicked.connect(self.toggle)
        header_layout.addWidget(self.toggle_button)
        
        header_layout.addStretch()
        
        # Clear button - de-emphasized style, stored as instance variable
        self.clear_button = QPushButton("Clear")
        self.clear_button.setFont(MacOSTheme.get_font('body'))
        self.clear_button.setStyleSheet(f"""
            QPushButton {{
                background-color: {MacOSTheme.COLORS['surface']};
                color: {MacOSTheme.COLORS['text_secondary']};
                border: 1px solid {MacOSTheme.COLORS['border_light']};
                border-radius: {MacOSTheme.RADIUS}px;
                padding: 8px 16px;
                font-weight: 500;
            }}
            QPushButton:hover {{
                background-color: {MacOSTheme.COLORS['hover']};
                color: {MacOSTheme.COLORS['text_primary']};
            }}
            QPushButton:pressed {{
                background-color: {MacOSTheme.COLORS['border_light']};
            }}
        """)
        self.clear_button.clicked.connect(self.clear)
        self.clear_button.hide()  # Hide initially since section starts collapsed
        header_layout.addWidget(self.clear_button)
        
        layout.addLayout(header_layout)
        
        # Text widget container (initially hidden)
        self.text_widget = QTextEdit()
        self.text_widget.setReadOnly(True)
        self.text_widget.setFixedHeight(120)
        self.text_widget.setPlaceholderText("API logs will appear here...")
        self.text_widget.hide()  # Start hidden
        
        layout.addWidget(self.text_widget)
    
    def toggle(self):
        """Toggle the visibility of the logs content."""
        self.is_expanded = not self.is_expanded
        
        if self.is_expanded:
            self.text_widget.show()
            self.clear_button.show()
            self.toggle_button.setText("▼ API Logs")
        else:
            self.text_widget.hide()
            self.clear_button.hide()
            self.toggle_button.setText("▶ API Logs")
    
    def log(self, message: str, level: str = "INFO"):
        """Add a log message.
        
        Args:
            message: Log message
            level: Log level (INFO, ERROR, etc.)
        """
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {level}: {message}\n"
        
        # Determine color based on level
        if level == "ERROR":
            color = MacOSTheme.COLORS['error']
        elif level == "SUCCESS":
            color = MacOSTheme.COLORS['success']
        else:
            color = MacOSTheme.COLORS['text_primary']
        
        # Insert with color - move cursor to end
        cursor = self.text_widget.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        self.text_widget.setTextCursor(cursor)
        self.text_widget.setTextColor(MacOSTheme.get_color(color))
        self.text_widget.insertPlainText(log_entry)
        
        # Auto-scroll to bottom
        scrollbar = self.text_widget.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
    
    def clear(self):
        """Clear all logs."""
        self.text_widget.clear()
