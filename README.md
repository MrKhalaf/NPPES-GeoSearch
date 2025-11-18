# NPPES GeoSearch

> A powerful Python GUI application for discovering healthcare providers using geographic proximity and medical specialty matching. Search the National Plan and Provider Enumeration System (NPPES) database by ZIP code and CPT procedure codes to find physicians who match your specific needs.


## NPPES GeoSearch

NPPES GeoSearch bridges the gap between medical procedure codes (CPT) and healthcare provider discovery. Whether you're a healthcare administrator, researcher, or developer building healthcare applications, this tool helps you:

- **Find providers by specialty** - Automatically map CPT procedure codes to medical specialties. Initial selecton of CPT codes & specialties supported, easily extensible.
- **Search by location** - Discover providers within 20 miles of any ZIP code
- **Explore NPPES data** - Interact with the official CMS provider database through an intuitive GUI
- **Filter intelligently** - Focus on individual physicians or expand to include organizations

## Key Features

### Smart CPT-to-Specialty Mapping
Automatically translates CPT procedure codes (e.g., `99213` for office visits) into relevant medical taxonomy codes. The application includes comprehensive mappings for hundreds of common procedures across specialties like:
- Primary Care (Family Medicine, Internal Medicine)
- Emergency Medicine
- Mental Health (Psychiatry, Psychology)
- Surgical Specialties (Orthopedics, Ophthalmology, Gastroenterology)
- And many more...

### Geographic Search with Neighbors
Enter a single ZIP code and the application automatically:
- Finds all neighboring ZIP codes within 20 miles
- Searches providers in the origin ZIP first, then expands to neighbors
- Displays the complete search set before executing
- Deduplicates results across multiple ZIP searches

### Modern, Intuitive GUI
Built with PyQt6, featuring:
- **macOS-inspired design** - Clean, modern interface that feels native
- **Real-time progress tracking** - See search progress as it happens
- **Interactive provider list** - Sortable, filterable results with detailed provider information
- **Live logging** - Monitor API calls and search activity in real-time
- **Collapsible sections** - Maximize screen space for results

### Real-time Search & Results
- **Incremental updates** - Results appear as they're discovered
- **Background processing** - Non-blocking searches keep the UI responsive
- **Comprehensive provider details** - NPI, name, specialty, taxonomy code, phone, and address
- **Smart deduplication** - Prevents duplicate providers across multiple searches

## Demo

<!-- Video demo will be added here -->
**Video Demo Coming Soon** - Watch a walkthrough of NPPES GeoSearch in action!

## Quick Start


### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "NPPES GeoSearch"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python run.py
   ```
   
   Or run as a module:
   ```bash
   python -m src.main
   ```

## Usage Guide

### Basic Workflow

1. **Select a CPT Code**
   - Choose from the dropdown menu of common CPT codes
   - Each code includes a description (e.g., "99213 - Office visit, established patient")
   - The application automatically maps your selection to relevant medical specialties

2. **Enter a ZIP Code**
   - Type a 5-digit ZIP code in the input field
   - The application displays:
     - Your origin ZIP code
     - All neighboring ZIP codes within 20 miles
     - Total count of ZIPs to be searched

3. **Review Taxonomy Mapping**
   - See which medical specialties match your CPT code
   - Multiple specialties may be shown if the CPT code applies broadly

4. **Search Providers**
   - Click "Search Providers" to begin
   - Watch real-time progress as the application queries the NPPES API
   - Results appear incrementally in the provider list

5. **Explore Results**
   - Browse the provider list with details including:
     - NPI (National Provider Identifier)
     - Provider name
     - Specialty and taxonomy code
     - Contact information
     - Address and ZIP code
   - Use "Clear Results" to start a new search

### Example Search

**Scenario**: Find orthopedic surgeons near ZIP code 90210 (Beverly Hills, CA) who perform knee arthroscopy (CPT code 29880).

1. Select CPT code `29880` from the dropdown
2. Enter ZIP code `90210`
3. Review mapped taxonomy: "Orthopedic Surgery"
4. Click "Search Providers"
5. Browse results showing orthopedic surgeons in Beverly Hills and surrounding areas

## Architecture

### Key Components

- **`NPPESClient`** - Handles all interactions with the NPPES Registry API
- **`ProcedureSpecialtyMapper`** - Maps CPT codes to taxonomy codes using intelligent rule-based matching
- **`ZIPNeighborFinder`** - Calculates neighboring ZIP codes using geographic coordinates
- **`MainWindow`** - PyQt6-based GUI with collapsible sections and real-time updates

## Technical Details

### Dependencies

- **PyQt6** (≥6.6.0) - Modern GUI framework
- **httpx** (≥0.24.0) - Async-capable HTTP client for API calls
- **pydantic** (≥2.0.0) - Data validation and models
- **uszipcode** (≥1.0.0) - ZIP code geographic data
- **python-dotenv** (≥1.0.0) - Environment variable management

See `requirements.txt` for the complete list.

### API Integration

NPPES GeoSearch uses the official [NPPES Registry API](https://npiregistry.cms.hhs.gov/api-page) provided by CMS. The application:
- Respects API rate limits
- Handles network errors gracefully
- Provides detailed logging of all API interactions
- Supports filtering by taxonomy description, ZIP code, and entity type

### Data Sources

- **NPPES Registry** - Official CMS provider database
- **NUCC Taxonomy** - Medical specialty taxonomy codes
- **ZIP Code Data** - Geographic coordinates and neighbor relationships

## Testing

Run the test suite:

```bash
python -m pytest tests/
```

Current test coverage includes:
- ZIP neighbor finding logic
- Provider model validation
- API client error handling

## Contributing

Contributions are welcome! Areas for improvement:
- Additional CPT code mappings
- Enhanced filtering options
- Export functionality (CSV/JSON)
- Provider detail views
- Map visualization
- Search history and saved searches

## License

This project is open source. See LICENSE file for details.

## Acknowledgments

- **CMS** - For providing the NPPES Registry API
- **NUCC** - For maintaining the healthcare provider taxonomy
- **PyQt Project** - For the excellent GUI framework

## Support

For issues, questions, or feature requests, please open an issue on the repository.

---

**Built for the healthcare community**
