"""Modern macOS theme for PyQt6 with clear, popping design."""

from PyQt6.QtGui import QFont, QColor, QPalette, QFontDatabase
from PyQt6.QtCore import Qt


class MacOSTheme:
    """Modern macOS theme configuration with clear, popping design."""
    
    # Modern color palette - macOS Big Sur/Sonoma style
    COLORS = {
        'background': '#f5f5f7',           # Light gray background (macOS style)
        'surface': '#ffffff',              # Pure white cards
        'surface_secondary': '#fafafa',     # Slightly off-white
        'border': '#d1d1d6',               # Subtle border
        'border_light': '#e5e5ea',         # Very light border
        'text_primary': '#1d1d1f',         # Deep black text
        'text_secondary': '#86868b',       # Medium gray secondary text
        'text_tertiary': '#a1a1a6',        # Light gray tertiary text
        'accent': '#0051d5',               # Dark blue for better contrast
        'accent_hover': '#003d9e',         # Darker blue on hover
        'accent_light': '#e3f2fd',         # Very light blue background
        'success': '#34c759',              # Modern green
        'warning': '#ff9500',              # Orange
        'error': '#ff3b30',                # Red
        'divider': '#d1d1d6',              # Divider line
        'hover': '#f2f2f7',                # Hover background
        'input_bg': '#ffffff',             # Input background
        'input_border': '#d1d1d6',         # Input border
        'card_shadow': 'rgba(0, 0, 0, 0.05)',  # Card shadow
    }
    
    # Typography - SF Pro style (Helvetica Neue as fallback)
    FONTS = {}
    
    # Set fallback fonts for macOS
    @classmethod
    def _init_fonts(cls):
        """Initialize fonts with fallbacks."""
        # Get available font families
        try:
            font_db = QFontDatabase()
            available_families = set(font_db.families())
        except Exception:
            # Fallback if font database isn't available
            available_families = set()
        
        def _get_font(font_name, fallbacks):
            """Get font name from available fonts or fallbacks."""
            if font_name in available_families:
                return font_name
            for fallback in fallbacks:
                if fallback in available_families:
                    return fallback
            # Last resort: use the first fallback (Qt will handle it)
            return fallbacks[0] if fallbacks else 'System'
        
        # Determine which fonts to use with fallback chains
        display_font = _get_font('SF Pro Display', ['Helvetica Neue', 'Helvetica', 'Arial', 'System'])
        text_font = _get_font('SF Pro Text', ['Helvetica Neue', 'Helvetica', 'Arial', 'System'])
        mono_font = _get_font('SF Mono', ['Menlo', 'Monaco', 'Courier New', 'Courier', 'System'])
        
        # Initialize fonts with proper fallbacks
        cls.FONTS = {
            'title': QFont(display_font, 32, QFont.Weight.Bold),
            'heading': QFont(display_font, 20, QFont.Weight.DemiBold),
            'subheading': QFont(display_font, 18, QFont.Weight.Medium),
            'body': QFont(text_font, 14, QFont.Weight.Normal),
            'body_bold': QFont(text_font, 14, QFont.Weight.DemiBold),
            'field_label': QFont(text_font, 14, QFont.Weight.DemiBold),
            'caption': QFont(text_font, 13, QFont.Weight.Normal),
            'mono': QFont(mono_font, 12, QFont.Weight.Normal),
        }
    
    # Spacing - Modern and generous
    SPACING = {
        'xs': 6,
        'sm': 10,
        'md': 14,
        'lg': 20,
        'xl': 28,
        'xxl': 36,
    }
    
    # Border radius for rounded corners
    RADIUS = 12
    
    # Shadow properties
    SHADOW = {
        'blur': 20,
        'offset': (0, 2),
        'color': QColor(0, 0, 0, 13),  # 5% opacity black
    }
    
    @classmethod
    def get_color(cls, color_name: str) -> QColor:
        """Get a QColor from the color palette.
        
        Args:
            color_name: Name of the color
            
        Returns:
            QColor object
        """
        color_hex = cls.COLORS.get(color_name, '#000000')
        return QColor(color_hex)
    
    @classmethod
    def get_font(cls, font_name: str) -> QFont:
        """Get a QFont from the font dictionary.
        
        Args:
            font_name: Name of the font
            
        Returns:
            QFont object
        """
        font = cls.FONTS.get(font_name, cls.FONTS['body'])
        return QFont(font)
    
    @classmethod
    def apply_style_sheet(cls) -> str:
        """Get a comprehensive stylesheet for the application.
        
        Returns:
            QSS stylesheet string
        """
        return f"""
        /* Main Window */
        QMainWindow {{
            background-color: {cls.COLORS['background']};
        }}
        
        /* Buttons - Modern macOS style */
        QPushButton {{
            background-color: {cls.COLORS['accent']};
            color: white;
            border: none;
            border-radius: {cls.RADIUS}px;
            padding: 12px 24px;
            font-weight: 600;
            font-size: 14px;
        }}
        
        QPushButton:hover {{
            background-color: {cls.COLORS['accent_hover']};
        }}
        
        QPushButton:pressed {{
            background-color: {cls.COLORS['accent_hover']};
        }}
        
        QPushButton:disabled {{
            background-color: #999999;
            color: white;
        }}
        
        /* Secondary Button */
        QPushButton[class="secondary"] {{
            background-color: {cls.COLORS['surface']};
            color: {cls.COLORS['accent']};
            border: 1px solid {cls.COLORS['border']};
        }}
        
        QPushButton[class="secondary"]:hover {{
            background-color: {cls.COLORS['hover']};
        }}
        
        /* Line Edit - Modern input fields */
        QLineEdit {{
            background-color: {cls.COLORS['input_bg']};
            border: 1px solid {cls.COLORS['input_border']};
            border-radius: 8px;
            padding: 10px 14px;
            font-size: 14px;
            color: {cls.COLORS['text_primary']};
        }}
        
        QLineEdit:focus {{
            border: 2px solid {cls.COLORS['accent']};
            padding: 9px 13px;
        }}
        
        /* ComboBox - Modern dropdown */
        QComboBox {{
            background-color: {cls.COLORS['input_bg']};
            border: 1px solid {cls.COLORS['input_border']};
            border-radius: 8px;
            padding: 10px 14px;
            font-size: 14px;
            color: {cls.COLORS['text_primary']};
        }}
        
        QComboBox:hover {{
            border: 1px solid {cls.COLORS['accent']};
        }}
        
        QComboBox:focus {{
            border: 2px solid {cls.COLORS['accent']};
            padding: 9px 13px;
        }}
        
        QComboBox::drop-down {{
            border: none;
            width: 30px;
        }}
        
        QComboBox::down-arrow {{
            image: none;
            border-left: 5px solid transparent;
            border-right: 5px solid transparent;
            border-top: 5px solid {cls.COLORS['text_secondary']};
            width: 0;
            height: 0;
            margin-right: 10px;
        }}
        
        QComboBox QAbstractItemView {{
            background-color: {cls.COLORS['surface']};
            border: 1px solid {cls.COLORS['border']};
            border-radius: 8px;
            selection-background-color: {cls.COLORS['accent_light']};
            selection-color: {cls.COLORS['text_primary']};
            padding: 4px;
        }}
        
        /* Checkbox */
        QCheckBox {{
            font-size: 14px;
            color: {cls.COLORS['text_primary']};
            spacing: 8px;
        }}
        
        QCheckBox::indicator {{
            width: 18px;
            height: 18px;
            border: 2px solid {cls.COLORS['border']};
            border-radius: 4px;
            background-color: {cls.COLORS['input_bg']};
        }}
        
        QCheckBox::indicator:hover {{
            border-color: {cls.COLORS['accent']};
        }}
        
        QCheckBox::indicator:checked {{
            background-color: {cls.COLORS['accent']};
            border-color: {cls.COLORS['accent']};
        }}
        
        /* Text Edit */
        QTextEdit {{
            background-color: {cls.COLORS['input_bg']};
            border: 1px solid {cls.COLORS['input_border']};
            border-radius: 8px;
            padding: 10px 14px;
            font-size: 14px;
            color: {cls.COLORS['text_primary']};
        }}
        
        QTextEdit:focus {{
            border: 2px solid {cls.COLORS['accent']};
            padding: 9px 13px;
        }}
        
        /* Tree Widget - Modern table */
        QTreeWidget {{
            background-color: {cls.COLORS['surface']};
            border: 1px solid {cls.COLORS['border_light']};
            border-radius: 8px;
            font-size: 14px;
            color: {cls.COLORS['text_primary']};
            alternate-background-color: {cls.COLORS['surface_secondary']};
        }}
        
        QTreeWidget::item {{
            padding: 8px;
            border: none;
        }}
        
        QTreeWidget::item:hover {{
            background-color: {cls.COLORS['hover']};
        }}
        
        QTreeWidget::item:selected {{
            background-color: {cls.COLORS['accent_light']};
            color: {cls.COLORS['text_primary']};
        }}
        
        QHeaderView::section {{
            background-color: {cls.COLORS['surface']};
            color: {cls.COLORS['text_primary']};
            padding: 10px;
            border: none;
            border-bottom: 1px solid {cls.COLORS['border_light']};
            font-weight: 600;
            font-size: 14px;
        }}
        
        /* Scrollbar - Modern style */
        QScrollBar:vertical {{
            background-color: transparent;
            width: 10px;
            margin: 0;
        }}
        
        QScrollBar::handle:vertical {{
            background-color: {cls.COLORS['border']};
            border-radius: 5px;
            min-height: 20px;
            margin: 2px;
        }}
        
        QScrollBar::handle:vertical:hover {{
            background-color: {cls.COLORS['text_secondary']};
        }}
        
        QScrollBar:horizontal {{
            background-color: transparent;
            height: 10px;
            margin: 0;
        }}
        
        QScrollBar::handle:horizontal {{
            background-color: {cls.COLORS['border']};
            border-radius: 5px;
            min-width: 20px;
            margin: 2px;
        }}
        
        QScrollBar::handle:horizontal:hover {{
            background-color: {cls.COLORS['text_secondary']};
        }}
        
        /* Labels */
        QLabel {{
            color: {cls.COLORS['text_primary']};
            font-size: 14px;
            background-color: transparent;
        }}
        
        QLabel[class="title"] {{
            font-size: 32px;
            font-weight: 700;
            color: {cls.COLORS['text_primary']};
        }}
        
        QLabel[class="heading"] {{
            font-size: 20px;
            font-weight: 600;
            color: {cls.COLORS['text_primary']};
        }}
        
        QLabel[class="caption"] {{
            font-size: 13px;
            color: {cls.COLORS['text_secondary']};
        }}
        
        /* Card Frame */
        QFrame[class="card"] {{
            background-color: {cls.COLORS['surface']};
            border: 1px solid {cls.COLORS['border_light']};
            border-radius: {cls.RADIUS}px;
        }}
        """
    
    @classmethod
    def init_fonts(cls):
        """Initialize fonts with proper fallbacks."""
        cls._init_fonts()


# Initialize fonts on import
MacOSTheme.init_fonts()
