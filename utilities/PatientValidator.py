"""
Nikunj Upadhyay
Class: CS 521 - Fall 1
Date: 10/16/2021
Homework Problem # Project
Description of Problem (1-2 sentence summary in your own words):

Patient Validator helps to validate the input values during search of patient.
The program validates state, gender, zip code, checks if input has invalid
characters like comma, date of birth is in valid format like mm/dd/YYYY.
It also generates a patient id for new patient registration, the value of it
will be unique as it simply increments the max value by 1.

"""
from datetime import datetime
import os
import re

from utilities.AppConstants import AppConstants
from utilities.CSVUtility import FileHandlerUtility


class PatientValidator:
    """Class which helps to search for a patient and other helper methods which
    validates gender abbreviation and returns appropriate value to be saved
    into the CSV file."""

    # Regex for 5 digit zip code.
    REGEX_FOR_ZIP_CODE = r"^[0-9]{5}$"

    # Regex for permissible characters.
    REGEX_FOR_INVALID_CHARACTERS = r"[{}]".format(",{}\\[\\]")

    # Valid date format for mm/dd/YYYY
    DATE_FORMAT = "%m/%d/%Y"

    # Set of Valid states abbreviation.
    VALID_STATES = {"AK", "AL", "AR", "AS", "AZ", "CA", "CO", "CT", "DC", "DE",
                    "FL", "GA", "GU", "HI", "IA", "ID", "IL", "IN", "KS", "KY",
                    "LA", "MA", "MD", "ME", "MI", "MN", "MO", "MP", "MS", "MT",
                    "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK",
                    "OR", "PA", "PR", "RI", "SC", "SD", "TN", "TX", "UM", "UT",
                    "VA", "VI", "VT", "WA", "WI", "WV", "WY"}

    def __get_records_matching(self, firstname, lastname, dob, gender):
        """Returns a list of patients matching first name, last name , date of
        birth and gender. If any of these input values are empty it returns
        default None. Search is case insensitive."""
        if len(firstname.strip()) != 0 and len(lastname.strip()) != 0 and len(
                dob.strip()) != 0:
            patient_data = FileHandlerUtility().read_all_records_row_data()
            patient_filter = filter(lambda patient:
                                    (patient.get_first_name().upper() ==
                                     firstname.upper()) and
                                    (patient.get_last_name().upper() ==
                                     lastname.upper()) and
                                    (patient.get_dob() == dob) and
                                    (patient.get_gender().upper() ==
                                     gender.upper()),
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

    def check_if_patient_exits(self, firstname, lastname, dob,
                               gender):
        """Identify if the patient with Name, date of birth or gender exists
        in the CSV file. Returns True if patient exists else False. Helps
        to avoid adding duplicate patients during patient registration"""
        patient_list = self.__get_records_matching(firstname, lastname, dob,
                                                   gender)
        if len(patient_list) > 0:
            return True
        else:
            return False

    def has_valid_state(self, state_str):
        """Validates the state and returns a upper case formatted state
        abbreviation. Value should be one in the VALID_STATES set.
        If validation is false it returns false and error message."""
        if len(state_str) == 2:
            state_str = state_str.upper()
            if state_str in PatientValidator.VALID_STATES:
                return True, state_str
        return False, "Error! Please enter a two character valid state value." \
                      " '{}' is invalid".format(state_str)

    def generate_new_patient_id(self):
        """Generates a new patient id from the CSV list. New patient id
        returned is one plus the max patient id. In case the CSV is empty
        it will return 1"""
        csv = FileHandlerUtility()
        patient_list = csv.read_all_records_row_data()
        if len(patient_list) > 0:
            patient_id_list = [int(patient.get_patient_id()) for patient in
                               patient_list]  # create int list of patient ids
            # new patient id is max patient id + 1
            new_patient_id = str(max(patient_id_list) + 1)
            return new_patient_id  # Return the result - new patient id
        else:
            return "1"  # There are no records in CSV so new patient id is 1

    def __strip_white_spaces(self, input_list):
        """Process a list of strings which could have white spaces at the
        leading  or trailing ends, it removes the white spaces at the ends
        and returns list of stripped string values"""

        # Map the values in the list to values which have whitespaces stripped
        # off.
        stripped_map = map(lambda input_str: input_str.strip(), input_list)

        return list(stripped_map)  # Get list from mapped object

    def get_list_from_input(self, input_str):
        """Splits the input string with the help of provided delimiter (ex: $)
        and converts it to a list. """

        # Convert string to list by splitting with delimiter `$`
        input_list = input_str.split(AppConstants.INPUT_DELIMITER)

        # Remove whitespace at leading or trailing end.
        whitespace_stripped_list = self.__strip_white_spaces(input_list)

        return whitespace_stripped_list  # Cleaned list of string values


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

    # 3. Test zip code
    assert validator.is_zip_code_valid("19105"), ("19105 should be a valid "
                                                  "zip code")

    assert validator.is_zip_code_valid("19105-") is False, (
        "19105- should be a in-valid zip code")

    # 4. Test input does not have invalid or prohibited character.
    assert validator.has_valid_character("{}-Hello")[0] is False, (
        "Result should be False as it has invalid characters"
    )

    assert validator.has_valid_character("Hello")[0] is True, (
        "Result should be True as it has valid characters"
    )

    # 5. Test if date format is valid
    assert validator.has_validate_date_format("1/1/80")[0] is False, (
        "Result should be False, as it is not in mm/dd/yyyy"
    )

    valid_dob_result = validator.has_validate_date_format("1/1/1980")
    assert valid_dob_result[0] is True and valid_dob_result[
        1] == "01/01/1980", (
        "Result should be True, and return date should be formatted in "
        "case we don't enter two digits for month and day."
    )

    # 6. Test if states entered are correct or not.
    assert validator.has_valid_state("MA")[0] is True, (
        "MA is a valid state abbreviation result, should return True")

    assert validator.has_valid_state("xy")[0] is False, (
        "XY is a in valid state abbreviation result, should return False")

    # 7. Test new patient should be generated and greater than 0
    assert int(validator.generate_new_patient_id()) > 0, (
        "New patient id should be generated when requested and "
        "should be greater than 0")

    # 8. Test values in list are trimmed at leading and trailing ends.
    input_str_with_spaces = "  John Smith  $Ted   $  Kyle$ Paul"
    expected_stripped_list = ["John Smith", "Ted", "Kyle", "Paul"]

    assert validator.get_list_from_input(
        input_str_with_spaces) == expected_stripped_list, (
        "List generated would have string values without "
        "leading/trailing space and should match with expected list.")

    print("Success! Completed Executing test case in PatientValidator")
