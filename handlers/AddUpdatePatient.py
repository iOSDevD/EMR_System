"""
Nikunj Upadhyay
Class: CS 521 - Fall 1
Date: 10/16/2021
Homework Problem # Project
Description of Problem (1-2 sentence summary in your own words):

AddUpdatePatient helps to add a new patient to the system or update
the demographic details of the patient. Common functionality like
update address and contact details are re-used between new patient flow
and update patient flow.
"""

from model.Patient import Patient
from utilities.CSVUtility import FileHandlerUtility
from utilities.PatientValidator import PatientValidator


class AddUpdateFlowHandler:
    """Helps to add a new patient or updated details of existing patient.
    Initializing the class with a non-empty patient, starts the flow in
    update demographic mode. It defaults to an empty patient object during
    initialization.
    """

    # Delimiter constant to accept entries from console separated by $
    INPUT_DELIMITER = "$"

    # Prompt to be displayed to request basic details like, name , date of
    # birth and gender.
    NAME_GENDER_INPUT_MESSAGE = "Please enter FirstName, LastName,Date of " \
                                "Birth and Gender of the patient you want " \
                                "to add, separated by '{}'\nFor Gender " \
                                "please enter M for Male, F for Female " \
                                "and O for Other.".format(INPUT_DELIMITER)

    # Prompt to be displayed to request address details like address line 1,
    # state, zip and etc.
    ADDRESS_INPUT_MESSAGE = "Please enter Address Line 1, Line 2, City, " \
                            "State and Zip all separated " \
                            "by '{}'".format(INPUT_DELIMITER)

    # Prompt to be displayed to request contact details like phone and email.
    CONTACT_INPUT_MESSAGE = "Please enter Phone and email-id separated " \
                            "by '{}'".format(INPUT_DELIMITER)

    # Error message to be displayed when invalid gender value is entered out
    # of permissible values.
    ERROR_MESSAGE_GENDER = "Error! Please enter a valid gender value."

    # Error message to be displayed when a duplicate match is found, which
    # matches name, dob and gender.
    ERROR_DUPLICATE_PATIENT = "Error! Found Duplicate patient with same" \
                              " name {},{}.\nSystem does not allow to" \
                              " add Duplicate entries. Please try again!"

    # Error message to be displayed when the user enters zip code in in-valid
    # format.
    ERROR_ZIP_CODE = "Error! Please enter a valid value for zip code ex:" \
                     " 12345"

    # Error message to be displayed when user enters invalid character like a
    # comma in the input, which could affect the CSV format.
    ERROR_INVALID_DELIMITER_ENTRIES = "Error! Please enter valid " \
                                      "entries separated by '{}'". \
        format(INPUT_DELIMITER)

    # Count pertaining First name, last name , date of birth and Gender as the
    # basic demographic entries expected from input function.
    BASIC_DEMOGRAPHIC_ENTRIES = 4

    # Count pertaining address details like Address line 1, line 2, City, State
    # amd zip, expected from input function.
    ADDRESS_ENTRIES = 5

    # Count pertaining contact details like phone and e-mail
    # expected from input function.
    CONTACT_ENTRIES = 2

    def __init__(self, patient=Patient()):
        """ Initialize with non empty patient object in case we want to use
        the current class in update patient details mode, else it defaults
        to new patient creation."""
        self.__patient = patient  # private patient attribute
        self.validator = PatientValidator()  # public validator attribute

    def add_update_patient_flow(self):
        """Start the create patient or update patient details mode. For
        a input patient object which is created using a non empty patient id
        it starts the update patient details mode.
        For update patient mode, name,dob and gender validation is skipped as
        the patient is already identified and
        flow directly  jumps to address and contact details validation.
        Also in update patient mode, it returns a patient object and does not
        save the object. It is upto the receiver to identify the change and
        save it.

        For new patient, the patient details are saved to the file.
        """
        name_dob_validation = False  # Name and dob validation status
        address_validation = False  # Address validation status
        contact_validation = False  # Contact validation status

        while True:  # Keep prompting user to enter patient details.
            if name_dob_validation is False and self.__is_in_new_patient_mode():
                # First perform basic details validation like name which exists
                # only for new patient.
                name_dob_validation = self.__handle_basic_entries()
            elif address_validation is False:
                # Second perform validation for address details.
                address_validation = self.__handle_address_entries()
            elif contact_validation is False:
                # At last perform validation for contact details.
                contact_validation = self.__handle_contact_entries()

            if (name_dob_validation or
                self.__is_in_new_patient_mode() is False) and \
                    address_validation and contact_validation:
                # All Validation passed so save the data.
                file_handler = FileHandlerUtility()  # CSV, File handler object

                if self.__is_in_new_patient_mode() is False:
                    return self.__patient  # Update returns modified patient
                else:
                    # New Patient writes to the CSV.
                    # New patient id is the max id + 1. This way a unique
                    # patient id is created with simple logic.
                    new_patient_id = self.validator.generate_new_patient_id()
                    self.__patient.set_patient_id(new_patient_id)

                    # Convert Patient object to list before saving to csv.
                    patient_details_list = \
                        self.__patient.get_list_template_to_save()
                    file_handler.write_new_record(patient_details_list)
                break

    def __is_in_new_patient_mode(self):
        """If the class is initialized with patient object which has a
         patient id, the flow starts in update demographic mode.
         It returns true to help identify if its a new patient creation else
         returns false for update demographics."""
        if len(self.__patient.get_patient_id()) == 0:
            return True  # New patient mode
        else:
            return False  # Update patient demographics mode.

    def __get_list_from_input(self, input_str):
        """Splits the input string with the help of provided delimiter (ex: $)
        and converts it to a list. """
        return input_str.split(AddUpdateFlowHandler.INPUT_DELIMITER)

    def __handle_basic_entries(self):
        """Handle the flow of basic patient entries like name, dob, gender and
        also perform the required validation with it. This is usually done
        during new patient registration.

        Returns True once the user enters all the input values correctly.
        After which flow can move to next input which is address details."""

        # Get the user input for address entries from console.
        name_dob = input(AddUpdateFlowHandler.NAME_GENDER_INPUT_MESSAGE)

        # Perform input string validation for invalid characters
        text_has_valid_chars = self.validator.has_valid_character(name_dob)
        if text_has_valid_chars[0] is False:  # In-valid input characters.
            # Error! Print invalid character message.s
            print(text_has_valid_chars[1])
        else:  # Found input text valid, proceed ahead.
            name_dob_input_list = self.__get_list_from_input(name_dob)

            if len(name_dob_input_list) != \
                    AddUpdateFlowHandler.BASIC_DEMOGRAPHIC_ENTRIES:
                # User entered less or more entries separated by delimiter.
                # Show the error message.
                print(AddUpdateFlowHandler.ERROR_INVALID_DELIMITER_ENTRIES)
            else:
                first_name_str, last_name_str, dob_str, gender_abbreviation_str\
                    = name_dob_input_list

                gender_str = self.validator.validate_gender(
                    gender_abbreviation_str)  # Validate gender abbreviation.

                dob_validation = self.validator.has_validate_date_format(
                    dob_str)  # Validate dob is in correct format or not.
                if dob_validation[0] is False:  # DOB validation failed.
                    print(dob_validation[1])  # Show DOB invalid message.
                elif gender_str is not None:
                    # All validation passed, finally check for duplicate.
                    if self.validator.check_if_patient_exits(first_name_str,
                                                               last_name_str,
                                                               dob_str,
                                                               gender_str):
                        # Duplicate patient found, show error message.
                        print(AddUpdateFlowHandler.ERROR_DUPLICATE_PATIENT.
                              format(last_name_str.title(), first_name_str))
                    else:
                        # No duplicates and all validation passed update
                        # the patient attribute.
                        self.__patient.set_gender(gender_str)
                        self.__patient.set_first_name(first_name_str)
                        self.__patient.set_last_name(last_name_str)
                        self.__patient.set_dob(dob_str)
                        return True  # True helps to end basic info entry flow
                else:  # Gender Validation failed
                    print(AddUpdateFlowHandler.ERROR_MESSAGE_GENDER)

        return False

    def __handle_address_entries(self):
        """Handles the flow to ask user for address details during new
        patient registration or during update demographics.

        Returns True once the user enters all the input values correctly.
        After which flow can move to next input which is contact details."""

        # Get the user input for address entries from console.
        address = input(AddUpdateFlowHandler.ADDRESS_INPUT_MESSAGE)

        # Perform input string validation for invalid characters
        text_has_valid_chars = self.validator.has_valid_character(address)
        if text_has_valid_chars[0] is False:  # In-valid input characters.
            # Error! Print invalid character message.
            print(text_has_valid_chars[1])
        else:  # Found input text valid, proceed ahead.
            address_input_list = self.__get_list_from_input(address)

            if len(address_input_list) != AddUpdateFlowHandler.ADDRESS_ENTRIES:
                # User entered less or more entries separated by delimiter.
                # Show the error message.
                print(AddUpdateFlowHandler.ERROR_INVALID_DELIMITER_ENTRIES)
            else:  # List size matches the expected size
                address1, address2, city, state, address_zip = \
                    address_input_list  # assign using multiple assignment

                # Validate state input, must be 2 characters and match
                # the available list of states.
                state_validation = self.validator.has_valid_state(state)

                if self.validator.is_zip_code_valid(address_zip) is False:
                    # User entered invalid zip code, show message.
                    print(self.ERROR_ZIP_CODE)
                elif state_validation[0] is False:  # State validation failed.
                    print(state_validation[1])  # print error message
                else:
                    # All validation passed update the patient attribute.
                    self.__patient.set_address_line_1(address1)
                    self.__patient.set_address_line_2(address2)
                    self.__patient.set_address_city(city)
                    self.__patient.set_address_state(state)
                    self.__patient.set_address_zip(address_zip)
                    return True  # True helps to end address entry flow

        return False

    def __handle_contact_entries(self):
        """Handles the flow to ask user for contact details like phone and
        email during patient registration or during update demographics.

        Returns True once the user enters all the input values correctly.
        After which flow can be completed either by updating the demographics
        or creating a new patient.
        """

        # Get the user input for contact entries from console
        contact_details = input(
            AddUpdateFlowHandler.CONTACT_INPUT_MESSAGE)

        # Perform input string validation for invalid characters
        text_has_valid_chars = self.validator. \
            has_valid_character(contact_details)
        if text_has_valid_chars[0] is False:  # In-valid input characters.
            # Error! Print invalid character message.
            print(text_has_valid_chars[1])
        else:  # Found input text valid, proceed ahead.
            contact_input_list = self.__get_list_from_input(contact_details)
            if len(contact_input_list) != AddUpdateFlowHandler.CONTACT_ENTRIES:
                # User entered less or more entries separated by delimiter.
                # Show the error message.
                print(AddUpdateFlowHandler.ERROR_INVALID_DELIMITER_ENTRIES)
            else:
                # All validation passed update the patient attribute.
                phone, email = contact_input_list
                self.__patient.set_phone(phone)
                self.__patient.set_email(email)
                return True  # True helps to end contact entry flow
        return False
