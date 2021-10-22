"""
Nikunj Upadhyay
Class: CS 521 - Fall 1
Date: 10/16/2021
Homework Problem # Project
Description of Problem (1-2 sentence summary in your own words):

This program handles the patient look up flow.
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

    # Prompt message to be displayed to the user during look up
    __UPDATE_DEMOGRAPHIC_MESSAGE = "Please enter FirstName, LastName,Date of " \
                                   "Birth and Gender of the patient you want " \
                                   "to search, separated by '$'\nFor Gender " \
                                   "please enter M for Male, F for Female " \
                                   "and O for Other."

    # Error Message invalid entries with provided delimiter.
    __ERROR_MESSAGE_INVALID_PRIMARY_ENTRIES = "Error! Please enter valid " \
                                              "entries separated by '$'"

    # Gender validation Failed, invalid Gender entry.
    __ERROR_MESSAGE_INVALID_GENDER_ENTRY = "Error! Please enter a " \
                                           "valid gender value. Try again!"

    # Error message when patient does not exists in he CSV file.
    __ERROR_MESSAGE_CANNOT_FIND_PATIENT = "Unable to find patient {},{} {},{}"

    # Message to be displayed when we find patient for the provided patient id.
    __SUCCESS_MESSAGE_FOUND_PATIENT = "Success! Found Patient and here " \
                                      "are the details=====\n{}\n"

    # Message to be displayed when the patient was deleted successfully.
    __SUCCESS_PATIENT_DELETE = "Patient {},{} has been " \
                               "deleted successfully from the system"

    # Error message displayed when there was error occurred while deleting the
    # patient
    __ERROR_FAILED_TO_DELETE_PATIENT = "Failed to delete the patient {},{}."

    # Error message displayed when there was error occurred while updating the
    # patient demographic details
    __ERROR_FAILED_TO_UPDATE_DEMOGRAPHICS = "Error! Failed to update patient" \
                                            " demographics! Please try again."

    # Message to be displayed when user updates the demographics but details
    # are same as before the update.
    __PATIENT_DATA_UP_TO_DATE = "Patient details entered are same, hence " \
                                "nothing to update. We already have the " \
                                "updated entries for the patient {},{}."

    # Message to be displayed when update of the patient details was success.
    __SUCCESS_PATIENT_UPDATE = "Patient Data updated successfully for {},{}"

    # Count pertaining First name, last name , date of birth and Gender as the
    # basic demographic entries expected from input function during search.
    BASIC_DEMOGRAPHIC_ENTRIES = 4

    def lookup_patient_flow(self):
        """ Initiate the patient look up for operations like update or delete
        patient details.
        """
        print("-" * 20)
        print("Main -> Patient Look Up\n")
        searched_patient = None
        while True:  # Keep prompting user for patient look up entries.
            # Display input message
            name_dob = input(self.__UPDATE_DEMOGRAPHIC_MESSAGE)

            # Convert input string to list of string entries split by
            # default whitespace.
            name_dob_input_list = name_dob.split(AppConstants.INPUT_DELIMITER)
            if len(name_dob_input_list) != \
                    LookUpFlowHandler.BASIC_DEMOGRAPHIC_ENTRIES:
                print(self.__ERROR_MESSAGE_INVALID_PRIMARY_ENTRIES)
            else:
                # Multiple assignment from list to variables.
                firstname, lastname, dob, gender = name_dob_input_list
                # Find patient matching name, dob and gender using validator.
                patient_validator = PatientValidator()

                # Validate gender abbreviation string and in return get
                # formatted values, ex: "F" converts to Female.
                gender = patient_validator.validate_gender(gender)

                if gender is None:  # Gender input string error
                    print(self.__ERROR_MESSAGE_INVALID_GENDER_ENTRY)
                else:
                    # Input good search for patient. If invalid characters are
                    # entered it would not find the result.
                    patient = patient_validator.search_for_patient(firstname,
                                                                   lastname,
                                                                   dob, gender)
                    if patient is None:  # Patient not found.
                        print(self.__ERROR_MESSAGE_CANNOT_FIND_PATIENT.format(
                            firstname, lastname, dob, gender))
                    else:  # Found patient.
                        # Store searched patient to be used further,
                        # ex: Update patient questionnaire.
                        searched_patient = patient
                        print(self.__SUCCESS_MESSAGE_FOUND_PATIENT.
                              format(patient))
                        break

        while True:  # Prompt actions to take after patient is found.

            # Prompt input for options like update patient details,
            # questionnaire and delete a patient.
            lookup_options_str = input(
                AppConstants().get_patient_look_up_prompt())

            if lookup_options_str in AppConstants.LOOKUP_OPTIONS.keys():
                if lookup_options_str == \
                        AppConstants.PATIENT_LOOK_UP_UPDATE_QUESTIONNAIRE_KEY:
                    # Update questionnaire flow.
                    self.__start_questionnaire_flow(searched_patient)
                elif lookup_options_str == \
                        AppConstants.PATIENT_LOOK_UP_UPDATE_PATIENT_KEY:
                    # Update patient demographic detail flow.
                    self.__update_patient_details(searched_patient)
                elif lookup_options_str == \
                        AppConstants.PATIENT_LOOK_UP_DELETE_PATIENT_KEY:
                    # Delete a patient flow.
                    self.__delete_patient(searched_patient)
            else:  # Any other input text, simply exit the LookUpPatient flow.
                print("*********Closing Patient Look up*************")
                break

    def __start_questionnaire_flow(self, patient):
        """ Start questionnaire flow for the provided patient object.
        :param patient: Patient object for which we need to update
                        questionnaire.
        """
        answers = []  # Default empty list of answers

        # current list of questions
        questionnaire_list = Questionnaire().questionnaire_list

        current_index = 0  # Start from question at index 0

        while current_index < len(questionnaire_list):  # Continue till last one
            # Display the current question on the console
            prompt_message = Questionnaire().get_question_str_for_prompt(
                questionnaire_list[current_index])

            # Get the Answer for question, yes or no or skipped.
            answer_input = input(prompt_message)

            if answer_input.upper() in Questionnaire.YES_ANSWER_SET:
                answers.append(1)  # Store 1 for Yes
            elif answer_input.upper() in Questionnaire.NO_ANSWER_SET:
                answers.append(0)  # Store 0 for No
            else:
                answers.append(-1)  # Store -1 for skipped by hitting enter.
            current_index += 1  # Move to next question.

        self.__update_questionnaire(patient, answers)  # Save questions to CSV

    def __update_questionnaire(self, patient, answers):
        """ Update the questionnaire for provided patient with the list of
        answers. If the patient does not have any questionnaire answered it
        will add them if the patient already has it in that case it will
        replace with new answers.

        :param patient: Patient id for which questionnaire will be updated.
        :param answers: List of answers containing values like 1 for Yes,
                        0 for No and -1 for None.
        """
        # Format the answers from list to string like "[1,0,0,-1]"
        formatted_answers_str = Questionnaire(). \
            get_formatted_answers_to_save(answers)
        # Update patient object with answers string
        patient.set_questionnaire(formatted_answers_str)

        # Update the patient record for questionnaire.
        FileHandlerUtility().update_a_record(
            patient.get_list_template_to_save(),
            patient.get_patient_id())

    def __delete_patient(self, patient):
        """ Delete the patient demographics details and questionnaire for the
        provided patient id.
        :param patient: Patient id for which records needs to be deleted.
        """
        if FileHandlerUtility().delete_a_record(
                patient.get_patient_id()) is True:  # Delete Success!
            print(self.__SUCCESS_PATIENT_DELETE.format(
                patient.get_first_name(), patient.get_last_name()))
        else:  # Delete Failed!
            print(self.__ERROR_FAILED_TO_DELETE_PATIENT.format(
                patient.get_first_name(), patient.get_last_name()))

    def __update_patient_details(self, patient):
        """ Starts the update demographic flow for the provided patient id.
        It calls AddUpdateFlowHandler which has common functionality to
        add/update demographic details.

        :param patient: Patient id for which record needs to be deleted.
        """
        # Create a copy of searched patient
        copy_of_patient = copy.copy(patient)
        # Initiate the update demographic class, calling a common class
        # which handles add or update.

        updated_patient = AddUpdateFlowHandler(copy_of_patient). \
            add_update_patient_flow()
        if updated_patient is not None:  # Returned patient object is not None
            # Check if there is any difference between the object being saved
            # and the current patient object
            if updated_patient != patient:  # Found difference, so save
                csv = FileHandlerUtility()
                patient_details_list = updated_patient. \
                    get_list_template_to_save()
                csv.update_a_record(patient_details_list,
                                    updated_patient.get_patient_id())
                print(LookUpFlowHandler.__SUCCESS_PATIENT_UPDATE.format(
                    patient.get_first_name(), patient.get_last_name()))
            else:  # No difference, nothing to save.
                print(LookUpFlowHandler.__PATIENT_DATA_UP_TO_DATE.format(
                    patient.get_first_name(), patient.get_last_name()))
        else:
            print(LookUpFlowHandler.__ERROR_FAILED_TO_UPDATE_DEMOGRAPHICS)


# Unit Tests
if __name__ == "__main__":
    # There are no test case for the current file as methods don't return a
    # specific value, the operations are mainly performed on FileHandlerUtility
    # and which has required test cases.
    pass
