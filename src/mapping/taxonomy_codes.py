"""Taxonomy code definitions for healthcare specialties.

These descriptions match what the NPPES API accepts for taxonomy_description parameter.
Based on testing, the API accepts shorter, simpler descriptions.
"""

# Common taxonomy codes mapped to NPPES API-accepted descriptions
TAXONOMY_CODES = {
    "207Q00000X": "Family Medicine",
    "207R00000X": "Internal Medicine",
    "207V00000X": "Obstetrics & Gynecology",
    "208D00000X": "General Practice",
    "208G00000X": "Thoracic Surgery",
    "208M00000X": "Hospitalist",
    "208000000X": "Pediatrics",
    "204F00000X": "Neurology",
    "207T00000X": "Emergency Medicine",
    "207W00000X": "Ophthalmology",
    "207X00000X": "Orthopedic",  # API accepts "Orthopedic" not "Orthopedic Surgery"
    "207Y00000X": "Otolaryngology",
    "208100000X": "Physical Medicine & Rehabilitation",
    "208200000X": "Anesthesiology",
    "208300000X": "Psychiatry & Neurology",
    "208400000X": "Psychiatry",
    "208500000X": "Child & Adolescent Psychiatry",
    "208600000X": "Geriatric Psychiatry",
    "208800000X": "Urology",
    "208C00000X": "Colon & Rectal Surgery",
    "207RG0100X": "Gastroenterology",
    "207RC0000X": "Cardiology",
    "207N00000X": "Dermatology",
    "2085R0202X": "Radiology",
    "363A00000X": "Physician Assistant",
    "363L00000X": "Nurse Practitioner",
}
