import pandas as pd
import random

# Define lists of components to construct clinical notes
patient_demographics = [
    "45-year-old male",
    "30-year-old female",
    "Senior patient",
    "Child",
    "50-year-old male",
    "25-year-old female",
    "60-year-old female",
    "35-year-old male",
    "40-year-old female",
    "55-year-old male"
]

conditions = [
    {"condition": "acute lower back pain", "icd10": "M54.5"},
    {"condition": "hypertension", "icd10": "I10"},
    {"condition": "type 2 diabetes mellitus", "icd10": "E11.9"},
    {"condition": "asthma", "icd10": "J45.40"},
    {"condition": "allergic rhinitis", "icd10": "J30.9"},
    {"condition": "osteoarthritis of the knee", "icd10": "M17.11"},
    {"condition": "chronic obstructive pulmonary disease", "icd10": "J44.9"},
    {"condition": "depression", "icd10": "F33.1"},
    {"condition": "otitis media", "icd10": "H66.90"},
    {"condition": "recurrent tonsillitis", "icd10": "J35.01"},
    {"condition": "meniscal tear", "icd10": "M23.221"},
    {"condition": "type 1 diabetes mellitus", "icd10": "E10.9"},
    {"condition": "allergic conjunctivitis", "icd10": "J30.2"},
    {"condition": "migraine headache", "icd10": "G43.909"},
    {"condition": "pneumonia", "icd10": "J18.9"}
]

procedures = [
    {"procedure": "prescribed physical therapy", "cpt": "97110"},
    {"procedure": "initiated insulin therapy", "cpt": "99214"},
    {"procedure": "performed ECG", "cpt": "93000"},
    {"procedure": "administered antibiotics", "cpt": "99213"},
    {"procedure": "prescribed inhalers", "cpt": "94640"},
    {"procedure": "administered bronchodilators", "cpt": "94660"},
    {"procedure": "performed laparoscopic appendectomy", "cpt": "44970"},
    {"procedure": "prescribed antihistamines", "cpt": "99213"},
    {"procedure": "scheduled pulmonary rehabilitation", "cpt": "99195"},
    {"procedure": "administered nasal corticosteroids", "cpt": "99214"},
    {"procedure": "initiated cognitive behavioral therapy", "cpt": "90834"},
    {"procedure": "prescribed antidepressants", "cpt": "90832"},
    {"procedure": "performed knee arthroscopy", "cpt": "29881"},
    {"procedure": "administered joint injections", "cpt": "20610"},
    {"procedure": "performed dental cleaning and examination", "cpt": "D0120;D1110"},
    {"procedure": "performed tonsillectomy", "cpt": "42820"},
    {"procedure": "administered inhaled corticosteroids", "cpt": "94640"},
    {"procedure": "scheduled follow-up appointment", "cpt": "99215"},
    {"procedure": "provided dietary and exercise recommendations", "cpt": "99396"},
    {"procedure": "administered pain management medications", "cpt": "97110"}
]

def generate_clinical_note():
    # Randomly select components
    demographics = random.choice(patient_demographics)
    condition = random.choice(conditions)
    procedure = random.choice(procedures)
    
    # Construct clinical note
    clinical_note = f"Patient is a {demographics} diagnosed with {condition['condition']}. {procedure['procedure'].capitalize()}."
    
    # Randomly decide if there are additional treatments or recommendations
    if random.random() < 0.3:  # 30% chance to add more
        additional_treatment = random.choice(procedures)
        clinical_note += f" {additional_treatment['procedure'].capitalize()}."
    
    return clinical_note, condition['icd10'], procedure['cpt']

# Generate 100 synthetic samples
num_samples = 100
data = {
    "clinical_note": [],
    "icd10_codes": [],
    "cpt_codes": []
}

for _ in range(num_samples):
    note, icd10, cpt = generate_clinical_note()
    # Handle multiple codes
    icd10_codes = icd10
    cpt_codes = cpt
    data["clinical_note"].append(note)
    data["icd10_codes"].append(icd10_codes)
    data["cpt_codes"].append(cpt_codes)

# Create DataFrame
df = pd.DataFrame(data)

# Optionally, introduce some entries with multiple ICD-10 and CPT codes
for i in range(0, num_samples, 15):  # Every 15th entry
    if i < num_samples:
        df.at[i, 'icd10_codes'] = df.at[i, 'icd10_codes'] + ";" + random.choice(conditions)['icd10']
        df.at[i, 'cpt_codes'] = df.at[i, 'cpt_codes'] + ";" + random.choice(procedures)['cpt']

# Save to CSV
df.to_csv("annotated_coding_data.csv", index=False)

print("CSV file 'annotated_coding_data.csv' with 100 annotated samples has been created.")
