"""API logs view component."""

import tkinter as tk
from tkinter import ttk
from datetime import datetime
from typing import Optional


class LogsView:
    """Component for displaying API call logs."""
    
    def __init__(self, parent):
        """Initialize the logs view.
        
        Args:
            parent: Parent widget
        """
        self.parent = parent
        
        # Create frame
        self.frame = ttk.LabelFrame(parent, text="API Logs", padding="5")
        
        # Text widget with scrollbar
        self.text_widget = tk.Text(
            self.frame,
            height=8,
            wrap=tk.WORD,
            font=("Courier", 9),
            bg="#f5f5f5",
            fg="#333333"
        )
        self.text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.text_widget.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_widget.config(yscrollcommand=scrollbar.set)
        
        # Clear button
        clear_button = ttk.Button(
            self.frame,
            text="Clear",
            command=self.clear,
            width=8
        )
        clear_button.pack(side=tk.BOTTOM, pady=(5, 0))
    
    def log(self, message: str, level: str = "INFO"):
        """Add a log message.
        
        Args:
            message: Log message
            level: Log level (INFO, ERROR, etc.)
        """
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {level}: {message}\n"
        
        self.text_widget.insert(tk.END, log_entry)
        self.text_widget.see(tk.END)  # Auto-scroll to bottom
        
        # Color coding
        if level == "ERROR":
            self.text_widget.tag_add("error", f"end-{len(log_entry)}c", tk.END)
            self.text_widget.tag_config("error", foreground="red")
        elif level == "SUCCESS":
            self.text_widget.tag_add("success", f"end-{len(log_entry)}c", tk.END)
            self.text_widget.tag_config("success", foreground="green")
    
    def clear(self):
        """Clear all logs."""
        self.text_widget.delete(1.0, tk.END)
    
    def grid(self, **kwargs):
        """Grid the component frame."""
        self.frame.grid(**kwargs)

