# build_taxonomy_mapping.py

import re
from pathlib import Path
from typing import Dict, Optional, List
from dataclasses import dataclass

import PyPDF2
from tqdm import tqdm


@dataclass
class TaxonomyEntry:
    code: str
    descriptive_name: str
    specialty: str
    specialization: Optional[str] = None
    provider_grouping: Optional[str] = None


# Fixed: Changed from {7} to {6} - NUCC taxonomy codes are 10 chars total:
# 3 digits + 6 alphanumeric + 'X' (e.g., 207K00000X)
CODE_RE = re.compile(r"^\d{3}[A-Z0-9]{6}X$")


def extract_pdf_text(pdf_path: Path) -> str:
    print(f"📄 Reading PDF: {pdf_path}")
    reader = PyPDF2.PdfReader(str(pdf_path))
    chunks: List[str] = []
    total_pages = len(reader.pages)

    for page in tqdm(reader.pages, desc="Extracting pages", total=total_pages, unit="page"):
        t = page.extract_text()
        if t:
            chunks.append(t)

    print(f"✓ Extracted text from {total_pages} pages")
    return "\n".join(chunks)


def normalize_line(line: str) -> str:
    return " ".join(line.split()).strip()


def is_heading(line: str) -> bool:
    # NUCC headings are typically Title Case and not codes
    if "HEALTH CARE PROVIDER TAXONOMY" in line:
        return False
    if CODE_RE.match(line.strip()):
        return False
    # crude: treat fully uppercase or Title Case standalone as heading
    stripped = line.strip()
    if not stripped:
        return False
    # ignore obvious noise like dates
    if re.search(r"\d{1,2}/\d{1,2}/\d{4}", stripped):
        return False
    return True


def parse_taxonomy(text: str) -> Dict[str, TaxonomyEntry]:
    print("🔍 Parsing taxonomy entries...")
    mapping: Dict[str, TaxonomyEntry] = {}

    provider_grouping: Optional[str] = None
    specialty: Optional[str] = None
    specialization: Optional[str] = None

    last_nonempty: Optional[str] = None
    pending_specialization_label: Optional[str] = None

    lines = [normalize_line(l) for l in text.splitlines()]

    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]

        if not line:
            i += 1
            continue

        # Detect obvious provider grouping lines (top-level section headers)
        # e.g. "Allopathic & Osteopathic Physicians", "Suppliers", etc.
        if "HEALTH CARE PROVIDER TAXONOMY CODE SET VERSION" in line:
            # next nonempty line after this header is usually a grouping
            j = i + 1
            while j < n and not lines[j]:
                j += 1
            if j < n:
                provider_grouping = lines[j]
            i += 1
            continue

        # Explicit NUCC grouping headers that appear without the big title
        if line in {
            "Allopathic & Osteopathic Physicians",
            "Behavioral Health & Social Service Providers",
            "Chiropractic Providers",
            "Dental Providers",
            "Dietary & Nutritional Service Providers",
            "Emergency Medical Service Providers",
            "Eye and Vision Service Providers",
            "Group",
            "Hospitals",
            "Laboratories",
            "Managed Care Organizations",
            "Nursing Service Providers",
            "Other Service Providers",
            "Pharmacy Service Providers",
            "Physician Assistants & Advanced Practice Nursing Providers",
            "Podiatric Medicine & Surgery Service Providers",
            "Respiratory, Developmental, Rehabilitative and Restorative Service Providers",
            "Speech, Language and Hearing Service Providers",
            "Suppliers",
            "Transportation Services",
            "Agencies",
            "Ambulatory Health Care Facilities",
            "Hospice Care, Community Based",
            "Nursing & Custodial Care Facilities",
            "Residential Treatment Facilities",
            "Skilled Nursing Facilities",
        }:
            provider_grouping = line
            # specialty will be defined by following lines
            i += 1
            continue

        # Specialization label line ends with 'Specialization:'
        if line.endswith("Specialization:"):
            # Strip the suffix to keep a cleaner label for specialization name
            pending_specialization_label = line[:-len("Specialization:")].strip()
            specialization = pending_specialization_label or None
            # The specialty for that specialization is the parent section title,
            # which tends to be the same as the descriptive name of the section.
            # We keep `specialty` as the last_nonempty heading before the specialization.
            # last_nonempty gets updated below.
            i += 1
            continue

        # Code line
        if CODE_RE.match(line):
            code = line.strip()

            # Find the descriptive name in subsequent lines:
            # typically the next non-empty line that is not a date or 'Definition to come...' etc.
            j = i + 1
            desc: Optional[str] = None
            while j < n:
                candidate = lines[j]
                j += 1
                if not candidate:
                    continue
                # Skip obvious noise
                if candidate.startswith("[") and candidate.endswith("]"):
                    continue
                if re.search(r"Effective Date|Last Modified Date|Deactivation Date", candidate):
                    continue
                if candidate.startswith("Definition to come"):
                    # If definition placeholder is encountered before name, keep looking
                    continue
                # Treat first remaining candidate as descriptive name
                desc = candidate
                break

            if desc is None:
                desc = code  # fallback

            # Specialty: if we’re inside a specialization, the specialty is the parent section.
            # Otherwise, use the last_nonempty heading as specialty.
            use_specialty = specialty or (last_nonempty or desc)

            entry = TaxonomyEntry(
                code=code,
                descriptive_name=desc,
                specialty=use_specialty,
                specialization=specialization,
                provider_grouping=provider_grouping,
            )
            mapping[code] = entry

            # After consuming a code block, do NOT forcibly reset specialization,
            # because some specializations list multiple codes.
            i += 1
            continue

        # If this line looks like a “specialty heading” (e.g., "Family Medicine", "Clinic/Center", etc.)
        # and is not a specialization label or code, treat as specialty.
        # The NUCC structure is fairly regular: Grouping → Specialty → Specialization/Code.
        if is_heading(line):
            # Heuristic: if last_nonempty was a grouping, this line is likely a specialty.
            if provider_grouping and line != provider_grouping:
                specialty = line

        last_nonempty = line
        i += 1

    print(f"✓ Parsed {len(mapping)} taxonomy codes")
    return mapping


