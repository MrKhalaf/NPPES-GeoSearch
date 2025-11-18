"""Export taxonomy mapping to various table formats (CSV, JSON, etc.).

This script exports the complete taxonomy mapping to table formats
for easy viewing and integration with other systems.
"""

import csv
import json
from pathlib import Path
from typing import List, Dict
from taxonomy_mapping import export_to_table, TAXONOMY_MAPPING


def export_to_csv(output_path: str = "taxonomy_mapping.csv") -> None:
    """Export taxonomy mapping to CSV file.
    
    Args:
        output_path: Path to output CSV file
    """
    table_data = export_to_table()
    
    if not table_data:
        print("No taxonomy data to export")
        return
    
    fieldnames = ["code", "descriptive_name", "specialty", "specialization", "provider_grouping"]
    
    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(table_data)
    
    print(f"Exported {len(table_data)} taxonomy entries to {output_path}")


def export_to_json(output_path: str = "taxonomy_mapping.json") -> None:
    """Export taxonomy mapping to JSON file.
    
    Args:
        output_path: Path to output JSON file
    """
    table_data = export_to_table()
    
    with open(output_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(table_data, jsonfile, indent=2, ensure_ascii=False)
    
    print(f"Exported {len(table_data)} taxonomy entries to {output_path}")


def print_table_summary() -> None:
    """Print a summary of the taxonomy mapping."""
    table_data = export_to_table()
    
    print(f"\n{'='*80}")
    print(f"TAXONOMY MAPPING SUMMARY")
    print(f"{'='*80}")
    print(f"Total entries: {len(table_data)}")
    print(f"\n{'Code':<15} {'Descriptive Name':<50} {'Specialty':<30}")
    print(f"{'-'*15} {'-'*50} {'-'*30}")
    
    for entry in table_data[:20]:  # Show first 20 entries
        code = entry['code']
        name = entry['descriptive_name'][:47] + "..." if len(entry['descriptive_name']) > 50 else entry['descriptive_name']
        specialty = entry['specialty'][:27] + "..." if len(entry['specialty']) > 30 else entry['specialty']
        print(f"{code:<15} {name:<50} {specialty:<30}")
    
    if len(table_data) > 20:
        print(f"\n... and {len(table_data) - 20} more entries")
    
    # Group by specialty
    specialties = {}
    for entry in table_data:
        specialty = entry['specialty']
        if specialty not in specialties:
            specialties[specialty] = []
        specialties[specialty].append(entry)
    
    print(f"\n{'='*80}")
    print(f"ENTRIES BY SPECIALTY")
    print(f"{'='*80}")
    for specialty, entries in sorted(specialties.items()):
        print(f"{specialty}: {len(entries)} entries")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        output_format = sys.argv[1].lower()
        output_path = sys.argv[2] if len(sys.argv) > 2 else None
        
        if output_format == "csv":
            export_to_csv(output_path or "taxonomy_mapping.csv")
        elif output_format == "json":
            export_to_json(output_path or "taxonomy_mapping.json")
        else:
            print(f"Unknown format: {output_format}")
            print("Usage: python export_taxonomy_table.py [csv|json] [output_path]")
    else:
        # Print summary by default
        print_table_summary()
        print("\nTo export to CSV: python export_taxonomy_table.py csv [output_path]")
        print("To export to JSON: python export_taxonomy_table.py json [output_path]")

