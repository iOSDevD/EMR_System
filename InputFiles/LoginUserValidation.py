"""
Nikunj Upadhyay
Class: CS 521 - Fall 1
Date: 10/16/2021
Homework Problem # Project
Description of Problem (1-2 sentence summary in your own words):
"""
from utilities.AppConstants import LoginConstants


def is_logged_in_user_valid(user_name, password):
    if user_name.upper() == "HELLO" and password == "World":
        return True
    else:
        return False


def perform_crendetial_validation(user_name_password):
    is_user_valid = False
    validation_message = ""
    try:
        user_name_str, password_str = user_name_password.split()
        is_user_valid = is_logged_in_user_valid(user_name_str, password_str)
        if is_user_valid:
            validation_message = LoginConstants.EMR_LOGIN_SUCCESS_MESSAGE
        else:
            validation_message = LoginConstants.EMR_LOGIN_INVALID_CREDENTIALS_MESSAGE
    except ValueError:
        validation_message = LoginConstants.CREDENTIAL_USER_ENTRY_ERROR_MESSAGE

    return (is_user_valid, validation_message)
