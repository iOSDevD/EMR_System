"""
Nikunj Upadhyay
Class: CS 521 - Fall 1
Date: 10/16/2021
Homework Problem # Project
Description of Problem (1-2 sentence summary in your own words):
"""

from utilities.AppConstants import AppConstants
from model.Patient import Patient
from utilities.CSVUtility import FileHandlerUtility
from utilities.PatientValidator import PatientValidator


class AddUpdateFlowHandler:
    INPUT_DELIMITER = "$"

    NAME_GENDER_INPUT_MESSAGE = "Please enter FirstName, LastName,Date of " \
                                "Birth and Gender of the patient you want " \
                                "to add, separated by '{}'\nFor Gender " \
                                "please enter M for Male, F for Female " \
                                "and O for Other.".format(INPUT_DELIMITER)

    ADDRESS_INPUT_MESSAGE = "Please enter Address Line 1, Line 2, City, " \
                            "State and Zip all separated " \
                            "by '{}'".format(INPUT_DELIMITER)

    CONTACT_INPUT_MESSAGE = "Please enter Phone and email-id separated " \
                            "by '{}'".format(INPUT_DELIMITER)

    ERROR_DUPLICATE_PATIENT = "Error! Found Duplicate patient with same" \
                              " name {},{}.\nSystem does not allow to" \
                              " add Duplicate entries. Please try again!"

    ERROR_ZIP_CODE = "Error! Please enter a valid value for zip code ex:" \
                     " 12345"

    ERROR_INVALID_DELIMITER_ENTRIES = "Error! Please enter valid " \
                                      "entries separated by '{}'". \
        format(INPUT_DELIMITER)

    def __init__(self, patient=Patient()):
        self.__patient = patient
        self.__validator = PatientValidator()

    def startAddNewPatientFlow(self):
        name_dob_validation = False
        address_validation = False
        contact_validation = False

        while True:
            if name_dob_validation is False and self.__is_in_new_patient_mode():
                name_dob_validation = self.__handle_basic_entries()
            elif address_validation is False:
                address_validation = self.__handle_address_entries()
            elif contact_validation is False:
                contact_validation = self.__handle_contact_entries()

            if (name_dob_validation or self.__is_in_new_patient_mode is False) \
                    and address_validation and contact_validation:
                # Validation passed so save the data.
                csv = FileHandlerUtility()

                if self.__is_in_new_patient_mode is False:
                    patient_details_list = self.__patient.get_list_template_to_save()
                    csv.update_a_record(patient_details_list,
                                        self.__patient.get_patient_id())
                else:
                    new_patient_id = len(csv.read_all_records_row_data())
                    self.__patient.set_patient_id(str(new_patient_id))
                    patient_details_list = self.__patient.get_list_template_to_save()
                    csv.write_new_record(patient_details_list)
                break

    def __is_in_new_patient_mode(self):
        if len(self.__patient.get_patient_id()) == 0:
            return True
        else:
            return False

    def __get_list_from_input(self, input_str):
        return input_str.split(AddUpdateFlowHandler.INPUT_DELIMITER)

    def __handle_basic_entries(self):
        name_dob = input(AddUpdateFlowHandler.NAME_GENDER_INPUT_MESSAGE)

        text_has_valid_chars = self.__validator.has_valid_character(name_dob)
        if text_has_valid_chars[0] is False:  # In-valid input characters.
            print(text_has_valid_chars[1])
        else:  # Found input text valid, proceed ahead.
            name_dob_input_list = self.__get_list_from_input(name_dob)

            if len(name_dob_input_list) != 4:
                print(AddUpdateFlowHandler.ERROR_INVALID_DELIMITER_ENTRIES)
            else:
                first_name_str, last_name_str, dob_str, \
                gender_abbreviation_str = name_dob_input_list

                gender_str = self.__validator.validate_gender(
                    gender_abbreviation_str)

                dob_validation = self.__validator.has_validate_date_format(
                    dob_str)
                if dob_validation[0] is False:
                    print(dob_validation[1])
                elif gender_str is not None:

                    if self.__validator.check_if_patient_exits(first_name_str,
                                                               last_name_str,
                                                               dob_str,
                                                               gender_str):
                        print(AddUpdateFlowHandler.ERROR_DUPLICATE_PATIENT.
                              format(last_name_str.title(), first_name_str))
                    else:
                        self.__patient.set_gender(gender_str)
                        self.__patient.set_first_name(first_name_str)
                        self.__patient.set_last_name(last_name_str)
                        self.__patient.set_dob(dob_str)
                        return True
                else:
                    print("Error! Please enter a valid gender value.")

        return False

    def __handle_address_entries(self):
        address = input(AddUpdateFlowHandler.ADDRESS_INPUT_MESSAGE)
        text_has_valid_chars = self.__validator.has_valid_character(address)
        if text_has_valid_chars[0] is False:  # In-valid input characters.
            print(text_has_valid_chars[1])
        else:  # Found input text valid, proceed ahead.
            address_input_list = self.__get_list_from_input(address)
            if len(address_input_list) != 5:
                print(AddUpdateFlowHandler.ERROR_INVALID_DELIMITER_ENTRIES)
            else:
                address1, address2, city, state, address_zip = \
                    address_input_list
                if self.__validator.is_zip_code_valid(address_zip) is False:
                    print(self.ERROR_ZIP_CODE)
                else:
                    self.__patient.set_address_line_1(address1)
                    self.__patient.set_address_line_2(address2)
                    self.__patient.set_address_city(city)
                    self.__patient.set_address_state(state)
                    self.__patient.set_address_zip(address_zip)
                    return True

        return False

    def __handle_contact_entries(self):
        contact_details = input(
            AddUpdateFlowHandler.CONTACT_INPUT_MESSAGE)

        text_has_valid_chars = self.__validator. \
            has_valid_character(contact_details)
        if text_has_valid_chars[0] is False:  # In-valid input characters.
            print(text_has_valid_chars[1])
        else:  # Found input text valid, proceed ahead.
            contact_input_list = self.__get_list_from_input(contact_details)
            if len(contact_input_list) != 2:
                print(AddUpdateFlowHandler.ERROR_INVALID_DELIMITER_ENTRIES)
            else:
                phone, email = contact_input_list
                self.__patient.set_phone(phone)
                self.__patient.set_email(email)
                return True
        return False
