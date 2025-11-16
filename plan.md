# NPPES GeoSearch - Repository Plan

## Overview
A Python GUI application for testing and exploring NPPES API searches with geographic (ZIP code) and specialty (CPT code → taxonomy) matching. The application will allow interactive exploration of provider search results with precomputed ZIP code neighbors.

## Repository Structure

```
NPPES-GeoSearch/
├── README.md
├── requirements.txt
├── .gitignore
├── setup.py (optional)
├── src/
│   ├── __init__.py
│   ├── main.py                 # GUI application entry point
│   ├── gui/
│   │   ├── __init__.py
│   │   ├── main_window.py      # Main GUI window
│   │   ├── components/
│   │   │   ├── __init__.py
│   │   │   ├── cpt_selector.py  # CPT code dropdown component
│   │   │   ├── zip_input.py     # ZIP code input component
│   │   │   ├── taxonomy_display.py  # Taxonomy/specialty display
│   │   │   └── provider_list.py # Provider results list component
│   │   └── styles.py            # GUI styling/theming
│   ├── nppes/
│   │   ├── __init__.py
│   │   ├── client.py            # NPPES API client (adapted from CareQuotesAI)
│   │   └── models.py            # Data models for providers
│   ├── mapping/
│   │   ├── __init__.py
│   │   ├── cpt_mapper.py        # CPT → Taxonomy mapping (adapted)
│   │   └── taxonomy_codes.py    # Taxonomy code definitions
│   ├── geo/
│   │   ├── __init__.py
│   │   └── zip_neighbors.py     # ZIP neighbor loader (adapted)
│   └── utils/
│       ├── __init__.py
│       └── filters.py           # Provider filtering utilities
├── data/
│   ├── zip_neighbors_20mi.json  # Precomputed ZIP neighbors (copy from CareQuotesAI)
│   └── cpt_codes.json           # CPT code definitions (optional, for dropdown)
├── tests/
│   ├── __init__.py
│   ├── test_nppes_client.py
│   ├── test_cpt_mapper.py
│   └── test_zip_neighbors.py
└── docs/
    ├── USER_GUIDE.md
    └── API_REFERENCE.md
```

## Core Features

### 1. CPT Code Selection
- **Dropdown component** with searchable list of CPT codes
- Codes should include descriptions (e.g., "99213 - Office visit, established patient")
- Based on `CMS_PROCEDURES` from CareQuotesAI
- Display selected CPT code and description prominently

### 2. Taxonomy/Specialty Display
- **Auto-populated** based on selected CPT code
- Show mapped taxonomy codes and specialty names
- Display multiple matches if CPT maps to multiple specialties
- Allow manual taxonomy override (optional advanced feature)

### 3. ZIP Code Input & Neighbors
- **Text input** for origin ZIP code (5-digit validation)
- **Display panel** showing:
  - Origin ZIP code
  - Precomputed neighboring ZIPs (from `zip_neighbors_20mi.json`)
  - Total count of ZIPs being searched
- Visual indicator of search order (origin first, then neighbors)

### 4. Provider Results List
- **Table/TreeView** displaying returned practitioners
- **Filter**: Show only physicians (exclude organizations, other provider types)
- **Columns**:
  - NPI
  - Name (individual or organization)
  - Specialty
  - Taxonomy Code
  - Phone
  - Address (formatted)
  - ZIP Code (extracted from address)
- **Sortable** columns
- **Selectable rows** for detailed view
- **Pagination** or virtual scrolling for large result sets
- **Status indicator** showing:
  - Number of results found
  - Which ZIP codes returned results
  - Search progress/status

### 5. Search Controls
- **Search button** to trigger NPPES API query
- **Search parameters**:
  - Limit per ZIP (default: 20)
  - Search origin ZIP only vs. include neighbors
  - Filter by taxonomy code (auto-populated from CPT)
- **Progress indicator** during search
- **Cancel button** for long-running searches

### 6. Advanced Features (Future)
- Export results to CSV/JSON
- Save/load search configurations
- Compare results across different CPT codes
- Map view showing provider locations (if coordinates available)
- Cache management for NPPES responses

## Technical Stack

### GUI Framework Options

