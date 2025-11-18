"""CPT code to taxonomy code mapping."""

from typing import List, Dict, Set
from .taxonomy_mapping import get_taxonomy_name


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
    "45380": "Colonoscopy, flexible; with biopsy, single or multiple",
    "45385": "Colonoscopy, flexible; with removal of tumor(s), polyp(s), or other lesion(s) by hot biopsy forceps",
    "43239": "Esophagogastroduodenoscopy, flexible, transoral; with biopsy, single or multiple",
    "43235": "Esophagogastroduodenoscopy, flexible, transoral; diagnostic, including specimen collection",
    "27447": "Arthroplasty, knee, condyle and plateau; medial AND lateral compartments",
    "29881": "Arthroscopy, shoulder, surgical; with repair of ruptured rotator cuff",
    "29880": "Arthroscopy, knee, surgical; with meniscectomy (medial OR lateral, including any meniscal shaving)",
    "29877": "Arthroscopy, knee, surgical; debridement/shaving of articular cartilage (chondroplasty)",
    "27130": "Arthroplasty, acetabular and proximal femoral prosthetic replacement (total hip arthroplasty)",
    "66984": "Extracapsular cataract removal with insertion of intraocular lens prosthesis",
    "92012": "Ophthalmological services: medical examination and evaluation, established patient",
    "92014": "Ophthalmological services: medical examination and evaluation, established patient, comprehensive",
    "92004": "Ophthalmological services: medical examination and evaluation, new patient, comprehensive",
    "11300": "Shaving of epidermal or dermal lesion, single lesion, trunk, arms or legs",
    "11301": "Shaving of epidermal or dermal lesion, single lesion, scalp, neck, hands, feet, genitalia",
    "11302": "Shaving of epidermal or dermal lesion, single lesion, face, ears, eyelids, nose, lips, mucous membrane",
    "11303": "Shaving of epidermal or dermal lesion, single lesion, trunk, arms or legs",
    "11305": "Shaving of epidermal or dermal lesion, single lesion, scalp, neck, hands, feet, genitalia",
    "11306": "Shaving of epidermal or dermal lesion, single lesion, face, ears, eyelids, nose, lips, mucous membrane",
    "11307": "Shaving of epidermal or dermal lesion, single lesion, trunk, arms or legs",
    "11308": "Shaving of epidermal or dermal lesion, single lesion, scalp, neck, hands, feet, genitalia",
    "11310": "Shaving of epidermal or dermal lesion, single lesion, face, ears, eyelids, nose, lips, mucous membrane",
    "11311": "Shaving of epidermal or dermal lesion, single lesion, trunk, arms or legs",
    "11312": "Shaving of epidermal or dermal lesion, single lesion, scalp, neck, hands, feet, genitalia",
    "11313": "Shaving of epidermal or dermal lesion, single lesion, face, ears, eyelids, nose, lips, mucous membrane",
    "11400": "Excision, benign lesion, trunk, arms or legs; excised diameter 0.5 cm or less",
    "11401": "Excision, benign lesion, trunk, arms or legs; excised diameter 0.6 to 1.0 cm",
    "11402": "Excision, benign lesion, trunk, arms or legs; excised diameter 1.1 to 2.0 cm",
    "11403": "Excision, benign lesion, trunk, arms or legs; excised diameter 2.1 to 3.0 cm",
    "11404": "Excision, benign lesion, trunk, arms or legs; excised diameter over 3.0 cm",
    "11406": "Excision, benign lesion, scalp, neck, hands, feet, genitalia; excised diameter 0.5 cm or less",
    "11420": "Excision, benign lesion, scalp, neck, hands, feet, genitalia; excised diameter 0.6 to 1.0 cm",
    "11421": "Excision, benign lesion, scalp, neck, hands, feet, genitalia; excised diameter 1.1 to 2.0 cm",
    "11422": "Excision, benign lesion, scalp, neck, hands, feet, genitalia; excised diameter 2.1 to 3.0 cm",
    "11423": "Excision, benign lesion, scalp, neck, hands, feet, genitalia; excised diameter over 3.0 cm",
    "11440": "Excision, benign lesion, face, ears, eyelids, nose, lips, mucous membrane; excised diameter 0.5 cm or less",
    "11441": "Excision, benign lesion, face, ears, eyelids, nose, lips, mucous membrane; excised diameter 0.6 to 1.0 cm",
    "11442": "Excision, benign lesion, face, ears, eyelids, nose, lips, mucous membrane; excised diameter 1.1 to 2.0 cm",
    "11443": "Excision, benign lesion, face, ears, eyelids, nose, lips, mucous membrane; excised diameter 2.1 to 3.0 cm",
    "11444": "Excision, benign lesion, face, ears, eyelids, nose, lips, mucous membrane; excised diameter over 3.0 cm",
    "11450": "Excision of skin and subcutaneous tissue for hidradenitis, axillary; with simple repair",
    "11451": "Excision of skin and subcutaneous tissue for hidradenitis, axillary; with intermediate repair",
    "11462": "Excision of skin and subcutaneous tissue for hidradenitis, inguinal; with simple repair",
    "11463": "Excision of skin and subcutaneous tissue for hidradenitis, inguinal; with intermediate repair",
    "11470": "Excision of skin and subcutaneous tissue for hidradenitis, perianal, perineal, or umbilical; with simple repair",
    "11471": "Excision of skin and subcutaneous tissue for hidradenitis, perianal, perineal, or umbilical; with intermediate repair",
    "17000": "Destruction, benign or premalignant lesion, single lesion; first lesion",
    "17003": "Destruction, benign or premalignant lesion, single lesion; second through 14 lesions, each",
    "17004": "Destruction, benign or premalignant lesion, single lesion; 15 or more lesions",
    "17110": "Destruction, malignant lesion, trunk, arms or legs; lesion diameter 0.5 cm or less",
    "17111": "Destruction, malignant lesion, trunk, arms or legs; lesion diameter 0.6 to 1.0 cm",
    "12001": "Simple repair of superficial wounds of scalp, neck, axillae, external genitalia, trunk and/or extremities; 2.5 cm or less",
    "12002": "Simple repair of superficial wounds of scalp, neck, axillae, external genitalia, trunk and/or extremities; 2.6 cm to 7.5 cm",
    "12004": "Simple repair of superficial wounds of scalp, neck, axillae, external genitalia, trunk and/or extremities; 7.6 cm to 12.5 cm",
    "12005": "Simple repair of superficial wounds of scalp, neck, axillae, external genitalia, trunk and/or extremities; 12.6 cm to 20.0 cm",
    "12006": "Simple repair of superficial wounds of scalp, neck, axillae, external genitalia, trunk and/or extremities; 20.1 cm to 30.0 cm",
    "12007": "Simple repair of superficial wounds of scalp, neck, axillae, external genitalia, trunk and/or extremities; over 30.0 cm",
    "12011": "Simple repair of superficial wounds of face, ears, eyelids, nose, lips and/or mucous membranes; 2.5 cm or less",
    "12013": "Simple repair of superficial wounds of face, ears, eyelids, nose, lips and/or mucous membranes; 2.6 cm to 5.0 cm",
    "12014": "Simple repair of superficial wounds of face, ears, eyelids, nose, lips and/or mucous membranes; 5.1 cm to 7.5 cm",
    "12015": "Simple repair of superficial wounds of face, ears, eyelids, nose, lips and/or mucous membranes; 7.6 cm to 12.5 cm",
    "12016": "Simple repair of superficial wounds of face, ears, eyelids, nose, lips and/or mucous membranes; 12.6 cm to 20.0 cm",
    "12017": "Simple repair of superficial wounds of face, ears, eyelids, nose, lips and/or mucous membranes; 20.1 cm to 30.0 cm",
    "12018": "Simple repair of superficial wounds of face, ears, eyelids, nose, lips and/or mucous membranes; over 30.0 cm",
    "52000": "Cystoscopy, diagnostic",
    "52601": "Transurethral electrosurgical resection of prostate, including control of postoperative bleeding, complete",
    "55866": "Laparoscopy, surgical prostatectomy, retropubic radical, including nerve sparing",
    "76805": "Ultrasound, pelvic (nonobstetric)",
    "76801": "Ultrasound, pregnant uterus, real time with image documentation, fetal and maternal evaluation, first trimester",
    "58150": "Total abdominal hysterectomy (corpus and cervix), with or without removal of tube(s), with or without removal of ovary(s)",
    "58558": "Laparoscopy, surgical, with total hysterectomy, for uterus 250 g or less; with removal of tube(s) and/or ovary(s)",
    "80061": "Lipid panel",
    "80048": "Basic metabolic panel (Calcium, total)",
    "87804": "Infectious agent detection by nucleic acid (DNA or RNA); Streptococcus, group A, amplified probe technique",
    "90471": "Immunization administration (includes percutaneous, intradermal, subcutaneous, intramuscular, and jet injections); 1 vaccine (single or combination vaccine/toxoid)",
    "90472": "Immunization administration (includes percutaneous, intradermal, subcutaneous, intramuscular, and jet injections); each additional vaccine (single or combination vaccine/toxoid)",
    "90460": "Immunization administration through 18 years of age via any route of administration, with counseling by physician or other qualified health care professional; first or only component of each vaccine or toxoid administered",
    "29515": "Strapping; ankle and/or foot",
    "29200": "Strapping; chest",
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
    
    # Cardiology
    "93000": ["207RC0000X", "207Q00000X", "207R00000X"],  # ECG - Cardiology, but also general practice
    "93010": ["207RC0000X"],  # ECG interpretation and report
    "93015": ["207RC0000X"],  # Cardiovascular stress test
    "93017": ["207RC0000X"],  # Cardiovascular stress test with interpretation
    "93306": ["207RC0000X"],  # Echocardiogram, transthoracic, complete
    "93307": ["207RC0000X"],  # Echocardiogram, transthoracic, complete, with Doppler
    
    # Radiology
    "71020": ["2085R0202X", "207Q00000X", "207R00000X"],  # Chest X-ray - Radiology, but also general practice
    "70450": ["2085R0202X"],  # CT head without contrast
    "70460": ["2085R0202X"],  # CT head with contrast
    "72141": ["2085R0202X"],  # MRI cervical spine
    "72146": ["2085R0202X"],  # MRI lumbar spine
    
    # Gastroenterology
    "45378": ["207RG0100X"],  # Gastroenterology
    "45380": ["207RG0100X"],  # Colonoscopy with biopsy
    "45385": ["207RG0100X"],  # Colonoscopy with removal of lesion
    "43239": ["207RG0100X"],  # Upper GI endoscopy
    "43235": ["207RG0100X"],  # Upper GI endoscopy with biopsy
    
    # Orthopedic Surgery
    "27447": ["207X00000X"],  # Knee arthroplasty
    "29881": ["207X00000X"],  # Shoulder arthroscopy
    "29880": ["207X00000X"],  # Knee arthroscopy
    "29877": ["207X00000X"],  # Knee arthroscopy, debridement
    "27130": ["207X00000X"],  # Total hip arthroplasty
    
    # Ophthalmology
    "66984": ["207W00000X"],  # Cataract removal
    "92012": ["207W00000X"],  # Eye exam, established patient
    "92014": ["207W00000X"],  # Eye exam, established patient, comprehensive
    "92004": ["207W00000X"],  # Eye exam, new patient, comprehensive
    
    # Dermatology
    "11300": ["207N00000X"],  # Shave removal, trunk/arms/legs
    "11301": ["207N00000X"],  # Shave removal, scalp/neck/hands/feet/genitalia
    "11302": ["207N00000X"],  # Shave removal, face/ears/eyelids/nose/lips
    "11303": ["207N00000X"],  # Shave removal, trunk/arms/legs
    "11305": ["207N00000X"],  # Shave removal, scalp/neck/hands/feet/genitalia
    "11306": ["207N00000X"],  # Shave removal, face/ears/eyelids/nose/lips
    "11307": ["207N00000X"],  # Shave removal, trunk/arms/legs
    "11308": ["207N00000X"],  # Shave removal, scalp/neck/hands/feet/genitalia
    "11310": ["207N00000X"],  # Shave removal, face/ears/eyelids/nose/lips
    "11311": ["207N00000X"],  # Shave removal, trunk/arms/legs
    "11312": ["207N00000X"],  # Shave removal, scalp/neck/hands/feet/genitalia
    "11313": ["207N00000X"],  # Shave removal, face/ears/eyelids/nose/lips
    "11400": ["207N00000X"],  # Excision benign lesion, trunk/arms/legs
    "11401": ["207N00000X"],  # Excision benign lesion, trunk/arms/legs
    "11402": ["207N00000X"],  # Excision benign lesion, trunk/arms/legs
    "11403": ["207N00000X"],  # Excision benign lesion, trunk/arms/legs
    "11404": ["207N00000X"],  # Excision benign lesion, trunk/arms/legs
    "11406": ["207N00000X"],  # Excision benign lesion, scalp/neck/hands/feet/genitalia
    "11420": ["207N00000X"],  # Excision benign lesion, scalp/neck/hands/feet/genitalia
    "11421": ["207N00000X"],  # Excision benign lesion, scalp/neck/hands/feet/genitalia
    "11422": ["207N00000X"],  # Excision benign lesion, scalp/neck/hands/feet/genitalia
    "11423": ["207N00000X"],  # Excision benign lesion, scalp/neck/hands/feet/genitalia
    "11440": ["207N00000X"],  # Excision benign lesion, face/ears/eyelids/nose/lips
    "11441": ["207N00000X"],  # Excision benign lesion, face/ears/eyelids/nose/lips
    "11442": ["207N00000X"],  # Excision benign lesion, face/ears/eyelids/nose/lips
    "11443": ["207N00000X"],  # Excision benign lesion, face/ears/eyelids/nose/lips
    "11444": ["207N00000X"],  # Excision benign lesion, face/ears/eyelids/nose/lips
    "11450": ["207N00000X"],  # Excision for hidradenitis, axillary
    "11451": ["207N00000X"],  # Excision for hidradenitis, axillary
    "11462": ["207N00000X"],  # Excision for hidradenitis, inguinal
    "11463": ["207N00000X"],  # Excision for hidradenitis, inguinal
    "11470": ["207N00000X"],  # Excision for hidradenitis, perianal/perineal/umbilical
    "11471": ["207N00000X"],  # Excision for hidradenitis, perianal/perineal/umbilical
    "17000": ["207N00000X"],  # Destruction benign/premalignant lesion
    "17003": ["207N00000X"],  # Destruction benign/premalignant lesion
    "17004": ["207N00000X"],  # Destruction benign/premalignant lesion
    "17110": ["207N00000X"],  # Destruction malignant lesion
    "17111": ["207N00000X"],  # Destruction malignant lesion
    "12001": ["207N00000X", "207Q00000X", "207R00000X"],  # Simple repair - Dermatology or general practice
    "12002": ["207N00000X", "207Q00000X", "207R00000X"],
    "12004": ["207N00000X", "207Q00000X", "207R00000X"],
    "12005": ["207N00000X", "207Q00000X", "207R00000X"],
    "12006": ["207N00000X", "207Q00000X", "207R00000X"],
    "12007": ["207N00000X", "207Q00000X", "207R00000X"],
    "12011": ["207N00000X", "207Q00000X", "207R00000X"],  # Simple repair face
    "12013": ["207N00000X", "207Q00000X", "207R00000X"],
    "12014": ["207N00000X", "207Q00000X", "207R00000X"],
    "12015": ["207N00000X", "207Q00000X", "207R00000X"],
    "12016": ["207N00000X", "207Q00000X", "207R00000X"],
    "12017": ["207N00000X", "207Q00000X", "207R00000X"],
    "12018": ["207N00000X", "207Q00000X", "207R00000X"],
    
    # Urology
    "52000": ["208800000X"],  # Cystoscopy
    "52601": ["208800000X"],  # TURP
    "55866": ["208800000X"],  # Laparoscopic prostatectomy
    
    # OB/GYN
    "76805": ["207V00000X"],  # Pelvic ultrasound
    "76801": ["207V00000X"],  # OB ultrasound
    "58150": ["207V00000X"],  # Total abdominal hysterectomy
    "58558": ["207V00000X"],  # Laparoscopic hysterectomy
    
    # Lab tests - general practice
    "80061": ["207Q00000X", "207R00000X", "208D00000X"],  # Lipid panel
    "80048": ["207Q00000X", "207R00000X", "208D00000X"],  # Basic metabolic panel
    "87804": ["207Q00000X", "207R00000X", "208D00000X"],  # Strep test
    
    # Vaccines/Injections - general practice
    "90471": ["207Q00000X", "207R00000X", "208D00000X", "208000000X"],  # Vaccine administration
    "90472": ["207Q00000X", "207R00000X", "208D00000X", "208000000X"],  # Vaccine administration additional
    "90460": ["207Q00000X", "207R00000X", "208D00000X", "208000000X"],  # Vaccine with counseling
    
    # Other procedures - general practice
    "29515": ["207Q00000X", "207R00000X", "208D00000X"],  # Strapping ankle/foot
    "29200": ["207Q00000X", "207R00000X", "208D00000X"],  # Strapping chest
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
    "colonoscopy": ["207RG0100X"],
    "endoscopy": ["207RG0100X"],
    "gastroenterology": ["207RG0100X"],
    "cardiology": ["207RC0000X"],
    "ecg": ["207RC0000X"],
    "echocardiogram": ["207RC0000X"],
    "dermatology": ["207N00000X"],
    "lesion": ["207N00000X"],
    "cystoscopy": ["208800000X"],
    "urology": ["208800000X"],
    "ultrasound": ["207V00000X", "2085R0202X"],
    "hysterectomy": ["207V00000X"],
    "obstetrics": ["207V00000X"],
    "gynecology": ["207V00000X"],
    "ct": ["2085R0202X"],
    "mri": ["2085R0202X"],
    "radiology": ["2085R0202X"],
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
        
        This returns the NPPES API-accepted description for the taxonomy code.
        
        Args:
            taxonomy_code: Taxonomy code
            
        Returns:
            Specialty name (NPPES API-accepted format) or the code itself if not found
        """
        return get_taxonomy_name(taxonomy_code)
    
    def get_taxonomy_descriptions(self, taxonomy_codes: List[str]) -> List[str]:
        """Get taxonomy descriptions for a list of taxonomy codes.
        
        These descriptions are formatted to work with the NPPES API's
        taxonomy_description parameter.
        
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

