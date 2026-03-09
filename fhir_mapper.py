import json
from fhir.resources.patient import Patient
from fhir.resources.humanname import HumanName

# 1. This is the "legacy" stuff from the old database
# Using a simple dictionary to represent a row from the old system
raw_patient_data = {
    "id": "101",
    "fname": "Johnathan",
    "lname": "Smith",
    "sex": "male",
    "dob": "1985-05-12"
}

print("Running mapper...")

# 2. Start the FHIR Patient resource
# I'm using the R4 standard here since that's what Epic uses mostly
patient = Patient()

# Mapping basic fields
patient.id = raw_patient_data["id"]
patient.gender = raw_patient_data["sex"]
patient.birthDate = raw_patient_data["dob"]
patient.active = True

# 3. Fixing the Name
# FHIR is picky—names have to be in a list, even if it's just one person
name_obj = HumanName()
name_obj.family = raw_patient_data["lname"]
name_obj.given = [raw_patient_data["fname"]]

# Attach it back to the patient
patient.name = [name_obj]

# 4. Final output
# Used the built-in .json() because regular json.dumps hates the date format
print("Done. Here is the FHIR JSON:")
print(patient.json(indent=2))
