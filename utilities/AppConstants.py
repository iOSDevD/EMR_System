"""
Nikunj Upadhyay
Class: CS 521 - Fall 1
Date: 10/16/2021[
Homework Problem # Project
Description of Problem (1-2 sentence summary in your own words):
"""


class LoginConstants:
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
    COLUMN_RANGE = range(0, 13)

    OPTION_KEY_ADD_NEW_PATIENT, OPTION_KEY_SEARCH_PATIENT, OPTION_KEY_PRINT_RECORDS, OPTION_KEY_SIGN_OFF = \
        "a", "b", "c", "d"

    OPTIONS = {OPTION_KEY_ADD_NEW_PATIENT: "Add a new Patient",
               OPTION_KEY_SEARCH_PATIENT: "Search Patient",
               OPTION_KEY_PRINT_RECORDS: "Print all Patient Records",
               OPTION_KEY_SIGN_OFF: "Sign off"}

    OPTION_KEY_UPDATE_QUESTIONNAIRE, OPTION_KEY_UPDATE_PATIENT, OPTION_KEY_DELETE_PATIENT = "a", "b", "c"

    LOOKUP_OPTIONS = {OPTION_KEY_UPDATE_QUESTIONNAIRE: "Add/Update Intake form",
                      OPTION_KEY_UPDATE_PATIENT: "Update patient details (Address and Contact)",
                      OPTION_KEY_DELETE_PATIENT: "Delete the patient"}

    FLOW_INITIATOR_OPTIONS = """What would you like to do?\n{}"""

    OPTIONS_LIST = ["{}.{}".format(k, v) for k, v in OPTIONS.items()]

    OPTIONS_LOOKUP_LIST = ["{}.{}".format(k, v) for k, v in
                           LOOKUP_OPTIONS.items()]

    GENDER_DICTIONARY = {"F": "Female", "M": "Male", "O": "Other"}

    def getMainScreenOptionsMessge(self):
        return """\n""".join(AppConstants.OPTIONS_LIST)

    def getEmptyDataTemplate(self):
        return ["" for e in list(AppConstants.COLUMN_RANGE)]

    def getPatientLookUpScreenOptionsMessge(self):
        return """\n""".join(AppConstants.OPTIONS_LOOKUP_LIST)
