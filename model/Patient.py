"""
Nikunj Upadhyay
Class: CS 521 - Fall 1
Date: 10/16/2021
Homework Problem # Project
Description of Problem (1-2 sentence summary in your own words):

Patient object which represents columns in the CSV. For example `Patient Id`
is re-presented by attribute `self.__patient_id`.
"""
import copy

from utilities.AppConstants import AppConstants


class Patient:
    """Patient object which can be created from a list. List of entries
    can be obtained from a CSV. For new patient it is created with
    default list"""

    def __init__(self, details_list=AppConstants().get_empty_data_template()):
        (self.__patient_id, self.__first_name, self.__last_name, self.__dob,
         self.__gender, self.__address_line_1, self.__address_line_2,
         self.__city, self.__state, self.__zip,
         self.__phone, self.__email, self.__questionnaire) = list(details_list)

    def get_patient_id(self):
        """Get the patient Id.
        CSV column: Patient Id"""
        return self.__patient_id

    def get_first_name(self):
        """Get the first name of the patient.
        CSV column: First Name"""
        return self.__first_name

    def get_last_name(self):
        """Get the last name of the patient.
        CSV column: Last Name"""
        return self.__last_name

    def get_dob(self):
        """Get the date of birth of the patient.
        CSV column: Date of Birth"""
        return self.__dob

    def get_gender(self):
        """Get the gender of the patient ex: Female, Male or Other.
        CSV column: Gender"""
        return self.__gender

    def get_address_line_1(self):
        """Get the address line 1 of the patient.
        CSV column: Address 1"""
        return self.__address_line_1

    def get_address_line_2(self):
        """Get the address line 2 of the patient.
        CSV column: Address 2"""
        return self.__address_line_2

    def get_address_city(self):
        """Get the address city of the patient.
        CSV column: City"""
        return self.__city

    def get_address_state(self):
        """Get the address state of the patient.
        CSV column: State"""
        return self.__state

    def get_address_zip(self):
        """Get the address zip of the patient.
        CSV column: Zip"""
        return self.__zip

    def get_phone(self):
        """Get the contact phone number of the patient.
        CSV column: Phone"""
        return self.__phone

    def get__questionnaire(self):
        """Get the questionnaire string which is saved in CSV column. For
        list representation use get_questionnaire_as_list()."""
        return self.__questionnaire

    def get_email(self):
        """Get the email-id of the patient.
        CSV column: email"""
        return self.__email

    def set_patient_id(self, patient_id):
        """Set the patient id of the patient. Usually for new patient this
        property is set before saving to the CSV.
        CSV column: Patient Id"""
        self.__patient_id = patient_id

    def set_first_name(self, first_name):
        """Set the first name of the patient. Usually for new patient this
        property is set before saving to the CSV.
        CSV column: First Name"""
        self.__first_name = first_name

    def set_last_name(self, last_name):
        """Set the last name of the patient. Usually for new patient this
        property is set before saving to the CSV.
        CSV column: Last Name"""
        self.__last_name = last_name

    def set_dob(self, dob):
        """Set the Date of birth of the patient. Usually for new patient this
        property is set before saving to the CSV.
        CSV column: Date of Birth"""
        self.__dob = dob

    def set_gender(self, gender):
        """Set the gender of the patient. Usually for new patient this
        property is set before saving to the CSV.
        CSV column: Gender"""
        self.__gender = gender

    def set_address_line_1(self, address_line_1):
        """Set the address line 1 of the patient. Usually for new patient this
        property is set before saving to the CSV.
        CSV column: Address 1"""
        self.__address_line_1 = address_line_1

    def set_address_line_2(self, address_line_2):
        """Set the address line 2 of the patient. Usually for new patient this
        property is set before saving to the CSV.
        CSV column: Address 2"""
        self.__address_line_2 = address_line_2

    def set_address_city(self, city):
        """Set the city of the patient. Usually for new patient this
        property is set before saving to the CSV.
        CSV column: City"""
        self.__city = city

    def set_address_state(self, state):
        """Set the state of the patient. Usually for new patient this
        property is set before saving to the CSV.
        CSV column: State"""
        self.__state = state

    def set_address_zip(self, address_zip):
        """Set the zip of the patient. Usually for new patient this
        property is set before saving to the CSV.
        CSV column: Zip"""
        self.__zip = address_zip

    def set_phone(self, phone):
        """Set the phone of the patient. Usually for new patient this
        property is set before saving to the CSV.
        CSV column: Phone"""
        self.__phone = phone

    def set_email(self, email):
        """Set the email of the patient. Usually for new patient this
        property is set before saving to the CSV.
        CSV column: email"""
        self.__email = email

    def set_questionnaire(self, questionnaire):
        """Set the questionnaire of the patient. Usually for new patient this
        property is set before saving to the CSV.
        CSV column: Questionnaire"""
        self.__questionnaire = questionnaire

    def get_questionnaire_as_list(self):
        """Converts the questionnaire from string representation of list
        like '[1,1,0,1]' to the actual list of integer values. In case of
        error expect None.
        CSV column: Questionnaire"""
        try:
            return eval(self.__questionnaire)
        except SyntaxError:
            return None

    def get_list_template_to_save(self):
        """Creates a template list to be saved into CSV from the current
        state of the patient object."""
        template_list = [self.__patient_id,
                         self.__first_name,
                         self.__last_name,
                         self.__dob,
                         self.__gender,
                         self.__address_line_1,
                         self.__address_line_2,
                         self.__city,
                         self.__state,
                         self.__zip,
                         self.__phone,
                         self.__email,
                         self.__questionnaire]
        return template_list

    def __repr__(self):
        pretty_print_data_list = list()
        pretty_print_data_list.append(
            "Patient ID: {}".format(self.get_patient_id()))

        pretty_print_data_list.append(
            "Date of Birth: {}".format(self.get_dob()))

        pretty_print_data_list.append("Name: {},{}".format(
            self.get_last_name(),
            self.get_first_name()))

        pretty_print_data_list.append("Address:\n{},{},\n{},{}-{}".format(
            self.get_address_line_1(),
            self.get_address_line_2(),
            self.get_address_city(),
            self.get_address_state(),
            self.get_address_zip()))

        pretty_print_data_list.append(
            "Contact Details:\nPhone {}\nEmail {}".format(
                self.get_phone(),
                self.get_email()))

        return "\n".join(pretty_print_data_list)

    def __eq__(self, other):
        return self.__patient_id == other.get_patient_id() and \
               self.__first_name == other.get_first_name() and \
               self.__last_name == other.get_last_name() and \
               self.__dob == other.get_dob() and \
               self.__gender == other.get_gender() and \
               self.__address_line_1 == other.get_address_line_1() and \
               self.__address_line_2 == other.get_address_line_2() and \
               self.__city == other.get_address_city() and \
               self.__state == other.get_address_state() and \
               self.__zip == other.get_address_zip() and \
               self.__phone == other.get_phone() and \
               self.__email == other.get_email() and \
               self.__questionnaire == other.get__questionnaire()