def write_mapping_module(mapping: Dict[str, TaxonomyEntry], out_path: Path) -> None:
    print(f"📝 Writing mapping module to {out_path}...")
    with out_path.open("w", encoding="utf-8") as f:
        f.write(
            '"""Comprehensive taxonomy code mapping based on NUCC Taxonomy Code Set Version 24.0.\n'
            "\n"
            "This module is auto-generated from taxonomy_24_0.pdf.\n"
            'Do not edit by hand; instead, regenerate using build_taxonomy_mapping.py.\n'
            'Source: Health Care Provider Taxonomy VERSION 24.0, January 2024\n'
            '© 2024 American Medical Association; NUCC.\n'
            '"""\n\n'
        )

        f.write("from dataclasses import dataclass\n")
        f.write("from typing import Dict, List, Optional\n\n\n")
        f.write("@dataclass\n")
        f.write("class TaxonomyEntry:\n")
        f.write("    code: str\n")
        f.write("    descriptive_name: str\n")
        f.write("    specialty: str\n")
        f.write("    specialization: Optional[str] = None\n")
        f.write("    provider_grouping: Optional[str] = None\n\n\n")
        f.write("TAXONOMY_MAPPING: Dict[str, TaxonomyEntry] = {}\n\n")

        # Deterministic ordering
        for code in sorted(mapping.keys()):
            entry = mapping[code]

            def esc(s: Optional[str]) -> str:
                if s is None:
                    return "None"
                return repr(s)

            f.write(f'TAXONOMY_MAPPING["{entry.code}"] = TaxonomyEntry(\n')
            f.write(f'    code="{entry.code}",\n')
            f.write(f"    descriptive_name={esc(entry.descriptive_name)},\n")
            f.write(f"    specialty={esc(entry.specialty)},\n")
            f.write(f"    specialization={esc(entry.specialization)},\n")
            f.write(f"    provider_grouping={esc(entry.provider_grouping)},\n")
            f.write(")\n\n")

        # Optional convenience helpers similar to your existing file
        f.write(
            "def get_taxonomy_specialty(code: str) -> Optional[str]:\n"
            '    """Get the specialty for a taxonomy code."""\n'
            "    entry = TAXONOMY_MAPPING.get(code)\n"
            "    return entry.specialty if entry else None\n\n\n"
        )
        f.write(
            "def get_taxonomy_specialization(code: str) -> Optional[str]:\n"
            '    """Get the specialization for a taxonomy code."""\n'
            "    entry = TAXONOMY_MAPPING.get(code)\n"
            "    return entry.specialization if entry else None\n\n\n"
        )
        f.write(
            "def search_by_specialty(specialty: str) -> List[TaxonomyEntry]:\n"
            '    """Search for all taxonomy codes matching a specialty (case-insensitive)."""\n'
            "    s = specialty.lower()\n"
            "    return [e for e in TAXONOMY_MAPPING.values() if e.specialty and e.specialty.lower() == s]\n\n\n"
        )
        f.write(
            "def search_by_name(term: str) -> List[TaxonomyEntry]:\n"
            '    """Search for taxonomy codes by descriptive name (case-insensitive substring)."""\n'
            "    t = term.lower()\n"
            "    return [e for e in TAXONOMY_MAPPING.values() if t in e.descriptive_name.lower()]\n\n\n"
        )
        f.write(
            "def get_all_specialties() -> List[str]:\n"
            '    """Return sorted list of unique specialties."""\n'
            "    return sorted({e.specialty for e in TAXONOMY_MAPPING.values() if e.specialty})\n\n\n"
        )
        f.write(
            "def get_all_codes() -> List[str]:\n"
            '    """Return sorted list of all taxonomy codes."""\n'
            "    return sorted(TAXONOMY_MAPPING.keys())\n"
        )


def main() -> None:
    pdf_path = Path("taxonomy.pdf")  # adjust if needed
    out_path = Path("taxonomy_mapping.py")

    print("=" * 60)
    print("🏥 NUCC Taxonomy Mapping Builder")
    print("=" * 60)

    text = extract_pdf_text(pdf_path)
    mapping = parse_taxonomy(text)
    write_mapping_module(mapping, out_path)

    print(f"✓ Successfully generated {out_path}")
    print(f"  Total taxonomy codes: {len(mapping)}")
    print("=" * 60)


if __name__ == "__main__":
    main()

