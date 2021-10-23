"""
Nikunj Upadhyay
Class: CS 521 - Fall 1
Date: 10/16/2021
Homework Problem # Project
Description of Problem (1-2 sentence summary in your own words):

The program holds two constant class which acts as helper to get messages
for main screen and patient login, patient look up and other uses like having
Gender description value.

"""


class LoginConstants:
    """Constants for Login Screen, for example welcome message and login
    messages"""

    # Welcome message when EMRSystemStart.py is called.
    WELCOME_MESSAGE = "\n\n################# Welcome to the " \
                      "BU Medical System #################\n\n"

    # Prompt the user to enter user name and password separated by space.
    EMR_LOGIN_CREDENTIAL_PROMPT_MESSAGE = "Please enter the user name and " \
                                          "password separated by space, to " \
                                          "login into the EMR system:\n"

    # Validation was success, use this text to show login success message.
    EMR_LOGIN_SUCCESS_MESSAGE = "Success! Loading the System now.........\n"

    # Validation failed, use this text to show failure message.
    EMR_LOGIN_INVALID_CREDENTIALS_MESSAGE = "Error! Invalid username or " \
                                            "password. Please try again with " \
                                            "a valid username and password"

    # Input entry validation failed, use this text to show message when
    # username and password are not space separated.
    CREDENTIAL_USER_ENTRY_ERROR_MESSAGE = "Error! Please try again with " \
                                          "username and password separated " \
                                          "by space."

    # Sign Off Message
    SIGN_OFF_MESSAGE = "\n\nSigning Off, from the System!...................."

    # Error message to be shown in case of invalid input is entered.
    INVALID_INPUT_TRY_AGAIN = "Please try again, invalid input entered"