# Unit Tests
if __name__ == "__main__":
    print("Started Executing test case in Patient")

    # Patient content in list, use to create patient object.
    patient_content_as_list = ["99", "Harry", "Smith", "10/09/1999", "Male",
                               "1 Home Drive", "Apt 2", "Boston", "MA", "02115",
                               "100-1000-2200", "harry@bu.edu", "[1,0,0,1]"]

    # 1. Test patient object created fromt the list is correct or not.
    patient = Patient(patient_content_as_list)
    assert patient.get_patient_id() == "99" and \
           patient.get_first_name() == "Harry" and \
           patient.get_last_name() == "Smith" and \
           patient.get_dob() == "10/09/1999" and \
           patient.get_gender() == "Male" and \
           patient.get_address_line_1() == "1 Home Drive" and \
           patient.get_address_line_2() == "Apt 2" and \
           patient.get_address_city() == "Boston" and \
           patient.get_phone() == "100-1000-2200" and \
           patient.get_email() == "harry@bu.edu" and \
           patient.get_questionnaire_as_list() == [1, 0, 0, 1], (
        "Patient object created from the content as list should "
        "match with the content in the list.")

    # 2. Test copy of patient should match, with "==" i.e check
    # magic method __eq__() is working fine.
    new_patient = copy.copy(patient)
    assert new_patient == patient, (
        "Copy of new patient created should match as there is no change")

    # 3. Test after update the patient object should not match.
    new_patient.set_address_line_1("Test Address change")
    assert new_patient != patient, (
        "After update patient object should not, values are different.")

    print("Success! Completed Executing test case in Patient")
