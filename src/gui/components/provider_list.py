"""Provider results list component using PyQt6."""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTreeWidget, QTreeWidgetItem, QCheckBox, QHeaderView
from PyQt6.QtCore import Qt
from typing import List, Optional
from ...nppes.models import Provider
from ..theme import MacOSTheme


class ProviderList(QWidget):
    """Table/list component for displaying provider search results."""
    
    def __init__(self, parent=None, filter_physicians: bool = True):
        """Initialize the provider list.
        
        Args:
            parent: Parent widget
            filter_physicians: If True, filter to show only physicians (Individual entity type)
        """
        super().__init__(parent)
        self.filter_physicians = filter_physicians
        self.providers: List[Provider] = []
        
        # Main layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(MacOSTheme.SPACING['md'])
        
        # Header with count and filter
        header_layout = QHBoxLayout()
        
        self.count_label = QLabel("No results")
        self.count_label.setFont(MacOSTheme.get_font('body_bold'))
        self.count_label.setStyleSheet(f"""
            color: {MacOSTheme.COLORS['text_primary']};
            background-color: {MacOSTheme.COLORS['surface']};
        """)
        header_layout.addWidget(self.count_label)
        
        header_layout.addStretch()
        
        self.filter_check = QCheckBox("Physicians Only")
        self.filter_check.setChecked(filter_physicians)
        self.filter_check.toggled.connect(self._on_filter_toggle)
        header_layout.addWidget(self.filter_check)
        
        layout.addLayout(header_layout)
        
        # Tree widget for results
        columns = ["NPI", "Name", "Specialty", "Taxonomy", "Phone", "ZIP"]
        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(columns)
        self.tree.setAlternatingRowColors(True)
        self.tree.setRootIsDecorated(False)
        self.tree.setSelectionBehavior(QTreeWidget.SelectionBehavior.SelectRows)
        
        # Configure columns
        header = self.tree.header()
        header.setStretchLastSection(False)
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)
        
        # Set minimum column widths
        self.tree.setColumnWidth(0, 110)
        self.tree.setColumnWidth(1, 250)
        self.tree.setColumnWidth(2, 180)
        self.tree.setColumnWidth(3, 140)
        self.tree.setColumnWidth(4, 130)
        self.tree.setColumnWidth(5, 90)
        
        layout.addWidget(self.tree)
    
    def _on_filter_toggle(self, checked: bool):
        """Handle filter toggle."""
        self.filter_physicians = checked
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
        self.tree.clear()
        
        # Filter providers
        display_providers = self.providers
        if self.filter_physicians:
            display_providers = [p for p in self.providers if p.entity_type == "Individual"]
        
        # Add to treeview
        for provider in display_providers:
            try:
                item = QTreeWidgetItem([
                    provider.npi,
                    provider.name[:50] if provider.name else "",
                    provider.specialty[:30] if provider.specialty else "",
                    provider.taxonomy_code or "",
                    provider.phone or "",
                    provider.zip_code or ""
                ])
                self.tree.addTopLevelItem(item)
            except Exception as e:
                print(f"Error inserting provider {provider.npi}: {e}")
        
        # Update count
        total = len(self.providers)
        displayed = len(display_providers)
        if total == displayed:
            self.count_label.setText(f"{displayed} result{'s' if displayed != 1 else ''}")
        else:
            self.count_label.setText(f"{displayed} of {total} result{'s' if total != 1 else ''}")
    
    def clear(self):
        """Clear all providers."""
        self.providers = []
        self._refresh_display()
