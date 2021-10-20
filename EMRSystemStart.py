"""
Nikunj Upadhyay
Class: CS 521 - Fall 1
Date: 10/03/2021
Homework Problem # Project
Description of Problem (1-2 sentence summary in your own words):
Pending
"""

import sys

from InputFiles.LoginUserValidation import perform_credential_validation
from utilities.AppConstants import AppConstants, LoginConstants
from handlers.AddUpdatePatient import AddUpdateFlowHandler

# Main Program Flow Starts here
from handlers.LookUpPatient import LookUpFlowHandler
from handlers.PrintPatientRecord import PrintFlowHandler

# Start of the main program

print(LoginConstants.WELCOME_MESSAGE)

while True:
    input_str = input(LoginConstants.EMR_LOGIN_CREDENTIAL_PROMPT_MESSAGE)

    is_user_valid, validation_message = perform_credential_validation(input_str)
    print(validation_message)
    if is_user_valid:
        break

while True:
    display_main_option_str = AppConstants().get_main_screen_prompt()  # Not static need to make it static
    selected_main_option_str = input(display_main_option_str)

    if selected_main_option_str in AppConstants.OPTIONS.keys():
        if selected_main_option_str == AppConstants.MAIN_SCREEN_PRINT_KEY:
            PrintFlowHandler().print_all_records()
        elif selected_main_option_str == AppConstants.MAIN_SCREEN_ADD_NEW_PATIENT_KEY:
            AddUpdateFlowHandler().add_update_patient_flow()
        elif selected_main_option_str == AppConstants.MAIN_SCREEN_SEARCH_PATIENT_KEY:
            LookUpFlowHandler().lookup_patient_flow()
        elif selected_main_option_str == AppConstants.MAIN_SCREEN_SIGN_OFF_KEY:
            print("\n\nSigning Off, from the System!....................")
            sys.exit()


    else:
        print("Please try again, invalid input entered")