class AppConstants:
    """Holds the constants for the App. which shows different modules like
    Main Screen options or Patient Look up options. It also helps to create
    empty template list of patient to be saved or create a new patient from
    scratch"""

    # Max column count in the CSV, helps to create a empty list template
    MAX_COLUMN_COUNT = 13

    # Main Screen option keys, these options are available after the login
    MAIN_SCREEN_ADD_NEW_PATIENT_KEY, MAIN_SCREEN_SEARCH_PATIENT_KEY, \
        MAIN_SCREEN_PRINT_KEY, MAIN_SCREEN_STATISTICS_KEY, \
        MAIN_SCREEN_SIGN_OFF_KEY = "a", "b", "c", "d", "e"

    # Main Screen options dictionary, having the option (ex: a) as key and
    # value as description about the operation that it can perform.
    OPTIONS = {MAIN_SCREEN_ADD_NEW_PATIENT_KEY: "Add a new Patient",
               MAIN_SCREEN_SEARCH_PATIENT_KEY: "Search Patient",
               MAIN_SCREEN_PRINT_KEY: "Print all Patient Records",
               MAIN_SCREEN_STATISTICS_KEY: "Statistics of Patient Records",
               MAIN_SCREEN_SIGN_OFF_KEY: "Sign off"}

    # Patient look up option additional message to help identify option
    # or exit.
    MAIN_SCREEN_ADDITIONAL_MESSAGE = "\nPlease select one of the option " \
                                     "(ex: a)\n"

    # Patient Look up option, sub options. These options are available
    # after the patient look up finds a patient.
    LOOK_UP_UPDATE_QUESTIONNAIRE_KEY, LOOK_UP_UPDATE_PATIENT_KEY, \
        LOOK_UP_DELETE_PATIENT_KEY = "a", "b", "c"

    # Patient look up options dictionary, having the option (ex: a) as key
    # and value as description about the operation that it can perform.
    LOOKUP_OPTIONS = {
        LOOK_UP_UPDATE_QUESTIONNAIRE_KEY: "Add/Update Intake form",
        LOOK_UP_UPDATE_PATIENT_KEY: "Update patient "
                                    "details (Address and Contact)",
        LOOK_UP_DELETE_PATIENT_KEY: "Delete the patient"}

    # Patient look up option additional message to help identify option
    # or exit.
    LOOKUP_ADDITIONAL_MESSAGE = "\nPlease select one of the option (ex: a)" \
                                " or simply press enter again to exit.\n"

    # Gender values used for presentation and saving to file.
    GENDER_VALUE_MALE, GENDER_VALUE_FEMALE, GENDER_VALUE_OTHER = \
        "Male", "Female", "Other"

    # Gender dictionary with keys as single character values with its
    # equivalent gender description value.
    GENDER_DICTIONARY = {"F": GENDER_VALUE_FEMALE, "M": GENDER_VALUE_MALE,
                         "O": GENDER_VALUE_OTHER}

    # Delimiter constant to accept entries from console separated by $.
    # Helps to capture multiple values from console.
    INPUT_DELIMITER = "$"

    def get_main_screen_prompt(self):
        """ Message to be displayed after the user logs in. Its the main screen
        message, which would list the operations that can be performed with this
        system.
        """
        sorted_options_str_list = self.get_sorted_formatted_list(
            AppConstants.OPTIONS)

        # Join the list to create a string separated by new line.
        prompt_message_str = """\n""".join(sorted_options_str_list) + \
                             AppConstants.MAIN_SCREEN_ADDITIONAL_MESSAGE
        return prompt_message_str

    def get_empty_data_template(self):
        """ Generates the empty list of entries matching the MAX_COLUMN_COUNT.
        MAX_COLUMN_COUNT represents number of columns."""
        return [""] * AppConstants.MAX_COLUMN_COUNT

    def get_patient_look_up_prompt(self):
        """Message to be displayed when patient lookup operation starts"""
        sorted_options_str_list = self.get_sorted_formatted_list(
            AppConstants.LOOKUP_OPTIONS)

        # Message combination of options details and a additional message
        # to enter option or exit.
        prompt_message_str = """\n""".join(sorted_options_str_list) + \
                             AppConstants.LOOKUP_ADDITIONAL_MESSAGE
        return prompt_message_str

    def get_sorted_formatted_list(self, option_description_dict):
        """Returns the sorted list of string representing option and its
        description from the input dictionary."""

        # Convert dictionary to list to tuple with option(key) and
        # description (value)
        main_screen_tuple_list = [(k, v) for (k, v) in
                                  option_description_dict.items()]

        # Sort the tuple with tuple at index 0, which is the option key like
        # a,b,c..etc
        main_screen_sorted_tuple = sorted(main_screen_tuple_list,
                                          key=lambda x: x[0])

        # Transform tuple list to string list with format as key.value
        # i.e a. Add a new Patient
        sorted_options_str_list = ["{}.{}".format(x[0], x[1]) for x in
                                   main_screen_sorted_tuple]
        return sorted_options_str_list  # Sorted list of string


# Unit Tests
if __name__ == "__main__":
    print("Started Executing test case in AppConstants")

    # 1. Test main screen message
    main_screen_message = "a.Add a new Patient\nb.Search Patient\n" \
                          "c.Print all Patient Records\nd.Statistics of " \
                          "Patient Records\ne.Sign off" + \
                          AppConstants.MAIN_SCREEN_ADDITIONAL_MESSAGE

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
                              "Contact)\nc.Delete the patient" + \
                              AppConstants.LOOKUP_ADDITIONAL_MESSAGE

    assert AppConstants().get_patient_look_up_prompt() == \
           patient_look_up_message, (
        "Patient look up prompt does "
        "not match with expected main "
        "screen message '{}'".format(patient_look_up_message))

    # 4. Test sorting of string list created from dictionary
    input_dictionary = {"v": "Test 2", "a": "Test 1"}
    expected_output_list = ["a.Test 1", "v.Test 2"]
    assert AppConstants().get_sorted_formatted_list(
        input_dictionary) == expected_output_list, (
        "List of string representing option and description should "
        "match with expected output")

    print("Success! Completed Executing test case in AppConstants")
