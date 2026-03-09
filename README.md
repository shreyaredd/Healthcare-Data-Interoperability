Healthcare Data Integration
This project demonstrates how to take "Legacy" hospital data (old database formats) and map it into the modern HL7 FHIR R4 standard.

Why I built this:
Modern Electronic Health Records (EHRs), need data to be in a very specific format to talk to other systems. This script acts as the "bridge" to ensure patient data is interoperable and compliant.

Technical Features:
Data Mapping: Converted unstructured JSON objects into structured FHIR Patient Resources.

Library Integration: Used the fhir.resources Python library to validate data types.

Error Handling: Resolved a common serialization issue where standard Python JSON libraries fail to process birthDate objects by utilizing the library's native .json() method.

How to Run:
Install requirements: pip install fhir.resources

Run the script: python fhir_mapper.py

Proof of Work:
Below is the terminal output showing the successful transformation of a legacy record into a standardized FHIR resource:
