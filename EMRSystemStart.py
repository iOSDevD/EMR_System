"""
Nikunj Upadhyay
Class: CS 521 - Fall 1
Date: 10/03/2021
Homework Problem # Project
Description of Problem (1-2 sentence summary in your own words):

Main Program file which starts the execution of the project.
It starts by validating the user and then provide the required actions
to be performed like patient look up, update demographics and questionnaire.

"""

import sys

from InputFiles.LoginUserValidation import perform_credential_validation
from handlers import PrintStatistics
from utilities.AppConstants import AppConstants, LoginConstants
from handlers.AddUpdatePatient import AddUpdateFlowHandler

# Main Program Flow Starts here
from handlers.LookUpPatient import LookUpFlowHandler
from handlers.PrintPatientRecord import PrintFlowHandler

# Start of the main program
print(LoginConstants.WELCOME_MESSAGE)

while True:  # Keep prompting user till valid user name and password is entered
    # Prompt user to enter user name and password.
    input_str = input(LoginConstants.EMR_LOGIN_CREDENTIAL_PROMPT_MESSAGE)

    # Get the tuple into two variables, status and other holds the validation
    # message.
    is_user_valid, validation_message = perform_credential_validation(input_str)

    print(validation_message)  # Print success or failure message.

    if is_user_valid:  # Found valid user
        break  # Break the loop and login into the system.

while True:
    # Display Options after user logs in
    display_main_option_str = AppConstants().get_main_screen_prompt()

    # Get the option input from the user
    selected_main_option_str = input(display_main_option_str)

    # Check if the option entered is a valid one.
    if selected_main_option_str in AppConstants.OPTIONS.keys():
        if selected_main_option_str == AppConstants.MAIN_SCREEN_PRINT_KEY:
            # users selects to print records
            PrintFlowHandler().print_all_records()
        elif selected_main_option_str == \
                AppConstants.MAIN_SCREEN_ADD_NEW_PATIENT_KEY:
            # user selects to add a new patient
            AddUpdateFlowHandler().add_update_patient_flow()
        elif selected_main_option_str == \
                AppConstants.MAIN_SCREEN_SEARCH_PATIENT_KEY:
            # user selects to search for patient and perform operation
            LookUpFlowHandler().lookup_patient_flow()
        elif selected_main_option_str == \
                AppConstants.MAIN_SCREEN_STATISTICS_KEY:
            PrintStatistics.StatisticsFlowHandler().start_print_statistics()
        elif selected_main_option_str == AppConstants.MAIN_SCREEN_SIGN_OFF_KEY:
            # user selects to sign off from the system
            print(LoginConstants.SIGN_OFF_MESSAGE)
            sys.exit()
    else:  # Invalid option entry, re-prompt user for valid entry.
        print(LoginConstants.INVALID_INPUT_TRY_AGAIN)
