"""
Nikunj Upadhyay
Class: CS 521 - Fall 1
Date: 10/16/2021
Homework Problem # Project
Description of Problem (1-2 sentence summary in your own words):
"""
import copy

from handlers.AddUpdatePatient import AddUpdateFlowHandler
from utilities.AppConstants import AppConstants
from utilities.CSVUtility import FileHandlerUtility
from utilities.PatientValidator import PatientValidator
from utilities.Questionnaire import Questionnaire


class LookUpFlowHandler:
    """ After the patient is found, tt helps to manage different functionality
    of the system, like update the address or contact, update questionnaire
    and delete the patient.
    """

    __UPDATE_DEMOGRAPHIC_MESSAGE = "Please enter FirstName, LastName,Date of " \
                                   "Birth and Gender of the patient you want " \
                                   "to search, separated by '$'\nFor Gender " \
                                   "please enter M for Male, F for Female " \
                                   "and O for Other."

    __ERROR_MESSAGE_INVALID_PRIMARY_ENTRIES = "Error! Please enter valid " \
                                              "entries separated by '$'"

    __ERROR_MESSAGE_INVALID_GENDER_ENTRY = "Error! Please enter a " \
                                           "valid gender value. Try again!"

    __ERROR_MESSAGE_CANNOT_FIND_PATIENT = "Unable to find patient {},{} {},{}"

    __SUCCESS_MESSAGE_FOUND_PATIENT = "Success! Found Patient and here " \
                                      "are the details=====\n{}\n"

    __SUCCESS_PATIENT_DELETE = "Patient {},{} has been " \
                               "deleted successfully from the system"

    __ERROR_FAILED_TO_DELETE_PATIENT = "Failed to delete the patient {},{}."

    def lookup_patient_flow(self):
        """ Initiate the patient look up for operations like update or delete
        patient details.
        """
        print("-"*20)
        print("Main -> Patient Look Up\n")
        searched_patient = None
        while True:
            name_dob = input(self.__UPDATE_DEMOGRAPHIC_MESSAGE)
            name_dob_input_list = name_dob.split("$")
            if len(name_dob_input_list) != 4:
                print(self.__ERROR_MESSAGE_INVALID_PRIMARY_ENTRIES)
            else:
                firstname, lastname, dob, gender = name_dob_input_list
                patient_validator = PatientValidator()
                gender = patient_validator.validate_gender(gender)
                if gender is None:
                    print(self.__ERROR_MESSAGE_INVALID_GENDER_ENTRY)
                else:
                    patient = patient_validator.search_for_patient(firstname,
                                                                   lastname,
                                                                   dob, gender)
                    if patient is None:
                        print(self.__ERROR_MESSAGE_CANNOT_FIND_PATIENT.format(
                            firstname, lastname, dob, gender))
                    else:
                        searched_patient = patient
                        print(self.__SUCCESS_MESSAGE_FOUND_PATIENT.
                              format(patient))
                        break

        while True:
            lookup_options_str = input(
                AppConstants().getPatientLookUpScreenOptionsMessge())

            if lookup_options_str in AppConstants.LOOKUP_OPTIONS.keys():
                if lookup_options_str == \
                        AppConstants.OPTION_KEY_UPDATE_QUESTIONNAIRE:
                    self.__start_questionnaire_flow(searched_patient)
                elif lookup_options_str == \
                        AppConstants.OPTION_KEY_UPDATE_PATIENT:
                    self.__update_patient_details(searched_patient)
                elif lookup_options_str == \
                        AppConstants.OPTION_KEY_DELETE_PATIENT:
                    self.__delete_patient(searched_patient)
            else:
                print("*********Closing Patient Look up*************")
                break

    def __start_questionnaire_flow(self, patient):
        """ Start questionnaire flow for the provided patient object.
        :param patient: Patient object for which we need to update
                        questionnaire.
        """
        answers = []
        questionnaire_list = Questionnaire.questionnaire_list
        current_index = 0
        while current_index < len(questionnaire_list):
            prompt_message = Questionnaire().get_question_str_for_prompt(
                questionnaire_list[current_index])
            answer_input = input(prompt_message)
            if answer_input.upper() in Questionnaire.YES_ANSWER_SET:
                answers.append(1)
            elif answer_input.upper() in Questionnaire.NO_ANSWER_SET:
                answers.append(0)
            else:
                answers.append(-1)
            current_index += 1

        self.__update_questionnaire(patient, answers)

    def __update_questionnaire(self, patient, answers):
        """ Update the questionnaire for provided patient with the list of
        answers. If the patient does not have any questionnaire answered it
        will add them if the patient already has it in that case it will
        replace with new answers.

        :param patient: Patient id for which questionnaire will be updated.
        :param answers: List of answers containing values like 1 for Yes,
                        0 for No and -1 for None.
        """
        formatted_answers_str = Questionnaire(). \
            get_formatted_answers_to_save(answers)
        patient.set_questionnaire(formatted_answers_str)
        FileHandlerUtility().update_a_record(
            patient.get_list_template_to_save(),
            patient.get_patient_id())

    def __delete_patient(self, patient):
        """ Delete the patient demographics details and questionnaire for the
        provided patient id.
        :param patient: Patient id for which records needs to be deleted.
        """
        if FileHandlerUtility().delete_a_record(
                patient.get_patient_id()) is True:
            print(self.__SUCCESS_PATIENT_DELETE.format(
                patient.get_first_name(), patient.get_last_name()))
        else:
            print(self.__ERROR_FAILED_TO_DELETE_PATIENT.format(
                patient.get_first_name(), patient.get_last_name()))

    def __update_patient_details(self, patient):
        """ Starts the update demographic flow for the provided patient id.
        It calls AddUpdateFlowHandler which has common functionality to
        add/update demographic details.

        :param patient: Patient id for which record needs to be deleted.
        """
        copy_of_patient = copy.copy(patient)
        AddUpdateFlowHandler(copy_of_patient).startAddNewPatientFlow()