#### Option 1: tkinter (Recommended for MVP)
- **Pros**: Built-in with Python, no dependencies, simple
- **Cons**: Less modern UI, limited styling options
- **Best for**: Quick prototype, cross-platform simplicity

#### Option 2: PyQt6/PySide6
- **Pros**: Modern UI, professional look, rich widgets
- **Cons**: Larger dependency, more complex
- **Best for**: Production-ready application

#### Option 3: CustomTkinter
- **Pros**: Modern tkinter styling, easy migration from tkinter
- **Cons**: Additional dependency
- **Best for**: Better UI with minimal changes

**Recommendation**: Start with **tkinter** for MVP, can migrate to CustomTkinter or PyQt6 later.

### Dependencies

```txt
# Core
httpx>=0.24.0          # HTTP client for NPPES API
typing-extensions>=4.5.0  # Type hints support

# GUI (choose one)
# Option 1: tkinter (built-in)
# Option 2: PyQt6>=6.5.0
# Option 3: customtkinter>=5.0.0

# Data handling
pydantic>=2.0.0        # Data validation/models (optional)

# Utilities
python-dotenv>=1.0.0   # Environment variables (if needed)
```

## Code Adaptation from CareQuotesAI

### 1. NPPES Client (`nppes/client.py`)
- Copy `NPPESClient` class from `backend/app/providers.py`
- Keep `search_providers()` method
- Keep `_normalise_entry()` method
- Add filtering for physicians only (entity type = "Individual")
- Add error handling with user-friendly messages

### 2. CPT Mapper (`mapping/cpt_mapper.py`)
- Copy `ProcedureSpecialtyMapper` class from `backend/app/providers.py`
- Keep `PROCEDURE_CODE_RULES`, `KEYWORD_RULES`, `DEFAULT_RULES`
- Keep `map()` method
- Add method to get all available CPT codes for dropdown

### 3. ZIP Neighbors (`geo/zip_neighbors.py`)
- Copy `zip_neighbors.py` from `backend/app/geo/zip_neighbors.py`
- Keep `get_neighbors()` and `iter_zip_search_set()` functions
- Keep JSON loading logic
- Ensure data file path is configurable

### 4. Provider Models (`nppes/models.py`)
- Create dataclass/Pydantic model for Provider:
  ```python
  @dataclass
  class Provider:
      npi: str
      name: str
      specialty: str | None
      taxonomy_code: str | None
      phone: str | None
      address: str | None
      zip_code: str | None
      entity_type: str  # "Individual" or "Organization"
      raw_data: dict  # Full NPPES response
  ```

## GUI Layout Design

