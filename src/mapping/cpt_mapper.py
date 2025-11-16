"""CPT code to taxonomy code mapping."""

from typing import List, Dict, Set
from .taxonomy_codes import TAXONOMY_CODES


# Common CPT codes with descriptions
CMS_PROCEDURES = {
    "99213": "Office or other outpatient visit for the evaluation and management of an established patient",
    "99214": "Office or other outpatient visit for the evaluation and management of an established patient",
    "99215": "Office or other outpatient visit for the evaluation and management of an established patient",
    "99203": "Office or other outpatient visit for the evaluation and management of a new patient",
    "99204": "Office or other outpatient visit for the evaluation and management of a new patient",
    "99205": "Office or other outpatient visit for the evaluation and management of a new patient",
    "99211": "Office or other outpatient visit for the evaluation and management of an established patient",
    "99212": "Office or other outpatient visit for the evaluation and management of an established patient",
    "99281": "Emergency department visit for the evaluation and management of a patient",
    "99282": "Emergency department visit for the evaluation and management of a patient",
    "99283": "Emergency department visit for the evaluation and management of a patient",
    "99284": "Emergency department visit for the evaluation and management of a patient",
    "99285": "Emergency department visit for the evaluation and management of a patient",
    "99231": "Subsequent hospital care, per day, for the evaluation and management of a patient",
    "99232": "Subsequent hospital care, per day, for the evaluation and management of a patient",
    "99233": "Subsequent hospital care, per day, for the evaluation and management of a patient",
    "90834": "Psychotherapy, 45 minutes with patient",
    "90837": "Psychotherapy, 60 minutes with patient",
    "90847": "Family psychotherapy (conjoint psychotherapy)",
    "36415": "Routine venipuncture for collection of specimen(s)",
    "80053": "Comprehensive metabolic panel",
    "85025": "Complete blood count (CBC)",
    "93000": "Electrocardiogram, routine ECG with at least 12 leads",
    "71020": "Radiologic examination, chest, 2 views, frontal and lateral",
    "45378": "Colonoscopy, flexible, proximal to splenic flexure",
    "27447": "Arthroplasty, knee, condyle and plateau; medial AND lateral compartments",
    "66984": "Extracapsular cataract removal with insertion of intraocular lens prosthesis",
}


# Procedure code rules: CPT code -> taxonomy codes
PROCEDURE_CODE_RULES: Dict[str, List[str]] = {
    # Office visits - primary care specialties
    "99213": ["207Q00000X", "207R00000X", "208D00000X"],  # Family Medicine, Internal Medicine, General Practice
    "99214": ["207Q00000X", "207R00000X", "208D00000X"],
    "99215": ["207Q00000X", "207R00000X", "208D00000X"],
    "99203": ["207Q00000X", "207R00000X", "208D00000X"],
    "99204": ["207Q00000X", "207R00000X", "208D00000X"],
    "99205": ["207Q00000X", "207R00000X", "208D00000X"],
    "99211": ["207Q00000X", "207R00000X", "208D00000X"],
    "99212": ["207Q00000X", "207R00000X", "208D00000X"],
    
    # Emergency department visits
    "99281": ["207T00000X"],  # Emergency Medicine
    "99282": ["207T00000X"],
    "99283": ["207T00000X"],
    "99284": ["207T00000X"],
    "99285": ["207T00000X"],
    
    # Hospital care
    "99231": ["207R00000X", "208M00000X"],  # Internal Medicine, Hospitalist
    "99232": ["207R00000X", "208M00000X"],
    "99233": ["207R00000X", "208M00000X"],
    
    # Psychiatry
    "90834": ["208400000X", "208500000X"],  # Psychiatry, Child & Adolescent Psychiatry
    "90837": ["208400000X", "208500000X"],
    "90847": ["208400000X", "208500000X"],
    
    # Lab work - general practice
    "36415": ["207Q00000X", "207R00000X", "208D00000X"],
    "80053": ["207Q00000X", "207R00000X", "208D00000X"],
    "85025": ["207Q00000X", "207R00000X", "208D00000X"],
    
    # Cardiology/General
    "93000": ["207Q00000X", "207R00000X"],
    
    # Radiology - general
    "71020": ["207Q00000X", "207R00000X"],
    
    # Gastroenterology
    "45378": ["207R00000X"],  # Internal Medicine (GI subspecialty)
    
    # Orthopedic Surgery
    "27447": ["207X00000X"],  # Orthopedic Surgery
    
    # Ophthalmology
    "66984": ["207W00000X"],  # Ophthalmology
}

# Keyword-based rules for fallback
KEYWORD_RULES: Dict[str, List[str]] = {
    "office": ["207Q00000X", "207R00000X", "208D00000X"],
    "emergency": ["207T00000X"],
    "hospital": ["207R00000X", "208M00000X"],
    "psych": ["208400000X"],
    "surgery": ["207X00000X"],
    "orthopedic": ["207X00000X"],
    "eye": ["207W00000X"],
    "ophthalmology": ["207W00000X"],
}

# Default fallback taxonomy codes
DEFAULT_RULES: List[str] = ["207Q00000X", "207R00000X", "208D00000X"]  # Family Medicine, Internal Medicine, General Practice


class ProcedureSpecialtyMapper:
    """Maps CPT procedure codes to taxonomy codes."""
    
    def __init__(self):
        """Initialize the mapper with procedure and keyword rules."""
        self.procedure_rules = PROCEDURE_CODE_RULES
        self.keyword_rules = KEYWORD_RULES
        self.default_rules = DEFAULT_RULES
    
    def map(self, cpt_code: str) -> List[str]:
        """Map a CPT code to taxonomy codes.
        
        Args:
            cpt_code: CPT procedure code
            
        Returns:
            List of taxonomy codes that match the CPT code
        """
        # Direct procedure code match
        if cpt_code in self.procedure_rules:
            return self.procedure_rules[cpt_code]
        
        # Keyword-based fallback
        cpt_lower = cpt_code.lower()
        description = CMS_PROCEDURES.get(cpt_code, "").lower()
        search_text = f"{cpt_lower} {description}"
        
        for keyword, taxonomy_codes in self.keyword_rules.items():
            if keyword in search_text:
                return taxonomy_codes
        
        # Default fallback
        return self.default_rules
    
    def get_all_cpt_codes(self) -> Dict[str, str]:
        """Get all available CPT codes with descriptions.
        
        Returns:
            Dictionary mapping CPT codes to descriptions
        """
        return CMS_PROCEDURES.copy()
    
    def get_taxonomy_name(self, taxonomy_code: str) -> str:
        """Get the specialty name for a taxonomy code.
        
        Args:
            taxonomy_code: Taxonomy code
            
        Returns:
            Specialty name or the code itself if not found
        """
        return TAXONOMY_CODES.get(taxonomy_code, taxonomy_code)
    
    def get_taxonomy_descriptions(self, taxonomy_codes: List[str]) -> List[str]:
        """Get taxonomy descriptions for a list of taxonomy codes.
        
        Args:
            taxonomy_codes: List of taxonomy codes
            
        Returns:
            List of taxonomy description names (for API search)
        """
        descriptions = []
        for code in taxonomy_codes:
            desc = self.get_taxonomy_name(code)
            descriptions.append(desc)
        return descriptions

