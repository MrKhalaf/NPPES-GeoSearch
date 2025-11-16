#!/usr/bin/env python3
"""Launcher script for NPPES GeoSearch application."""

import sys
from pathlib import Path

# Add project root to path so we can import src as a package
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Import and run the main function
from src.main import main

if __name__ == "__main__":
    main()