```
┌─────────────────────────────────────────────────────────────┐
│  NPPES GeoSearch                              [Settings]    │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  Search Configuration                                         │
│  ┌─────────────────────────────────────────────────────┐     │
│  │ CPT Code: [Dropdown ▼] 99213 - Office visit...     │     │
│  └─────────────────────────────────────────────────────┘     │
│                                                               │
│  ┌─────────────────────────────────────────────────────┐     │
│  │ ZIP Code: [90210        ]  [Include Neighbors ✓]  │     │
│  └─────────────────────────────────────────────────────┘     │
│                                                               │
│  Mapped Taxonomy:                                             │
│  • Family Medicine (207Q00000X)                              │
│  • Internal Medicine (207R00000X)                            │
│                                                               │
│  ZIP Codes to Search:                                         │
│  Origin: 90210 | Neighbors: 90211, 90212, 90035, 90067...   │
│  Total: 6 ZIP codes                                          │
│                                                               │
│  [Search Providers]  [Clear]  [Export Results]                │
│                                                               │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  Provider Results (42 found)                                  │
│  ┌─────────────────────────────────────────────────────┐     │
│  │ NPI      │ Name          │ Specialty │ Taxonomy │ ZIP│     │
│  ├─────────────────────────────────────────────────────┤     │
│  │ 123456789│ Dr. John Doe  │ Family... │207Q00000X│90210│     │
│  │ 987654321│ Dr. Jane Smith│ Internal..│207R00000X│90211│     │
│  │ ...      │ ...           │ ...       │ ...      │ ... │     │
│  └─────────────────────────────────────────────────────┘     │
│                                                               │
│  [Show Details]  [Filter: Physicians Only ✓]                 │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

## Implementation Phases

### Phase 1: Core Infrastructure (Week 1)
- [ ] Set up repository structure
- [ ] Copy and adapt NPPES client
- [ ] Copy and adapt CPT mapper
- [ ] Copy and adapt ZIP neighbors loader
- [ ] Copy ZIP neighbors data file
- [ ] Create provider data models
- [ ] Basic unit tests

### Phase 2: Basic GUI (Week 1-2)
- [ ] Create main window with tkinter
- [ ] Implement CPT code dropdown
- [ ] Implement ZIP code input
- [ ] Display taxonomy mappings
- [ ] Display ZIP neighbors
- [ ] Basic search button and handler

### Phase 3: Results Display (Week 2)
- [ ] Create provider results table/list
- [ ] Implement physician filtering
- [ ] Add result count display
- [ ] Add search progress indicator
- [ ] Handle API errors gracefully

### Phase 4: Polish & Testing (Week 2-3)
- [ ] Improve UI styling
- [ ] Add keyboard shortcuts
- [ ] Add export functionality
- [ ] Comprehensive testing
- [ ] User documentation

### Phase 5: Advanced Features (Future)
- [ ] Provider detail view
- [ ] Search history
- [ ] Comparison mode
- [ ] Map visualization
- [ ] Caching layer

## Key Design Decisions

### 1. Physician Filtering
- Filter by `entity_type_code` from NPPES response
- Entity type "1" = Individual (physicians)
- Entity type "2" = Organization
- Default: Show only physicians, with toggle to show all

### 2. ZIP Code Search Strategy
- Always search origin ZIP first
- Then search neighbors in order
- Deduplicate providers by (NPI, phone)
- Show which ZIP each provider came from

### 3. Taxonomy Matching
- Auto-populate from CPT code selection
- Allow manual override for testing
- Show all matching taxonomy codes if CPT maps to multiple
- Search with each taxonomy code sequentially

### 4. Error Handling
- Network errors: Show user-friendly message, retry option
- Invalid ZIP: Validate format, show error
- No results: Clear message, suggest alternatives
- API rate limits: Queue requests, show warning

## Testing Strategy

### Unit Tests
- NPPES client mocking
- CPT mapper logic
- ZIP neighbor loading
- Provider filtering

### Integration Tests
- End-to-end search flow
- GUI component interactions
- Error scenarios

### Manual Testing Checklist
- [ ] Select CPT code → verify taxonomy mapping
- [ ] Enter ZIP → verify neighbors loaded
- [ ] Search → verify results displayed
- [ ] Filter physicians → verify only individuals shown
- [ ] Invalid ZIP → verify error handling
- [ ] No results → verify appropriate message
- [ ] Network error → verify graceful degradation

## Documentation Requirements

### README.md
- Installation instructions
- Quick start guide
- Screenshots
- Requirements
- License

### USER_GUIDE.md
- Feature walkthrough
- Search strategies
- Understanding results
- Troubleshooting

### API_REFERENCE.md
- NPPES API usage
- Taxonomy codes reference
- CPT code mappings

## Future Enhancements

1. **Caching**: Cache NPPES responses locally to reduce API calls
2. **Batch Mode**: Search multiple CPT codes/ZIPs at once
3. **Analytics**: Track search patterns, common mappings
4. **Integration**: Export to CareQuotesAI format
5. **Visualization**: Map view with provider locations
6. **Advanced Filtering**: Filter by distance, specialty combinations
7. **Provider Details**: Full NPPES record viewer
8. **Comparison**: Side-by-side comparison of search parameters

## Success Criteria

- ✅ Can select CPT code and see taxonomy mappings
- ✅ Can enter ZIP and see neighbors
- ✅ Can search and see physician results
- ✅ Results are deduplicated and properly formatted
- ✅ UI is responsive and user-friendly
- ✅ Handles errors gracefully
- ✅ Code is well-structured and testable

## Notes

- Keep code modular for easy adaptation back to CareQuotesAI
- Use similar naming conventions to CareQuotesAI for consistency
- Consider making this a reusable library that CareQuotesAI could import
- Ensure ZIP neighbors data file is included or easily obtainable
- Consider adding configuration file for API timeouts, limits, etc.

