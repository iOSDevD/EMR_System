"""
Nikunj Upadhyay
Class: CS 521 - Fall 1
Date: 10/16/2021[
Homework Problem # Project
Description of Problem (1-2 sentence summary in your own words):

The program holds two constant class which acts as helper to get messages
for main screen and patient login.

"""


class LoginConstants:
    """Constants for Login Screen, for example welcome message and login
    messages"""

    WELCOME_MESSAGE = "\n\n################# Welcome to the " \
                      "BU Medical System #################\n\n"

    EMR_LOGIN_CREDENTIAL_PROMPT_MESSAGE = "Please enter the user name and " \
                                          "password separated by space, to " \
                                          "login into the EMR system"

    EMR_LOGIN_SUCCESS_MESSAGE = "Success! Loading the System now.........\n"

    EMR_LOGIN_INVALID_CREDENTIALS_MESSAGE = "Error! Invalid username or " \
                                            "password. Please try again with " \
                                            "a valid username and password"

    CREDENTIAL_USER_ENTRY_ERROR_MESSAGE = "Error! Please try again with " \
                                          "username and password separated " \
                                          "by space."


class AppConstants:
    """Holds the constants for the App. which shows different modules like
    Main Screen options or Patient Look up options. It also helps to create
    empty template list of patient to be saved or create a new patient from
    scratch"""

    MAX_COLUMN_COUNT = 13

    COLUMN_RANGE = range(0, MAX_COLUMN_COUNT)

    MAIN_SCREEN_ADD_NEW_PATIENT_KEY, MAIN_SCREEN_SEARCH_PATIENT_KEY, \
        MAIN_SCREEN_PRINT_KEY, MAIN_SCREEN_SIGN_OFF_KEY = \
        "a", "b", "c", "d"

    OPTIONS = {MAIN_SCREEN_ADD_NEW_PATIENT_KEY: "Add a new Patient",
               MAIN_SCREEN_SEARCH_PATIENT_KEY: "Search Patient",
               MAIN_SCREEN_PRINT_KEY: "Print all Patient Records",
               MAIN_SCREEN_SIGN_OFF_KEY: "Sign off"}

    PATIENT_LOOK_UP_UPDATE_QUESTIONNAIRE_KEY, \
        PATIENT_LOOK_UP_UPDATE_PATIENT_KEY, PATIENT_LOOK_UP_DELETE_PATIENT_KEY \
        = "a", "b", "c"

    LOOKUP_OPTIONS = {
        PATIENT_LOOK_UP_UPDATE_QUESTIONNAIRE_KEY: "Add/Update Intake form",
        PATIENT_LOOK_UP_UPDATE_PATIENT_KEY: "Update patient "
                                            "details (Address and Contact)",
        PATIENT_LOOK_UP_DELETE_PATIENT_KEY: "Delete the patient"}

    FLOW_INITIATOR_OPTIONS = """What would you like to do?\n{}"""

    OPTIONS_LIST = ["{}.{}".format(k, v) for k, v in OPTIONS.items()]

    OPTIONS_LOOKUP_LIST = ["{}.{}".format(k, v) for k, v in
                           LOOKUP_OPTIONS.items()]

    GENDER_DICTIONARY = {"F": "Female", "M": "Male", "O": "Other"}

    INPUT_DELIMITER = "$"

    def get_main_screen_prompt(self):
        """ Message to be displayed after the user logs in. Its the main screen
        message, which would list the operations that can be performed with this
        system.
        """
        return """\n""".join(AppConstants.OPTIONS_LIST)

    def get_empty_data_template(self):
        """ Generates the empty list of entries matching the MAX_COLUMN_COUNT.
        MAX_COLUMN_COUNT represents number of columns."""
        return [""] * AppConstants.MAX_COLUMN_COUNT

    def get_patient_look_up_prompt(self):
        """Message to be displayed when patient lookup operation starts"""
        return """\n""".join(AppConstants.OPTIONS_LOOKUP_LIST)


# Unit Tests
if __name__ == "__main__":
    # 1. Test main screen message
    main_screen_message = "a.Add a new Patient\nb.Search Patient\n" \
                          "c.Print all Patient Records\nd.Sign off"

    assert AppConstants().get_main_screen_prompt() == \
           main_screen_message, "Option message for prompt does not" \
                                "match with expected main screen" \
                                "message '{}'".format(
        main_screen_message)

    # 2. Test empty template list of patient data
    empty_patient_list = [""] * AppConstants.MAX_COLUMN_COUNT
    assert AppConstants().get_empty_data_template() == empty_patient_list, \
        "It should be empty string list of size {}".format(
            AppConstants.MAX_COLUMN_COUNT)

    # 3. Test Patient Look up Prompt Message
    patient_look_up_message = "a.Add/Update Intake form\nb.Update " \
                              "patient details (Address and " \
                              "Contact)\nc.Delete the patient"

    assert AppConstants().get_patient_look_up_prompt() == \
           patient_look_up_message, (
        "Patient look up prompt does "
        "not match with expected main "
        "screen message '{}'".format(patient_look_up_message))
