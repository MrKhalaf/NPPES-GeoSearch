# NPPES GeoSearch

A Python GUI application for testing and exploring NPPES API searches with geographic (ZIP code) and specialty (CPT code → taxonomy) matching.

## Features

- Search NPPES providers by CPT code and ZIP code
- Automatic taxonomy mapping from CPT codes
- Dynamic ZIP code neighbor search (within 20 miles)
- Filter results to physicians only
- Interactive GUI for exploring search results
- API call logging and progress tracking

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python run.py
```

Or run as a module:

```bash
python -m src.main
```

## Requirements

- Python 3.8+
- See `requirements.txt` for dependencies

