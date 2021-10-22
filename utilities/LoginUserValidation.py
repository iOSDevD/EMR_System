"""
Nikunj Upadhyay
Class: CS 521 - Fall 1
Date: 10/16/2021
Homework Problem # Project
Description of Problem (1-2 sentence summary in your own words):

The program illustrate that it has functions which can be used
to validate the user name and password.
"""
from utilities.AppConstants import LoginConstants


def is_logged_in_user_valid(user_name, password):
    """ Function that validates if the user entered correct user name
    and password. User name is case insensitive and password is case sensitive.
    """
    if user_name.upper() == "HELLO" and password == "World":
        return True  # User input matches user name and password.
    else:
        return False  # User input does not match user name and password.s


def perform_credential_validation(user_name_password):
    """Function that helps to perform the validation of the string containing
    username and password separated by space.
    Returns a tuple (Boolean, Message), the value is True if the username
    and password is correct along with success message. It will return false
    if the input is invalid along with the error message.
    """

    is_user_valid = False  # Logged in user valid flag
    validation_message = ""  # Error! user name and password entry.
    try:
        # Use default white space delimiter.
        user_name_str, password_str = user_name_password.split()

        # perform user name and password validation.
        is_user_valid = is_logged_in_user_valid(user_name_str, password_str)
        if is_user_valid:  # User valid - Success
            validation_message = LoginConstants.EMR_LOGIN_SUCCESS_MESSAGE
        else:  # User in-valid - Failure.
            validation_message = \
                LoginConstants.EMR_LOGIN_INVALID_CREDENTIALS_MESSAGE
    except ValueError:  # Error thrown in case there is no white space.
        validation_message = LoginConstants.CREDENTIAL_USER_ENTRY_ERROR_MESSAGE

    return is_user_valid, validation_message  # Tuple - validation and message


# Unit Tests
if __name__ == "__main__":
    # help to run test case efficiently.
    print("Started Executing test case for functions in LoginUserValidation")

    # 1. Test case check if user name and password are correct.
    assert is_logged_in_user_valid("hello", "World"), (
        "User name and password are valid so it should not fail.")

    # Invalid password returns False.
    assert is_logged_in_user_valid("hello", "test") is False, (
        "User name and password are in-valid so it should fail.")

    # Test user name and password string is not separated by space.
    validation_result_failure = perform_credential_validation("HelloWorld")
    assert validation_result_failure[0] is False and \
           validation_result_failure[1] == \
           LoginConstants.CREDENTIAL_USER_ENTRY_ERROR_MESSAGE, (
        "As user name and password are not whitespace separated "
        "or some error occurred, it should return appropriate error message.")

    # Test user name and password string separated by space but does match
    # with the record in the system".
    validation_result_invalid_credential = \
        perform_credential_validation("Hello test")
    assert validation_result_invalid_credential[0] is False and \
           validation_result_invalid_credential[1] == \
           LoginConstants.EMR_LOGIN_INVALID_CREDENTIALS_MESSAGE, (
        "User entered wrong user name or password the method should "
        "return fail")

    print("Success! Completed Executing test case in LoginUserValidation")
