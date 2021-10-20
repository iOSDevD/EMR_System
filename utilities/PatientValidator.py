"""
Nikunj Upadhyay
Class: CS 521 - Fall 1
Date: 10/16/2021
Homework Problem # Project
Description of Problem (1-2 sentence summary in your own words):

Patient Validator helps to validate the input values during search of patient.

"""
from datetime import datetime
import os
import re
import string

from utilities.AppConstants import AppConstants
from utilities.CSVUtility import FileHandlerUtility


class PatientValidator:
    """Class which helps to search for a patient and other helper methods which
    validates gender abbreviation and returns appropriate value to be saved
    into the CSV file."""

    REGEX_FOR_ZIP_CODE = r"^[0-9]{5}$"

    REGEX_FOR_INVALID_CHARACTERS = r"[{}]".format(",{}\\[\\]")

    DATE_FORMAT = "%m/%d/%Y"

    def __get_records_matching(self, firstname, lastname, dob, gender):
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
            return patient_list

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
        patient_list = self.__get_records_matching(firstname, lastname, dob,
                                                   gender)
        if patient_list is not None:
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

    def is_zip_code_valid(self, input_zip_code):
        """Validates if the input zip code is of 5 digit or not.
        Returns True if its valid else False."""
        zip_code_match_count = re.findall(PatientValidator.REGEX_FOR_ZIP_CODE,
                                          input_zip_code)

        if len(zip_code_match_count) == 1:
            return True
        else:
            return False

    def has_valid_character(self, input_str):
        """Identifies if the input entered from the console has invalid
        characters which are not allowed. Characters not allowed is
        represented as REGEX_FOR_INVALID_CHARACTERS"""
        invalid_chars = re.findall(PatientValidator.
                                   REGEX_FOR_INVALID_CHARACTERS, input_str)
        if len(invalid_chars) > 0:
            return (False,
                    "Error! Found invalid character '{}' as input."
                    "Please try again without invalid characters.".format(
                        ",".join(invalid_chars)))
        else:
            return True, None

    def has_validate_date_format(self, date_str):
        """Validates if the input date string is in valid mm/dd/YYYY format.
        If the user enters single digit for month and days a re-formatted
        date string is returned. For example: enter 1/1/1980 it will return
        01/01/1980.
        Returns multiple results as tuple of (boolean,reformatted date str).
        If the validation fails, value false is returned along with the error
        message."""
        result_date_str = date_str
        try:
            date_object = datetime.strptime(date_str,
                                            PatientValidator.DATE_FORMAT)
            result_date_str = date_object.strftime(PatientValidator.DATE_FORMAT)
        except ValueError:
            return False, "Error! Please enter a valid date in " \
                          "mm/dd/yyyy format."

        return True, result_date_str


# Unit Tests
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
                                                    "01/01/1980", "Male")
    assert searched_patient is not None and \
           len(searched_patient.get_patient_id()) > 0, (
            "Object should not be none and patient id should exists.")

    # 2. Test case to get gender value from its abbreviation.
    assert validator.validate_gender("f") == "Female", \
        "For input 'f' it should return gender as 'Female'"

    assert validator.validate_gender("M") == "Male", \
        "For input 'm' it should return gender as 'Female'"

    assert validator.validate_gender("o") == "Other", \
        "For input 'o' it should return gender as 'Other'"

    assert validator.validate_gender("xas") is None, \
        "For invalid input it should return None"

    assert validator.is_zip_code_valid("19105"), ("19105 should be a valid "
                                                  "zip code")

    assert validator.is_zip_code_valid("19105-") is False, (
        "19105- should be a in-valid zip code")

    assert validator.has_valid_character("{}-Hello")[0] is False, (
        "Result should be False as it has invalid characters"
    )

    assert validator.has_valid_character("Hello")[0] is True, (
        "Result should be True as it has valid characters"
    )

    assert validator.has_validate_date_format("1/1/80")[0] is False, (
        "Result should be False, as it is not in mm/dd/yyyy"
    )

    valid_dob_result = validator.has_validate_date_format("1/1/1980")
    assert valid_dob_result[0] is True and valid_dob_result[
        1] == "01/01/1980", (
        "Result should be True, and return date should be formatted in "
        "case we don't enter two digits for month and day."
    )

    print("Success! Completed Executing test case in PatientValidator")
