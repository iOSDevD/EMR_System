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


class AddUpdateFlowHandler:

    def __init__(self,patient = Patient()):
        self.__patient = patient

    def startAddNewPatientFlow(self):
        name_dob_validation = False
        addres_validation = False
        contact_validation = False
        while True:
            if name_dob_validation is False and self.__is_in_update_mode() is not True:
                name_dob = input(
                    "Please enter FirstName, LastName,Date of Birth and Gender of the patient you want to add, separated by '$'\nFor Gender please enter M for Male, F for Female and O for Other.")
                name_dob_input_list = name_dob.split("$")
                if len(name_dob_input_list) != 4:
                    print("Error! Please enter valid entries separated by '$'")
                else:
                    first_name_str, last_name_str, dob_str, gender_abbreviation_str = name_dob_input_list

                    self.__patient.set_first_name(first_name_str)
                    self.__patient.set_last_name(last_name_str)
                    self.__patient.set_dob(dob_str)

                    gender_str = self.__validate_gender(gender_abbreviation_str)
                    if gender_str is not None:
                        self.__patient.set_gender(gender_str)

                        if self.__validate_duplicate_patient(first_name_str,
                                                             last_name_str,
                                                             dob_str,
                                                             gender_str):
                            print(
                                "Error! Found Duplicate patient with same name {},{}.\nSystem does not allow to add Duplicate entries. Please try again!".format(
                                    last_name_str.title(), first_name_str))
                        else:
                            name_dob_validation = True
                    else:
                        print("Error! Please enter a valid gender value.")
            elif addres_validation is False:
                address = input(
                    "Please enter Address Line 1, Line 2, City, State and Zip all separated by '$'")
                address_input_list = address.split("$")
                if len(address_input_list) != 5:
                    print("Please enter valid address details separated by '$'")
                else:
                    address1, address2, city, state, zip = address_input_list
                    self.__patient.set_address_line_1(address1)
                    self.__patient.set_address_line_2(address2)
                    self.__patient.set_address_city(city)
                    self.__patient.set_address_state(state)
                    self.__patient.set_address_zip(zip)
                    addres_validation = True
            elif contact_validation is False:
                contact_details = input(
                    "Please enter Phone and email-id separated by '$'")
                contact_input_list = contact_details.split("$")
                if len(contact_input_list) != 2:
                    print("Please enter valid contact details separated by '$'")
                else:
                    phone,email = contact_input_list
                    self.__patient.set_phone(phone)
                    self.__patient.set_email(email)
                    contact_validation = True

            if (name_dob_validation or self.__is_in_update_mode()) and addres_validation and contact_validation:
                # Validation passed so save the data.
                csv = FileHandlerUtility()

                if self.__is_in_update_mode() is True:
                    patient_details_list = self.__patient.get_list_template_to_save()
                    csv.update_a_record(patient_details_list, self.__patient.get_patient_id())
                else:
                    new_patient_id = len(csv.read_all_records_row_data())
                    self.__patient.set_patient_id(str(new_patient_id))
                    patient_details_list = self.__patient.get_list_template_to_save()
                    csv.write_new_record(patient_details_list)
                break

    def __is_in_update_mode(self):
        if len(self.__patient.get_patient_id()) > 0:
            return True

    def __validate_gender(self, gender_abbreviation):
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

    def __validate_duplicate_patient(self, first_name, last_name, date_of_birth,
                                     gender_value):
        row_data = FileHandlerUtility().read_all_records_row_data()
        row_duplicate_filter = filter(
            lambda patient: patient.get_first_name() == first_name and
                            patient.get_last_name() == last_name and
                            patient.get_dob() == date_of_birth and
                            patient.get_gender() == gender_value, row_data)

        row_duplicate_list = list(row_duplicate_filter)
        if len(row_duplicate_list) == 1:
            return True
        else:
            return False
