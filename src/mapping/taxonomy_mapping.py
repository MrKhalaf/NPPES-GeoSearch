"""Comprehensive taxonomy code mapping based on NUCC Taxonomy Code Set Version 24.0.

This module is auto-generated from taxonomy_24_0.pdf.
Do not edit by hand; instead, regenerate using build_taxonomy_mapping.py.
Source: Health Care Provider Taxonomy VERSION 24.0, January 2024
© 2024 American Medical Association; NUCC.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class TaxonomyEntry:
    code: str
    descriptive_name: str
    specialty: str
    specialization: Optional[str] = None
    provider_grouping: Optional[str] = None


TAXONOMY_MAPPING: Dict[str, TaxonomyEntry] = {}

TAXONOMY_MAPPING["101200000X"] = TaxonomyEntry(
    code="101200000X",
    descriptive_name='Drama therapists are trained in the intentional use of drama and theatre processes to achieve therapeutic',
    specialty='Drama Therapist',
    specialization='School',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["101Y00000X"] = TaxonomyEntry(
    code="101Y00000X",
    descriptive_name='A provider who is trained and educated in the performance of behavior health services through',
    specialty='Counselor',
    specialization='Clinical',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["101YA0400X"] = TaxonomyEntry(
    code="101YA0400X",
    descriptive_name='#Type!',
    specialty='American Association of Pastoral Counselors.',
    specialization='Addiction (Substance Use Disorder)',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["101YM0800X"] = TaxonomyEntry(
    code="101YM0800X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Mental Health',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["101YP1600X"] = TaxonomyEntry(
    code="101YP1600X",
    descriptive_name='#Type!',
    specialty='Counselor',
    specialization='Pastoral',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["101YP2500X"] = TaxonomyEntry(
    code="101YP2500X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Professional',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["101YS0200X"] = TaxonomyEntry(
    code="101YS0200X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='School',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["102L00000X"] = TaxonomyEntry(
    code="102L00000X",
    descriptive_name='Psychoanalysis is a comprehensive, theoretical framework which, when applied to a treatment process,',
    specialty='Psychoanalyst',
    specialization='School',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["102X00000X"] = TaxonomyEntry(
    code="102X00000X",
    descriptive_name='A medical or mental health professional who has attained credentials after satisfactorily completing a',
    specialty='Poetry Therapist',
    specialization='School',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["103G00000X"] = TaxonomyEntry(
    code="103G00000X",
    descriptive_name='A clinical psychologist who applies principles of assessment and intervention based upon the scientific',
    specialty='Clinical Neuropsychologist',
    specialization='Pediatric Urology',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["103GC0700X"] = TaxonomyEntry(
    code="103GC0700X",
    descriptive_name='Counselor',
    specialty='definition modified]',
    specialization='Clinical',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["103K00000X"] = TaxonomyEntry(
    code="103K00000X",
    descriptive_name="A behavior analyst is qualified by at least a master's degree and Behavior Analyst Certification Board",
    specialty='Behavior Analyst',
    specialization='Pediatric Urology',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["103T00000X"] = TaxonomyEntry(
    code="103T00000X",
    descriptive_name='A psychologist is an individual who is licensed to practice psychology which is defined as the observation,',
    specialty='Psychologist',
    specialization='School',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["103TA0400X"] = TaxonomyEntry(
    code="103TA0400X",
    descriptive_name='A psychologist with a proficiency that involves the application of psychological treatment of addiction',
    specialty='consultation. Psychological services may be rendered to individuals, families, groups and the public.',
    specialization='Addiction (Substance Use Disorder)',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["103TA0700X"] = TaxonomyEntry(
    code="103TA0700X",
    descriptive_name='A psychologist who specializes in geropsychology, which applies the knowledge and methods of',
    specialty='Additional Resources: The APA proficiency is Addiction Psychology.',
    specialization='Adult Development & Aging',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["103TB0200X"] = TaxonomyEntry(
    code="103TB0200X",
    descriptive_name='A psychologist who reflects an experimental-clinical approach distinguished by use of principles of human',
    specialty='Additional Resources: The APA specialty is "Clinical Child Psychology."',
    specialization='Cognitive & Behavioral',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["103TC0700X"] = TaxonomyEntry(
    code="103TC0700X",
    descriptive_name='A psychologist who provides continuing and comprehensive mental and behavioral health care for',
    specialty='Psychologist',
    specialization='Clinical',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["103TC1900X"] = TaxonomyEntry(
    code="103TC1900X",
    descriptive_name='A psychologist who specializes in general practice and health service. It focuses on how people function',
    specialty='Psychologist',
    specialization='Counseling',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["103TC2200X"] = TaxonomyEntry(
    code="103TC2200X",
    descriptive_name='A psychologist who develops and applies scientific knowledge to the delivery of psychological services to',
    specialty='encompasses all ages, multiple diversities and varied systems.',
    specialization='Clinical Child & Adolescent',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["103TE1000X"] = TaxonomyEntry(
    code="103TE1000X",
    descriptive_name='Exercise & Sports Specialization:',
    specialty='symptoms.',
    specialization='Educational',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["103TE1100X"] = TaxonomyEntry(
    code="103TE1100X",
    descriptive_name='A psychologist with a proficiency in sports psychology that uses psychological knowledge and skills to',
    specialty='symptoms.',
    specialization='Exercise & Sports',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["103TF0000X"] = TaxonomyEntry(
    code="103TF0000X",
    descriptive_name='A psychologist whose specialty is founded on principles of systems theory with the interpersonal system',
    specialty='Additional Resources: The APA proficiency is "Sport Psychology."',
    specialization='Family',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["103TF0200X"] = TaxonomyEntry(
    code="103TF0200X",
    descriptive_name='A psychologist whose specialty is characterized by activities primarily intended to provide professional',
    specialty='Psychologist',
    specialization='Forensic',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["103TH0004X"] = TaxonomyEntry(
    code="103TH0004X",
    descriptive_name='A psychologist who specializes in clinical health psychology that investigates and implements clinical',
    specialty='Additional Resources: The APA specialty is "Group Psychology and Group Psychotherapy."',
    specialization='Health',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["103TH0100X"] = TaxonomyEntry(
    code="103TH0100X",
    descriptive_name='A psychologist, certified/licensed at the independent practice level in his/her state, who is duly trained and',
    specialty='specialty is "Clinical Health Psychology."',
    specialization='Health Service',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["103TM1700X"] = TaxonomyEntry(
    code="103TM1700X",
    descriptive_name='Prescribing (Medical) Specialization:',
    specialty='Definition to come...',
    specialization='Men & Masculinity',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["103TM1800X"] = TaxonomyEntry(
    code="103TM1800X",
    descriptive_name='Men & Masculinity Specialization:',
    specialty='Psychologist',
    specialization='Intellectual & Developmental Disabilities',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["103TP0016X"] = TaxonomyEntry(
    code="103TP0016X",
    descriptive_name='A licensed, doctoral-level psychologist authorized to prescribe and has undergone specialized education',
    specialty='Definition to come...',
    specialization='Prescribing (Medical)',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["103TP0814X"] = TaxonomyEntry(
    code="103TP0814X",
    descriptive_name='A psychologist whose specialty is distinguished from other specialties by its body of knowledge and its',
    specialty='modified, source modified]',
    specialization='Psychoanalysis',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["103TP2700X"] = TaxonomyEntry(
    code="103TP2700X",
    descriptive_name='87 JANUARY 2024',
    specialty='modified]',
    specialization='Psychotherapy',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["103TP2701X"] = TaxonomyEntry(
    code="103TP2701X",
    descriptive_name='A psychologist who specializes in group psychology and group psychotherapy that is an evidenced-based',
    specialty='psychological expertise within the judicial and legal systems.',
    specialization='Group Psychotherapy',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["103TR0400X"] = TaxonomyEntry(
    code="103TR0400X",
    descriptive_name='A psychologist who specializes in the study and application of psychological principles on behalf of',
    specialty='Psychologist',
    specialization='Rehabilitation',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["103TS0200X"] = TaxonomyEntry(
    code="103TS0200X",
    descriptive_name='A psychologist whose specialty is concerned with the science and practice of psychology with children,',
    specialty='advocacy, with the broad goal of fostering independence and opportunity for people with disabilities.',
    specialization='School',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["103TW0100X"] = TaxonomyEntry(
    code="103TW0100X",
    descriptive_name='Social Worker',
    specialty='and psychological services that promote healthy development',
    specialization='Women',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["104100000X"] = TaxonomyEntry(
    code="104100000X",
    descriptive_name='A social worker is a person who is qualified by a Social Work degree, and licensed, certified or registered',
    specialty='Social Worker',
    specialization='Women',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["1041C0700X"] = TaxonomyEntry(
    code="1041C0700X",
    descriptive_name="A social worker who holds a master's or doctoral degree in social work from an accredited school of",
    specialty='Social Worker',
    specialization='Clinical',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["1041S0200X"] = TaxonomyEntry(
    code="1041S0200X",
    descriptive_name='#Type!',
    specialty='mental illness, emotional, or behavioral disturbances.',
    specialization='School',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["106E00000X"] = TaxonomyEntry(
    code="106E00000X",
    descriptive_name='An assistant behavior analyst is qualified by Behavior Analyst Certification Board certification and/or a',
    specialty='Assistant Behavior Analyst',
    specialization='Pediatric Urology',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["106H00000X"] = TaxonomyEntry(
    code="106H00000X",
    descriptive_name="A marriage and family therapist is a person with a master's degree in marriage and family therapy, or a",
    specialty='Marriage & Family Therapist',
    specialization='School',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["106S00000X"] = TaxonomyEntry(
    code="106S00000X",
    descriptive_name='The behavior technician is a paraprofessional who practices under the close, ongoing supervision of a',
    specialty='Behavior Technician',
    specialization='Pediatric Urology',
    provider_grouping='Behavioral Health & Social Service Providers',
)

TAXONOMY_MAPPING["111N00000X"] = TaxonomyEntry(
    code="111N00000X",
    descriptive_name='A provider qualified by a Doctor of Chiropractic (D.C.), licensed by the State and who practices',
    specialty='Chiropractor',
    specialization='School',
    provider_grouping='Chiropractic Providers',
)

TAXONOMY_MAPPING["111NI0013X"] = TaxonomyEntry(
    code="111NI0013X",
    descriptive_name='A special evaluator not involved with the medical care of the individual examinee that impartially',
    specialty='#Type!',
    specialization='Independent Medical Examiner',
    provider_grouping='Chiropractic Providers',
)

TAXONOMY_MAPPING["111NI0900X"] = TaxonomyEntry(
    code="111NI0900X",
    descriptive_name='The chiropractic internist may serve as a primary care physician or may see patients referred from other',
    specialty='Chiropractor',
    specialization='Internist',
    provider_grouping='Chiropractic Providers',
)

TAXONOMY_MAPPING["111NN0400X"] = TaxonomyEntry(
    code="111NN0400X",
    descriptive_name='Chiropractic Neurology is defined as the field of functional neurology that engages the internal - and',
    specialty='promote patient health and avoidance of disease.',
    specialization='Neurology',
    provider_grouping='Chiropractic Providers',
)

TAXONOMY_MAPPING["111NN1001X"] = TaxonomyEntry(
    code="111NN1001X",
    descriptive_name='Chiropractic Nutrition is that specialty within the chiropractic profession that deals with the overall factors',
    specialty='Source: American Chiropractic Neurology Board, 2008 & American Chiropractic Association, 2008',
    specialization='Nutrition',
    provider_grouping='Chiropractic Providers',
)

TAXONOMY_MAPPING["111NP0017X"] = TaxonomyEntry(
    code="111NP0017X",
    descriptive_name='The Pediatric Chiropractor is a chiropractor with specialized, advanced training and certification in the',
    specialty='field of the orthopedic specialty.',
    specialization='Pediatric Chiropractor',
    provider_grouping='Chiropractic Providers',
)

TAXONOMY_MAPPING["111NR0200X"] = TaxonomyEntry(
    code="111NR0200X",
    descriptive_name='Chiropractic radiology is a referral specialty that provides consultation services at the request of other',
    specialty='Chiropractor',
    specialization='Radiology',
    provider_grouping='Chiropractic Providers',
)

TAXONOMY_MAPPING["111NR0400X"] = TaxonomyEntry(
    code="111NR0400X",
    descriptive_name="Rehabilitation is the discipline focused on restoring a patient's functional abilities to pre-injury or pre-",
    specialty='and scope of practice laws.',
    specialization='Rehabilitation',
    provider_grouping='Chiropractic Providers',
)

TAXONOMY_MAPPING["111NS0005X"] = TaxonomyEntry(
    code="111NS0005X",
    descriptive_name='A sports chiropractor is uniquely trained to provide care and treatment of injuries or illness resulting from',
    specialty='Chiropractor',
    specialization='Sports Physician',
    provider_grouping='Chiropractic Providers',
)

TAXONOMY_MAPPING["111NT0100X"] = TaxonomyEntry(
    code="111NT0100X",
    descriptive_name='The NUCC recommends this code not be used. Choose a more appropriate code.',
    specialty='everything in between, using a variety of techniques and modalities.',
    specialization='Thermography',
    provider_grouping='Chiropractic Providers',
)

TAXONOMY_MAPPING["111NX0100X"] = TaxonomyEntry(
    code="111NX0100X",
    descriptive_name='Occupational Health is that specialty within the chiropractic profession that deals with the prevention and',
    specialty='Chiropractor',
    specialization='Occupational Health',
    provider_grouping='Chiropractic Providers',
)

TAXONOMY_MAPPING["111NX0800X"] = TaxonomyEntry(
    code="111NX0800X",
    descriptive_name='Chiropractic Orthopedics is defined as that branch of chiropractic medicine that includes the continued',
    specialty='services.',
    specialization='Orthopedic',
    provider_grouping='Chiropractic Providers',
)

TAXONOMY_MAPPING["122300000X"] = TaxonomyEntry(
    code="122300000X",
    descriptive_name='A dentist is a person qualified by a doctorate in dental surgery (D.D.S.) or dental medicine (D.M.D.),',
    specialty='Dentist',
    specialization='Thermography',
    provider_grouping='Dental Providers',
)

TAXONOMY_MAPPING["1223D0001X"] = TaxonomyEntry(
    code="1223D0001X",
    descriptive_name='The science and art of preventing and controlling dental diseases and promoting dental health through',
    specialty='Source: Council on Dental Education and Licensure, American Dental Association',
    specialization='Dental Public Health',
    provider_grouping='Dental Providers',
)

TAXONOMY_MAPPING["1223D0004X"] = TaxonomyEntry(
    code="1223D0004X",
    descriptive_name='A dentist who has successfully completed an accredited postdoctoral anesthesiology residency training',
    specialty='Source: Council on Dental Education and Licensure, American Dental Association',
    specialization='Dentist Anesthesiologist',
    provider_grouping='Dental Providers',
)

TAXONOMY_MAPPING["1223E0200X"] = TaxonomyEntry(
    code="1223E0200X",
    descriptive_name='The branch of dentistry that is concerned with the morphology, physiology and pathology of the human',
    specialty='examination by the American Dental Board of Anesthesiology.',
    specialization='Endodontics',
    provider_grouping='Dental Providers',
)

TAXONOMY_MAPPING["1223G0001X"] = TaxonomyEntry(
    code="1223G0001X",
    descriptive_name='A general dentist is the primary dental care provider for patients of all ages. The general dentist is',
    specialty='Dentist',
    specialization='General Practice',
    provider_grouping='Dental Providers',
)

TAXONOMY_MAPPING["1223P0106X"] = TaxonomyEntry(
    code="1223P0106X",
    descriptive_name='The specialty of dentistry and discipline of pathology that deals with the nature, identification, and',
    specialty='Source: Academy of General Dentistry',
    specialization='Oral and Maxillofacial Pathology',
    provider_grouping='Dental Providers',
)

TAXONOMY_MAPPING["1223P0221X"] = TaxonomyEntry(
    code="1223P0221X",
    descriptive_name='An age-defined specialty that provides both primary and comprehensive preventive and therapeutic oral',
    specialty='#Type!',
    specialization='Pediatric Dentistry',
    provider_grouping='Dental Providers',
)

TAXONOMY_MAPPING["1223P0300X"] = TaxonomyEntry(
    code="1223P0300X",
    descriptive_name='That specialty of dentistry which encompasses the prevention, diagnosis and treatment of diseases of the',
    specialty='Source: Council on Dental Education and Licensure, American Dental Association',
    specialization='Periodontics',
    provider_grouping='Dental Providers',
)

TAXONOMY_MAPPING["1223P0700X"] = TaxonomyEntry(
    code="1223P0700X",
    descriptive_name='That branch of dentistry pertaining to the restoration and maintenance of oral functions, comfort,',
    specialty='Dentist',
    specialization='Prosthodontics',
    provider_grouping='Dental Providers',
)

TAXONOMY_MAPPING["1223S0112X"] = TaxonomyEntry(
    code="1223S0112X",
    descriptive_name='The specialty of dentistry which includes the diagnosis, surgical and adjunctive treatment of diseases,',
    specialty='Source: Council on Dental Education and Licensure, American Dental Association',
    specialization='Oral and Maxillofacial Surgery',
    provider_grouping='Dental Providers',
)

TAXONOMY_MAPPING["1223X0008X"] = TaxonomyEntry(
    code="1223X0008X",
    descriptive_name='The specialty of dentistry and discipline of radiology concerned with the production and interpretation of',
    specialty='Source: Council on Dental Education and Licensure, American Dental Association',
    specialization='Oral and Maxillofacial Radiology',
    provider_grouping='Dental Providers',
)

TAXONOMY_MAPPING["1223X0400X"] = TaxonomyEntry(
    code="1223X0400X",
    descriptive_name='That area of dentistry concerned with the supervision, guidance and correction of the growing or mature',
    specialty='Additional Resources: American Board of Orofacial Pain, http://www.abop.net',
    specialization='Orthodontics and Dentofacial Orthopedics',
    provider_grouping='Dental Providers',
)

TAXONOMY_MAPPING["1223X2210X"] = TaxonomyEntry(
    code="1223X2210X",
    descriptive_name='A dentist who assesses, diagnoses, and treats patients with complex chronic orofacial pain and',
    specialty='Dentist',
    specialization='Orofacial Pain',
    provider_grouping='Dental Providers',
)

TAXONOMY_MAPPING["122400000X"] = TaxonomyEntry(
    code="122400000X",
    descriptive_name='A denturist is a licensed professional that serves patients with removable dental prosthetic oral health',
    specialty='Denturist',
    specialization='Prosthodontics',
    provider_grouping='Dental Providers',
)

TAXONOMY_MAPPING["124Q00000X"] = TaxonomyEntry(
    code="124Q00000X",
    descriptive_name='An individual who has completed an accredited dental hygiene education program, and an individual who',
    specialty='Dental Hygienist',
    specialization='Thermography',
    provider_grouping='Dental Providers',
)

TAXONOMY_MAPPING["125J00000X"] = TaxonomyEntry(
    code="125J00000X",
    descriptive_name='A Dental Therapist is an individual who has completed an accredited or non-accredited dental therapy',
    specialty='Dental Therapist',
    specialization='Thermography',
    provider_grouping='Dental Providers',
)

TAXONOMY_MAPPING["125K00000X"] = TaxonomyEntry(
    code="125K00000X",
    descriptive_name='An Advanced Practice Dental Therapist is:',
    specialty='Advanced Practice Dental Therapist',
    specialization='Thermography',
    provider_grouping='Dental Providers',
)

TAXONOMY_MAPPING["125Q00000X"] = TaxonomyEntry(
    code="125Q00000X",
    descriptive_name='A dentist with advanced training specializing in the recognition and treatment of oral conditions resulting',
    specialty='Oral Medicinist',
    specialization='Prosthodontics',
    provider_grouping='Dental Providers',
)

TAXONOMY_MAPPING["126800000X"] = TaxonomyEntry(
    code="126800000X",
    descriptive_name='An individual who may or may not have completed an accredited dental assisting education program and',
    specialty='Dental Assistant',
    specialization='Thermography',
    provider_grouping='Dental Providers',
)

TAXONOMY_MAPPING["126900000X"] = TaxonomyEntry(
    code="126900000X",
    descriptive_name='An individual who has the skill and knowledge in the fabrication of dental appliances, prostheses and',
    specialty='Dental Laboratory Technician',
    specialization='Thermography',
    provider_grouping='Dental Providers',
)

TAXONOMY_MAPPING["132700000X"] = TaxonomyEntry(
    code="132700000X",
    descriptive_name='A dietary manager is a trained food services professional who is charged with maintaining cost/profit',
    specialty='Dietary Manager',
    specialization='Prosthodontics',
    provider_grouping='Dietary & Nutritional Service Providers',
)

TAXONOMY_MAPPING["133N00000X"] = TaxonomyEntry(
    code="133N00000X",
    descriptive_name='A specialist in adapting and applying food and nutrient knowledge to the solution of food and nutritional',
    specialty='Nutritionist',
    specialization='Nutrition, Sports Dietetics',
    provider_grouping='Dietary & Nutritional Service Providers',
)

TAXONOMY_MAPPING["133NN1002X"] = TaxonomyEntry(
    code="133NN1002X",
    descriptive_name='#Type!',
    specialty='Facts On File Publications, 1988.',
    specialization='Nutrition, Education',
    provider_grouping='Dietary & Nutritional Service Providers',
)

TAXONOMY_MAPPING["133V00000X"] = TaxonomyEntry(
    code="133V00000X",
    descriptive_name='A Registered Dietitian (RD)/Registered Dietitian Nutritionist (RDN) is an individual uniquely trained in the',
    specialty='Dietitian, Registered',
    specialization='Prosthodontics',
    provider_grouping='Dietary & Nutritional Service Providers',
)

TAXONOMY_MAPPING["133VN1004X"] = TaxonomyEntry(
    code="133VN1004X",
    descriptive_name='An individual who is a Board Certified Specialist in Pediatric Nutrition and applies evidence-based',
    specialty='Dietitian, Registered',
    specialization='Nutrition, Pediatric',
    provider_grouping='Dietary & Nutritional Service Providers',
)

TAXONOMY_MAPPING["133VN1005X"] = TaxonomyEntry(
    code="133VN1005X",
    descriptive_name='An individual who is a Board Certified Specialist in Renal Nutrition and works directly with adult and/or',
    specialty='Source: The Commission on Dietetic Registration, https://www.cdrnet.org/certifications/specialty-',
    specialization='Nutrition, Renal',
    provider_grouping='Dietary & Nutritional Service Providers',
)

TAXONOMY_MAPPING["133VN1006X"] = TaxonomyEntry(
    code="133VN1006X",
    descriptive_name='#Type!',
    specialty='Source: The Commission on Dietetic Registration, https://www.cdrnet.org/certifications/specialty-',
    specialization='Nutrition, Metabolic',
    provider_grouping='Dietary & Nutritional Service Providers',
)

TAXONOMY_MAPPING["133VN1101X"] = TaxonomyEntry(
    code="133VN1101X",
    descriptive_name='An individual who is a Specialist in Gerontological Nutrition and provides nutrition care to promote quality',
    specialty='Dietitian, Registered',
    specialization='Nutrition, Gerontological',
    provider_grouping='Dietary & Nutritional Service Providers',
)

TAXONOMY_MAPPING["133VN1201X"] = TaxonomyEntry(
    code="133VN1201X",
    descriptive_name='An individual who is a Board Certified Specialist for Obesity and Weight Management and educates,',
    specialty='#Type!',
    specialization='Nutrition, Obesity and Weight Management',
    provider_grouping='Dietary & Nutritional Service Providers',
)

TAXONOMY_MAPPING["133VN1301X"] = TaxonomyEntry(
    code="133VN1301X",
    descriptive_name='An individual who is a Board Certified Specialist in Oncology Nutrition and provides direct nutrition care',
    specialty='Source: The Commission on Dietetic Registration, https://www.cdrnet.org/certifications/specialty-',
    specialization='Nutrition, Oncology',
    provider_grouping='Dietary & Nutritional Service Providers',
)

TAXONOMY_MAPPING["133VN1401X"] = TaxonomyEntry(
    code="133VN1401X",
    descriptive_name='An individual who is a Board Certified Specialist in Pediatric Critical Care Nutrition and applies evidence-',
    specialty='Source: The Commission on Dietetic Registration, https://www.cdrnet.org/certifications/specialty-',
    specialization='Nutrition, Pediatric Critical Care',
    provider_grouping='Dietary & Nutritional Service Providers',
)

TAXONOMY_MAPPING["133VN1501X"] = TaxonomyEntry(
    code="133VN1501X",
    descriptive_name='An individual who is a Board Certified Specialist in Sports Dietetics and applies evidence-based nutrition',
    specialty='Source: The Commission on Dietetic Registration, https://www.cdrnet.org/certifications/specialty-',
    specialization='Nutrition, Sports Dietetics',
    provider_grouping='Dietary & Nutritional Service Providers',
)

TAXONOMY_MAPPING["136A00000X"] = TaxonomyEntry(
    code="136A00000X",
    descriptive_name='A Dietetic Technician, Registered (DTR)/Nutrition and Dietetics Technician, Registered (NDTR) is an',
    specialty='Dietetic Technician, Registered',
    specialization='Prosthodontics',
    provider_grouping='Dietary & Nutritional Service Providers',
)

TAXONOMY_MAPPING["146D00000X"] = TaxonomyEntry(
    code="146D00000X",
    descriptive_name='Individuals that are specially trained to assist patients living at home with urgent/emergent situations.',
    specialty='Personal Emergency Response Attendant',
    specialization='Nutrition, Education',
    provider_grouping='Emergency Medical Service Providers',
)

TAXONOMY_MAPPING["146L00000X"] = TaxonomyEntry(
    code="146L00000X",
    descriptive_name='An EMT, Paramedic is an individual trained and certified to perform advanced life support (ALS) in',
    specialty='Emergency Medical Technician, Paramedic',
    specialization='Nutrition, Education',
    provider_grouping='Emergency Medical Service Providers',
)

TAXONOMY_MAPPING["146M00000X"] = TaxonomyEntry(
    code="146M00000X",
    descriptive_name='An Intermediate EMT is an individual trained and certified to perform intermediate life support treatment in',
    specialty='Emergency Medical Technician, Intermediate',
    specialization='Nutrition, Education',
    provider_grouping='Emergency Medical Service Providers',
)

TAXONOMY_MAPPING["146N00000X"] = TaxonomyEntry(
    code="146N00000X",
    descriptive_name='A Basic EMT is an individual trained and certified to perform basic life support treatment in medical',
    specialty='Emergency Medical Technician, Basic',
    specialization='Nutrition, Education',
    provider_grouping='Emergency Medical Service Providers',
)

TAXONOMY_MAPPING["152W00000X"] = TaxonomyEntry(
    code="152W00000X",
    descriptive_name='Doctors of optometry (ODs) are the primary health care professionals for the eye. Optometrists examine,',
    specialty='Optometrist',
    specialization='Nutrition, Education',
    provider_grouping='Emergency Medical Service Providers',
)

TAXONOMY_MAPPING["152WC0802X"] = TaxonomyEntry(
    code="152WC0802X",
    descriptive_name='The professional activities performed by an Optometrist related to the fitting of contact lenses to an eye,',
    specialty="Source: American Optometric Association (AOA), approved by the AOA's Board of Trustees, June 21,",
    specialization='Corneal and Contact Management',
    provider_grouping='Emergency Medical Service Providers',
)

TAXONOMY_MAPPING["152WL0500X"] = TaxonomyEntry(
    code="152WL0500X",
    descriptive_name='Optometrists who specialize in low-vision care having training to assess visual function, prescribe low-',
    specialty='Optometrist',
    specialization='Low Vision Rehabilitation',
    provider_grouping='Eye and Vision Services Providers',
)

TAXONOMY_MAPPING["152WP0200X"] = TaxonomyEntry(
    code="152WP0200X",
    descriptive_name='Optometrists who work in Pediatrics are concerned with the prevention, development, diagnosis, and',
    specialty='aspects of the relationship between work and vision, visual performances, eye safety, and health.',
    specialization='Pediatrics',
    provider_grouping='Eye and Vision Services Providers',
)

TAXONOMY_MAPPING["152WS0006X"] = TaxonomyEntry(
    code="152WS0006X",
    descriptive_name='An optometrist who offers services designed to care for unique vision care needs of athletes, which may',
    specialty='treatment of visual problems in children.',
    specialization='Sports Vision',
    provider_grouping='Eye and Vision Services Providers',
)

TAXONOMY_MAPPING["152WV0400X"] = TaxonomyEntry(
    code="152WV0400X",
    descriptive_name='Optometrists who specialize in vision therapy as a treatment process used to improve vision function. It',
    specialty="may include vision therapy and techniques to improve visual skills specific to the athlete's sport.",
    specialization='Vision Therapy',
    provider_grouping='Eye and Vision Services Providers',
)

TAXONOMY_MAPPING["152WX0102X"] = TaxonomyEntry(
    code="152WX0102X",
    descriptive_name='Optometrists who work in Occupational Vision, the branch of environmental optometry, consider all',
    specialty='vision devices, develop treatment plans, and recommend other vision rehabilitation services.',
    specialization='Occupational Vision',
    provider_grouping='Eye and Vision Services Providers',
)

TAXONOMY_MAPPING["156F00000X"] = TaxonomyEntry(
    code="156F00000X",
    descriptive_name='A broad category grouping different kinds of technologists and technicians. See individual definitions.',
    specialty='Technician/Technologist',
    specialization='Vision Therapy',
    provider_grouping='Eye and Vision Services Providers',
)

TAXONOMY_MAPPING["156FC0800X"] = TaxonomyEntry(
    code="156FC0800X",
    descriptive_name='An optician or other ancillary support staff person who, where authorized by state law and trained or',
    specialty='#Type!',
    specialization='Contact Lens',
    provider_grouping='Eye and Vision Services Providers',
)

TAXONOMY_MAPPING["156FC0801X"] = TaxonomyEntry(
    code="156FC0801X",
    descriptive_name='An optician or other ancillary support staff person who, where authorized by state law and trained or',
    specialty='optometrist or medical physician.',
    specialization='Contact Lens Fitter',
    provider_grouping='Eye and Vision Services Providers',
)

TAXONOMY_MAPPING["156FX1100X"] = TaxonomyEntry(
    code="156FX1100X",
    descriptive_name='An ophthalmic technician/technologist assists ophthalmologists by performing ophthalmic clinical',
    specialty='maintenance of their prosthesis.',
    specialization='Ophthalmic',
    provider_grouping='Eye and Vision Services Providers',
)

TAXONOMY_MAPPING["156FX1101X"] = TaxonomyEntry(
    code="156FX1101X",
    descriptive_name='An ophthalmic assistant assists ophthalmologists by performing duties including, but not limited to, patient',
    specialty='Technician/Technologist',
    specialization='Ophthalmic Assistant',
    provider_grouping='Eye and Vision Services Providers',
)

TAXONOMY_MAPPING["156FX1201X"] = TaxonomyEntry(
    code="156FX1201X",
    descriptive_name='An optometric assistant assists optometrists by performing duties, including but not limited to, customer',
    specialty='Optometrists. They also help customers decide which eyeglass frame or contact lenses to buy.',
    specialization='Optometric Assistant',
    provider_grouping='Eye and Vision Services Providers',
)

TAXONOMY_MAPPING["156FX1202X"] = TaxonomyEntry(
    code="156FX1202X",
    descriptive_name='An optometric technician assists optometrists by performing duties, including but not limited to, basic eye',
    specialty='service, basic eye testing, and patient education.',
    specialization='Optometric Technician',
    provider_grouping='Eye and Vision Services Providers',
)

TAXONOMY_MAPPING["156FX1700X"] = TaxonomyEntry(
    code="156FX1700X",
    descriptive_name='An ocularist is a thoroughly trained professional skilled in the art of fitting, painting, and fabricating custom',
    specialty='optometrist or medical physician.',
    specialization='Ocularist',
    provider_grouping='Eye and Vision Services Providers',
)

TAXONOMY_MAPPING["156FX1800X"] = TaxonomyEntry(
    code="156FX1800X",
    descriptive_name='Opticians help fit eyeglasses and contact lenses, following prescriptions from Ophthalmologists and',
    specialty='charting, patient education, and basic eye testing.',
    specialization='Optician',
    provider_grouping='Eye and Vision Services Providers',
)

TAXONOMY_MAPPING["156FX1900X"] = TaxonomyEntry(
    code="156FX1900X",
    descriptive_name='An orthoptist is an allied health professional skilled in evaluation and treatment of children and adults with',
    specialty='testing, diagnostic tests, and assistance with corrective lenses.',
    specialization='Orthoptist',
    provider_grouping='Eye and Vision Services Providers',
)

TAXONOMY_MAPPING["163W00000X"] = TaxonomyEntry(
    code="163W00000X",
    descriptive_name='(1) A registered nurse is a person qualified by graduation from an accredited nursing school (depending',
    specialty='Registered Nurse',
    specialization='Orthoptist',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WA0400X"] = TaxonomyEntry(
    code="163WA0400X",
    descriptive_name='#Type!',
    specialty='York: Facts On File Publications, 1988.',
    specialization='Addiction (Substance Use Disorder)',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WA2000X"] = TaxonomyEntry(
    code="163WA2000X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Administrator',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WC0200X"] = TaxonomyEntry(
    code="163WC0200X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Critical Care Medicine',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WC0400X"] = TaxonomyEntry(
    code="163WC0400X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Case Management',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WC1400X"] = TaxonomyEntry(
    code="163WC1400X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='College Health',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WC1500X"] = TaxonomyEntry(
    code="163WC1500X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Community Health',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WC1600X"] = TaxonomyEntry(
    code="163WC1600X",
    descriptive_name='#Type!',
    specialty='Registered Nurse',
    specialization='Continuing Education/Staff Development',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WC2100X"] = TaxonomyEntry(
    code="163WC2100X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Continence Care',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WC3500X"] = TaxonomyEntry(
    code="163WC3500X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Cardiac Rehabilitation',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WD0400X"] = TaxonomyEntry(
    code="163WD0400X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Diabetes Educator',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WD1100X"] = TaxonomyEntry(
    code="163WD1100X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Dialysis, Peritoneal',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WE0003X"] = TaxonomyEntry(
    code="163WE0003X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Emergency',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WE0900X"] = TaxonomyEntry(
    code="163WE0900X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Enterostomal Therapy',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WF0300X"] = TaxonomyEntry(
    code="163WF0300X",
    descriptive_name='#Type!',
    specialty='Registered Nurse',
    specialization='Flight',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WG0000X"] = TaxonomyEntry(
    code="163WG0000X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='General Practice',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WG0100X"] = TaxonomyEntry(
    code="163WG0100X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Gastroenterology',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WG0600X"] = TaxonomyEntry(
    code="163WG0600X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Gerontology',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WH0200X"] = TaxonomyEntry(
    code="163WH0200X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Home Health',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WH0500X"] = TaxonomyEntry(
    code="163WH0500X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Hemodialysis',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WH1000X"] = TaxonomyEntry(
    code="163WH1000X",
    descriptive_name='#Type!',
    specialty='Registered Nurse',
    specialization='Hospice',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WI0500X"] = TaxonomyEntry(
    code="163WI0500X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Infusion Therapy',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WI0600X"] = TaxonomyEntry(
    code="163WI0600X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Infection Control',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WL0100X"] = TaxonomyEntry(
    code="163WL0100X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Lactation Consultant',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WM0102X"] = TaxonomyEntry(
    code="163WM0102X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Maternal Newborn',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WM0705X"] = TaxonomyEntry(
    code="163WM0705X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Medical-Surgical',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WM1400X"] = TaxonomyEntry(
    code="163WM1400X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Nurse Massage Therapist (NMT)',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WN0002X"] = TaxonomyEntry(
    code="163WN0002X",
    descriptive_name='#Type!',
    specialty='Registered Nurse',
    specialization='Neonatal Intensive Care',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WN0003X"] = TaxonomyEntry(
    code="163WN0003X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Neonatal, Low-Risk',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WN0300X"] = TaxonomyEntry(
    code="163WN0300X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Nephrology',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WN0800X"] = TaxonomyEntry(
    code="163WN0800X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Neuroscience',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WN1003X"] = TaxonomyEntry(
    code="163WN1003X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Nutrition Support',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WP0000X"] = TaxonomyEntry(
    code="163WP0000X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Pain Management',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WP0200X"] = TaxonomyEntry(
    code="163WP0200X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Pediatrics',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WP0218X"] = TaxonomyEntry(
    code="163WP0218X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Pediatric Oncology',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WP0807X"] = TaxonomyEntry(
    code="163WP0807X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Psychiatric/Mental Health, Child & Adolescent',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WP0808X"] = TaxonomyEntry(
    code="163WP0808X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Psychiatric/Mental Health',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WP0809X"] = TaxonomyEntry(
    code="163WP0809X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Psychiatric/Mental Health, Adult',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WP1700X"] = TaxonomyEntry(
    code="163WP1700X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Perinatal',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WP2201X"] = TaxonomyEntry(
    code="163WP2201X",
    descriptive_name='#Type!',
    specialty='Registered Nurse',
    specialization='Ambulatory Care',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WR0006X"] = TaxonomyEntry(
    code="163WR0006X",
    descriptive_name='A perioperative registered nurse who works in collaboration with the surgeon and other health care team',
    specialty='#Type!',
    specialization='Registered Nurse First Assistant',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WR0400X"] = TaxonomyEntry(
    code="163WR0400X",
    descriptive_name='#Type!',
    specialty='Source: AORN Official Statement on RNFAs ratified by the AORN House of Delegates in 2004.',
    specialization='Rehabilitation',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WR1000X"] = TaxonomyEntry(
    code="163WR1000X",
    descriptive_name='#Type!',
    specialty='Registered Nurse',
    specialization='Reproductive Endocrinology/Infertility',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WS0121X"] = TaxonomyEntry(
    code="163WS0121X",
    descriptive_name='#Type!',
    specialty='Registered Nurse',
    specialization='Plastic Surgery',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WS0200X"] = TaxonomyEntry(
    code="163WS0200X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='School',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WU0100X"] = TaxonomyEntry(
    code="163WU0100X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Urology',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WW0000X"] = TaxonomyEntry(
    code="163WW0000X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Wound Care',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WW0101X"] = TaxonomyEntry(
    code="163WW0101X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization="Women's Health Care, Ambulatory",
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WX0002X"] = TaxonomyEntry(
    code="163WX0002X",
    descriptive_name='#Type!',
    specialty='Registered Nurse',
    specialization='Obstetric, High-Risk',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WX0003X"] = TaxonomyEntry(
    code="163WX0003X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Obstetric, Inpatient',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WX0106X"] = TaxonomyEntry(
    code="163WX0106X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Occupational Health',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WX0200X"] = TaxonomyEntry(
    code="163WX0200X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Oncology',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WX0601X"] = TaxonomyEntry(
    code="163WX0601X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Otorhinolaryngology & Head-Neck',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WX0800X"] = TaxonomyEntry(
    code="163WX0800X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Orthopedic',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WX1100X"] = TaxonomyEntry(
    code="163WX1100X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Ophthalmic',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["163WX1500X"] = TaxonomyEntry(
    code="163WX1500X",
    descriptive_name='#Type!',
    specialty='Registered Nurse',
    specialization='Ostomy Care',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["164W00000X"] = TaxonomyEntry(
    code="164W00000X",
    descriptive_name='An individual with post-high school vocational training and practical experience in the provision of nursing',
    specialty='Licensed Practical Nurse',
    specialization='Orthoptist',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["164X00000X"] = TaxonomyEntry(
    code="164X00000X",
    descriptive_name='An individual with post-high school vocational training and practical experience in the provision of nursing',
    specialty='Licensed Vocational Nurse',
    specialization='Orthoptist',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["167G00000X"] = TaxonomyEntry(
    code="167G00000X",
    descriptive_name='An individual licensed by the state board as a Psychiatric Technician based upon completion of a',
    specialty='Licensed Psychiatric Technician',
    specialization='Orthoptist',
    provider_grouping='Nursing Service Providers',
)

TAXONOMY_MAPPING["170100000X"] = TaxonomyEntry(
    code="170100000X",
    descriptive_name='A medical geneticist works in association with a medical specialist, is affiliated with a clinical genetics',
    specialty='Medical Genetics, Ph.D. Medical Genetics',
    specialization='Vehicle Modifications',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["170300000X"] = TaxonomyEntry(
    code="170300000X",
    descriptive_name='A masters trained health care provider who collects and interprets genetic family histories; assesses the',
    specialty='Genetic Counselor, MS',
    specialization='Vehicle Modifications',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["171000000X"] = TaxonomyEntry(
    code="171000000X",
    descriptive_name='Active duty military health care providers not otherwise classified who need to be separately identified for',
    specialty='Military Health Care Provider',
    specialization='Vehicle Modifications',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["1710I1002X"] = TaxonomyEntry(
    code="1710I1002X",
    descriptive_name='A Navy Independent Duty Corpsman (IDC) is an active duty Sailor who has successfully completed one',
    specialty='operational, clinical, or administrative processes.',
    specialization='Independent Duty Corpsman',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["1710I1003X"] = TaxonomyEntry(
    code="1710I1003X",
    descriptive_name='An Independent Duty Medical Technician (IDMT) is specially trained and educated to perform primary',
    specialty='forces and other supporting forces such as contractors and foreign nationals.',
    specialization='Independent Duty Medical Technicians',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["171100000X"] = TaxonomyEntry(
    code="171100000X",
    descriptive_name='An acupuncturist is a person who performs ancient therapy for alleviation of pain, anesthesia and',
    specialty='Acupuncturist',
    specialization='Personal Care Attendant',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["171400000X"] = TaxonomyEntry(
    code="171400000X",
    descriptive_name='The Health & Wellness Coach is trained in motivational theories, strategies, and communication',
    specialty='Health & Wellness Coach',
    specialization='Vehicle Modifications',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["171M00000X"] = TaxonomyEntry(
    code="171M00000X",
    descriptive_name='A person who provides case management services and assists an individual in gaining access to needed',
    specialty='Case Manager/Care Coordinator',
    specialization='Personal Care Attendant',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["171R00000X"] = TaxonomyEntry(
    code="171R00000X",
    descriptive_name='An Interpreter is a person who translates oral communication between two or more people. This includes',
    specialty='Interpreter',
    specialization='Vehicle Modifications',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["171W00000X"] = TaxonomyEntry(
    code="171W00000X",
    descriptive_name='A person who contracts to supply certain materials or do certain work for a stipulated sum; esp., one',
    specialty='Contractor',
    specialization='Personal Care Attendant',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["171WH0202X"] = TaxonomyEntry(
    code="171WH0202X",
    descriptive_name='#Type!',
    specialty='Collins + World Publishing Co., Inc., New York: 1974, p. 308',
    specialization='Home Modifications',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["171WV0202X"] = TaxonomyEntry(
    code="171WV0202X",
    descriptive_name='A contractor who makes modifications to private vehicles to accommodate a health condition.',
    specialty='#Type!',
    specialization='Vehicle Modifications',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["172A00000X"] = TaxonomyEntry(
    code="172A00000X",
    descriptive_name='A person employed to operate a motor vehicle as a carrier of persons or property.',
    specialty='Driver',
    specialization='Vehicle Modifications',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["172M00000X"] = TaxonomyEntry(
    code="172M00000X",
    descriptive_name='A practitioner of mechanotherapy examines patients by verbal inquiry, examination of the',
    specialty='Mechanotherapist',
    specialization='Vehicle Modifications',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["172P00000X"] = TaxonomyEntry(
    code="172P00000X",
    descriptive_name='Naprapathy means a branch of medicine that focuses on the evaluation and treatment of neuron-',
    specialty='Naprapath',
    specialization='Independent Duty Medical Technicians',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["172V00000X"] = TaxonomyEntry(
    code="172V00000X",
    descriptive_name='Community health workers (CHW) are lay members of communities who work either for pay or as',
    specialty='Community Health Worker',
    specialization='Personal Care Attendant',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["173000000X"] = TaxonomyEntry(
    code="173000000X",
    descriptive_name='The specialty areas of medicine concerned with matters of, and relations with, substantive law and legal',
    specialty='Legal Medicine',
    specialization='Vehicle Modifications',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["173C00000X"] = TaxonomyEntry(
    code="173C00000X",
    descriptive_name='Reflexologists perform a non-invasive complementary modality involving thumb and finger techniques to',
    specialty='Reflexologist',
    specialization='Independent Duty Medical Technicians',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["173F00000X"] = TaxonomyEntry(
    code="173F00000X",
    descriptive_name='Sleep medicine is a clinical specialty with a focus on clinical problems that require accurate diagnosis and',
    specialty='Sleep Specialist, PhD',
    specialization='Independent Duty Medical Technicians',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["174200000X"] = TaxonomyEntry(
    code="174200000X",
    descriptive_name='A public or privately owned facility providing meals to individuals traveling long distances or receiving',
    specialty='Meals',
    specialization='Nursing Care, Pediatric',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["174400000X"] = TaxonomyEntry(
    code="174400000X",
    descriptive_name='An individual educated and trained in an applied knowledge discipline used in the performance of work at',
    specialty='Specialist',
    specialization='Independent Duty Medical Technicians',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["1744G0900X"] = TaxonomyEntry(
    code="1744G0900X",
    descriptive_name='#Type!',
    specialty='Specialist',
    specialization='Graphics Designer',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["1744P3200X"] = TaxonomyEntry(
    code="1744P3200X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Prosthetics Case Management',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["1744R1102X"] = TaxonomyEntry(
    code="1744R1102X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Research Study',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["1744R1103X"] = TaxonomyEntry(
    code="1744R1103X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Research Data Abstracter/Coder',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["174H00000X"] = TaxonomyEntry(
    code="174H00000X",
    descriptive_name='Health educators work in a variety of settings providing education to individuals or groups of individuals',
    specialty='Health Educator',
    specialization='Vehicle Modifications',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["174M00000X"] = TaxonomyEntry(
    code="174M00000X",
    descriptive_name='A doctor of veterinary medicine, trained and authorized to practice veterinarian medicine and surgery.',
    specialty='Veterinarian',
    specialization='Research Study',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["174MM1900X"] = TaxonomyEntry(
    code="174MM1900X",
    descriptive_name='#Type!',
    specialty='1994, p. 1823',
    specialization='Medical Research',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["174N00000X"] = TaxonomyEntry(
    code="174N00000X",
    descriptive_name='An individual trained to provide breastfeeding assistance services to both mothers and infants. Lactation',
    specialty='Lactation Consultant, Non-RN',
    specialization='Vehicle Modifications',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["174V00000X"] = TaxonomyEntry(
    code="174V00000X",
    descriptive_name='A clinical ethicist has been trained in bioethics and ethics case consultation. The clinical ethicist',
    specialty='Clinical Ethicist',
    specialization='Personal Care Attendant',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["175F00000X"] = TaxonomyEntry(
    code="175F00000X",
    descriptive_name='Diagnoses, treats, and cares for patients, using system of practice that bases treatment of physiological',
    specialty='Naturopath',
    specialization='Independent Duty Medical Technicians',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["175L00000X"] = TaxonomyEntry(
    code="175L00000X",
    descriptive_name='A provider who is educated and trained in a system of therapeutics in which diseases are treated by',
    specialty='Homeopath',
    specialization='Vehicle Modifications',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["175M00000X"] = TaxonomyEntry(
    code="175M00000X",
    descriptive_name='A person qualified by experience and limited specialized training to provide obstetric and neo-natal care in',
    specialty='Midwife, Lay',
    specialization='Vehicle Modifications',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["175T00000X"] = TaxonomyEntry(
    code="175T00000X",
    descriptive_name='Individuals certified to perform peer support services through a training process defined by a government',
    specialty='Peer Specialist',
    specialization='Independent Duty Medical Technicians',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["176B00000X"] = TaxonomyEntry(
    code="176B00000X",
    descriptive_name='A Midwife is a trained professional with special expertise in supporting women to maintain a healthy',
    specialty='Midwife',
    specialization='Vehicle Modifications',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["176P00000X"] = TaxonomyEntry(
    code="176P00000X",
    descriptive_name='A person, usually an embalmer, whose business is to arrange for the burial or cremation of the dead and',
    specialty='Funeral Director',
    specialization='Vehicle Modifications',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["177F00000X"] = TaxonomyEntry(
    code="177F00000X",
    descriptive_name='A public or privately owned facility providing overnight lodging to individuals traveling long distances or',
    specialty='Lodging',
    specialization='Nursing Care, Pediatric',
    provider_grouping='Other Service Providers',
)

TAXONOMY_MAPPING["183500000X"] = TaxonomyEntry(
    code="183500000X",
    descriptive_name='An individual licensed by the appropriate state regulatory agency to engage in the practice of pharmacy.',
    specialty='Pharmacist',
    specialization='Medical Research',
    provider_grouping='Pharmacy Service Providers',
)

TAXONOMY_MAPPING["1835C0205X"] = TaxonomyEntry(
    code="1835C0205X",
    descriptive_name='A licensed pharmacist who has demonstrated specialized knowledge and skill in the delivery of patient',
    specialty='Source: Board of Pharmacy Specialties, www.bpsweb.org',
    specialization='Critical Care',
    provider_grouping='Pharmacy Service Providers',
)

TAXONOMY_MAPPING["1835C0206X"] = TaxonomyEntry(
    code="1835C0206X",
    descriptive_name='A licensed pharmacist who has demonstrated specialized knowledge and skill in direct patient care to',
    specialty='community.',
    specialization='Cardiology',
    provider_grouping='Pharmacy Service Providers',
)

TAXONOMY_MAPPING["1835C0207X"] = TaxonomyEntry(
    code="1835C0207X",
    descriptive_name='A licensed pharmacist who has demonstrated specialized knowledge and skill to ensure that sterile',
    specialty='Source: Board of Pharmacy Specialties, www.bpsweb.org',
    specialization='Compounded Sterile Preparations',
    provider_grouping='Pharmacy Service Providers',
)

TAXONOMY_MAPPING["1835E0208X"] = TaxonomyEntry(
    code="1835E0208X",
    descriptive_name='A licensed pharmacist who has demonstrated specialized knowledge and skill in the care for patients at',
    specialty='Pharmacist',
    specialization='Emergency Medicine',
    provider_grouping='Pharmacy Service Providers',
)

TAXONOMY_MAPPING["1835G0000X"] = TaxonomyEntry(
    code="1835G0000X",
    descriptive_name='Geriatric Specialization:',
    specialty='Source: Board of Pharmacy Specialties, www.bpsweb.org',
    specialization='General Practice',
    provider_grouping='Pharmacy Service Providers',
)

TAXONOMY_MAPPING["1835G0303X"] = TaxonomyEntry(
    code="1835G0303X",
    descriptive_name='A pharmacist who is certified in geriatric pharmacy practice is designated as a "Certified Geriatric',
    specialty='Source: Board of Pharmacy Specialties, www.bpsweb.org',
    specialization='Geriatric',
    provider_grouping='Pharmacy Service Providers',
)

TAXONOMY_MAPPING["1835I0206X"] = TaxonomyEntry(
    code="1835I0206X",
    descriptive_name='A licensed pharmacist who has demonstrated specialized knowledge and skill in the use of microbiology',
    specialty='of geriatric pharmacotherapy and the provision of pharmaceutical care to the elderly.',
    specialization='Infectious Diseases',
    provider_grouping='Pharmacy Service Providers',
)

TAXONOMY_MAPPING["1835N0905X"] = TaxonomyEntry(
    code="1835N0905X",
    descriptive_name='A licensed pharmacist who has demonstrated specialized knowledge and skill in procurement,',
    specialty='Source: Board of Pharmacy Specialties, www.bpsweb.org',
    specialization='Nuclear',
    provider_grouping='Pharmacy Service Providers',
)

TAXONOMY_MAPPING["1835N1003X"] = TaxonomyEntry(
    code="1835N1003X",
    descriptive_name='A licensed pharmacist who has demonstrated specialized knowledge and skill in maintenance and/or',
    specialty='Pharmacist',
    specialization='Nutrition Support',
    provider_grouping='Pharmacy Service Providers',
)

TAXONOMY_MAPPING["1835P0018X"] = TaxonomyEntry(
    code="1835P0018X",
    descriptive_name='Pharmacist Clinician/Clinical Pharmacy Specialist is a pharmacist with additional training and an',
    specialty='neonates through adolescents.',
    specialization='Pharmacist Clinician (PhC)/ Clinical Pharmacy Specialist',
    provider_grouping='Pharmacy Service Providers',
)

TAXONOMY_MAPPING["1835P0200X"] = TaxonomyEntry(
    code="1835P0200X",
    descriptive_name='A licensed pharmacist who has demonstrated specialized knowledge and skill in the delivery of patient',
    specialty='Source: Specialty certification and recertification program administered by Board of Pharmaceutical',
    specialization='Pediatrics',
    provider_grouping='Pharmacy Service Providers',
)

TAXONOMY_MAPPING["1835P1200X"] = TaxonomyEntry(
    code="1835P1200X",
    descriptive_name='A licensed pharmacist who has demonstrated specialized knowledge and skill in optimizing',
    specialty='disease management.',
    specialization='Pharmacotherapy',
    provider_grouping='Pharmacy Service Providers',
)

TAXONOMY_MAPPING["1835P1300X"] = TaxonomyEntry(
    code="1835P1300X",
    descriptive_name='A licensed pharmacist who has demonstrated specialized knowledge and skill in optimizing care of',
    specialty='Pharmacist',
    specialization='Psychiatric',
    provider_grouping='Pharmacy Service Providers',
)

TAXONOMY_MAPPING["1835P2201X"] = TaxonomyEntry(
    code="1835P2201X",
    descriptive_name='A licensed pharmacist who has demonstrated specialized knowledge and skill in the provision of',
    specialty='Source: Adapted from National Association of Boards of Pharmacy Model State Pharmacy Act, Article 1,',
    specialization='Ambulatory Care',
    provider_grouping='Pharmacy Service Providers',
)

TAXONOMY_MAPPING["1835S0206X"] = TaxonomyEntry(
    code="1835S0206X",
    descriptive_name='A licensed pharmacist who has demonstrated specialized knowledge and skill delivering direct patient',
    specialty='Source: Specialty certification and recertification program administered by Board of Pharmaceutical',
    specialization='Solid Organ Transplant',
    provider_grouping='Pharmacy Service Providers',
)

TAXONOMY_MAPPING["1835X0200X"] = TaxonomyEntry(
    code="1835X0200X",
    descriptive_name='A licensed pharmacist who has demonstrated specialized knowledge and skill in developing,',
    specialty='Source: Specialty certification and recertification program administered by Board of Pharmaceutical',
    specialization='Oncology',
    provider_grouping='Pharmacy Service Providers',
)

TAXONOMY_MAPPING["183700000X"] = TaxonomyEntry(
    code="183700000X",
    descriptive_name='A person who works under the direct supervision of a licensed pharmacist and performs many pharmacy-',
    specialty='Pharmacy Technician',
    specialization='Solid Organ Transplant',
    provider_grouping='Pharmacy Service Providers',
)

TAXONOMY_MAPPING["193200000X"] = TaxonomyEntry(
    code="193200000X",
    descriptive_name='A business group of one or more individual practitioners, who practice with different areas of',
    specialty='Multi-Specialty',
    specialization='Orthoptist',
    provider_grouping='Group',
)

TAXONOMY_MAPPING["193400000X"] = TaxonomyEntry(
    code="193400000X",
    descriptive_name='A business group of one or more individual practitioners, all of who practice with the same area of',
    specialty='Single Specialty',
    specialization='Orthoptist',
    provider_grouping='Group',
)

TAXONOMY_MAPPING["202C00000X"] = TaxonomyEntry(
    code="202C00000X",
    descriptive_name='A special evaluator not involved with the medical care of the individual examinee that impartially',
    specialty='Independent Medical Examiner',
    specialization='Sports Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["202D00000X"] = TaxonomyEntry(
    code="202D00000X",
    descriptive_name='A physician who specializes in the treatment of the whole person through prevention and treatment based',
    specialty='Integrative Medicine',
    specialization='Sports Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["202K00000X"] = TaxonomyEntry(
    code="202K00000X",
    descriptive_name='Phlebology is the medical discipline that involves the diagnosis and treatment of venous disorders,',
    specialty='Phlebology',
    specialization='Sports Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["204C00000X"] = TaxonomyEntry(
    code="204C00000X",
    descriptive_name='A Neuromusculoskeletal Medicine and Osteopathic Manipulative Medicine physician trained to be',
    specialty='Neuromusculoskeletal Medicine, Sports Medicine',
    specialization='Ph.D. Medical Genetics',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["204D00000X"] = TaxonomyEntry(
    code="204D00000X",
    descriptive_name='The Neuromusculoskeletal Medicine and Osteopathic Manipulative Medicine physician directs special',
    specialty='Neuromusculoskeletal Medicine & OMM',
    specialization='Ph.D. Medical Genetics',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["204E00000X"] = TaxonomyEntry(
    code="204E00000X",
    descriptive_name='Oral and maxillofacial surgeons are trained to recognize and treat a wide spectrum of diseases, injuries',
    specialty='Oral & Maxillofacial Surgery',
    specialization='Uveitis and Ocular Inflammatory Disease',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["204F00000X"] = TaxonomyEntry(
    code="204F00000X",
    descriptive_name='A surgeon who specializes in transplant surgery.',
    specialty='Transplant Surgery',
    specialization='Vascular Surgery',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["204R00000X"] = TaxonomyEntry(
    code="204R00000X",
    descriptive_name='Electrodiagnostic medicine is the medical subspecialty that applies neurophysiologic techniques to',
    specialty='Electrodiagnostic Medicine',
    specialization='Procedural Dermatology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207K00000X"] = TaxonomyEntry(
    code="207K00000X",
    descriptive_name='An allergist-immunologist is trained in evaluation, physical and laboratory diagnosis, and management of',
    specialty='Allergy & Immunology',
    specialization=None,
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207KA0200X"] = TaxonomyEntry(
    code="207KA0200X",
    descriptive_name='A physician who specializes in the diagnosis, treatment, and management of allergies.',
    specialty='allergy/immunology and pediatric rheumatology; and allergy/immunology and adult rheumatology.',
    specialization='Allergy',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207KI0005X"] = TaxonomyEntry(
    code="207KI0005X",
    descriptive_name='An allergy and immunology physician who specializes in clinical and laboratory immunology disease',
    specialty='Source: National Uniform Claim Committee',
    specialization='Clinical & Laboratory Immunology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207L00000X"] = TaxonomyEntry(
    code="207L00000X",
    descriptive_name='An anesthesiologist is trained to provide pain relief and maintenance, or restoration, of a stable condition',
    specialty='Anesthesiology',
    specialization='Clinical & Laboratory Immunology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207LA0401X"] = TaxonomyEntry(
    code="207LA0401X",
    descriptive_name='An anesthesiologist who specializes in the diagnosis and treatment of addictions.',
    specialty='Anesthesiology.',
    specialization='Addiction Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207LC0200X"] = TaxonomyEntry(
    code="207LC0200X",
    descriptive_name='An anesthesiologist, who specializes in critical care medicine diagnoses, treats and supports patients with',
    specialty='American Osteopathic Board of Anesthesiology.',
    specialization='Critical Care Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207LH0002X"] = TaxonomyEntry(
    code="207LH0002X",
    descriptive_name='An anesthesiologist with special knowledge and skills to prevent and relieve the suffering experienced by',
    specialty='Anesthesiology',
    specialization='Hospice and Palliative Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207LP2900X"] = TaxonomyEntry(
    code="207LP2900X",
    descriptive_name='An anesthesiologist who provides a high level of care, either as a primary physician or consultant, for',
    specialty='patient; and legal and ethical decision making in end-of-life care.',
    specialization='Pain Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207LP3000X"] = TaxonomyEntry(
    code="207LP3000X",
    descriptive_name='An anesthesiologist who has had additional skill and experience in and is primarily concerned with the',
    specialty='Anesthesiology.',
    specialization='Pediatric Anesthesiology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207N00000X"] = TaxonomyEntry(
    code="207N00000X",
    descriptive_name='A dermatologist is trained to diagnose and treat pediatric and adult patients with benign and malignant',
    specialty='Dermatology',
    specialization='Pediatric Anesthesiology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207ND0101X"] = TaxonomyEntry(
    code="207ND0101X",
    descriptive_name='The highly-trained surgeons that perform Mohs Micrographic Surgery are specialists both in dermatology',
    specialty='Dermatology.',
    specialization='MOHS-Micrographic Surgery',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207ND0900X"] = TaxonomyEntry(
    code="207ND0900X",
    descriptive_name='A dermatopathologist has the expertise to diagnose and monitor diseases of the skin including infectious,',
    specialty='http://www.abderm.org/ Board certification is provided by the American Board of Dermatology.',
    specialization='Dermatopathology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207NI0002X"] = TaxonomyEntry(
    code="207NI0002X",
    descriptive_name='A dermatologist who utilizes various specialized laboratory procedures to diagnose disorders',
    specialty='Dermatology',
    specialization='Clinical & Laboratory Dermatological Immunology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207NP0225X"] = TaxonomyEntry(
    code="207NP0225X",
    descriptive_name='A pediatric dermatologist has, through additional special training, developed expertise in the treatment of',
    specialty='Dermatology',
    specialization='Pediatric Dermatology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207NS0135X"] = TaxonomyEntry(
    code="207NS0135X",
    descriptive_name='Procedural Dermatology, a subspecialty of Dermatology, encompassing a wide variety of surgical',
    specialty='Accredited Residency Program Requirements: None.',
    specialization='Procedural Dermatology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207P00000X"] = TaxonomyEntry(
    code="207P00000X",
    descriptive_name='An emergency physician focuses on the immediate decision making and action necessary to prevent',
    specialty='Emergency Medicine',
    specialization='Procedural Dermatology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207PE0004X"] = TaxonomyEntry(
    code="207PE0004X",
    descriptive_name='An emergency medicine physician who specializes in non-hospital based emergency medical services',
    specialty='Board of Emergency Medicine.',
    specialization='Emergency Medical Services',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207PE0005X"] = TaxonomyEntry(
    code="207PE0005X",
    descriptive_name='A specialist who treats decompression illness and diving accident cases and uses hyperbaric oxygen',
    specialty='Board of Emergency Medicine.',
    specialization='Undersea and Hyperbaric Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207PH0002X"] = TaxonomyEntry(
    code="207PH0002X",
    descriptive_name='An emergency medicine physician with special knowledge and skills to prevent and relieve the suffering',
    specialty='Osteopathic Board of Emergency Medicine.',
    specialization='Hospice and Palliative Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207PP0204X"] = TaxonomyEntry(
    code="207PP0204X",
    descriptive_name='Pediatric Emergency Medicine is a clinical subspecialty that focuses on the care of the acutely ill or',
    specialty='Board of Emergency Medicine.',
    specialization='Pediatric Emergency Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207PS0010X"] = TaxonomyEntry(
    code="207PS0010X",
    descriptive_name='An emergency physician with special knowledge in sports medicine is responsible for continuous care in',
    specialty='Emergency Medicine',
    specialization='Sports Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207PT0002X"] = TaxonomyEntry(
    code="207PT0002X",
    descriptive_name='Medical toxicologists are physicians who specialize in the prevention, evaluation, treatment and',
    specialty='Emergency Medicine',
    specialization='Medical Toxicology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207Q00000X"] = TaxonomyEntry(
    code="207Q00000X",
    descriptive_name='Family Medicine is the medical specialty which is concerned with the total health care of the individual',
    specialty='Family Medicine',
    specialization='Undersea and Hyperbaric Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207QA0000X"] = TaxonomyEntry(
    code="207QA0000X",
    descriptive_name='A family medicine physician with multidisciplinary training in the unique physical, psychological and social',
    specialty='American Osteopathic Board of Family Physicians.',
    specialization='Adolescent Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207QA0401X"] = TaxonomyEntry(
    code="207QA0401X",
    descriptive_name='A family medicine physician who specializes in the diagnosis and treatment of addictions.',
    specialty='Family Physicians or the American Board of Family Medicine.',
    specialization='Addiction Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207QA0505X"] = TaxonomyEntry(
    code="207QA0505X",
    descriptive_name='The NUCC recommends this code not be used. Choose a more appropriate code.',
    specialty='Family Medicine',
    specialization='Adult Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207QB0002X"] = TaxonomyEntry(
    code="207QB0002X",
    descriptive_name='A physician who specializes in the treatment of obesity demonstrates competency in and a thorough',
    specialty='Family Medicine',
    specialization='Obesity Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207QG0300X"] = TaxonomyEntry(
    code="207QG0300X",
    descriptive_name='A family medicine physician with special knowledge of the aging process and special skills in the',
    specialty='#Type!',
    specialization='Geriatric Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207QH0002X"] = TaxonomyEntry(
    code="207QH0002X",
    descriptive_name='A family medicine physician with special knowledge and skills to prevent and relieve the suffering',
    specialty='Family Medicine.',
    specialization='Hospice and Palliative Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207QS0010X"] = TaxonomyEntry(
    code="207QS0010X",
    descriptive_name='A family medicine physician that is trained to be responsible for continuous care in the field of sports',
    specialty='sleep related movement disorders.',
    specialization='Sports Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207QS1201X"] = TaxonomyEntry(
    code="207QS1201X",
    descriptive_name='A Family Medicine Physician who practices Sleep Medicine is certified in the subspecialty of sleep',
    specialty='definition modified] Additional Resource: American Society of Bariatric Physicians, www.asbp.org.',
    specialization='Sleep Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207R00000X"] = TaxonomyEntry(
    code="207R00000X",
    descriptive_name='A physician who provides long-term, comprehensive care in the office and the hospital, managing both',
    specialty='Internal Medicine',
    specialization='Sports Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207RA0000X"] = TaxonomyEntry(
    code="207RA0000X",
    descriptive_name='An internist who specializes in adolescent medicine is a multi-disciplinary healthcare specialist trained in',
    specialty='Additional Resources: http://www.osteopathic.org/certification',
    specialization='Adolescent Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207RA0001X"] = TaxonomyEntry(
    code="207RA0001X",
    descriptive_name='Specialists in Advanced Heart Failure and Transplant Cardiology would participate in the inpatient and',
    specialty='hypertension.',
    specialization='Advanced Heart Failure and Transplant Cardiology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207RA0002X"] = TaxonomyEntry(
    code="207RA0002X",
    descriptive_name='A physician who specializes in the care and treatment of adults with congenital heart disease. Adult',
    specialty='Internal Medicine',
    specialization='Adult Congenital Heart Disease',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207RA0201X"] = TaxonomyEntry(
    code="207RA0201X",
    descriptive_name='An internist doctor of osteopathy that specializes in the treatment of allergy and immunologic disorders. A',
    specialty='devices, and end-of-life care for patients with end-stage heart failure.',
    specialization='Allergy & Immunology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207RA0401X"] = TaxonomyEntry(
    code="207RA0401X",
    descriptive_name='An internist doctor of osteopathy that specializes in the treatment of addiction disorders. A doctor of',
    specialty='Internal Medicine.',
    specialization='Addiction Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207RB0002X"] = TaxonomyEntry(
    code="207RB0002X",
    descriptive_name='A physician who specializes in the treatment of obesity demonstrates competency in and a thorough',
    specialty='Internal Medicine.',
    specialization='Obesity Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207RC0000X"] = TaxonomyEntry(
    code="207RC0000X",
    descriptive_name='An internist who specializes in diseases of the heart and blood vessels and manages complex cardiac',
    specialty='Additional Resources: http://www.osteopathic.org/certification',
    specialization='Cardiovascular Disease',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207RC0001X"] = TaxonomyEntry(
    code="207RC0001X",
    descriptive_name='A field of special interest within the subspecialty of cardiovascular disease, specialty of Internal Medicine,',
    specialty='Medicine.',
    specialization='Clinical Cardiac Electrophysiology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207RC0200X"] = TaxonomyEntry(
    code="207RC0200X",
    descriptive_name='An internist who diagnoses, treats and supports patients with multiple organ dysfunction. This specialist',
    specialty='Internal Medicine.',
    specialization='Critical Care Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207RE0101X"] = TaxonomyEntry(
    code="207RE0101X",
    descriptive_name='An internist who concentrates on disorders of the internal (endocrine) glands such as the thyroid and',
    specialty='Internal Medicine',
    specialization='Endocrinology, Diabetes & Metabolism',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207RG0100X"] = TaxonomyEntry(
    code="207RG0100X",
    descriptive_name='An internist who specializes in diagnosis and treatment of diseases of the digestive organs including the',
    specialty='Internal Medicine.',
    specialization='Gastroenterology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207RG0300X"] = TaxonomyEntry(
    code="207RG0300X",
    descriptive_name='An internist who has special knowledge of the aging process and special skills in the diagnostic,',
    specialty='Internal Medicine',
    specialization='Geriatric Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207RH0000X"] = TaxonomyEntry(
    code="207RH0000X",
    descriptive_name='An internist with additional training who specializes in diseases of the blood, spleen and lymph. This',
    specialty='Internal Medicine.',
    specialization='Hematology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207RH0002X"] = TaxonomyEntry(
    code="207RH0002X",
    descriptive_name='An internal medicine physician with special knowledge and skills to prevent and relieve the suffering',
    specialty='ACGME Accredited Residency Program Requirements: None',
    specialization='Hospice and Palliative Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207RH0003X"] = TaxonomyEntry(
    code="207RH0003X",
    descriptive_name='An internist doctor of osteopathy that specializes in the treatment of the combination of hematology and',
    specialty='Internal Medicine.',
    specialization='Hematology & Oncology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207RH0005X"] = TaxonomyEntry(
    code="207RH0005X",
    descriptive_name='A Hypertension Specialist is a physician who concentrates on all aspects of the diagnosis and treatment',
    specialty='of the imminently dying patient; and legal and ethical decision making in end-of-life care.',
    specialization='Hypertension Specialist',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207RI0001X"] = TaxonomyEntry(
    code="207RI0001X",
    descriptive_name='An internal medicine physician who specializes in clinical and laboratory immunology disease',
    specialty='Internal Medicine',
    specialization='Clinical & Laboratory Immunology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207RI0008X"] = TaxonomyEntry(
    code="207RI0008X",
    descriptive_name='The discipline of Hepatology encompasses the structure, function, and diseases of the liver and biliary',
    specialty='Internal Medicine',
    specialization='Hepatology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207RI0011X"] = TaxonomyEntry(
    code="207RI0011X",
    descriptive_name='An area of medicine within the subspecialty of cardiology, which uses specialized imaging and other',
    specialty='Internal Medicine.',
    specialization='Interventional Cardiology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207RI0200X"] = TaxonomyEntry(
    code="207RI0200X",
    descriptive_name='An internist who deals with infectious diseases of all types and in all organ systems. Conditions requiring',
    specialty='Internal Medicine',
    specialization='Infectious Disease',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207RM1200X"] = TaxonomyEntry(
    code="207RM1200X",
    descriptive_name='The NUCC recommends this code not be used. Choose a more appropriate code.',
    specialty='ABMS Approved Subspecialty Certificate (Internal Medicine)',
    specialization='Magnetic Resonance Imaging (MRI)',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207RN0300X"] = TaxonomyEntry(
    code="207RN0300X",
    descriptive_name='An internist who treats disorders of the kidney, high blood pressure, fluid and mineral balance and dialysis',
    specialty='consults with surgeons and radiotherapists on other treatments for cancer.',
    specialization='Nephrology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207RP1001X"] = TaxonomyEntry(
    code="207RP1001X",
    descriptive_name='An internist who treats diseases of the lungs and airways. The pulmonologist diagnoses and treats',
    specialty='Internal Medicine',
    specialization='Pulmonary Disease',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207RR0500X"] = TaxonomyEntry(
    code="207RR0500X",
    descriptive_name='An internist who treats diseases of joints, muscle, bones and tendons. This specialist diagnoses and',
    specialty='Internal Medicine.',
    specialization='Rheumatology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207RS0010X"] = TaxonomyEntry(
    code="207RS0010X",
    descriptive_name='An internist trained to be responsible for continuous care in the field of sports medicine, not only for the',
    specialty='Internal Medicine',
    specialization='Sports Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207RS0012X"] = TaxonomyEntry(
    code="207RS0012X",
    descriptive_name='An Internist who practices Sleep Medicine is certified in the subspecialty of sleep medicine and',
    specialty='Internal Medicine.',
    specialization='Sleep Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207RT0003X"] = TaxonomyEntry(
    code="207RT0003X",
    descriptive_name='An internist with special knowledge and the skill required of a gastroenterologist to care for patients prior',
    specialty='Internal Medicine.',
    specialization='Transplant Hepatology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207RX0202X"] = TaxonomyEntry(
    code="207RX0202X",
    descriptive_name='An internist who specializes in the diagnosis and treatment of all types of cancer and other benign and',
    specialty='Internal Medicine',
    specialization='Medical Oncology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207SC0300X"] = TaxonomyEntry(
    code="207SC0300X",
    descriptive_name='A clinical cytogeneticist demonstrates competence in providing laboratory diagnostic and clinical',
    specialty='Board of Medical Genetics.',
    specialization='Clinical Cytogenetics',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207SG0201X"] = TaxonomyEntry(
    code="207SG0201X",
    descriptive_name='A clinical geneticist demonstrates competence in providing comprehensive diagnostic, management and',
    specialty='Medical Genetics',
    specialization='Clinical Genetics (M.D.)',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207SG0202X"] = TaxonomyEntry(
    code="207SG0202X",
    descriptive_name='A clinical biochemical geneticist demonstrates competence in performing and interpreting biochemical',
    specialty='Medical Genetics',
    specialization='Clinical Biochemical Genetics',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207SG0203X"] = TaxonomyEntry(
    code="207SG0203X",
    descriptive_name='A clinical molecular geneticist demonstrates competence in performing and interpreting molecular',
    specialty='Board of Medical Genetics.',
    specialization='Clinical Molecular Genetics',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207SG0205X"] = TaxonomyEntry(
    code="207SG0205X",
    descriptive_name='A medical geneticist works in association with a medical specialist, is affiliated with a clinical genetics',
    specialty='Medical Genetics',
    specialization='Ph.D. Medical Genetics',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207SG0207X"] = TaxonomyEntry(
    code="207SG0207X",
    descriptive_name='A medical biochemical geneticist specializes in the diagnosis, evaluation, prevention, and treatment of',
    specialty='Board of Medical Genetics.',
    specialization='Medical Biochemical Genetics',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207SM0001X"] = TaxonomyEntry(
    code="207SM0001X",
    descriptive_name='A board certified subspecialty, the molecular genetic pathologist is expert in the principles, theory and',
    specialty='Training does not include those skills and knowledge necessary to direct a clinical laboratory.',
    specialization='Molecular Genetic Pathology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207T00000X"] = TaxonomyEntry(
    code="207T00000X",
    descriptive_name='A neurological surgeon provides the operative and non-operative management (i.e., prevention,',
    specialty='Neurological Surgery',
    specialization='Ph.D. Medical Genetics',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207U00000X"] = TaxonomyEntry(
    code="207U00000X",
    descriptive_name='A nuclear medicine specialist employs the properties of radioactive atoms and molecules in the diagnosis',
    specialty='Nuclear Medicine',
    specialization='Ph.D. Medical Genetics',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207UN0901X"] = TaxonomyEntry(
    code="207UN0901X",
    descriptive_name='A nuclear medicine physician who specializes in nuclear cardiology.',
    specialty='Nuclear Medicine',
    specialization='Nuclear Cardiology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207UN0902X"] = TaxonomyEntry(
    code="207UN0902X",
    descriptive_name='A nuclear medicine physician who specializes in nuclear imaging and therapy.',
    specialty='American Osteopathic Board of Nuclear Medicine.',
    specialization='Nuclear Imaging & Therapy',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207UN0903X"] = TaxonomyEntry(
    code="207UN0903X",
    descriptive_name='A nuclear medicine physician who specializes in in vivo and in vitro nuclear medicine.',
    specialty='Board certification for Medical Doctors (MDs) is provided by the American Board of Nuclear Medicine.',
    specialization='In Vivo & In Vitro Nuclear Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207V00000X"] = TaxonomyEntry(
    code="207V00000X",
    descriptive_name='An obstetrician/gynecologist possesses special knowledge, skills and professional capability in the',
    specialty='Obstetrics & Gynecology',
    specialization='Nuclear Imaging & Therapy',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207VB0002X"] = TaxonomyEntry(
    code="207VB0002X",
    descriptive_name='A physician who specializes in the treatment of obesity demonstrates competency in and a thorough',
    specialty='Osteopathic Board of Obstetrics and Gynecology.',
    specialization='Obesity Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207VC0200X"] = TaxonomyEntry(
    code="207VC0200X",
    descriptive_name='An obstetrician/gynecologist, who specializes in critical care medicine diagnoses, treats and supports',
    specialty='Obstetrics & Gynecology',
    specialization='Critical Care Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207VC0300X"] = TaxonomyEntry(
    code="207VC0300X",
    descriptive_name='A complex family planning physician specializes in the diagnosis and treatment of individuals with',
    specialty='Osteopathic Board of Obstetrics and Gynecology.',
    specialization='Complex Family Planning',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207VE0102X"] = TaxonomyEntry(
    code="207VE0102X",
    descriptive_name='An obstetrician/gynecologist who is capable of managing complex problems relating to reproductive',
    specialty='Obstetrics & Gynecology',
    specialization='Reproductive Endocrinology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207VF0040X"] = TaxonomyEntry(
    code="207VF0040X",
    descriptive_name='A subspecialist in Female Pelvic Medicine and Reconstructive Surgery is a physician in Urology or',
    specialty='Osteopathic Board of Obstetrics and Gynecology.',
    specialization='Female Pelvic Medicine and Reconstructive Surgery',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207VG0400X"] = TaxonomyEntry(
    code="207VG0400X",
    descriptive_name='A physician who specializes in diagnosis, treatment, and management of patients with gynecologic',
    specialty='Osteopathic Board of Obstetrics and Gynecology.',
    specialization='Gynecology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207VH0002X"] = TaxonomyEntry(
    code="207VH0002X",
    descriptive_name='An obstetrician/gynecologist with special knowledge and skills to prevent and relieve the suffering',
    specialty='Source: National Uniform Claim Committee',
    specialization='Hospice and Palliative Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207VM0101X"] = TaxonomyEntry(
    code="207VM0101X",
    descriptive_name='An obstetrician/gynecologist who cares for, or provides consultation on, patients with complications of',
    specialty='Obstetrics & Gynecology',
    specialization='Maternal & Fetal Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207VX0000X"] = TaxonomyEntry(
    code="207VX0000X",
    descriptive_name='A physician who specializes in diagnosis, treatment, and management of patients with obstetric',
    specialty='definition modified] Additional Resource: American Society of Bariatric Physicians, www.asbp.org.',
    specialization='Obstetrics',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207VX0201X"] = TaxonomyEntry(
    code="207VX0201X",
    descriptive_name='An obstetrician/gynecologist who provides consultation and comprehensive management of patients with',
    specialty='Obstetrics & Gynecology',
    specialization='Gynecologic Oncology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207W00000X"] = TaxonomyEntry(
    code="207W00000X",
    descriptive_name='An ophthalmologist has the knowledge and professional skills needed to provide comprehensive eye and',
    specialty='Ophthalmology',
    specialization='Reproductive Endocrinology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207WX0009X"] = TaxonomyEntry(
    code="207WX0009X",
    descriptive_name='An ophthalmologist who specializes in the treatment of glaucoma and other disorders related to increased',
    specialty='Ophthalmology',
    specialization='Glaucoma Specialist',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207WX0107X"] = TaxonomyEntry(
    code="207WX0107X",
    descriptive_name='An ophthalmologist who specializes in the diagnosis and treatment of vitreoretinal diseases.',
    specialty='Ophthalmology',
    specialization='Retina Specialist',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207WX0108X"] = TaxonomyEntry(
    code="207WX0108X",
    descriptive_name='An ophthalmologist who specializes in the treatment of intraocular inflammation, scleritis, keratitis and',
    specialty='Ophthalmology, www.aupo.org.',
    specialization='Uveitis and Ocular Inflammatory Disease',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207WX0109X"] = TaxonomyEntry(
    code="207WX0109X",
    descriptive_name='A neuro-ophthalmologist is a subspecialist of ophthalmology. This physician evaluates, treats, and',
    specialty='Association of University Professors of Ophthalmology, www.aupo.org',
    specialization='Neuro-ophthalmology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207WX0110X"] = TaxonomyEntry(
    code="207WX0110X",
    descriptive_name='An ophthalmologist who specializes in pediatric ophthalmology and strabismus management. The',
    specialty='structures of the face and neck.',
    specialization='Pediatric Ophthalmology and Strabismus Specialist',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207WX0120X"] = TaxonomyEntry(
    code="207WX0120X",
    descriptive_name='An ophthalmologist who specializes in diseases of the cornea, sclera, eyelids, conjunctiva, and anterior',
    specialty='Ophthalmology and Otolaryngology.',
    specialization='Cornea and External Diseases Specialist',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207WX0200X"] = TaxonomyEntry(
    code="207WX0200X",
    descriptive_name='A physician who specializes in oculofacial plastic and reconstructive surgery. This subspecialty combines',
    specialty='Additional Resources: Association of University Professors of Ophthalmology, www.aupo.org.',
    specialization='Ophthalmic Plastic and Reconstructive Surgery',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207X00000X"] = TaxonomyEntry(
    code="207X00000X",
    descriptive_name='An orthopaedic surgeon is trained in the preservation, investigation and restoration of the form and',
    specialty='Orthopaedic Surgery',
    specialization='Uveitis and Ocular Inflammatory Disease',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207XP3100X"] = TaxonomyEntry(
    code="207XP3100X",
    descriptive_name='An orthopedic surgeon who has additional training and experience in diagnosing, treating and managing',
    specialty='Orthopaedic Surgery',
    specialization='Pediatric Orthopaedic Surgery',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207XS0106X"] = TaxonomyEntry(
    code="207XS0106X",
    descriptive_name='An orthopaedic surgeon trained in the investigation, preservation and restoration by medical, surgical and',
    specialty='Orthopaedic Surgery',
    specialization='Hand Surgery',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207XS0114X"] = TaxonomyEntry(
    code="207XS0114X",
    descriptive_name='Recognized by several state medical boards as a fellowship subspecialty program of orthopaedic surgery,',
    specialty='Board of Orthopaedic Surgery.',
    specialization='Adult Reconstructive Orthopaedic Surgery',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207XS0117X"] = TaxonomyEntry(
    code="207XS0117X",
    descriptive_name='Recognized by several state medical boards as a fellowship subspecialty program of orthopaedic surgery,',
    specialty='Board of Orthopaedic Surgery.',
    specialization='Orthopaedic Surgery of the Spine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207XX0004X"] = TaxonomyEntry(
    code="207XX0004X",
    descriptive_name='Recognized by several state medical boards as a fellowship subspecialty program of orthopaedic surgery,',
    specialty='http://www.abos.org/. Separate board certification is not currently offered.',
    specialization='Foot and Ankle Surgery',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207XX0005X"] = TaxonomyEntry(
    code="207XX0005X",
    descriptive_name='An orthopaedic surgeon trained in sports medicine provides appropriate care for all structures of the',
    specialty='bones.',
    specialization='Sports Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207XX0801X"] = TaxonomyEntry(
    code="207XX0801X",
    descriptive_name='Recognized by several state medical boards as a fellowship subspecialty program of orthopaedic surgery,',
    specialty='http://www.abos.org/. Separate board certification is not currently offered.',
    specialization='Orthopaedic Trauma',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207Y00000X"] = TaxonomyEntry(
    code="207Y00000X",
    descriptive_name='An otolaryngologist-head and neck surgeon provides comprehensive medical and surgical care for',
    specialty='Otolaryngology',
    specialization='Sports Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207YP0228X"] = TaxonomyEntry(
    code="207YP0228X",
    descriptive_name='A pediatric otolaryngologist has special expertise in the management of infants and children with',
    specialty='Board of Otolaryngology.',
    specialization='Pediatric Otolaryngology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207YS0012X"] = TaxonomyEntry(
    code="207YS0012X",
    descriptive_name='An Otolaryngologist who practices Sleep Medicine is certified in the subspecialty of sleep medicine and',
    specialty='subspecialty of Otolaryngology/Facial Plastic Surgery (see Taxonomy Code 207YX0905X)',
    specialization='Sleep Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207YS0123X"] = TaxonomyEntry(
    code="207YS0123X",
    descriptive_name='An otolaryngologist who specializes in facial plastic surgery.',
    specialty='Ophthalmology and Otolaryngology.',
    specialization='Facial Plastic Surgery',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207YX0007X"] = TaxonomyEntry(
    code="207YX0007X",
    descriptive_name='An otolaryngologist with additional training in plastic and reconstructive procedures within the head, face,',
    specialty='Otolaryngology',
    specialization='Plastic Surgery within the Head & Neck',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207YX0602X"] = TaxonomyEntry(
    code="207YX0602X",
    descriptive_name='An otolaryngologist who specializes in the diagnosis and treatment of otolaryngic allergies and other',
    specialty='Board of Ophthalmology and Otolaryngology.',
    specialization='Otolaryngic Allergy',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207YX0901X"] = TaxonomyEntry(
    code="207YX0901X",
    descriptive_name='An otolaryngologist who treats diseases of the ear and temporal bone, including disorders of hearing and',
    specialty='Ophthalmology and Otolaryngology.',
    specialization='Otology & Neurotology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207YX0905X"] = TaxonomyEntry(
    code="207YX0905X",
    descriptive_name='An otolaryngologist who specializes in the diagnosis and surgical treatment of head and neck conditions.',
    specialty='Otolaryngology',
    specialization='Otolaryngology/Facial Plastic Surgery',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207ZB0001X"] = TaxonomyEntry(
    code="207ZB0001X",
    descriptive_name='A physician who specializes in blood banking/transfusion medicine is responsible for the maintenance of',
    specialty='pathology may be combined with some of the subspecialty certifications.',
    specialization='Blood Banking & Transfusion Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207ZC0006X"] = TaxonomyEntry(
    code="207ZC0006X",
    descriptive_name='A pathologist deals with the causes and nature of disease and contributes to diagnosis, prognosis and',
    specialty='Pathology',
    specialization='Clinical Pathology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207ZC0008X"] = TaxonomyEntry(
    code="207ZC0008X",
    descriptive_name='Physicians who practice Clinical Informatics collaborate with other health care and information technology',
    specialty='Pathology. The Certification is NO longer provided.',
    specialization='Clinical Informatics',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207ZC0500X"] = TaxonomyEntry(
    code="207ZC0500X",
    descriptive_name='A cytopathologist is an anatomic pathologist trained in the diagnosis of human disease by means of the',
    specialty='Pathology',
    specialization='Cytopathology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207ZD0900X"] = TaxonomyEntry(
    code="207ZD0900X",
    descriptive_name='A dermatopathologist is an expert in diagnosing and monitoring diseases of the skin including infectious,',
    specialty='Board certification for Medical Doctors (MDs) is provided by the American Board of Pathology.',
    specialization='Dermatopathology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207ZF0201X"] = TaxonomyEntry(
    code="207ZF0201X",
    descriptive_name='A forensic pathologist is expert in investigating and evaluating cases of sudden, unexpected, suspicious',
    specialty='Requirements: None.',
    specialization='Forensic Pathology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207ZH0000X"] = TaxonomyEntry(
    code="207ZH0000X",
    descriptive_name='A hematopathologist is expert in diseases that affect blood cells, blood clotting mechanisms, bone',
    specialty='Pathology',
    specialization='Hematology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207ZI0100X"] = TaxonomyEntry(
    code="207ZI0100X",
    descriptive_name='A pathologist who specializes in the diagnosis of immunologic diseases.',
    specialty='Pathology. The Certification is NO longer provided.',
    specialization='Immunopathology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207ZM0300X"] = TaxonomyEntry(
    code="207ZM0300X",
    descriptive_name='A medical microbiologist is expert in the isolation and identification of microbial agents that cause',
    specialty='American Osteopathic Board of Pathology.',
    specialization='Medical Microbiology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207ZN0500X"] = TaxonomyEntry(
    code="207ZN0500X",
    descriptive_name='A neuropathologist is expert in the diagnosis of diseases of the nervous system and skeletal muscles and',
    specialty='ACGME Accredited Residency Program Requirements: Proposal under development.',
    specialization='Neuropathology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207ZP0007X"] = TaxonomyEntry(
    code="207ZP0007X",
    descriptive_name='A molecular genetic pathologist is expert in the principles, theory and technologies of molecular biology',
    specialty='Pathology',
    specialization='Molecular Genetic Pathology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207ZP0101X"] = TaxonomyEntry(
    code="207ZP0101X",
    descriptive_name='A pathologist deals with the causes and nature of disease and contributes to diagnosis, prognosis and',
    specialty='Pathology',
    specialization='Anatomic Pathology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207ZP0102X"] = TaxonomyEntry(
    code="207ZP0102X",
    descriptive_name='A pathologist deals with the causes and nature of disease and contributes to diagnosis, prognosis and',
    specialty='Pathology',
    specialization='Anatomic Pathology & Clinical Pathology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207ZP0104X"] = TaxonomyEntry(
    code="207ZP0104X",
    descriptive_name='A chemical pathologist has expertise in the biochemistry of the human body as it applies to the',
    specialty='Pathology',
    specialization='Chemical Pathology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207ZP0105X"] = TaxonomyEntry(
    code="207ZP0105X",
    descriptive_name='A pathologist deals with the causes and nature of disease and contributes to diagnosis, prognosis and',
    specialty='combined with some of the subspecialty certifications.',
    specialization='Clinical Pathology/Laboratory Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["207ZP0213X"] = TaxonomyEntry(
    code="207ZP0213X",
    descriptive_name='A pediatric pathologist is expert in the laboratory diagnosis of diseases that occur during fetal growth,',
    specialty='Pathology. The Certification is NO longer provided.',
    specialization='Pediatric Pathology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["208000000X"] = TaxonomyEntry(
    code="208000000X",
    descriptive_name='A pediatrician is concerned with the physical, emotional and social health of children from birth to young',
    specialty='Pediatrics',
    specialization='Pediatric Pathology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2080A0000X"] = TaxonomyEntry(
    code="2080A0000X",
    descriptive_name='A pediatrician who specializes in adolescent medicine is a multi-disciplinary healthcare specialist trained',
    specialty='Pediatrics.',
    specialization='Adolescent Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2080B0002X"] = TaxonomyEntry(
    code="2080B0002X",
    descriptive_name='A physician who specializes in the treatment of obesity demonstrates competency in and a thorough',
    specialty='Pediatrics',
    specialization='Obesity Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2080C0008X"] = TaxonomyEntry(
    code="2080C0008X",
    descriptive_name='A Child Abuse Pediatrician serves as a resource to children, families and communities by accurately',
    specialty='Pediatrics.',
    specialization='Child Abuse Pediatrics',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2080H0002X"] = TaxonomyEntry(
    code="2080H0002X",
    descriptive_name='A pediatrician with special knowledge and skills to prevent and relieve the suffering experienced by',
    specialty='American Board of Pediatrics.',
    specialization='Hospice and Palliative Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2080I0007X"] = TaxonomyEntry(
    code="2080I0007X",
    descriptive_name='A pediatrician who specializes in clinical and laboratory immunology disease management.',
    specialty='Pediatrics',
    specialization='Clinical & Laboratory Immunology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2080N0001X"] = TaxonomyEntry(
    code="2080N0001X",
    descriptive_name='A pediatrician who is the principal care provider for sick newborn infants. Clinical expertise is used for',
    specialty='Approved Subspecialty Certificates (Emergency Medicine) (Pediatrics) (Preventive Medicine)',
    specialization='Neonatal-Perinatal Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2080P0006X"] = TaxonomyEntry(
    code="2080P0006X",
    descriptive_name='A developmental-behavioral specialist is a pediatrician with special training and experience who aims to',
    specialty='Additional Resources: A certification was, but is no longer issued by the American Board of Pediatrics.',
    specialization='Developmental - Behavioral Pediatrics',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2080P0008X"] = TaxonomyEntry(
    code="2080P0008X",
    descriptive_name='A pediatrician who specializes in the treatment of individuals with developmental delays and learning',
    specialty='Pediatrics.',
    specialization='Neurodevelopmental Disabilities',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2080P0201X"] = TaxonomyEntry(
    code="2080P0201X",
    descriptive_name='A pediatrician who specializes in the diagnosis and treatment of allergies, allergic reactions, and',
    specialty='American Society of Bariatric Physicians, www.asbp.org.',
    specialization='Pediatric Allergy/Immunology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2080P0202X"] = TaxonomyEntry(
    code="2080P0202X",
    descriptive_name='A pediatric cardiologist provides comprehensive care to patients with cardiovascular problems. This',
    specialty='Osteopathic Board of Pediatrics.',
    specialization='Pediatric Cardiology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2080P0203X"] = TaxonomyEntry(
    code="2080P0203X",
    descriptive_name='A pediatrician expert in advanced life support for children from the term or near-term neonate to the',
    specialty='Pediatrics',
    specialization='Pediatric Critical Care Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2080P0204X"] = TaxonomyEntry(
    code="2080P0204X",
    descriptive_name='A pediatrician who has special qualifications to manage emergencies in infants and children.',
    specialty='(Pediatrics)',
    specialization='Pediatric Emergency Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2080P0205X"] = TaxonomyEntry(
    code="2080P0205X",
    descriptive_name='A pediatrician who provides expert care to infants, children and adolescents who have diseases that',
    specialty='Board certification for Medical Doctors (MDs) is provided by the American Board of Pediatrics.',
    specialization='Pediatric Endocrinology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2080P0206X"] = TaxonomyEntry(
    code="2080P0206X",
    descriptive_name='A pediatrician who specializes in the diagnosis and treatment of diseases of the digestive systems of',
    specialty='Pediatrics',
    specialization='Pediatric Gastroenterology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2080P0207X"] = TaxonomyEntry(
    code="2080P0207X",
    descriptive_name='A pediatrician trained in the combination of pediatrics, hematology and oncology to recognize and',
    specialty='Board certification for Medical Doctors (MDs) is provided by the American Board of Pediatrics.',
    specialization='Pediatric Hematology-Oncology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2080P0208X"] = TaxonomyEntry(
    code="2080P0208X",
    descriptive_name='A pediatrician trained to care for children in the diagnosis, treatment and prevention of infectious',
    specialty='Pediatrics. The Certification is no longer offered.',
    specialization='Pediatric Infectious Diseases',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2080P0210X"] = TaxonomyEntry(
    code="2080P0210X",
    descriptive_name='A pediatrician who deals with the normal and abnormal development and maturation of the kidney and',
    specialty='Pediatrics',
    specialization='Pediatric Nephrology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2080P0214X"] = TaxonomyEntry(
    code="2080P0214X",
    descriptive_name='A pediatrician dedicated to the prevention and treatment of all respiratory diseases affecting infants,',
    specialty='Pediatrics. The Certification is no longer offered.',
    specialization='Pediatric Pulmonology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2080P0216X"] = TaxonomyEntry(
    code="2080P0216X",
    descriptive_name='A pediatrician who treats diseases of joints, muscle, bones and tendons. A pediatric rheumatologist',
    specialty='Pediatrics. The Certification is no longer offered.',
    specialization='Pediatric Rheumatology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2080S0010X"] = TaxonomyEntry(
    code="2080S0010X",
    descriptive_name='A pediatrician who is responsible for continuous care in the field of sports medicine, not only for the',
    specialty='related movement disorders.',
    specialization='Sports Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2080S0012X"] = TaxonomyEntry(
    code="2080S0012X",
    descriptive_name='A Pediatrician who practices Sleep Medicine is certified in the subspecialty of sleep medicine and',
    specialty='Doctors (MDs) is provided by the American Board of Pediatrics.',
    specialization='Sleep Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2080T0002X"] = TaxonomyEntry(
    code="2080T0002X",
    descriptive_name='Medical toxicologists are physicians that specialize in the prevention, evaluation, treatment and',
    specialty='Pediatrics',
    specialization='Medical Toxicology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2080T0004X"] = TaxonomyEntry(
    code="2080T0004X",
    descriptive_name='A pediatrician with expertise in transplant hepatology encompasses the special knowledge and skill',
    specialty='Pediatrics',
    specialization='Pediatric Transplant Hepatology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["208100000X"] = TaxonomyEntry(
    code="208100000X",
    descriptive_name='Physical medicine and rehabilitation, also referred to as rehabilitation medicine, is the medical specialty',
    specialty='Physical Medicine & Rehabilitation',
    specialization='Sports Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2081H0002X"] = TaxonomyEntry(
    code="2081H0002X",
    descriptive_name='A physical medicine and rehabilitation physician with special knowledge and skills to prevent and relieve',
    specialty='new]',
    specialization='Hospice and Palliative Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2081N0008X"] = TaxonomyEntry(
    code="2081N0008X",
    descriptive_name='A physician who specializes in neuromuscular medicine possesses specialized knowledge in the science,',
    specialty='life care.',
    specialization='Neuromuscular Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2081P0004X"] = TaxonomyEntry(
    code="2081P0004X",
    descriptive_name='A physician who addresses the prevention, diagnosis, treatment and management of traumatic spinal',
    specialty='ABMS in 1999. ACGME Accredited Residency Program Requirements: Early discussions underway',
    specialization='Spinal Cord Injury Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2081P0010X"] = TaxonomyEntry(
    code="2081P0010X",
    descriptive_name='A physiatrist who utilizes an interdisciplinary approach and addresses the prevention, diagnosis,',
    specialty='development.',
    specialization='Pediatric Rehabilitation Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2081P0301X"] = TaxonomyEntry(
    code="2081P0301X",
    descriptive_name='A Brain Injury Medicine physician specializes in disorders of brain function due to injury and disease.',
    specialty='Physical Medicine & Rehabilitation',
    specialization='Brain Injury Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2081P2900X"] = TaxonomyEntry(
    code="2081P2900X",
    descriptive_name='A physician who provides a high level of care, either as a primary physician or consultant, for patients',
    specialty='Physical Medicine & Rehabilitation',
    specialization='Pain Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2081S0010X"] = TaxonomyEntry(
    code="2081S0010X",
    descriptive_name='A physician who specializes in Sports Medicine is responsible for continuous care related to the',
    specialty='Physical Medicine & Rehabilitation',
    specialization='Sports Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["208200000X"] = TaxonomyEntry(
    code="208200000X",
    descriptive_name='A plastic surgeon deals with the repair, reconstruction or replacement of physical defects of form or',
    specialty='Plastic Surgery',
    specialization='Sports Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2082S0099X"] = TaxonomyEntry(
    code="2082S0099X",
    descriptive_name='A plastic surgeon with additional training in plastic and reconstructive procedures within the head, face,',
    specialty='Board of Plastic Surgery.',
    specialization='Plastic Surgery Within the Head and Neck',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2082S0105X"] = TaxonomyEntry(
    code="2082S0105X",
    descriptive_name='A plastic surgeon with additional training in the investigation, preservation, and restoration by medical,',
    specialty='Plastic Surgery',
    specialization='Surgery of the Hand',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2083A0100X"] = TaxonomyEntry(
    code="2083A0100X",
    descriptive_name='Aerospace medicine focuses on the clinical care, research, and operational support of the health, safety,',
    specialty='evaluation, diagnosis, treatment, and recovery of persons with the disease of addiction.',
    specialization='Aerospace Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2083A0300X"] = TaxonomyEntry(
    code="2083A0300X",
    descriptive_name='A physician engaged in the subspecialty practice of Addiction Medicine who specializes in the prevention,',
    specialty='Preventive Medicine',
    specialization='Addiction Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2083B0002X"] = TaxonomyEntry(
    code="2083B0002X",
    descriptive_name='A physician who specializes in the treatment of obesity demonstrates competency in and a thorough',
    specialty='American Board of Preventive Medicine.',
    specialization='Obesity Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2083C0008X"] = TaxonomyEntry(
    code="2083C0008X",
    descriptive_name='Physicians who practice Clinical Informatics collaborate with other health care and information technology',
    specialty='Preventive Medicine',
    specialization='Clinical Informatics',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2083P0011X"] = TaxonomyEntry(
    code="2083P0011X",
    descriptive_name='A specialist who treats decompression illness and diving accident cases and uses hyperbaric oxygen',
    specialty='Osteopathic Board of Preventive Medicine.',
    specialization='Undersea and Hyperbaric Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2083P0500X"] = TaxonomyEntry(
    code="2083P0500X",
    descriptive_name='A preventive medicine physician who specializes in preventive medicine/occupational-environmental',
    specialty='American Board of Preventive Medicine.',
    specialization='Preventive Medicine/Occupational Environmental Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2083P0901X"] = TaxonomyEntry(
    code="2083P0901X",
    descriptive_name='Public health and general preventive medicine focuses on promoting health, preventing disease, and',
    specialty='Medicine.',
    specialization='Public Health & General Preventive Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2083S0010X"] = TaxonomyEntry(
    code="2083S0010X",
    descriptive_name='A preventive medicine physician who specializes in the diagnosis and treatment of sports related',
    specialty='Preventive Medicine',
    specialization='Sports Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2083T0002X"] = TaxonomyEntry(
    code="2083T0002X",
    descriptive_name='Medical toxicologists are physicians who specialize in the prevention, evaluation, treatment and',
    specialty='American Board of Preventive Medicine, www.theabpm.org',
    specialization='Medical Toxicology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2083X0100X"] = TaxonomyEntry(
    code="2083X0100X",
    descriptive_name='Occupational medicine focuses on the health of workers, including the ability to perform work; the',
    specialty='Preventive Medicine',
    specialization='Occupational Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2084A0401X"] = TaxonomyEntry(
    code="2084A0401X",
    descriptive_name='A doctor of osteopathy board eligible/certified in the field of Psychiatry by the American Osteopathic',
    specialty='Psychiatry & Neurology',
    specialization='Addiction Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2084A2900X"] = TaxonomyEntry(
    code="2084A2900X",
    descriptive_name='The medical subspecialty of Neurocritical Care is devoted to the comprehensive, multisystem care of the',
    specialty='of the imminently dying patient; and legal and ethical decision making in end-of-life care.',
    specialization='Neurocritical Care',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2084B0002X"] = TaxonomyEntry(
    code="2084B0002X",
    descriptive_name='A physician who specializes in the treatment of obesity demonstrates competency in and a thorough',
    specialty='certification for Medical Doctors (MDs) is provided by the American Board of Psychiatry and Neurology',
    specialization='Obesity Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2084B0040X"] = TaxonomyEntry(
    code="2084B0040X",
    descriptive_name='Behavioral Neurology & Neuropsychiatry is a medical subspecialty involving the diagnosis and treatment',
    specialty='Psychiatry & Neurology',
    specialization='Behavioral Neurology & Neuropsychiatry',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2084D0003X"] = TaxonomyEntry(
    code="2084D0003X",
    descriptive_name='A licensed physician, who has completed a residency program in Neurology, and who has additional',
    specialty='Psychiatry & Neurology',
    specialization='Diagnostic Neuroimaging',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2084E0001X"] = TaxonomyEntry(
    code="2084E0001X",
    descriptive_name='Epilepsy is a subspecialty of neurology focused on the diagnosis and treatment of patients with epilepsy,',
    specialty='neuroimaging.',
    specialization='Epilepsy',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2084F0202X"] = TaxonomyEntry(
    code="2084F0202X",
    descriptive_name='Forensic Psychiatry is a subspecialty with psychiatric focus on interrelationships with civil, criminal and',
    specialty='that provides comprehensive care of the patient.',
    specialization='Forensic Psychiatry',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2084H0002X"] = TaxonomyEntry(
    code="2084H0002X",
    descriptive_name='A psychiatrist or neurologist with special knowledge and skills to prevent and relieve the suffering',
    specialty='Psychiatry & Neurology',
    specialization='Hospice and Palliative Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2084N0008X"] = TaxonomyEntry(
    code="2084N0008X",
    descriptive_name='A neurologist or child neurologist who specializes in the diagnosis and management of disorders of nerve,',
    specialty='definition]',
    specialization='Neuromuscular Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2084N0400X"] = TaxonomyEntry(
    code="2084N0400X",
    descriptive_name='A Neurologist specializes in the diagnosis and treatment of diseases or impaired function of the brain,',
    specialty='Source: National Uniform Claim Committee, www.nucc.org',
    specialization='Neurology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2084N0402X"] = TaxonomyEntry(
    code="2084N0402X",
    descriptive_name='A Child Neurologist specializes in neurology with special skills in diagnosis and treatment of neurologic',
    specialty='Psychiatry & Neurology',
    specialization='Neurology with Special Qualifications in Child Neurology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2084N0600X"] = TaxonomyEntry(
    code="2084N0600X",
    descriptive_name='Clinical Neurophysiology is a subspecialty with psychiatric or neurologic expertise in the diagnosis and',
    specialty='definition]',
    specialization='Clinical Neurophysiology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2084P0005X"] = TaxonomyEntry(
    code="2084P0005X",
    descriptive_name='A neurologist who specializes in the treatment of individuals with developmental delays and learning',
    specialty='Source: Adapted from the United Council for Neurologic Subspecialties website definition at:',
    specialization='Neurodevelopmental Disabilities',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2084P0015X"] = TaxonomyEntry(
    code="2084P0015X",
    descriptive_name='Psychosomatic Medicine is subspecialty in the diagnosis and treatment of psychiatric disorders and',
    specialty='definition]',
    specialization='Psychosomatic Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2084P0301X"] = TaxonomyEntry(
    code="2084P0301X",
    descriptive_name='A Brain Injury Medicine physician specializes in disorders of brain function due to injury and disease.',
    specialty='Academy of Neurology, www.aan.com.',
    specialization='Brain Injury Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2084P0800X"] = TaxonomyEntry(
    code="2084P0800X",
    descriptive_name='A Psychiatrist specializes in the prevention, diagnosis, and treatment of mental disorders, emotional',
    specialty='ACGME Accredited Residency Program Requirements: None.',
    specialization='Psychiatry',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2084P0802X"] = TaxonomyEntry(
    code="2084P0802X",
    descriptive_name='Addiction Psychiatry is a subspecialty of psychiatry that focuses on evaluation and treatment of',
    specialty='Additional Resources: http://www.osteopathic.org/certification',
    specialization='Addiction Psychiatry',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2084P0804X"] = TaxonomyEntry(
    code="2084P0804X",
    descriptive_name='Child & Adolescent Psychiatry is a subspecialty of psychiatry with additional skills and training in the',
    specialty='new]',
    specialization='Child & Adolescent Psychiatry',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2084P0805X"] = TaxonomyEntry(
    code="2084P0805X",
    descriptive_name='Geriatric Psychiatry is a subspecialty with psychiatric expertise in prevention, evaluation, diagnosis and',
    specialty='definition]',
    specialization='Geriatric Psychiatry',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2084P2900X"] = TaxonomyEntry(
    code="2084P2900X",
    descriptive_name='A neurologist, child neurologists or psychiatrist who provides a high level of care, either as a primary',
    specialty='Psychiatry & Neurology',
    specialization='Pain Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2084S0010X"] = TaxonomyEntry(
    code="2084S0010X",
    descriptive_name='A psychiatrist or neurologist who specializes in the diagnosis and treatment of sports related conditions',
    specialty='sleep related movement disorders.',
    specialization='Sports Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2084S0012X"] = TaxonomyEntry(
    code="2084S0012X",
    descriptive_name='A Psychiatrist or Neurologist who practices Sleep Medicine is certified in the subspecialty of sleep',
    specialty='Psychiatry & Neurology',
    specialization='Sleep Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2084V0102X"] = TaxonomyEntry(
    code="2084V0102X",
    descriptive_name='Vascular Neurology is a subspecialty in the evaluation, prevention, treatment and recovery from vascular',
    specialty='American Osteopathic Board of Neurology and Psychiatry.',
    specialization='Vascular Neurology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2085B0100X"] = TaxonomyEntry(
    code="2085B0100X",
    descriptive_name='A Radiology doctor of Osteopathy that specializes in Body Imaging.',
    specialty='Radiology',
    specialization='Body Imaging',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2085D0003X"] = TaxonomyEntry(
    code="2085D0003X",
    descriptive_name='A licensed physician, who has completed a residency program in Neurology, and who has additional',
    specialty='Radiology',
    specialization='Diagnostic Neuroimaging',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2085H0002X"] = TaxonomyEntry(
    code="2085H0002X",
    descriptive_name='A radiologist with special knowledge and skills to prevent and relieve the suffering experienced by',
    specialty='Radiology',
    specialization='Hospice and Palliative Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2085N0700X"] = TaxonomyEntry(
    code="2085N0700X",
    descriptive_name='A radiologist who diagnoses and treats diseases utilizing imaging procedures as they relate to the brain,',
    specialty='patient; and legal and ethical decision making in end-of-life care.',
    specialization='Neuroradiology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2085N0904X"] = TaxonomyEntry(
    code="2085N0904X",
    descriptive_name='A radiologist who is involved in the analysis and imaging of radionuclides and radiolabeled substances in',
    specialty='Radiology.',
    specialization='Nuclear Radiology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2085P0229X"] = TaxonomyEntry(
    code="2085P0229X",
    descriptive_name='A radiologist who is proficient in all forms of diagnostic imaging as it pertains to the treatment of diseases',
    specialty='Radiology',
    specialization='Pediatric Radiology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2085R0001X"] = TaxonomyEntry(
    code="2085R0001X",
    descriptive_name='A radiologist who deals with the therapeutic applications of radiant energy and its modifiers and the study',
    specialty='Radiology.',
    specialization='Radiation Oncology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2085R0202X"] = TaxonomyEntry(
    code="2085R0202X",
    descriptive_name='A radiologist who utilizes x-ray, radionuclides, ultrasound and electromagnetic radiation to diagnose and',
    specialty='neuroimaging.',
    specialization='Diagnostic Radiology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2085R0203X"] = TaxonomyEntry(
    code="2085R0203X",
    descriptive_name='#Type!',
    specialty='Radiology',
    specialization='Therapeutic Radiology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2085R0204X"] = TaxonomyEntry(
    code="2085R0204X",
    descriptive_name='A radiologist who diagnoses and treats diseases by various radiologic imaging modalities. These include',
    specialty='#Type!',
    specialization='Vascular & Interventional Radiology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2085R0205X"] = TaxonomyEntry(
    code="2085R0205X",
    descriptive_name='A radiological physicist deals with the diagnostic and therapeutic applications of roentgen rays, gamma',
    specialty='http://www.osteopathic.org/certification',
    specialization='Radiological Physics',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2085U0001X"] = TaxonomyEntry(
    code="2085U0001X",
    descriptive_name='A Radiology doctor of Osteopathy that specializes in Diagnostic Ultrasound.',
    specialty='Radiology.',
    specialization='Diagnostic Ultrasound',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["208600000X"] = TaxonomyEntry(
    code="208600000X",
    descriptive_name='A general surgeon has expertise related to the diagnosis - preoperative, operative and postoperative',
    specialty='Surgery',
    specialization='Vascular & Interventional Radiology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2086H0002X"] = TaxonomyEntry(
    code="2086H0002X",
    descriptive_name='A surgeon with special knowledge and skills to prevent and relieve the suffering experienced by patients',
    specialty='Surgery',
    specialization='Hospice and Palliative Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2086S0102X"] = TaxonomyEntry(
    code="2086S0102X",
    descriptive_name='A surgeon with expertise in the management of the critically ill and postoperative patient, particularly the',
    specialty='Surgery',
    specialization='Surgical Critical Care',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2086S0105X"] = TaxonomyEntry(
    code="2086S0105X",
    descriptive_name='A surgeon with expertise in the investigation, preservation and restoration by medical, surgical and',
    specialty='Additional Resources: A General Certificate is issued by the American Osteopathic Board of Surgery.',
    specialization='Surgery of the Hand',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2086S0120X"] = TaxonomyEntry(
    code="2086S0120X",
    descriptive_name='A surgeon with expertise in the management of surgical conditions in premature and newborn infants,',
    specialty='patient; and legal and ethical decision making in end-of-life care.',
    specialization='Pediatric Surgery',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2086S0122X"] = TaxonomyEntry(
    code="2086S0122X",
    descriptive_name='A surgeon who specializes in plastic and reconstructive surgery.',
    specialty='Board certification for Medical Doctors (MDs) is provided by the American Board of Surgery.',
    specialization='Plastic and Reconstructive Surgery',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2086S0127X"] = TaxonomyEntry(
    code="2086S0127X",
    descriptive_name='Trauma surgery is a recognized subspecialty of general surgery. Trauma surgeons are physicians who',
    specialty='certification is not currently offered.',
    specialization='Trauma Surgery',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2086S0129X"] = TaxonomyEntry(
    code="2086S0129X",
    descriptive_name='A surgeon with expertise in the management of surgical disorders of the blood vessels, excluding the',
    specialty='Surgery',
    specialization='Vascular Surgery',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2086X0206X"] = TaxonomyEntry(
    code="2086X0206X",
    descriptive_name='A surgical oncologist is a well-qualified surgeon who has obtained additional training and experience in',
    specialty='certification for Doctors of Osteopathy (DOs) is provided by the American Osteopathic Board of Surgery.',
    specialization='Surgical Oncology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["208800000X"] = TaxonomyEntry(
    code="208800000X",
    descriptive_name='A urologist manages benign and malignant medical and surgical disorders of the genitourinary system',
    specialty='Urology',
    specialization='Vascular Surgery',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2088F0040X"] = TaxonomyEntry(
    code="2088F0040X",
    descriptive_name='A subspecialist in Female Pelvic Medicine and Reconstructive Surgery is a physician in Urology or',
    specialty='certification for Medical Doctors (MDs) is provided by the American Board of Urology.',
    specialization='Female Pelvic Medicine and Reconstructive Surgery',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["2088P0231X"] = TaxonomyEntry(
    code="2088P0231X",
    descriptive_name="Surgeons who can diagnose, treat, and manage children's urinary and genital problems. A pediatric",
    specialty='resulting from them.',
    specialization='Pediatric Urology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["208C00000X"] = TaxonomyEntry(
    code="208C00000X",
    descriptive_name='A colon and rectal surgeon is trained to diagnose and treat various diseases of the intestinal tract, colon,',
    specialty='Colon & Rectal Surgery',
    specialization='Pediatric Anesthesiology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["208D00000X"] = TaxonomyEntry(
    code="208D00000X",
    descriptive_name='A physician who specializes in the general practice of diagnosing, treating, and managing patients with a',
    specialty='General Practice',
    specialization='Sports Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["208G00000X"] = TaxonomyEntry(
    code="208G00000X",
    descriptive_name='A thoracic surgeon provides the operative, perioperative and critical care of patients with pathologic',
    specialty='Thoracic Surgery (Cardiothoracic Vascular Surgery)',
    specialization='Vascular Surgery',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["208M00000X"] = TaxonomyEntry(
    code="208M00000X",
    descriptive_name='Hospitalists are physicians whose primary professional focus is the general medical care of hospitalized',
    specialty='Hospitalist',
    specialization='Sports Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["208U00000X"] = TaxonomyEntry(
    code="208U00000X",
    descriptive_name='Clinical pharmacology encompasses the spectrum of activities related to the discovery, development,',
    specialty='Clinical Pharmacology',
    specialization='Pediatric Anesthesiology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["208VP0000X"] = TaxonomyEntry(
    code="208VP0000X",
    descriptive_name='Pain Medicine is a primary medical specialty based on a distinct body of knowledge and a well-defined',
    specialty='Pain Medicine',
    specialization='Pain Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["208VP0014X"] = TaxonomyEntry(
    code="208VP0014X",
    descriptive_name='Interventional Pain Medicine is the discipline of medicine devoted to the diagnosis and treatment of pain',
    specialty='Pain Medicine',
    specialization='Interventional Pain Medicine',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["209800000X"] = TaxonomyEntry(
    code="209800000X",
    descriptive_name='Legal Medicine is a special field of medicine that focuses on various aspects of medicine and law.',
    specialty='Legal Medicine',
    specialization='Transplant Hepatology',
    provider_grouping='Allopathic & Osteopathic Physicians',
)

TAXONOMY_MAPPING["211D00000X"] = TaxonomyEntry(
    code="211D00000X",
    descriptive_name='An individual who assists a podiatrist in tasks, such as exposing and developing x-rays; taking and',
    specialty='Assistant, Podiatric',
    specialization='Surgical',
    provider_grouping='Podiatric Medicine & Surgery Service Providers',
)

TAXONOMY_MAPPING["213E00000X"] = TaxonomyEntry(
    code="213E00000X",
    descriptive_name='A podiatrist is a person qualified by a Doctor of Podiatric Medicine (D.P.M.) degree, licensed by the state,',
    specialty='Podiatrist',
    specialization='Surgical',
    provider_grouping='Podiatric Medicine & Surgery Service Providers',
)

TAXONOMY_MAPPING["213EG0000X"] = TaxonomyEntry(
    code="213EG0000X",
    descriptive_name='144 JANUARY 2024',
    specialty='#Type!',
    specialization='General Practice',
    provider_grouping='Podiatric Medicine & Surgery Service Providers',
)

TAXONOMY_MAPPING["213EP0504X"] = TaxonomyEntry(
    code="213EP0504X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Public Medicine',
    provider_grouping='Podiatric Medicine & Surgery Service Providers',
)

TAXONOMY_MAPPING["213EP1101X"] = TaxonomyEntry(
    code="213EP1101X",
    descriptive_name='#Type!',
    specialty='Podiatrist',
    specialization='Primary Podiatric Medicine',
    provider_grouping='Podiatric Medicine & Surgery Service Providers',
)

TAXONOMY_MAPPING["213ER0200X"] = TaxonomyEntry(
    code="213ER0200X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Radiology',
    provider_grouping='Podiatric Medicine & Surgery Service Providers',
)

TAXONOMY_MAPPING["213ES0000X"] = TaxonomyEntry(
    code="213ES0000X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Sports Medicine',
    provider_grouping='Podiatric Medicine & Surgery Service Providers',
)

TAXONOMY_MAPPING["213ES0103X"] = TaxonomyEntry(
    code="213ES0103X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Foot & Ankle Surgery',
    provider_grouping='Podiatric Medicine & Surgery Service Providers',
)

TAXONOMY_MAPPING["213ES0131X"] = TaxonomyEntry(
    code="213ES0131X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Foot Surgery',
    provider_grouping='Podiatric Medicine & Surgery Service Providers',
)

TAXONOMY_MAPPING["221700000X"] = TaxonomyEntry(
    code="221700000X",
    descriptive_name='(1) An individual who uses art to achieve the therapeutic goals of symptom relief, emotional integration,',
    specialty='Art Therapist',
    specialization='Sports Medicine',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["222Q00000X"] = TaxonomyEntry(
    code="222Q00000X",
    descriptive_name='A Developmental Therapist is a person qualified by completion of an approved program in Developmental',
    specialty='Developmental Therapist',
    specialization='Sports Medicine',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["222Z00000X"] = TaxonomyEntry(
    code="222Z00000X",
    descriptive_name='A health care professional who is specifically educated and trained to manage comprehensive orthotic',
    specialty='Orthotist',
    specialization='Low Vision',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["224900000X"] = TaxonomyEntry(
    code="224900000X",
    descriptive_name='An individual trained in the fitting and adjusting of breast prostheses and management of post-',
    specialty='Mastectomy Fitter',
    specialization='Sports Medicine',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["224L00000X"] = TaxonomyEntry(
    code="224L00000X",
    descriptive_name='An individual who is trained in the management and treatment of conditions of the foot, ankle, and lower',
    specialty='Pedorthist',
    specialization='Low Vision',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["224P00000X"] = TaxonomyEntry(
    code="224P00000X",
    descriptive_name='A health care professional who is specifically educated and trained to manage comprehensive prosthetic',
    specialty='Prosthetist',
    specialization='Sports',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["224Y00000X"] = TaxonomyEntry(
    code="224Y00000X",
    descriptive_name='A Clinical Exercise Physiologist is a health care professional who is trained to work with patients with',
    specialty='Clinical Exercise Physiologist',
    specialization='Sports Medicine',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["224Z00000X"] = TaxonomyEntry(
    code="224Z00000X",
    descriptive_name='An occupational therapy assistant is a person who has graduated from an occupational therapy assistant',
    specialty='Occupational Therapy Assistant',
    specialization='Physical Rehabilitation',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["224ZE0001X"] = TaxonomyEntry(
    code="224ZE0001X",
    descriptive_name='Occupational therapy assistants provide environmental modifications under the supervision of an',
    specialty='Occupational Therapy Assistant',
    specialization='Environmental Modification',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["224ZF0002X"] = TaxonomyEntry(
    code="224ZF0002X",
    descriptive_name='Occupational therapy assistants provide environmental modifications under the supervision of an',
    specialty='employment. </ul>Fact Sheet: Home Modifications and OT, AOTA Website: Specialty Certifications',
    specialization='Feeding, Eating & Swallowing',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["224ZL0004X"] = TaxonomyEntry(
    code="224ZL0004X",
    descriptive_name='Occupational therapy assistants contribute to the completion of an individualized occupational therapy',
    specialty='Occupational Therapy Assistant',
    specialization='Low Vision',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["224ZR0403X"] = TaxonomyEntry(
    code="224ZR0403X",
    descriptive_name='Occupational therapy assistants contribute to the completion of an individualized occupational therapy',
    specialty='Occupational Therapy Assistant',
    specialization='Driving and Community Mobility',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["225000000X"] = TaxonomyEntry(
    code="225000000X",
    descriptive_name='An individual trained in the management of fitting prefabricated orthoses.',
    specialty='Orthotic Fitter',
    specialization='Low Vision',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["225100000X"] = TaxonomyEntry(
    code="225100000X",
    descriptive_name='Physical therapists (PTs) are licensed health care professionals who diagnose and treat individuals of all',
    specialty='Physical Therapist',
    specialization='Low Vision',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2251C2600X"] = TaxonomyEntry(
    code="2251C2600X",
    descriptive_name='A licensed physical therapist, including but not limited to an individual who is a Board Certified Specialist',
    specialty='Physical Therapist',
    specialization='Cardiopulmonary',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2251E1200X"] = TaxonomyEntry(
    code="2251E1200X",
    descriptive_name='A licensed physical therapist who has demonstrated specialized knowledge and skills pertaining to the',
    specialty='examination-evaluation ; http://www.abpts.org/Certification/ClinicalElectrophysiology/',
    specialization='Ergonomics',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2251E1300X"] = TaxonomyEntry(
    code="2251E1300X",
    descriptive_name='A licensed physical therapist, including but not limited to an individual who is a Board Certified Specialist',
    specialty='http://www.abpts.org/uploadedFiles/ABPTSorg/Specialist_Certification/DSP/DSP-Cardio.pdf',
    specialization='Electrophysiology, Clinical',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2251G0304X"] = TaxonomyEntry(
    code="2251G0304X",
    descriptive_name='A licensed physical therapist, including but not limited to an individual who is a Board Certified Specialist',
    specialty='Physical Therapist',
    specialization='Geriatrics',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2251H1200X"] = TaxonomyEntry(
    code="2251H1200X",
    descriptive_name='#Type!',
    specialty='www.apta.org',
    specialization='Hand',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2251H1300X"] = TaxonomyEntry(
    code="2251H1300X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Human Factors',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2251N0400X"] = TaxonomyEntry(
    code="2251N0400X",
    descriptive_name='A licensed physical therapist, including but not limited to an individual who is a Board Certified Specialist',
    specialty='#Type!',
    specialization='Neurology',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2251P0200X"] = TaxonomyEntry(
    code="2251P0200X",
    descriptive_name='A licensed physical therapist, including but not limited to an individual who is a Board Certified Specialist',
    specialty='http://www.abpts.org/uploadedFiles/ABPTSorg/Specialist_Certification/DSP/DSP-Orthopaedics.pdf',
    specialization='Pediatrics',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2251S0007X"] = TaxonomyEntry(
    code="2251S0007X",
    descriptive_name='A licensed physical therapist, including but not limited to an individual who is a Board Certified Specialist',
    specialty='http://www.abpts.org/uploadedFiles/ABPTSorg/Specialist_Certification/DSP/DSP-Pediatrics.pdf',
    specialization='Sports',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2251X0800X"] = TaxonomyEntry(
    code="2251X0800X",
    descriptive_name='A licensed physical therapist, including but not limited to an individual who is a Board Certified Specialist',
    specialty='Physical Therapist',
    specialization='Orthopedic',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["225200000X"] = TaxonomyEntry(
    code="225200000X",
    descriptive_name='(1)Physical therapist assistants are skilled health care providers who are graduates of a physical therapist',
    specialty='Physical Therapy Assistant',
    specialization='Sports',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["225400000X"] = TaxonomyEntry(
    code="225400000X",
    descriptive_name='A health care practitioner who trains or retrains individuals disabled by disease or injury to help them',
    specialty='Rehabilitation Practitioner',
    specialization='Orientation and Mobility Training Provider',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["225500000X"] = TaxonomyEntry(
    code="225500000X",
    descriptive_name='General classification identifying individuals who are trained on a specific piece of equipment or technical',
    specialty='Specialist/Technologist',
    specialization='SNF/Subacute Care',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2255A2300X"] = TaxonomyEntry(
    code="2255A2300X",
    descriptive_name='Athletic trainers are allied health care professionals who work in consultation with or under the direction of',
    specialty='Specialist/Technologist',
    specialization='Athletic Trainer',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2255R0406X"] = TaxonomyEntry(
    code="2255R0406X",
    descriptive_name='#Type!',
    specialty='modified source]',
    specialization='Rehabilitation, Blind',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["225600000X"] = TaxonomyEntry(
    code="225600000X",
    descriptive_name='The dance therapist, sometimes called a movement therapist, focuses on rhythmic body movements as a',
    specialty='Dance Therapist',
    specialization='Sports Medicine',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["225700000X"] = TaxonomyEntry(
    code="225700000X",
    descriptive_name='An individual trained in the manipulation of tissues (as by rubbing, stroking, kneading, or tapping) with the',
    specialty='Massage Therapist',
    specialization='Sports Medicine',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["225800000X"] = TaxonomyEntry(
    code="225800000X",
    descriptive_name='A recreation therapist uses recreational activities for intervention in some physical, social or emotional',
    specialty='Recreation Therapist',
    specialization='Sports',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["225A00000X"] = TaxonomyEntry(
    code="225A00000X",
    descriptive_name="Music therapists use music interventions to assess clients' strengths and needs, develop goals,",
    specialty='Music Therapist',
    specialization='Sports Medicine',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["225B00000X"] = TaxonomyEntry(
    code="225B00000X",
    descriptive_name='An individual who is trained and qualified to perform pulmonary diagnostic tests. In the course of',
    specialty='Pulmonary Function Technologist',
    specialization='Sports',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["225C00000X"] = TaxonomyEntry(
    code="225C00000X",
    descriptive_name='An individual trained and educated in a systematic process of assisting persons with physical, mental,',
    specialty='Rehabilitation Counselor',
    specialization='Sports',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["225CA2400X"] = TaxonomyEntry(
    code="225CA2400X",
    descriptive_name='#Type!',
    specialty='File Dictionary of Health Care Management, New York: Facts On File Publications, 1988.',
    specialization='Assistive Technology Practitioner',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["225CA2500X"] = TaxonomyEntry(
    code="225CA2500X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Assistive Technology Supplier',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["225CX0006X"] = TaxonomyEntry(
    code="225CX0006X",
    descriptive_name='Orientation and Mobility (O&M) specialists teach children and adults who have visual impairments the',
    specialty='Rehabilitation Counselor',
    specialization='Orientation and Mobility Training Provider',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["225X00000X"] = TaxonomyEntry(
    code="225X00000X",
    descriptive_name='An occupational therapist is a person who has graduated from an entry-level occupational therapy',
    specialty='Occupational Therapist',
    specialization='Sports Medicine',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["225XE0001X"] = TaxonomyEntry(
    code="225XE0001X",
    descriptive_name='Occupational therapy practitioners are experts at identifying the cause of difficulties in performance of',
    specialty='or voluntary. <li>Verification of employment. </ul> AOTA Fact Sheets: Older Driver',
    specialization='Environmental Modification',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["225XE1200X"] = TaxonomyEntry(
    code="225XE1200X",
    descriptive_name='#Type!',
    specialty='Occupational Therapist',
    specialization='Ergonomics',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["225XF0002X"] = TaxonomyEntry(
    code="225XF0002X",
    descriptive_name='Occupational therapists provide interventions to clients of all ages with feeding, eating and swallowing',
    specialty='#Type!',
    specialization='Feeding, Eating & Swallowing',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["225XG0600X"] = TaxonomyEntry(
    code="225XG0600X",
    descriptive_name='Occupational therapists work with older adults in virtually every setting: assisted living, wellness',
    specialty='Occupational Therapist',
    specialization='Gerontology',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["225XH1200X"] = TaxonomyEntry(
    code="225XH1200X",
    descriptive_name='#Type!',
    specialty='Senior Center and Assisted Living Facilities',
    specialization='Hand',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["225XH1300X"] = TaxonomyEntry(
    code="225XH1300X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Human Factors',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["225XL0004X"] = TaxonomyEntry(
    code="225XL0004X",
    descriptive_name='Occupational therapists enable children and adults with visual impairment to engage in their chosen daily',
    specialty='Occupational Therapist',
    specialization='Low Vision',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["225XM0800X"] = TaxonomyEntry(
    code="225XM0800X",
    descriptive_name='Occupational therapists provide treatment for people recovering from a mental or physical illness to',
    specialty='Fact Sheets: Low Vision; OT Services for Individuals with Visual Impairments',
    specialization='Mental Health',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["225XN1300X"] = TaxonomyEntry(
    code="225XN1300X",
    descriptive_name='#Type!',
    specialty='Occupational Therapist',
    specialization='Neurorehabilitation',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["225XP0019X"] = TaxonomyEntry(
    code="225XP0019X",
    descriptive_name='Occupational therapists are experts at helping people lead as independent a life as possible.',
    specialty='Occupational Therapist',
    specialization='Physical Rehabilitation',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["225XP0200X"] = TaxonomyEntry(
    code="225XP0200X",
    descriptive_name='Occupational therapists provide services to infants, toddlers and children who have or who are at risk for',
    specialty='#Type!',
    specialization='Pediatrics',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["225XR0403X"] = TaxonomyEntry(
    code="225XR0403X",
    descriptive_name="Occupational therapists can optimize and prolong an older driver's ability to drive safely and ease the",
    specialty='Occupational Therapist',
    specialization='Driving and Community Mobility',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["226000000X"] = TaxonomyEntry(
    code="226000000X",
    descriptive_name='Recreational Therapist Assistants work in support of or assistant to Recreational Therapists treating',
    specialty='Recreational Therapist Assistant',
    specialization='Sports',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["226300000X"] = TaxonomyEntry(
    code="226300000X",
    descriptive_name='A provider trained and educated in the applied science of medically prescribed therapeutic exercise,',
    specialty='Kinesiotherapist',
    specialization='Sports Medicine',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["227800000X"] = TaxonomyEntry(
    code="227800000X",
    descriptive_name='A Certified Respiratory Therapist (CRT) is a an entry level therapist who has passed a standardized',
    specialty='Respiratory Therapist, Certified',
    specialization='Orientation and Mobility Training Provider',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2278C0205X"] = TaxonomyEntry(
    code="2278C0205X",
    descriptive_name='Respiratory emergencies are commonplace in the treatment of critical care patients. Included in the',
    specialty='Respiratory Therapist, Certified',
    specialization='Critical Care',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2278E0002X"] = TaxonomyEntry(
    code="2278E0002X",
    descriptive_name='The immediate availability of diagnostic and therapeutic cardiopulmonary services in the assessment and',
    specialty='#Type!',
    specialization='Emergency Care',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2278E1000X"] = TaxonomyEntry(
    code="2278E1000X",
    descriptive_name='The focus of patient and family education activities is to promote knowledge of disease process, medical',
    specialty='#Type!',
    specialization='Educational',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2278G0305X"] = TaxonomyEntry(
    code="2278G0305X",
    descriptive_name='Care of older patients who have age and/or disease related decremental pulmonary changes. Diagnosis',
    specialty='#Type!',
    specialization='Geriatric Care',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2278G1100X"] = TaxonomyEntry(
    code="2278G1100X",
    descriptive_name='This level of care includes diagnostics testing, therapeutics, monitoring, rehabilitation of patients with',
    specialty='#Type!',
    specialization='General Care',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2278H0200X"] = TaxonomyEntry(
    code="2278H0200X",
    descriptive_name='Home care fosters individual responsibility for self-management of chronic respiratory conditions. It',
    specialty='Respiratory Therapist, Certified',
    specialization='Home Health',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2278P1004X"] = TaxonomyEntry(
    code="2278P1004X",
    descriptive_name='Included in the area of pulmonary diagnostics are the following; collection and analysis of physiological',
    specialty='#Type!',
    specialization='Pulmonary Diagnostics',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2278P1005X"] = TaxonomyEntry(
    code="2278P1005X",
    descriptive_name='The respiratory therapist can assist the chronic pulmonary patient in returning to an optimal role in society',
    specialty='#Type!',
    specialization='Pulmonary Rehabilitation',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2278P1006X"] = TaxonomyEntry(
    code="2278P1006X",
    descriptive_name='An individual who is trained and qualified to perform pulmonary diagnostic tests. In the course of',
    specialty='Respiratory Therapist, Certified',
    specialization='Pulmonary Function Technologist',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2278P3800X"] = TaxonomyEntry(
    code="2278P3800X",
    descriptive_name='A coordinated plan of care to help dying patients and their families handle the burden of terminal care.',
    specialty='#Type!',
    specialization='Palliative/Hospice',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2278P3900X"] = TaxonomyEntry(
    code="2278P3900X",
    descriptive_name='The care and treatment of premature infants, newborns and children. This includes management of',
    specialty='#Type!',
    specialization='Neonatal/Pediatrics',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2278P4000X"] = TaxonomyEntry(
    code="2278P4000X",
    descriptive_name='Transport respiratory therapist provide patient assessment, initiation of treatment modalities and',
    specialty='#Type!',
    specialization='Patient Transport',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2278S1500X"] = TaxonomyEntry(
    code="2278S1500X",
    descriptive_name='Care of residents in a long-term care environment. Respiratory modalities delivered include those similar',
    specialty='#Type!',
    specialization='SNF/Subacute Care',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["227900000X"] = TaxonomyEntry(
    code="227900000X",
    descriptive_name='A Registered Respiratory Therapist (RRT) is an advanced therapist who has passed standardized written',
    specialty='Respiratory Therapist, Registered',
    specialization='SNF/Subacute Care',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2279C0205X"] = TaxonomyEntry(
    code="2279C0205X",
    descriptive_name='Respiratory emergencies are commonplace in the treatment of critical care patients. Included in the',
    specialty='Respiratory Therapist, Registered',
    specialization='Critical Care',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2279E0002X"] = TaxonomyEntry(
    code="2279E0002X",
    descriptive_name='The immediate availability of diagnostic and therapeutic cardiopulmonary services in the assessment and',
    specialty='#Type!',
    specialization='Emergency Care',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2279E1000X"] = TaxonomyEntry(
    code="2279E1000X",
    descriptive_name='The focus of patient and family education activities is to promote knowledge of disease process, medical',
    specialty='#Type!',
    specialization='Educational',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2279G0305X"] = TaxonomyEntry(
    code="2279G0305X",
    descriptive_name='Care of older patients who have age and/or disease related decremental pulmonary changes. Diagnosis',
    specialty='#Type!',
    specialization='Geriatric Care',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2279G1100X"] = TaxonomyEntry(
    code="2279G1100X",
    descriptive_name='This level of care includes diagnostics testing, therapeutics, monitoring, rehabilitation of patients with',
    specialty='#Type!',
    specialization='General Care',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2279H0200X"] = TaxonomyEntry(
    code="2279H0200X",
    descriptive_name='Home care fosters individual responsibility for self-management of chronic respiratory conditions. It',
    specialty='Respiratory Therapist, Registered',
    specialization='Home Health',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2279P1004X"] = TaxonomyEntry(
    code="2279P1004X",
    descriptive_name='Included in the area of pulmonary diagnostics are the following; collection and analysis of physiological',
    specialty='#Type!',
    specialization='Pulmonary Diagnostics',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2279P1005X"] = TaxonomyEntry(
    code="2279P1005X",
    descriptive_name='The respiratory therapist can assist the chronic pulmonary patient in returning to an optimal role in society',
    specialty='#Type!',
    specialization='Pulmonary Rehabilitation',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2279P1006X"] = TaxonomyEntry(
    code="2279P1006X",
    descriptive_name='An individual who is trained and qualified to perform pulmonary diagnostic tests. In the course of',
    specialty='Respiratory Therapist, Registered',
    specialization='Pulmonary Function Technologist',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2279P3800X"] = TaxonomyEntry(
    code="2279P3800X",
    descriptive_name='A coordinated plan of care to help dying patients and their families handle the burden of terminal care.',
    specialty='#Type!',
    specialization='Palliative/Hospice',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2279P3900X"] = TaxonomyEntry(
    code="2279P3900X",
    descriptive_name='The care and treatment of premature infants, newborns and children. This includes management of',
    specialty='#Type!',
    specialization='Neonatal/Pediatrics',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2279P4000X"] = TaxonomyEntry(
    code="2279P4000X",
    descriptive_name='Transport respiratory therapist provide patient assessment, initiation of treatment modalities and',
    specialty='#Type!',
    specialization='Patient Transport',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["2279S1500X"] = TaxonomyEntry(
    code="2279S1500X",
    descriptive_name='Care of residents in a long-term care environment. Respiratory modalities delivered include those similar',
    specialty='#Type!',
    specialization='SNF/Subacute Care',
    provider_grouping='Respiratory, Developmental, Rehabilitative and Restorative Service',
)

TAXONOMY_MAPPING["229N00000X"] = TaxonomyEntry(
    code="229N00000X",
    descriptive_name='An anaplastologist is a professional who creates prostheses for the face and body. Patients treated',
    specialty='Anaplastologist',
    specialization='Sports Medicine',
    provider_grouping='Podiatric Medicine & Surgery Service Providers',
)

TAXONOMY_MAPPING["231H00000X"] = TaxonomyEntry(
    code="231H00000X",
    descriptive_name='(1) A specialist in evaluation, habilitation and rehabilitation of those whose communication disorders',
    specialty='Audiologist',
    specialization='Rehabilitation, Blind',
    provider_grouping='Speech, Language and Hearing Service Providers',
)

TAXONOMY_MAPPING["231HA2400X"] = TaxonomyEntry(
    code="231HA2400X",
    descriptive_name='#Type!',
    specialty='Audiologist',
    specialization='Assistive Technology Practitioner',
    provider_grouping='Speech, Language and Hearing Service Providers',
)

TAXONOMY_MAPPING["231HA2500X"] = TaxonomyEntry(
    code="231HA2500X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Assistive Technology Supplier',
    provider_grouping='Speech, Language and Hearing Service Providers',
)

TAXONOMY_MAPPING["235500000X"] = TaxonomyEntry(
    code="235500000X",
    descriptive_name='General classification identifying individuals who are trained on a specific piece of equipment or technical',
    specialty='Specialist/Technologist',
    specialization='Assistive Technology Supplier',
    provider_grouping='Speech, Language and Hearing Service Providers',
)

TAXONOMY_MAPPING["2355A2700X"] = TaxonomyEntry(
    code="2355A2700X",
    descriptive_name='#Type!',
    specialty='Specialist/Technologist',
    specialization='Audiology Assistant',
    provider_grouping='Speech, Language and Hearing Service Providers',
)

TAXONOMY_MAPPING["2355S0801X"] = TaxonomyEntry(
    code="2355S0801X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Speech-Language Assistant',
    provider_grouping='Speech, Language and Hearing Service Providers',
)

TAXONOMY_MAPPING["235Z00000X"] = TaxonomyEntry(
    code="235Z00000X",
    descriptive_name='The speech-language pathologist is the professional who engages in clinical services, prevention,',
    specialty='Speech-Language Pathologist',
    specialization='Speech-Language Assistant',
    provider_grouping='Speech, Language and Hearing Service Providers',
)

TAXONOMY_MAPPING["237600000X"] = TaxonomyEntry(
    code="237600000X",
    descriptive_name='An audiologist/hearing aid fitter is the professional who specializes in evaluating and treating people with',
    specialty='Audiologist-Hearing Aid Fitter',
    specialization='Assistive Technology Supplier',
    provider_grouping='Speech, Language and Hearing Service Providers',
)

TAXONOMY_MAPPING["237700000X"] = TaxonomyEntry(
    code="237700000X",
    descriptive_name='Individuals who test hearing for the selection, adaptation, fitting, adjusting, servicing, and sale of hearing',
    specialty='Hearing Instrument Specialist',
    specialization='Assistive Technology Supplier',
    provider_grouping='Speech, Language and Hearing Service Providers',
)

TAXONOMY_MAPPING["242T00000X"] = TaxonomyEntry(
    code="242T00000X",
    descriptive_name='A perfusionist operates extracorporeal circulation and autotransfusion equipment during any medical',
    specialty='Perfusionist',
    specialization='Speech-Language Assistant',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["243U00000X"] = TaxonomyEntry(
    code="243U00000X",
    descriptive_name='A Radiology Practitioner Assistant (RPA) is a health professional certified as a registered radiographer',
    specialty='Radiology Practitioner Assistant',
    specialization='Vascular-Interventional Technology',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246Q00000X"] = TaxonomyEntry(
    code="246Q00000X",
    descriptive_name='(1) An individual educated and trained in clinical chemistry, microbiology or other biological sciences; and',
    specialty='Specialist/Technologist, Pathology',
    specialization='Surgical Technologist',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246QB0000X"] = TaxonomyEntry(
    code="246QB0000X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Blood Banking',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246QC1000X"] = TaxonomyEntry(
    code="246QC1000X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Chemistry',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246QC2700X"] = TaxonomyEntry(
    code="246QC2700X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Cytotechnology',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246QH0000X"] = TaxonomyEntry(
    code="246QH0000X",
    descriptive_name='#Type!',
    specialty='Specialist/Technologist, Pathology',
    specialization='Hematology',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246QH0401X"] = TaxonomyEntry(
    code="246QH0401X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Hemapheresis Practitioner',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246QH0600X"] = TaxonomyEntry(
    code="246QH0600X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Histology',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246QI0000X"] = TaxonomyEntry(
    code="246QI0000X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Immunology',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246QL0900X"] = TaxonomyEntry(
    code="246QL0900X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Laboratory Management',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246QL0901X"] = TaxonomyEntry(
    code="246QL0901X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Laboratory Management, Diplomate',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246QM0706X"] = TaxonomyEntry(
    code="246QM0706X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Medical Technologist',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246QM0900X"] = TaxonomyEntry(
    code="246QM0900X",
    descriptive_name='#Type!',
    specialty='Specialist/Technologist, Pathology',
    specialization='Microbiology',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246R00000X"] = TaxonomyEntry(
    code="246R00000X",
    descriptive_name='An individual with knowledge of specific techniques and instruments who performs all of the routine tests',
    specialty='Technician, Pathology',
    specialization='Veterinary',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246RH0600X"] = TaxonomyEntry(
    code="246RH0600X",
    descriptive_name='#Type!',
    specialty='CFR 42 Part 493.1405.',
    specialization='Histology',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246RM2200X"] = TaxonomyEntry(
    code="246RM2200X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Medical Laboratory',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246RP1900X"] = TaxonomyEntry(
    code="246RP1900X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Phlebotomy',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246W00000X"] = TaxonomyEntry(
    code="246W00000X",
    descriptive_name='An individual who has knowledge of specific techniques, instruments, and equipment required in',
    specialty='Technician, Cardiology',
    specialization='Microbiology',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246X00000X"] = TaxonomyEntry(
    code="246X00000X",
    descriptive_name='An allied health professional who performs diagnostic examinations at the request or direction of a',
    specialty='Specialist/Technologist Cardiovascular',
    specialization='Vascular-Interventional Technology',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246XC2901X"] = TaxonomyEntry(
    code="246XC2901X",
    descriptive_name='#Type!',
    specialty='1994, p. 159.',
    specialization='Cardiovascular Invasive Specialist',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246XC2903X"] = TaxonomyEntry(
    code="246XC2903X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Vascular Specialist',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246XS1301X"] = TaxonomyEntry(
    code="246XS1301X",
    descriptive_name='#Type!',
    specialty='Specialist/Technologist Cardiovascular',
    specialization='Sonography',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246Y00000X"] = TaxonomyEntry(
    code="246Y00000X",
    descriptive_name='An individual with a high school diploma, on-the-job experience and coding education from seminars or',
    specialty='Specialist/Technologist, Health Information',
    specialization='Vascular Specialist',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246YC3301X"] = TaxonomyEntry(
    code="246YC3301X",
    descriptive_name='None',
    specialty='Source: American Health Information Management Association, Chicago, IL, 1996.',
    specialization='Coding Specialist, Hospital Based',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246YC3302X"] = TaxonomyEntry(
    code="246YC3302X",
    descriptive_name='None',
    specialty='None',
    specialization='Coding Specialist, Physician Office Based',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246YR1600X"] = TaxonomyEntry(
    code="246YR1600X",
    descriptive_name='None',
    specialty='None',
    specialization='Registered Record Administrator',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246Z00000X"] = TaxonomyEntry(
    code="246Z00000X",
    descriptive_name='General classification identifying individuals trained on specific equipment and technical procedures in',
    specialty='Specialist/Technologist, Other',
    specialization='Registered Record Administrator',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246ZA2600X"] = TaxonomyEntry(
    code="246ZA2600X",
    descriptive_name='None',
    specialty='#Type!',
    specialization='Art, Medical',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246ZB0301X"] = TaxonomyEntry(
    code="246ZB0301X",
    descriptive_name='None',
    specialty='#Type!',
    specialization='Biomedical Engineering',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246ZB0302X"] = TaxonomyEntry(
    code="246ZB0302X",
    descriptive_name='None',
    specialty='None',
    specialization='Biomedical Photographer',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246ZB0500X"] = TaxonomyEntry(
    code="246ZB0500X",
    descriptive_name='#Type!',
    specialty='None',
    specialization='Biochemist',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246ZB0600X"] = TaxonomyEntry(
    code="246ZB0600X",
    descriptive_name='None',
    specialty='None',
    specialization='Biostatistician',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246ZC0007X"] = TaxonomyEntry(
    code="246ZC0007X",
    descriptive_name='A surgical assistant is a skilled practitioner who has undergone formalized education and training as a',
    specialty='Resources: National Board for Certification of Orthopaedic Assistants',
    specialization='Surgical Assistant',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246ZE0500X"] = TaxonomyEntry(
    code="246ZE0500X",
    descriptive_name='#Type!',
    specialty='Specialist/Technologist, Other',
    specialization='EEG',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246ZE0600X"] = TaxonomyEntry(
    code="246ZE0600X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Electroneurodiagnostic',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246ZG0701X"] = TaxonomyEntry(
    code="246ZG0701X",
    descriptive_name='None',
    specialty='#Type!',
    specialization='Graphics Methods',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246ZG1000X"] = TaxonomyEntry(
    code="246ZG1000X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Geneticist, Medical (PhD)',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246ZI1000X"] = TaxonomyEntry(
    code="246ZI1000X",
    descriptive_name='None',
    specialty='None',
    specialization='Illustration, Medical',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246ZN0300X"] = TaxonomyEntry(
    code="246ZN0300X",
    descriptive_name='#Type!',
    specialty='None',
    specialization='Nephrology',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246ZS0410X"] = TaxonomyEntry(
    code="246ZS0410X",
    descriptive_name='Surgical technologists are allied health professionals, who are an integral part of the team of medical',
    specialty='National Surgical Assistant Association, www.nsaa.net.',
    specialization='Surgical Technologist',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["246ZX2200X"] = TaxonomyEntry(
    code="246ZX2200X",
    descriptive_name='An Orthopaedic Assistant is a person who has been trained to work as a physician extender in both',
    specialty='Specialist/Technologist, Other',
    specialization='Orthopedic Assistant',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["247000000X"] = TaxonomyEntry(
    code="247000000X",
    descriptive_name="Preferred term for an Accredited Record Technician who is an individual with an associate's degree from",
    specialty='Technician, Health Information',
    specialization='Microbiology',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["2470A2800X"] = TaxonomyEntry(
    code="2470A2800X",
    descriptive_name='None',
    specialty='Source: American Health Information Management Association, Chicago, IL, 1996.',
    specialization='Assistant Record Technician',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["247100000X"] = TaxonomyEntry(
    code="247100000X",
    descriptive_name='A medical imaging or radiation therapy professional who is appropriately educated and trained to perform',
    specialty='Radiologic Technologist',
    specialization='Speech-Language Assistant',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["2471B0102X"] = TaxonomyEntry(
    code="2471B0102X",
    descriptive_name='A radiologic technologist who specializes in bone densitometry and is appropriately educated and trained,',
    specialty='definition]',
    specialization='Bone Densitometry',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["2471C1101X"] = TaxonomyEntry(
    code="2471C1101X",
    descriptive_name='A radiologic technologist who specializes in cardiovascular interventional technology.',
    specialty='Radiologic Technologist',
    specialization='Cardiovascular-Interventional Technology',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["2471C1106X"] = TaxonomyEntry(
    code="2471C1106X",
    descriptive_name='A radiologic technologist who specializes in cardiac interventional and is appropriately educated and',
    specialty='definition]',
    specialization='Cardiac-Interventional Technology',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["2471C3401X"] = TaxonomyEntry(
    code="2471C3401X",
    descriptive_name='A radiologic technologist who specializes in computed tomography (CT) and is appropriately educated',
    specialty='definition]',
    specialization='Computed Tomography',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["2471C3402X"] = TaxonomyEntry(
    code="2471C3402X",
    descriptive_name='A radiologic technologist who specializes in radiography (also known as x-rays) and is appropriately',
    specialty='definition]',
    specialization='Radiography',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["2471M1202X"] = TaxonomyEntry(
    code="2471M1202X",
    descriptive_name='A radiologic technologist who specializes in magnetic resonance imaging (MRI) and is appropriately',
    specialty='definition]',
    specialization='Magnetic Resonance Imaging',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["2471M2300X"] = TaxonomyEntry(
    code="2471M2300X",
    descriptive_name='A radiologic technologist who specializes in mammography and is appropriately educated and trained,',
    specialty='modified]',
    specialization='Mammography',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["2471N0900X"] = TaxonomyEntry(
    code="2471N0900X",
    descriptive_name='A radiologic technologist who specializes in nuclear medicine technology and is appropriately educated',
    specialty='definition]',
    specialization='Nuclear Medicine Technology',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["2471Q0001X"] = TaxonomyEntry(
    code="2471Q0001X",
    descriptive_name='A radiologic technologist who specializes in quality management.',
    specialty='Radiologic Technologist',
    specialization='Quality Management',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["2471R0002X"] = TaxonomyEntry(
    code="2471R0002X",
    descriptive_name='A radiologic technologist who specializes in radiation therapy and is appropriately educated and trained,',
    specialty='Source: American Registry of Radiologic Technologists, https://www.arrt.org/. At this time, ARRT no',
    specialization='Radiation Therapy',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["2471S1302X"] = TaxonomyEntry(
    code="2471S1302X",
    descriptive_name='A radiologic technologist who specializes in sonography and is appropriately educated and trained,',
    specialty='definition]',
    specialization='Sonography',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["2471V0105X"] = TaxonomyEntry(
    code="2471V0105X",
    descriptive_name='A radiologic technologist who specializes in vascular sonography and is trained in the use of ultrasound',
    specialty='modified]',
    specialization='Vascular Sonography',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["2471V0106X"] = TaxonomyEntry(
    code="2471V0106X",
    descriptive_name='A radiologic technologist who specializes in vascular interventional and is appropriately educated and',
    specialty='Radiologic Technologist',
    specialization='Vascular-Interventional Technology',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["247200000X"] = TaxonomyEntry(
    code="247200000X",
    descriptive_name='A collective term for persons with specialized training in various narrow fields of expertise whose',
    specialty='Technician, Other',
    specialization='Assistant Record Technician',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["2472B0301X"] = TaxonomyEntry(
    code="2472B0301X",
    descriptive_name='None',
    specialty='Technician, Other',
    specialization='Biomedical Engineering',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["2472D0500X"] = TaxonomyEntry(
    code="2472D0500X",
    descriptive_name='None',
    specialty='None',
    specialization='Darkroom',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["2472E0500X"] = TaxonomyEntry(
    code="2472E0500X",
    descriptive_name='#Type!',
    specialty='None',
    specialization='EEG',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["2472R0900X"] = TaxonomyEntry(
    code="2472R0900X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Renal Dialysis',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["2472V0600X"] = TaxonomyEntry(
    code="2472V0600X",
    descriptive_name='None',
    specialty='#Type!',
    specialization='Veterinary',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["247ZC0005X"] = TaxonomyEntry(
    code="247ZC0005X",
    descriptive_name='An individual who is state-licensed as a clinical laboratory director and meets the qualifications in the',
    specialty='Technician, Pathology',
    specialization='Clinical Laboratory Director, Non-physician',
    provider_grouping='Technologists, Technicians & Other Technical Service Providers',
)

TAXONOMY_MAPPING["251300000X"] = TaxonomyEntry(
    code="251300000X",
    descriptive_name='The term local education agency means a public board of education or other public authority legally',
    specialty='Local Education Agency (LEA)',
    specialization='Phlebotomy',
    provider_grouping='Agencies',
)

TAXONOMY_MAPPING["251B00000X"] = TaxonomyEntry(
    code="251B00000X",
    descriptive_name='An organization that is responsible for providing case management services. The agency provides',
    specialty='Case Management',
    specialization='Phlebotomy',
    provider_grouping='Agencies',
)

TAXONOMY_MAPPING["251C00000X"] = TaxonomyEntry(
    code="251C00000X",
    descriptive_name='These agencies are authorized to provide day habilitation services to developmentally disabled individuals',
    specialty='Day Training, Developmentally Disabled Services',
    specialization='Phlebotomy',
    provider_grouping='Agencies',
)

TAXONOMY_MAPPING["251E00000X"] = TaxonomyEntry(
    code="251E00000X",
    descriptive_name='A public agency or private organization, or a subdivision of such an agency or organization, that is',
    specialty='Home Health',
    specialization='Phlebotomy',
    provider_grouping='Agencies',
)

TAXONOMY_MAPPING["251F00000X"] = TaxonomyEntry(
    code="251F00000X",
    descriptive_name='#Type!',
    specialty='Home Infusion',
    specialization='Phlebotomy',
    provider_grouping='Agencies',
)

TAXONOMY_MAPPING["251G00000X"] = TaxonomyEntry(
    code="251G00000X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Phlebotomy',
    provider_grouping='Hospice Care, Community Based',
)

TAXONOMY_MAPPING["251J00000X"] = TaxonomyEntry(
    code="251J00000X",
    descriptive_name='A Nursing Care Agency is an entity that provides skilled nursing care through the services of a Registered',
    specialty='Nursing Care',
    specialization='Phlebotomy',
    provider_grouping='Agencies',
)

TAXONOMY_MAPPING["251K00000X"] = TaxonomyEntry(
    code="251K00000X",
    descriptive_name='#Type!',
    specialty='Public Health or Welfare',
    specialization='Phlebotomy',
    provider_grouping='Agencies',
)

TAXONOMY_MAPPING["251S00000X"] = TaxonomyEntry(
    code="251S00000X",
    descriptive_name='A private or public agency usually under local government jurisdiction, responsible for assuring the',
    specialty='Community/Behavioral Health',
    specialization='Phlebotomy',
    provider_grouping='Agencies',
)

TAXONOMY_MAPPING["251T00000X"] = TaxonomyEntry(
    code="251T00000X",
    descriptive_name='A PACE provider organization is a not-for-profit private or public entity that is primarily engaged in',
    specialty='Program of All-Inclusive Care for the Elderly (PACE) Provider Organization',
    specialization='Phlebotomy',
    provider_grouping='Agencies',
)

TAXONOMY_MAPPING["251V00000X"] = TaxonomyEntry(
    code="251V00000X",
    descriptive_name='#Type!',
    specialty='Voluntary or Charitable',
    specialization='Phlebotomy',
    provider_grouping='Agencies',
)

TAXONOMY_MAPPING["251X00000X"] = TaxonomyEntry(
    code="251X00000X",
    descriptive_name='A provider of service/function that assists participating individuals to make informed decisions about what',
    specialty='Supports Brokerage',
    specialization='Phlebotomy',
    provider_grouping='Agencies',
)

TAXONOMY_MAPPING["252Y00000X"] = TaxonomyEntry(
    code="252Y00000X",
    descriptive_name='Early intervention services are an effective way to address the needs of infants and toddlers who have',
    specialty='Early Intervention Provider Agency',
    specialization='Phlebotomy',
    provider_grouping='Agencies',
)

TAXONOMY_MAPPING["253J00000X"] = TaxonomyEntry(
    code="253J00000X",
    descriptive_name='A Foster Care Agency is an agency that provides foster care as defined in the Code of Federal',
    specialty='Foster Care Agency',
    specialization='Phlebotomy',
    provider_grouping='Agencies',
)

TAXONOMY_MAPPING["253Z00000X"] = TaxonomyEntry(
    code="253Z00000X",
    descriptive_name="An In Home Supportive Care Agency provides services in the patient's home with the goal of enabling the",
    specialty='In Home Supportive Care',
    specialization='Phlebotomy',
    provider_grouping='Agencies',
)

TAXONOMY_MAPPING["261Q00000X"] = TaxonomyEntry(
    code="261Q00000X",
    descriptive_name='A facility or distinct part of one used for the diagnosis and treatment of outpatients. "Clinic/Center" is',
    specialty='Clinic/Center',
    specialization='Phlebotomy',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QA0005X"] = TaxonomyEntry(
    code="261QA0005X",
    descriptive_name='An abortion/family planning facility where services are provided at a fixed specific location. An',
    specialty='Clinic/Center',
    specialization='Ambulatory Family Planning Facility',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QA0006X"] = TaxonomyEntry(
    code="261QA0006X",
    descriptive_name='A fertility facility, which may be licensed, registered, or certified in some states, that is not hospital-based,',
    specialty='#Type!',
    specialization='Ambulatory Fertility Facility',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QA0600X"] = TaxonomyEntry(
    code="261QA0600X",
    descriptive_name='#Type!',
    specialty='education and/or training.',
    specialization='Adult Day Care',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QA0900X"] = TaxonomyEntry(
    code="261QA0900X",
    descriptive_name='An entity, facility, or distinct part of a facility providing counseling, fitting, custom design, prescriptive, and',
    specialty='#Type!',
    specialization='Amputee',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QA1903X"] = TaxonomyEntry(
    code="261QA1903X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Ambulatory Surgical',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QA3000X"] = TaxonomyEntry(
    code="261QA3000X",
    descriptive_name='An entity, facility, or distinct part of a facility staffed by audiology and/or speech professionals with special',
    specialty='training services related to congenital or postoperative absence of all or part of a limb or limbs.',
    specialization='Augmentative Communication',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QB0400X"] = TaxonomyEntry(
    code="261QB0400X",
    descriptive_name='A freestanding birth center is a health facility other than a hospital where childbirth is planned to occur',
    specialty='Clinic/Center',
    specialization='Birthing',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QC0050X"] = TaxonomyEntry(
    code="261QC0050X",
    descriptive_name='An outpatient entity, facility, or distinct part of a facility within or affiliated with a Critical Access Hospital',
    specialty='#Type!',
    specialization='Critical Access Hospital',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QC1500X"] = TaxonomyEntry(
    code="261QC1500X",
    descriptive_name='#Type!',
    specialty='postpartum care, as well as other ambulatory services for women and newborns.',
    specialization='Community Health',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QC1800X"] = TaxonomyEntry(
    code="261QC1800X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Corporate Health',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QD0000X"] = TaxonomyEntry(
    code="261QD0000X",
    descriptive_name='#Type!',
    specialty='certified.',
    specialization='Dental',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QD1600X"] = TaxonomyEntry(
    code="261QD1600X",
    descriptive_name='An entity, facility, or distinct part of a facility providing comprehensive, multidiscipline diagnostic,',
    specialty='#Type!',
    specialization='Developmental Disabilities',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QE0002X"] = TaxonomyEntry(
    code="261QE0002X",
    descriptive_name='#Type!',
    specialty='Clinic/Center',
    specialization='Emergency Care',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QE0700X"] = TaxonomyEntry(
    code="261QE0700X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='End-Stage Renal Disease (ESRD) Treatment',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QE0800X"] = TaxonomyEntry(
    code="261QE0800X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Endoscopy',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QF0050X"] = TaxonomyEntry(
    code="261QF0050X",
    descriptive_name='An entity, facility, or distinct part of a facility, or mobile unit providing non-surgical, family',
    specialty='#Type!',
    specialization='Family Planning, Non-Surgical',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QF0400X"] = TaxonomyEntry(
    code="261QF0400X",
    descriptive_name='#Type!',
    specialty='contraceptives or prescriptions for contraceptives.',
    specialization='Federally Qualified Health Center (FQHC)',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QG0250X"] = TaxonomyEntry(
    code="261QG0250X",
    descriptive_name='An entity, facility, or distinct part of a facility providing analysis of family history, genetic laboratory testing',
    specialty='#Type!',
    specialization='Genetics',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QH0100X"] = TaxonomyEntry(
    code="261QH0100X",
    descriptive_name='Hearing and Speech Specialization:',
    specialty='Clinic/Center',
    specialization='Health Service',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QH0700X"] = TaxonomyEntry(
    code="261QH0700X",
    descriptive_name='An entity, facility, or distinct part of a facility providing diagnostic, treatment, prescriptive, and therapy',
    specialty='Definition to come...',
    specialization='Hearing and Speech',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QI0500X"] = TaxonomyEntry(
    code="261QI0500X",
    descriptive_name='#Type!',
    specialty='speech ability.',
    specialization='Infusion Therapy',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QL0400X"] = TaxonomyEntry(
    code="261QL0400X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Lithotripsy',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QM0801X"] = TaxonomyEntry(
    code="261QM0801X",
    descriptive_name='#Type!',
    specialty='respiratory/ventilator care, medications and therapies, etc.).',
    specialization='Mental Health (Including Community Mental Health Center)',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QM0850X"] = TaxonomyEntry(
    code="261QM0850X",
    descriptive_name='An entity, facility, or distinct part of a facility providing diagnostic, treatment, and prescriptive services',
    specialty='#Type!',
    specialization='Adult Mental Health',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QM0855X"] = TaxonomyEntry(
    code="261QM0855X",
    descriptive_name='An entity, facility, or distinct part of a facility providing diagnostic, treatment, and prescriptive services',
    specialty='#Type!',
    specialization='Adolescent and Children Mental Health',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QM1000X"] = TaxonomyEntry(
    code="261QM1000X",
    descriptive_name='#Type!',
    specialty='services related to individuals with drug addiction.',
    specialization='Migrant Health',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QM1100X"] = TaxonomyEntry(
    code="261QM1100X",
    descriptive_name='The Defense Health Program or U.S. Coast Guard funded "fixed" facilities or distinct parts of a facility,',
    specialty='pharmacy or patient transport.',
    specialization='Military/U.S. Coast Guard Outpatient',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QM1101X"] = TaxonomyEntry(
    code="261QM1101X",
    descriptive_name='That part of a "fixed" (non-temporary, non-deployed) DoD or Coast Guard entity furnishing surgical',
    specialty='Clinic/Center',
    specialization='Military and U.S. Coast Guard Ambulatory Procedure',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QM1102X"] = TaxonomyEntry(
    code="261QM1102X",
    descriptive_name='"Non-fixed" facilities or distinct parts of a "non-fixed" facility, providing outpatient medical and dental',
    specialty='pharmaceuticals.',
    specialization='Military Outpatient Operational (Transportable) Component',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QM1103X"] = TaxonomyEntry(
    code="261QM1103X",
    descriptive_name='"Non-fixed" facilities or distinct parts of a "non-fixed" facility, providing outpatient surgical procedures',
    specialty='#Type!',
    specialization='Military Ambulatory Procedure Visits Operational (Transportable)',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QM1200X"] = TaxonomyEntry(
    code="261QM1200X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Magnetic Resonance Imaging (MRI)',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QM1300X"] = TaxonomyEntry(
    code="261QM1300X",
    descriptive_name='#Type!',
    specialty='issued directly to a patient from an outpatient pharmacy or patient transport.',
    specialization='Multi-Specialty',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QM2500X"] = TaxonomyEntry(
    code="261QM2500X",
    descriptive_name='An entity, facility, or distinct part of a facility providing diagnostic, treatment, and prescriptive services',
    specialty='#Type!',
    specialization='Medical Specialty',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QM2800X"] = TaxonomyEntry(
    code="261QM2800X",
    descriptive_name='An entity, facility, or distinct part of a facility providing diagnostic, and replacement maintenance treatment',
    specialty='#Type!',
    specialization='Methadone',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QM3000X"] = TaxonomyEntry(
    code="261QM3000X",
    descriptive_name='An entity, facility, or distinct part of a facility specially equipped and staffed to provide care for medically',
    specialty='Clinic/Center',
    specialization='Medically Fragile Infants and Children Day Care',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QP0904X"] = TaxonomyEntry(
    code="261QP0904X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Public Health, Federal',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QP0905X"] = TaxonomyEntry(
    code="261QP0905X",
    descriptive_name='#Type!',
    specialty='Clinic/Center',
    specialization='Public Health, State or Local',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QP1100X"] = TaxonomyEntry(
    code="261QP1100X",
    descriptive_name='#Type!',
    specialty='http://guidetoptpractice.apta.org/ ; American Physical Therapy Association, www.apta.org.',
    specialization='Podiatric',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QP2000X"] = TaxonomyEntry(
    code="261QP2000X",
    descriptive_name='An entity, facility, or distinct part of a facility providing diagnostic and treatment services related to',
    specialty='Clinic/Center',
    specialization='Physical Therapy',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QP2300X"] = TaxonomyEntry(
    code="261QP2300X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Primary Care',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QP2400X"] = TaxonomyEntry(
    code="261QP2400X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Prison Health',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QP3300X"] = TaxonomyEntry(
    code="261QP3300X",
    descriptive_name='#Type!',
    specialty='Source: Council on Dental Education and Licensure, American Dental Association',
    specialization='Pain',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QR0200X"] = TaxonomyEntry(
    code="261QR0200X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Radiology',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QR0206X"] = TaxonomyEntry(
    code="261QR0206X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Radiology, Mammography',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QR0207X"] = TaxonomyEntry(
    code="261QR0207X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Radiology, Mobile Mammography',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QR0208X"] = TaxonomyEntry(
    code="261QR0208X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Radiology, Mobile',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QR0400X"] = TaxonomyEntry(
    code="261QR0400X",
    descriptive_name='#Type!',
    specialty='Clinic/Center',
    specialization='Rehabilitation',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QR0401X"] = TaxonomyEntry(
    code="261QR0401X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Rehabilitation, Comprehensive Outpatient Rehabilitation Facility (CORF)',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QR0404X"] = TaxonomyEntry(
    code="261QR0404X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Rehabilitation, Cardiac Facilities',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QR0405X"] = TaxonomyEntry(
    code="261QR0405X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Rehabilitation, Substance Use Disorder',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QR0800X"] = TaxonomyEntry(
    code="261QR0800X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Recovery Care',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QR1100X"] = TaxonomyEntry(
    code="261QR1100X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Research',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QR1300X"] = TaxonomyEntry(
    code="261QR1300X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Rural Health',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QS0112X"] = TaxonomyEntry(
    code="261QS0112X",
    descriptive_name='The specialty of dentistry which includes the diagnosis, surgical and adjunctive treatment of diseases,',
    specialty='#Type!',
    specialization='Oral and Maxillofacial Surgery',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QS0132X"] = TaxonomyEntry(
    code="261QS0132X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Ophthalmologic Surgery',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QS1000X"] = TaxonomyEntry(
    code="261QS1000X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Student Health',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QS1200X"] = TaxonomyEntry(
    code="261QS1200X",
    descriptive_name='#Type!',
    specialty='Clinic/Center',
    specialization='Sleep Disorder Diagnostic',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QU0200X"] = TaxonomyEntry(
    code="261QU0200X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Urgent Care',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QV0200X"] = TaxonomyEntry(
    code="261QV0200X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='VA',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QX0100X"] = TaxonomyEntry(
    code="261QX0100X",
    descriptive_name='#Type!',
    specialty='Clinic/Center',
    specialization='Occupational Medicine',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QX0200X"] = TaxonomyEntry(
    code="261QX0200X",
    descriptive_name='An entity, facility, or distinct part of a facility providing diagnostic, treatment and prescriptive services',
    specialty='#Type!',
    specialization='Oncology',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["261QX0203X"] = TaxonomyEntry(
    code="261QX0203X",
    descriptive_name='#Type!',
    specialty='chemotherapeutic agents.',
    specialization='Oncology, Radiation',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["273100000X"] = TaxonomyEntry(
    code="273100000X",
    descriptive_name='An Epilepsy Unit is a distinct unit of a hospital that provides services that may include observation, urgent',
    specialty='Epilepsy Unit',
    specialization='VA',
    provider_grouping='Ambulatory Health Care Facilities',
)

TAXONOMY_MAPPING["273R00000X"] = TaxonomyEntry(
    code="273R00000X",
    descriptive_name='In general, a distinct unit of a hospital that provides acute or long-term care to emotionally disturbed',
    specialty='Psychiatric Unit',
    specialization='VA',
    provider_grouping='Hospital Units',
)

TAXONOMY_MAPPING["273Y00000X"] = TaxonomyEntry(
    code="273Y00000X",
    descriptive_name='In general, a distinct unit of a general acute care hospital that provides care encompassing a',
    specialty='Rehabilitation Unit',
    specialization='VA',
    provider_grouping='Hospital Units',
)

TAXONOMY_MAPPING["275N00000X"] = TaxonomyEntry(
    code="275N00000X",
    descriptive_name='A unit of a hospital that has a Medicare provider agreement and has been granted approval from HCFA',
    specialty='Medicare Defined Swing Bed Unit',
    specialization='VA',
    provider_grouping='Hospital Units',
)

TAXONOMY_MAPPING["276400000X"] = TaxonomyEntry(
    code="276400000X",
    descriptive_name='A distinct part of a hospital that provides medically monitored, interdisciplinary addiction-focused',
    specialty='Rehabilitation, Substance Use Disorder Unit',
    specialization='VA',
    provider_grouping='Hospital Units',
)

TAXONOMY_MAPPING["281P00000X"] = TaxonomyEntry(
    code="281P00000X",
    descriptive_name='(1) A hospital including a physical plant and personnel that provides multidisciplinary diagnosis and',
    specialty='Chronic Disease Hospital',
    specialization='VA',
    provider_grouping='Hospitals',
)

TAXONOMY_MAPPING["281PC2000X"] = TaxonomyEntry(
    code="281PC2000X",
    descriptive_name='#Type!',
    specialty='Management, New York: Facts On File Publications, 1988.',
    specialization='Children',
    provider_grouping='Hospitals',
)

TAXONOMY_MAPPING["282E00000X"] = TaxonomyEntry(
    code="282E00000X",
    descriptive_name='Long-term care hospitals (LTCHs) furnish extended medical and rehabilitative care to individuals who are',
    specialty='Long Term Care Hospital',
    specialization='Women',
    provider_grouping='Hospitals',
)

TAXONOMY_MAPPING["282J00000X"] = TaxonomyEntry(
    code="282J00000X",
    descriptive_name='Furnishes only nonmedical nursing items and services to patients who choose to rely solely upon a',
    specialty='Religious Nonmedical Health Care Institution',
    specialization='Children',
    provider_grouping='Hospitals',
)

TAXONOMY_MAPPING["282N00000X"] = TaxonomyEntry(
    code="282N00000X",
    descriptive_name='An acute general hospital is an institution whose primary function is to provide inpatient diagnostic and',
    specialty='General Acute Care Hospital',
    specialization='Children',
    provider_grouping='Hospitals',
)

TAXONOMY_MAPPING["282NC0060X"] = TaxonomyEntry(
    code="282NC0060X",
    descriptive_name='205 JANUARY 2024',
    specialty='#Type!',
    specialization='Critical Access',
    provider_grouping='Hospitals',
)

TAXONOMY_MAPPING["282NC2000X"] = TaxonomyEntry(
    code="282NC2000X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Children',
    provider_grouping='Hospitals',
)

TAXONOMY_MAPPING["282NR1301X"] = TaxonomyEntry(
    code="282NR1301X",
    descriptive_name='#Type!',
    specialty='General Acute Care Hospital',
    specialization='Rural',
    provider_grouping='Hospitals',
)

TAXONOMY_MAPPING["282NW0100X"] = TaxonomyEntry(
    code="282NW0100X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Women',
    provider_grouping='Hospitals',
)

TAXONOMY_MAPPING["283Q00000X"] = TaxonomyEntry(
    code="283Q00000X",
    descriptive_name='An organization including a physical plant and personnel that provides multidisciplinary diagnostic and',
    specialty='Psychiatric Hospital',
    specialization='Military General Acute Care Hospital. Operational (Transportable)',
    provider_grouping='Hospitals',
)

TAXONOMY_MAPPING["283X00000X"] = TaxonomyEntry(
    code="283X00000X",
    descriptive_name='A hospital or facility that provides health-related, social and/or vocational services to disabled persons to',
    specialty='Rehabilitation Hospital',
    specialization='Military General Acute Care Hospital. Operational (Transportable)',
    provider_grouping='Hospitals',
)

TAXONOMY_MAPPING["283XC2000X"] = TaxonomyEntry(
    code="283XC2000X",
    descriptive_name='#Type!',
    specialty='Rehabilitation Hospital',
    specialization='Children',
    provider_grouping='Hospitals',
)

TAXONOMY_MAPPING["284300000X"] = TaxonomyEntry(
    code="284300000X",
    descriptive_name='A designation by the AHA of a hospital whose primary function of the institution is to provide diagnostic',
    specialty='Special Hospital',
    specialization='Children',
    provider_grouping='Hospitals',
)

TAXONOMY_MAPPING["286500000X"] = TaxonomyEntry(
    code="286500000X",
    descriptive_name='A health care facility operated by the Department of Defense.',
    specialty='Military Hospital',
    specialization='Women',
    provider_grouping='Hospitals',
)

TAXONOMY_MAPPING["2865C1500X"] = TaxonomyEntry(
    code="2865C1500X",
    descriptive_name='206 JANUARY 2024',
    specialty='#Type!',
    specialization='Community Health',
    provider_grouping='Hospitals',
)

TAXONOMY_MAPPING["2865M2000X"] = TaxonomyEntry(
    code="2865M2000X",
    descriptive_name='A Department of Defense (DoD) health care organization furnishing inpatient care 24 hours per day in',
    specialty='Military Hospital',
    specialization='Military General Acute Care Hospital',
    provider_grouping='Hospitals',
)

TAXONOMY_MAPPING["2865X1600X"] = TaxonomyEntry(
    code="2865X1600X",
    descriptive_name='A Department of Defense (DoD) health care organization furnishing inpatient care 24 hours per day in',
    specialty='well as "pass-through" items.',
    specialization='Military General Acute Care Hospital. Operational (Transportable)',
    provider_grouping='Hospitals',
)

TAXONOMY_MAPPING["287300000X"] = TaxonomyEntry(
    code="287300000X",
    descriptive_name='Inactive, use 282J00000X',
    specialty='Christian Science Sanitorium',
    specialization='VA',
    provider_grouping='Hospitals',
)

TAXONOMY_MAPPING["291900000X"] = TaxonomyEntry(
    code="291900000X",
    descriptive_name='A Department of Defense (DoD) medical clinical reference laboratory not associated with a DoD Hospital',
    specialty='Military Clinical Medical Laboratory',
    specialization='Children',
    provider_grouping='Laboratories',
)

TAXONOMY_MAPPING["291U00000X"] = TaxonomyEntry(
    code="291U00000X",
    descriptive_name='(1) A clinical laboratory is a facility for the biological, microbiological, serological, chemical,',
    specialty='Clinical Medical Laboratory',
    specialization='Children',
    provider_grouping='Laboratories',
)

TAXONOMY_MAPPING["292200000X"] = TaxonomyEntry(
    code="292200000X",
    descriptive_name="A commercial laboratory specializing in the construction of dental appliances that conform to a dentist's",
    specialty='Dental Laboratory',
    specialization='Children',
    provider_grouping='Laboratories',
)

TAXONOMY_MAPPING["293D00000X"] = TaxonomyEntry(
    code="293D00000X",
    descriptive_name="A laboratory that operates independently of a hospital and physician's office to furnish physiological",
    specialty='Physiological Laboratory',
    specialization='Children',
    provider_grouping='Laboratories',
)

TAXONOMY_MAPPING["302F00000X"] = TaxonomyEntry(
    code="302F00000X",
    descriptive_name='(1) An EPO is a form of PPO, in which patients must visit a caregiver that is specified on its panel of',
    specialty='Exclusive Provider Organization',
    specialization='Children',
    provider_grouping='Managed Care Organizations',
)

TAXONOMY_MAPPING["302R00000X"] = TaxonomyEntry(
    code="302R00000X",
    descriptive_name="(1) A form of health insurance in which its members prepay a premium for the HMO's health services",
    specialty='Health Maintenance Organization',
    specialization='Children',
    provider_grouping='Managed Care Organizations',
)

TAXONOMY_MAPPING["305R00000X"] = TaxonomyEntry(
    code="305R00000X",
    descriptive_name='A group of physicians and/or hospitals who contract with an employer to provide services to their',
    specialty='Preferred Provider Organization',
    specialization='Children',
    provider_grouping='Managed Care Organizations',
)

TAXONOMY_MAPPING["305S00000X"] = TaxonomyEntry(
    code="305S00000X",
    descriptive_name='This product may also be called an open-ended HMO and offers a transition product incorporating',
    specialty='Point of Service',
    specialization='Children',
    provider_grouping='Managed Care Organizations',
)

TAXONOMY_MAPPING["310400000X"] = TaxonomyEntry(
    code="310400000X",
    descriptive_name='A facility providing supportive services to individuals who can function independently in most areas of',
    specialty='Assisted Living Facility',
    specialization='Children',
    provider_grouping='Nursing & Custodial Care Facilities',
)

TAXONOMY_MAPPING["3104A0625X"] = TaxonomyEntry(
    code="3104A0625X",
    descriptive_name='A facility providing supportive services to individuals who can function independently in most areas of',
    specialty='special training in dealing with and redirecting negative, violent or destructive behaviors.',
    specialization='Assisted Living, Mental Illness',
    provider_grouping='Nursing & Custodial Care Facilities',
)

TAXONOMY_MAPPING["3104A0630X"] = TaxonomyEntry(
    code="3104A0630X",
    descriptive_name='A facility providing supportive services to individuals who can function independently in most areas of',
    specialty='activity, but need assistance and/or monitoring to assure safety and well being.',
    specialization='Assisted Living, Behavioral Disturbances',
    provider_grouping='Nursing & Custodial Care Facilities',
)

TAXONOMY_MAPPING["310500000X"] = TaxonomyEntry(
    code="310500000X",
    descriptive_name='A nursing facility that provides an intermediate level of nursing care to individuals whose functional',
    specialty='Intermediate Care Facility, Mental Illness',
    specialization='Adult Care Home',
    provider_grouping='Nursing & Custodial Care Facilities',
)

TAXONOMY_MAPPING["311500000X"] = TaxonomyEntry(
    code="311500000X",
    descriptive_name='A freestanding facility or special care unit of a long term care facility focusing on patient care of',
    specialty='Alzheimer Center (Dementia Center)',
    specialization='Children',
    provider_grouping='Nursing & Custodial Care Facilities',
)

TAXONOMY_MAPPING["311Z00000X"] = TaxonomyEntry(
    code="311Z00000X",
    descriptive_name='A facility providing care that serves to assist an individual in the activities of daily living, such as',
    specialty='Custodial Care Facility',
    specialization='Assisted Living, Mental Illness',
    provider_grouping='Nursing & Custodial Care Facilities',
)

TAXONOMY_MAPPING["311ZA0620X"] = TaxonomyEntry(
    code="311ZA0620X",
    descriptive_name='A custodial care facility providing supportive and personal care services to disabled and/or elderly',
    specialty='Source: Paraphrased from Section 3159 A3 of the Medicare Intermediary Manual.',
    specialization='Adult Care Home',
    provider_grouping='Nursing & Custodial Care Facilities',
)

TAXONOMY_MAPPING["313M00000X"] = TaxonomyEntry(
    code="313M00000X",
    descriptive_name='An institution (or a distinct part of an institution) which- (1) is primarily engaged in providing to residents-',
    specialty='Nursing Facility/Intermediate Care Facility',
    specialization='Adult Care Home',
    provider_grouping='Nursing & Custodial Care Facilities',
)

TAXONOMY_MAPPING["314000000X"] = TaxonomyEntry(
    code="314000000X",
    descriptive_name='(1) A skilled nursing facility is a facility or distinct part of an institution whose primary function is to provide',
    specialty='Skilled Nursing Facility',
    specialization='Adult Care Home',
    provider_grouping='Nursing & Custodial Care Facilities',
)

TAXONOMY_MAPPING["3140N1450X"] = TaxonomyEntry(
    code="3140N1450X",
    descriptive_name='A nursing care facility designed and staffed for the provision of nursing care and appropriate educational',
    specialty='(2) AHA Guide, 1996 Annual Survey.',
    specialization='Nursing Care, Pediatric',
    provider_grouping='Nursing & Custodial Care Facilities',
)

TAXONOMY_MAPPING["315D00000X"] = TaxonomyEntry(
    code="315D00000X",
    descriptive_name='A provider organization, or distinct part of the organization, which renders an interdisciplinary program',
    specialty='Hospice, Inpatient',
    specialization='Adult Care Home',
    provider_grouping='Nursing & Custodial Care Facilities',
)

TAXONOMY_MAPPING["315P00000X"] = TaxonomyEntry(
    code="315P00000X",
    descriptive_name='An intermediate care facility providing services for individuals with intellectual disabilities.',
    specialty='Intermediate Care Facility, Intellectual Disabilities',
    specialization='Adult Care Home',
    provider_grouping='Nursing & Custodial Care Facilities',
)

TAXONOMY_MAPPING["317400000X"] = TaxonomyEntry(
    code="317400000X",
    descriptive_name='Inactive, use 282J00000X',
    specialty='Christian Science Facility',
    specialization='Assisted Living, Mental Illness',
    provider_grouping='Nursing & Custodial Care Facilities',
)

TAXONOMY_MAPPING["320600000X"] = TaxonomyEntry(
    code="320600000X",
    descriptive_name='A residential facility that provides habilitation services and other care and treatment to adults or children',
    specialty='Residential Treatment Facility, Intellectual and/or Developmental Disabilities',
    specialization='Nursing Care, Pediatric',
    provider_grouping='Residential Treatment Facilities',
)

TAXONOMY_MAPPING["320700000X"] = TaxonomyEntry(
    code="320700000X",
    descriptive_name='A residential facility that provides habilitation services and other care and treatment to adults or children',
    specialty='Residential Treatment Facility, Physical Disabilities',
    specialization='Nursing Care, Pediatric',
    provider_grouping='Residential Treatment Facilities',
)

TAXONOMY_MAPPING["320800000X"] = TaxonomyEntry(
    code="320800000X",
    descriptive_name='A home-like residential facility providing psychiatric treatment and psycho/social rehabilitative services to',
    specialty='Community Based Residential Treatment Facility, Mental Illness',
    specialization='Nursing Care, Pediatric',
    provider_grouping='Residential Treatment Facilities',
)

TAXONOMY_MAPPING["320900000X"] = TaxonomyEntry(
    code="320900000X",
    descriptive_name='A home-like residential facility providing habilitation, support and monitoring services to individuals',
    specialty='Disabilities',
    specialization='Nursing Care, Pediatric',
    provider_grouping='Residential Treatment Facilities',
)

TAXONOMY_MAPPING["322D00000X"] = TaxonomyEntry(
    code="322D00000X",
    descriptive_name='A residential facility that provides habilitation services and other care and treatment to children diagnosed',
    specialty='Residential Treatment Facility, Emotionally Disturbed Children',
    specialization='Nursing Care, Pediatric',
    provider_grouping='Residential Treatment Facilities',
)

TAXONOMY_MAPPING["323P00000X"] = TaxonomyEntry(
    code="323P00000X",
    descriptive_name='A residential treatment facility (RTF) is a facility or distinct part of a facility that provides to children and',
    specialty='Psychiatric Residential Treatment Facility',
    specialization='Nursing Care, Pediatric',
    provider_grouping='Residential Treatment Facilities',
)

TAXONOMY_MAPPING["324500000X"] = TaxonomyEntry(
    code="324500000X",
    descriptive_name='A facility or distinct part of a facility that provides a 24 hr therapeutically planned living and rehabilitative',
    specialty='Substance Abuse Rehabilitation Facility',
    specialization='Nursing Care, Pediatric',
    provider_grouping='Residential Treatment Facilities',
)

TAXONOMY_MAPPING["3245S0500X"] = TaxonomyEntry(
    code="3245S0500X",
    descriptive_name='A facility or distinct part of a facility that provides a 24 hr therapeutically planned living and rehabilitative',
    specialty='other substances.',
    specialization='Substance Abuse Treatment, Children',
    provider_grouping='Residential Treatment Facilities',
)

TAXONOMY_MAPPING["331L00000X"] = TaxonomyEntry(
    code="331L00000X",
    descriptive_name='An institution (organization or distinct part thereof) that performs, or is responsible for the performance of,',
    specialty='Blood Bank',
    specialization='Respite Care, Physical Disabilities, Child',
    provider_grouping='Suppliers',
)

TAXONOMY_MAPPING["332000000X"] = TaxonomyEntry(
    code="332000000X",
    descriptive_name='A Department of Defense (DoD) or U.S. Coast Guard entity whose primary function is to store, prepare',
    specialty='Military/U.S. Coast Guard Pharmacy',
    specialization='Parenteral & Enteral Nutrition',
    provider_grouping='Suppliers',
)

TAXONOMY_MAPPING["332100000X"] = TaxonomyEntry(
    code="332100000X",
    descriptive_name='Department of Veterans Affairs (VA) Pharmacy means any place under VA jurisdiction where drugs are',
    specialty='Department of Veterans Affairs (VA) Pharmacy',
    specialization='Respite Care, Physical Disabilities, Child',
    provider_grouping='Suppliers',
)

TAXONOMY_MAPPING["332800000X"] = TaxonomyEntry(
    code="332800000X",
    descriptive_name='An Indian Health Service/Tribal/Urban Indian Health (I/T/U) Pharmacy means a pharmacy operated by',
    specialty='Indian Health Service/Tribal/Urban Indian Health (I/T/U) Pharmacy',
    specialization='Parenteral & Enteral Nutrition',
    provider_grouping='Suppliers',
)

TAXONOMY_MAPPING["332900000X"] = TaxonomyEntry(
    code="332900000X",
    descriptive_name='A site other than a pharmacy that dispenses medicinal preparations under the supervision of a physician',
    specialty='Non-Pharmacy Dispensing Site',
    specialization='Parenteral & Enteral Nutrition',
    provider_grouping='Suppliers',
)

TAXONOMY_MAPPING["332B00000X"] = TaxonomyEntry(
    code="332B00000X",
    descriptive_name='A supplier of medical equipment such as respirators, wheelchairs, home dialysis systems, or monitoring',
    specialty='Durable Medical Equipment & Medical Supplies',
    specialization='Respite Care, Physical Disabilities, Child',
    provider_grouping='Suppliers',
)

TAXONOMY_MAPPING["332BC3200X"] = TaxonomyEntry(
    code="332BC3200X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Customized Equipment',
    provider_grouping='Suppliers',
)

TAXONOMY_MAPPING["332BD1200X"] = TaxonomyEntry(
    code="332BD1200X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Dialysis Equipment & Supplies',
    provider_grouping='Suppliers',
)

TAXONOMY_MAPPING["332BN1400X"] = TaxonomyEntry(
    code="332BN1400X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Nursing Facility Supplies',
    provider_grouping='Suppliers',
)

TAXONOMY_MAPPING["332BP3500X"] = TaxonomyEntry(
    code="332BP3500X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Parenteral & Enteral Nutrition',
    provider_grouping='Suppliers',
)

TAXONOMY_MAPPING["332BX2000X"] = TaxonomyEntry(
    code="332BX2000X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Oxygen Equipment & Supplies',
    provider_grouping='Suppliers',
)

TAXONOMY_MAPPING["332G00000X"] = TaxonomyEntry(
    code="332G00000X",
    descriptive_name='An eye bank procures and distributes eyes for transplant, education and research. To promote patient',
    specialty='Eye Bank',
    specialization='Parenteral & Enteral Nutrition',
    provider_grouping='Suppliers',
)

TAXONOMY_MAPPING["332H00000X"] = TaxonomyEntry(
    code="332H00000X",
    descriptive_name='An organization that provides spectacles, contact lenses, and other vision enhancement devices',
    specialty='Eyewear Supplier',
    specialization='Parenteral & Enteral Nutrition',
    provider_grouping='Suppliers',
)

TAXONOMY_MAPPING["332S00000X"] = TaxonomyEntry(
    code="332S00000X",
    descriptive_name='The manufacture and/or sale of electronic hearing aids, their component parts, and related products and',
    specialty='Hearing Aid Equipment',
    specialization='Parenteral & Enteral Nutrition',
    provider_grouping='Suppliers',
)

TAXONOMY_MAPPING["332U00000X"] = TaxonomyEntry(
    code="332U00000X",
    descriptive_name='Home-delivered meals are those services or activities designed to prepare and deliver one or more meals',
    specialty='Home Delivered Meals',
    specialization='Parenteral & Enteral Nutrition',
    provider_grouping='Suppliers',
)

TAXONOMY_MAPPING["333300000X"] = TaxonomyEntry(
    code="333300000X",
    descriptive_name='A supplier of a personal emergency response system (PERS), which is an electronic device that enables',
    specialty='Emergency Response System Companies',
    specialization='Parenteral & Enteral Nutrition',
    provider_grouping='Suppliers',
)

TAXONOMY_MAPPING["333600000X"] = TaxonomyEntry(
    code="333600000X",
    descriptive_name='A facility used by pharmacists for the compounding and dispensing of medicinal preparations and other',
    specialty='Pharmacy',
    specialization='Parenteral & Enteral Nutrition',
    provider_grouping='Suppliers',
)

TAXONOMY_MAPPING["3336C0002X"] = TaxonomyEntry(
    code="3336C0002X",
    descriptive_name='A pharmacy in a clinic, emergency room or hospital (outpatient) that dispenses medications to patients for',
    specialty='definition]',
    specialization='Clinic Pharmacy',
    provider_grouping='Suppliers',
)

TAXONOMY_MAPPING["3336C0003X"] = TaxonomyEntry(
    code="3336C0003X",
    descriptive_name='A pharmacy where pharmacists store, prepare, and dispense medicinal preparations and/or prescriptions',
    specialty='Source: Developed by National Council for Prescription Drug Programs (NCPDP), National Home Infusion',
    specialization='Community/Retail Pharmacy',
    provider_grouping='Suppliers',
)

TAXONOMY_MAPPING["3336C0004X"] = TaxonomyEntry(
    code="3336C0004X",
    descriptive_name='A pharmacy that specializes in the preparation of components into a drug preparation as the result of a',
    specialty='Pharmacy',
    specialization='Compounding Pharmacy',
    provider_grouping='Suppliers',
)

TAXONOMY_MAPPING["3336H0001X"] = TaxonomyEntry(
    code="3336H0001X",
    descriptive_name='Pharmacy-based, decentralized patient care organization with expertise in USP 797-compliant sterile',
    specialty='Sources: NABP Model Practice Act, Appendix C - Good Compounding Practice, USP <795> and <797>,',
    specialization='Home Infusion Therapy Pharmacy',
    provider_grouping='Suppliers',
)

TAXONOMY_MAPPING["3336I0012X"] = TaxonomyEntry(
    code="3336I0012X",
    descriptive_name='A pharmacy in a hospital (inpatient) or institution used by pharmacists for the compounding and delivery',
    specialty='infusion nursing services, supplies and equipment are provided to optimize efficacy and compliance.',
    specialization='Institutional Pharmacy',
    provider_grouping='Suppliers',
)

TAXONOMY_MAPPING["3336L0003X"] = TaxonomyEntry(
    code="3336L0003X",
    descriptive_name='A pharmacy that dispenses medicinal preparations delivered to patients residing within an intermediate or',
    specialty='Source: Developed by National Council for Prescription Drug Programs (NCPDP), National Home Infusion',
    specialization='Long Term Care Pharmacy',
    provider_grouping='Suppliers',
)

TAXONOMY_MAPPING["3336M0002X"] = TaxonomyEntry(
    code="3336M0002X",
    descriptive_name='A pharmacy where pharmacists compound or dispense prescriptions or other medications in accordance',
    specialty='Pharmacy',
    specialization='Mail Order Pharmacy',
    provider_grouping='Suppliers',
)

TAXONOMY_MAPPING["3336M0003X"] = TaxonomyEntry(
    code="3336M0003X",
    descriptive_name='A pharmacy owned by a managed care organization (MCO) used by pharmacists for the compounding',
    specialty='Source: Developed by National Council for Prescription Drug Programs (NCPDP), National Home Infusion',
    specialization='Managed Care Organization Pharmacy',
    provider_grouping='Suppliers',
)

TAXONOMY_MAPPING["3336N0007X"] = TaxonomyEntry(
    code="3336N0007X",
    descriptive_name='A pharmacy dedicated to the compounding and dispensing of radioactive materials for use in nuclear',
    specialty='Source: Developed by National Council for Prescription Drug Programs (NCPDP), National Home Infusion',
    specialization='Nuclear Pharmacy',
    provider_grouping='Suppliers',
)

TAXONOMY_MAPPING["3336S0011X"] = TaxonomyEntry(
    code="3336S0011X",
    descriptive_name='A pharmacy that dispenses generally low volume and high cost medicinal preparations to patients who',
    specialty='Source: Developed by National Council for Prescription Drug Programs (NCPDP), National Home Infusion',
    specialization='Specialty Pharmacy',
    provider_grouping='Suppliers',
)

TAXONOMY_MAPPING["335E00000X"] = TaxonomyEntry(
    code="335E00000X",
    descriptive_name='An organization that provides prosthetic and orthotic care which may include, but is not limited to, patient',
    specialty='Prosthetic/Orthotic Supplier',
    specialization='Specialty Pharmacy',
    provider_grouping='Suppliers',
)

TAXONOMY_MAPPING["335G00000X"] = TaxonomyEntry(
    code="335G00000X",
    descriptive_name='A supplier of special replacement foods for clients with errors of metabolism that prohibit them from',
    specialty='Medical Foods Supplier',
    specialization='Parenteral & Enteral Nutrition',
    provider_grouping='Suppliers',
)

TAXONOMY_MAPPING["335U00000X"] = TaxonomyEntry(
    code="335U00000X",
    descriptive_name='A federally designated organization that works with hospital personnel in retrieval of organs for',
    specialty='Organ Procurement Organization',
    specialization='Parenteral & Enteral Nutrition',
    provider_grouping='Suppliers',
)

TAXONOMY_MAPPING["335V00000X"] = TaxonomyEntry(
    code="335V00000X",
    descriptive_name='A supplier that provides one or more of the following portable services, including but not limited to, x-ray,',
    specialty='Portable X-ray and/or Other Portable Diagnostic Imaging Supplier',
    specialization='Specialty Pharmacy',
    provider_grouping='Suppliers',
)

TAXONOMY_MAPPING["341600000X"] = TaxonomyEntry(
    code="341600000X",
    descriptive_name='An emergency vehicle used for transporting patients to a health care facility after injury or illness. Types',
    specialty='Ambulance',
    specialization='Specialty Pharmacy',
    provider_grouping='Transportation Services',
)

TAXONOMY_MAPPING["3416A0800X"] = TaxonomyEntry(
    code="3416A0800X",
    descriptive_name='Land Transport Specialization:',
    specialty='37.',
    specialization='Air Transport',
    provider_grouping='Transportation Services',
)

TAXONOMY_MAPPING["3416L0300X"] = TaxonomyEntry(
    code="3416L0300X",
    descriptive_name='Water Transport Specialization:',
    specialty='Definition to come...',
    specialization='Land Transport',
    provider_grouping='Transportation Services',
)

TAXONOMY_MAPPING["3416S0300X"] = TaxonomyEntry(
    code="3416S0300X",
    descriptive_name='Bus',
    specialty='Definition to come...',
    specialization='Water Transport',
    provider_grouping='Transportation Services',
)

TAXONOMY_MAPPING["341800000X"] = TaxonomyEntry(
    code="341800000X",
    descriptive_name='226 JANUARY 2024',
    specialty='Military/U.S. Coast Guard Transport',
    specialization='Water Transport',
    provider_grouping='Transportation Services',
)

TAXONOMY_MAPPING["3418M1110X"] = TaxonomyEntry(
    code="3418M1110X",
    descriptive_name='Vehicle and staff for patient emergency or non-emergency ground transport. Includes traditional',
    specialty='modified title, added source]',
    specialization='Military or U.S. Coast Guard Ambulance, Ground Transport',
    provider_grouping='Transportation Services',
)

TAXONOMY_MAPPING["3418M1120X"] = TaxonomyEntry(
    code="3418M1120X",
    descriptive_name='Vehicle and staff for patient emergency or non-emergency air transport.',
    specialty='Military/U.S. Coast Guard Transport',
    specialization='Military or U.S. Coast Guard Ambulance, Air Transport',
    provider_grouping='Transportation Services',
)

TAXONOMY_MAPPING["3418M1130X"] = TaxonomyEntry(
    code="3418M1130X",
    descriptive_name='Vehicle and staff for patient emergency or non-emergency sea/water transport',
    specialty='modified title, added source]',
    specialization='Military or U.S. Coast Guard Ambulance, Water Transport',
    provider_grouping='Transportation Services',
)

TAXONOMY_MAPPING["342000000X"] = TaxonomyEntry(
    code="342000000X",
    descriptive_name='A ride-sharing company that provides prearranged or contracted non-emergency medical transportation',
    specialty='Transportation Network Company',
    specialization='Military or U.S. Coast Guard Ambulance, Water Transport',
    provider_grouping='Transportation Services',
)

TAXONOMY_MAPPING["343800000X"] = TaxonomyEntry(
    code="343800000X",
    descriptive_name='A public or privately owned transportation service with vehicles, specially equipped to provide enhanced',
    specialty='Secured Medical Transport (VAN)',
    specialization='Military or U.S. Coast Guard Ambulance, Water Transport',
    provider_grouping='Transportation Services',
)

TAXONOMY_MAPPING["343900000X"] = TaxonomyEntry(
    code="343900000X",
    descriptive_name='A land vehicle with a capacity to meet special height, clearance, access, and seating, for the conveyance',
    specialty='Non-emergency Medical Transport (VAN)',
    specialization='Military or U.S. Coast Guard Ambulance, Water Transport',
    provider_grouping='Transportation Services',
)

TAXONOMY_MAPPING["344600000X"] = TaxonomyEntry(
    code="344600000X",
    descriptive_name='A land commercial vehicle used for the transporting of persons in non-emergency situations. The vehicle',
    specialty='Taxi',
    specialization='Military or U.S. Coast Guard Ambulance, Water Transport',
    provider_grouping='Transportation Services',
)

TAXONOMY_MAPPING["344800000X"] = TaxonomyEntry(
    code="344800000X",
    descriptive_name='An air company that the Federal Aviation Administration, the certificate-holding district office (CHDO),',
    specialty='Air Carrier',
    specialization='Specialty Pharmacy',
    provider_grouping='Transportation Services',
)

TAXONOMY_MAPPING["347B00000X"] = TaxonomyEntry(
    code="347B00000X",
    descriptive_name='A public or private organization or business licensed to provide bus services.',
    specialty='Bus',
    specialization='Water Transport',
    provider_grouping='Transportation Services',
)

TAXONOMY_MAPPING["347C00000X"] = TaxonomyEntry(
    code="347C00000X",
    descriptive_name='An individual paid to provide non-emergency transportation using their privately owned/leased vehicle.',
    specialty='Private Vehicle',
    specialization='Military or U.S. Coast Guard Ambulance, Water Transport',
    provider_grouping='Transportation Services',
)

TAXONOMY_MAPPING["347D00000X"] = TaxonomyEntry(
    code="347D00000X",
    descriptive_name='An organization or business licensed to provide passenger train service, including light rail, subway, and',
    specialty='Train',
    specialization='Military or U.S. Coast Guard Ambulance, Water Transport',
    provider_grouping='Transportation Services',
)

TAXONOMY_MAPPING["347E00000X"] = TaxonomyEntry(
    code="347E00000X",
    descriptive_name='An organization that provides transportation for individuals who need access to medical care or services',
    specialty='Transportation Broker',
    specialization='Military or U.S. Coast Guard Ambulance, Water Transport',
    provider_grouping='Transportation Services',
)

TAXONOMY_MAPPING["363A00000X"] = TaxonomyEntry(
    code="363A00000X",
    descriptive_name='A physician assistant is a person who has successfully completed an accredited education program for',
    specialty='Physician Assistant',
    specialization="Women's Health",
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["363AM0700X"] = TaxonomyEntry(
    code="363AM0700X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Medical',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["363AS0400X"] = TaxonomyEntry(
    code="363AS0400X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Surgical',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["363L00000X"] = TaxonomyEntry(
    code="363L00000X",
    descriptive_name='(1) A registered nurse provider with a graduate degree in nursing prepared for advanced practice',
    specialty='Nurse Practitioner',
    specialization="Women's Health",
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["363LA2100X"] = TaxonomyEntry(
    code="363LA2100X",
    descriptive_name='#Type!',
    specialty='1994, p. 549.',
    specialization='Acute Care',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["363LA2200X"] = TaxonomyEntry(
    code="363LA2200X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Adult Health',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["363LC0200X"] = TaxonomyEntry(
    code="363LC0200X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Critical Care Medicine',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["363LC1500X"] = TaxonomyEntry(
    code="363LC1500X",
    descriptive_name='#Type!',
    specialty='Nurse Practitioner',
    specialization='Community Health',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["363LF0000X"] = TaxonomyEntry(
    code="363LF0000X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Family',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["363LG0600X"] = TaxonomyEntry(
    code="363LG0600X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Gerontology',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["363LN0000X"] = TaxonomyEntry(
    code="363LN0000X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Neonatal',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["363LN0005X"] = TaxonomyEntry(
    code="363LN0005X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Neonatal, Critical Care',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["363LP0200X"] = TaxonomyEntry(
    code="363LP0200X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Pediatrics',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["363LP0222X"] = TaxonomyEntry(
    code="363LP0222X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Pediatrics, Critical Care',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["363LP0808X"] = TaxonomyEntry(
    code="363LP0808X",
    descriptive_name='#Type!',
    specialty='Nurse Practitioner',
    specialization='Psychiatric/Mental Health',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["363LP1700X"] = TaxonomyEntry(
    code="363LP1700X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Perinatal',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["363LP2300X"] = TaxonomyEntry(
    code="363LP2300X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Primary Care',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["363LS0200X"] = TaxonomyEntry(
    code="363LS0200X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='School',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["363LW0102X"] = TaxonomyEntry(
    code="363LW0102X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization="Women's Health",
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["363LX0001X"] = TaxonomyEntry(
    code="363LX0001X",
    descriptive_name='#Type!',
    specialty='Nurse Practitioner',
    specialization='Obstetrics & Gynecology',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["363LX0106X"] = TaxonomyEntry(
    code="363LX0106X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Occupational Health',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["364S00000X"] = TaxonomyEntry(
    code="364S00000X",
    descriptive_name='A registered nurse who, through a graduate degree program in nursing, or through a formal post-basic',
    specialty='Clinical Nurse Specialist',
    specialization='Solid Organ Transplant',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["364SA2100X"] = TaxonomyEntry(
    code="364SA2100X",
    descriptive_name='#Type!',
    specialty='Catalogue and The Interagency Conference on Nursing Statistics.',
    specialization='Acute Care',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["364SA2200X"] = TaxonomyEntry(
    code="364SA2200X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Adult Health',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["364SC0200X"] = TaxonomyEntry(
    code="364SC0200X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Critical Care Medicine',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["364SC1501X"] = TaxonomyEntry(
    code="364SC1501X",
    descriptive_name='#Type!',
    specialty='Clinical Nurse Specialist',
    specialization='Community Health/Public Health',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["364SC2300X"] = TaxonomyEntry(
    code="364SC2300X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Chronic Care',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["364SE0003X"] = TaxonomyEntry(
    code="364SE0003X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Emergency',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["364SE1400X"] = TaxonomyEntry(
    code="364SE1400X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Ethics',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["364SF0001X"] = TaxonomyEntry(
    code="364SF0001X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Family Health',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["364SG0600X"] = TaxonomyEntry(
    code="364SG0600X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Gerontology',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["364SH0200X"] = TaxonomyEntry(
    code="364SH0200X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Home Health',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["364SH1100X"] = TaxonomyEntry(
    code="364SH1100X",
    descriptive_name='#Type!',
    specialty='Clinical Nurse Specialist',
    specialization='Holistic',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["364SI0800X"] = TaxonomyEntry(
    code="364SI0800X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Informatics',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["364SL0600X"] = TaxonomyEntry(
    code="364SL0600X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Long-Term Care',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["364SM0705X"] = TaxonomyEntry(
    code="364SM0705X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Medical-Surgical',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["364SN0000X"] = TaxonomyEntry(
    code="364SN0000X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Neonatal',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["364SN0800X"] = TaxonomyEntry(
    code="364SN0800X",
    descriptive_name='#Type!',
    specialty='Clinical Nurse Specialist',
    specialization='Neuroscience',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["364SP0200X"] = TaxonomyEntry(
    code="364SP0200X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Pediatrics',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["364SP0807X"] = TaxonomyEntry(
    code="364SP0807X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Psychiatric/Mental Health, Child & Adolescent',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["364SP0808X"] = TaxonomyEntry(
    code="364SP0808X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Psychiatric/Mental Health',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["364SP0809X"] = TaxonomyEntry(
    code="364SP0809X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Psychiatric/Mental Health, Adult',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["364SP0810X"] = TaxonomyEntry(
    code="364SP0810X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Psychiatric/Mental Health, Child & Family',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["364SP0811X"] = TaxonomyEntry(
    code="364SP0811X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Psychiatric/Mental Health, Chronically Ill',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["364SP0812X"] = TaxonomyEntry(
    code="364SP0812X",
    descriptive_name='#Type!',
    specialty='Clinical Nurse Specialist',
    specialization='Psychiatric/Mental Health, Community',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["364SP0813X"] = TaxonomyEntry(
    code="364SP0813X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Psychiatric/Mental Health, Geropsychiatric',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["364SP1700X"] = TaxonomyEntry(
    code="364SP1700X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Perinatal',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["364SP2800X"] = TaxonomyEntry(
    code="364SP2800X",
    descriptive_name='#Type!',
    specialty='Clinical Nurse Specialist',
    specialization='Perioperative',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["364SR0400X"] = TaxonomyEntry(
    code="364SR0400X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Rehabilitation',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["364SS0200X"] = TaxonomyEntry(
    code="364SS0200X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='School',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["364ST0500X"] = TaxonomyEntry(
    code="364ST0500X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Transplantation',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["364SW0102X"] = TaxonomyEntry(
    code="364SW0102X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization="Women's Health",
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["364SX0106X"] = TaxonomyEntry(
    code="364SX0106X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Occupational Health',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["364SX0200X"] = TaxonomyEntry(
    code="364SX0200X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Oncology',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["364SX0204X"] = TaxonomyEntry(
    code="364SX0204X",
    descriptive_name='#Type!',
    specialty='#Type!',
    specialization='Oncology, Pediatrics',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["367500000X"] = TaxonomyEntry(
    code="367500000X",
    descriptive_name='(1) A licensed registered nurse with advanced specialty education in anesthesia who, in collaboration with',
    specialty='Nurse Anesthetist, Certified Registered',
    specialization="Women's Health",
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["367A00000X"] = TaxonomyEntry(
    code="367A00000X",
    descriptive_name='Advanced practice midwifery encompasses the independent provision of care during pregnancy,',
    specialty='Advanced Practice Midwife',
    specialization='Solid Organ Transplant',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["367H00000X"] = TaxonomyEntry(
    code="367H00000X",
    descriptive_name='An individual certified by the state to perform anesthesia services under the direct supervision of an',
    specialty='Anesthesiologist Assistant',
    specialization='Solid Organ Transplant',
    provider_grouping='Physician Assistants & Advanced Practice Nursing Providers',
)

TAXONOMY_MAPPING["372500000X"] = TaxonomyEntry(
    code="372500000X",
    descriptive_name='An individual who provides home maintenance services required to sustain a safe, sanitary living',
    specialty='Chore Provider',
    specialization='Wound Care',
    provider_grouping='Nursing Service Related Providers',
)

TAXONOMY_MAPPING["372600000X"] = TaxonomyEntry(
    code="372600000X",
    descriptive_name='An individual who provides supervision, socialization, and non-medical care to a functionally impaired',
    specialty='Adult Companion',
    specialization='Wound Care',
    provider_grouping='Nursing Service Related Providers',
)

TAXONOMY_MAPPING["373H00000X"] = TaxonomyEntry(
    code="373H00000X",
    descriptive_name='Individuals experienced or trained in working with developmentally disabled individuals who need',
    specialty='Day Training/Habilitation Specialist',
    specialization='Wound Care',
    provider_grouping='Nursing Service Related Providers',
)

TAXONOMY_MAPPING["374700000X"] = TaxonomyEntry(
    code="374700000X",
    descriptive_name='(1) A person with specialized training in a narrow field of expertise whose occupation requires training',
    specialty='Technician',
    specialization='Wound Care',
    provider_grouping='Nursing Service Related Providers',
)

TAXONOMY_MAPPING["3747A0650X"] = TaxonomyEntry(
    code="3747A0650X",
    descriptive_name='An individual who provides hands-on care, of both a supportive and health related nature, specific to the',
    specialty='Healthcare Organizations, Oakbrook Terrace, Illinois: 1994, p. 776.',
    specialization='Attendant Care Provider',
    provider_grouping='Nursing Service Related Providers',
)

TAXONOMY_MAPPING["3747P1801X"] = TaxonomyEntry(
    code="3747P1801X",
    descriptive_name='An individual who provides assistance with eating, bathing, dressing, personal hygiene, activities of daily',
    specialty='Technician',
    specialization='Personal Care Attendant',
    provider_grouping='Nursing Service Related Providers',
)

TAXONOMY_MAPPING["374J00000X"] = TaxonomyEntry(
    code="374J00000X",
    descriptive_name='Doulas work in a variety of settings and have been trained to provide physical, emotional, and',
    specialty='Doula',
    specialization='Wound Care',
    provider_grouping='Nursing Service Related Providers',
)

TAXONOMY_MAPPING["374K00000X"] = TaxonomyEntry(
    code="374K00000X",
    descriptive_name='A religious nonmedical practitioner offers spiritually-based care. Services may be rendered in an office,',
    specialty='Religious Nonmedical Practitioner',
    specialization='Wound Care',
    provider_grouping='Nursing Service Related Providers',
)

TAXONOMY_MAPPING["374T00000X"] = TaxonomyEntry(
    code="374T00000X",
    descriptive_name='Religious nonmedical nursing personnel are experienced in caring for the physical needs of nonmedical',
    specialty='Religious Nonmedical Nursing Personnel',
    specialization='Wound Care',
    provider_grouping='Nursing Service Related Providers',
)

TAXONOMY_MAPPING["374U00000X"] = TaxonomyEntry(
    code="374U00000X",
    descriptive_name='A person trained to assist public health nurses, home health nurses, and other health professionals in the',
    specialty='Home Health Aide',
    specialization='Wound Care',
    provider_grouping='Nursing Service Related Providers',
)

TAXONOMY_MAPPING["376G00000X"] = TaxonomyEntry(
    code="376G00000X",
    descriptive_name='An individual, often licensed by the state, who is responsible for the management of a nursing home.',
    specialty='Nursing Home Administrator',
    specialization='Wound Care',
    provider_grouping='Nursing Service Related Providers',
)

TAXONOMY_MAPPING["376J00000X"] = TaxonomyEntry(
    code="376J00000X",
    descriptive_name='An individual who provides general household activities such as meal preparation, laundry, and light',
    specialty='Homemaker',
    specialization='Wound Care',
    provider_grouping='Nursing Service Related Providers',
)

TAXONOMY_MAPPING["376K00000X"] = TaxonomyEntry(
    code="376K00000X",
    descriptive_name='(1) An unlicensed individual who is trained to function in an assistive role to the licensed nurse in the',
    specialty="Nurse's Aide",
    specialization='Wound Care',
    provider_grouping='Nursing Service Related Providers',
)

TAXONOMY_MAPPING["385H00000X"] = TaxonomyEntry(
    code="385H00000X",
    descriptive_name='#Type!',
    specialty='Respite Care',
    specialization='Substance Abuse Treatment, Children',
    provider_grouping='Residential Treatment Facilities',
)

TAXONOMY_MAPPING["385HR2050X"] = TaxonomyEntry(
    code="385HR2050X",
    descriptive_name='A camping facility that provides specialized respite care to individuals requiring enhanced services to',
    specialty='#Type!',
    specialization='Respite Care Camp',
    provider_grouping='Residential Treatment Facilities',
)

TAXONOMY_MAPPING["385HR2055X"] = TaxonomyEntry(
    code="385HR2055X",
    descriptive_name='A facility or distinct part of a facility that provides short term, residential care to children, diagnosed with',
    specialty='Respite Care',
    specialization='Respite Care, Mental Illness, Child',
    provider_grouping='Respite Care Facility',
)

TAXONOMY_MAPPING["385HR2060X"] = TaxonomyEntry(
    code="385HR2060X",
    descriptive_name='A facility or distinct part of a facility that provides short term, residential care to children diagnosed with',
    specialty="dealing with emergency situations which might be related to or exacerbate the individual's condition.",
    specialization='Respite Care, Intellectual and/or Developmental Disabilities, Child',
    provider_grouping='Residential Treatment Facilities',
)

TAXONOMY_MAPPING["385HR2065X"] = TaxonomyEntry(
    code="385HR2065X",
    descriptive_name='A facility or distinct part of a facility that providers short term, residential care to children, diagnosed with',
    specialty='mental illness, as respite for the regular caregivers.',
    specialization='Respite Care, Physical Disabilities, Child',
    provider_grouping='Respite Care Facility',
)

TAXONOMY_MAPPING["390200000X"] = TaxonomyEntry(
    code="390200000X",
    descriptive_name='An individual who is enrolled in an organized health care education/training program leading to a degree,',
    specialty='Student in an Organized Health Care Education/Training Program',
    specialization='Speech-Language Assistant',
    provider_grouping='Speech, Language and Hearing Service Providers',
)

TAXONOMY_MAPPING["405300000X"] = TaxonomyEntry(
    code="405300000X",
    descriptive_name='Prevention Professionals work in programs aimed to address specific patient needs, such as suicide',
    specialty='Prevention Professional',
    specialization='Independent Duty Medical Technicians',
    provider_grouping='Other Service Providers',
)

# Fallback mappings for codes that may be missing or have parsing errors
# These are known correct NPPES API-accepted descriptions
FALLBACK_TAXONOMY_CODES = {
    "207Q00000X": "Family Medicine",
    "207R00000X": "Internal Medicine",
    "207V00000X": "Obstetrics & Gynecology",
    "208D00000X": "General Practice",
    "208G00000X": "Thoracic Surgery",
    "208M00000X": "Hospitalist",
    "208000000X": "Pediatrics",
    "204F00000X": "Neurology",
    "207T00000X": "Emergency Medicine",  # PDF parsing error - mapped incorrectly
    "207W00000X": "Ophthalmology",
    "207X00000X": "Orthopedic",  # API accepts "Orthopedic" not "Orthopedic Surgery"
    "207Y00000X": "Otolaryngology",
    "208100000X": "Physical Medicine & Rehabilitation",
    "208200000X": "Anesthesiology",
    "208300000X": "Psychiatry & Neurology",
    "208400000X": "Psychiatry",  # Missing from PDF parsing
    "208500000X": "Child & Adolescent Psychiatry",  # Missing from PDF parsing
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


def get_taxonomy_name(code: str) -> str:
    """Get the NPPES API-accepted description for a taxonomy code.
    
    This function returns the specialty name formatted for use with the
    NPPES API's taxonomy_description parameter. It handles common
    formatting issues like removing "Surgery" suffixes.
    
    Uses fallback mappings for codes that may be missing or have parsing errors
    from the PDF extraction process.
    
    Args:
        code: Taxonomy code (e.g., "207Q00000X")
        
    Returns:
        NPPES API-accepted description (e.g., "Family Medicine", "Orthopedic")
        or the code itself if not found
    """
    # Check fallback first for known correct mappings
    if code in FALLBACK_TAXONOMY_CODES:
        return FALLBACK_TAXONOMY_CODES[code]
    
    entry = TAXONOMY_MAPPING.get(code)
    if not entry or not entry.specialty:
        # Fallback to code if not found
        return code
    
    specialty = entry.specialty.strip()
    
    # Handle malformed entries (parsing errors from PDF)
    if (specialty.startswith('#') or 
        specialty.startswith('Board of') or 
        specialty.startswith('American') or
        len(specialty) < 3):  # Too short to be valid
        # Use fallback if available, otherwise return code
        return FALLBACK_TAXONOMY_CODES.get(code, code)
    
    # Remove common suffixes that NPPES API doesn't accept
    # Based on testing, API accepts "Orthopedic" not "Orthopedic Surgery"
    if specialty.endswith(' Surgery'):
        specialty = specialty[:-9]  # Remove " Surgery"
    elif specialty.endswith(' Surgeon'):
        specialty = specialty[:-8]  # Remove " Surgeon"
    
    # Handle specific known mappings (check before suffix removal)
    if specialty == 'Orthopaedic Surgery':
        specialty = 'Orthopedic'
    elif specialty == 'Orthopaedic':
        specialty = 'Orthopedic'
    elif specialty == 'Family Practice':
        specialty = 'Family Medicine'
    elif specialty == 'Neurological Surgery' and code == '207T00000X':
        # Known parsing error - this should be Emergency Medicine
        specialty = 'Emergency Medicine'
    
    return specialty


def get_taxonomy_specialty(code: str) -> Optional[str]:
    """Get the specialty for a taxonomy code."""
    entry = TAXONOMY_MAPPING.get(code)
    return entry.specialty if entry else None


def get_taxonomy_specialization(code: str) -> Optional[str]:
    """Get the specialization for a taxonomy code."""
    entry = TAXONOMY_MAPPING.get(code)
    return entry.specialization if entry else None


def search_by_specialty(specialty: str) -> List[TaxonomyEntry]:
    """Search for all taxonomy codes matching a specialty (case-insensitive)."""
    s = specialty.lower()
    return [e for e in TAXONOMY_MAPPING.values() if e.specialty and e.specialty.lower() == s]


def search_by_name(term: str) -> List[TaxonomyEntry]:
    """Search for taxonomy codes by descriptive name (case-insensitive substring)."""
    t = term.lower()
    return [e for e in TAXONOMY_MAPPING.values() if t in e.descriptive_name.lower()]


def get_all_specialties() -> List[str]:
    """Return sorted list of unique specialties."""
    return sorted({e.specialty for e in TAXONOMY_MAPPING.values() if e.specialty})


def get_all_codes() -> List[str]:
    """Return sorted list of all taxonomy codes."""
    return sorted(TAXONOMY_MAPPING.keys())
