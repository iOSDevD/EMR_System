"""
Nikunj Upadhyay
Class: CS 521 - Fall 1
Date: 10/16/2021
Homework Problem # Project
Description of Problem (1-2 sentence summary in your own words):
"""
import os

from utilities.AppConstants import AppConstants
from utilities.CSVUtility import FileHandlerUtility


class PatientValidator:

    def search_for_patient(self, firstname, lastname, dob, gender):
        """ Searches for the patient with required details in the CSV.
        All fields are required, if any of the input is empty string, search
        would not be performed.

        :param firstname: First name of the patient
        :param lastname: Last name of the patient
        :param dob: DOB of the patient
        :param gender: Gender of the patient.
        :return: Patient object in case match is found.
        """
        if len(firstname.strip()) != 0 and len(lastname.strip()) != 0 and len(
                dob.strip()) != 0:
            patient_data = FileHandlerUtility().read_all_records_row_data()
            patient_filter = filter(lambda patient:
                                    patient.get_first_name() == firstname and
                                    patient.get_last_name() == lastname and
                                    patient.get_dob() == dob and
                                    patient.get_gender() == gender,
                                    patient_data)
            patient_list = list(patient_filter)
            if len(patient_list) == 1:
                return patient_list[0]

    def validate_gender(self, gender_abbreviation):
        """ Validate gender abbreviation is correct or not
        'm' should return Male
        'f' should return Female
        'O' should return Other
        """
        gender_filter = filter(lambda e: e[0] == str.upper(gender_abbreviation),
                               AppConstants.GENDER_DICTIONARY.items())
        gender_dict = dict(gender_filter)
        if len(gender_dict) == 1:
            return gender_dict[str.upper(gender_abbreviation)]


if __name__ == "__main__":
    print("Started Executing test case in PatientValidator")

    # Move to one step up from utilities dir to get
    # InputFiles/PatientRecords.csv
    parent = os.path.dirname(os.getcwd())
    os.chdir(parent)

    validator = PatientValidator()

    # 1. Test case to search patient
    assert validator.search_for_patient("", "", "", "") is None, \
        "There should be no patient search for empty string values"

    searched_patient = validator.search_for_patient("Edward", "Jones",
                                                    "1/1/80", "Male")
    assert searched_patient is not None and \
           len(searched_patient.get_patient_id()) > 0, \
           "Object should not be none and patient id should exists."

    # 2. Test case to get gender value from its abbreviation.
    assert validator.validate_gender("f") == "Female", \
        "For input 'f' it should return gender as 'Female'"

    assert validator.validate_gender("M") == "Male", \
        "For input 'm' it should return gender as 'Female'"

    assert validator.validate_gender("o") == "Other", \
        "For input 'o' it should return gender as 'Other'"

    assert validator.validate_gender("xas") is None, \
        "For invalid input it should return None"

print("Success! Completed Executing test case in PatientValidator")
