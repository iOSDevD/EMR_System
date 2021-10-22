"""
Nikunj Upadhyay
Class: CS 521 - Fall 1
Date: 10/16/2021
Homework Problem # Project
Description of Problem (1-2 sentence summary in your own words):

The Program handles displaying the list of existing records and print more
details for a specific patient id. More details printed also prints
questionnaire that was answered.

"""
from view import TableView
from utilities.CSVUtility import FileHandlerUtility
from utilities.Questionnaire import Questionnaire


class PrintFlowHandler:
    """Helps to print the patient records as in tabular format displayed
     using a new Table view. We can also print details of a specific patient."""

    # Prompt message to be displayed to the user, either to print a specific
    # record or skip by tapping enter.
    PRINT_INPUT_MESSAGE = "Would you like to print patient detail as " \
                          "summary?\nIf yes please enter the patient id or " \
                          "simply press enter again to exit this option."

    # Format to print the patient summary with the help of Patient object
    # and questionnaire object.
    PRINT_PATIENT_RESULT = "{}\nQuestionnaire Results:-\n{}"

    # Error Message to be shown if we could not find a unique patient
    # object for the provided patient id.
    INVALID_PATIENT_ID_FOR_PRINT = "Could not find patient data for provided" \
                                   " patient Id {}\nPlease try again with" \
                                   " a valid patient id."

    def print_all_records(self):
        """Prints all the patient records available in the CSV file.
        It will also prompt the user to print a specific record by typing the
        patient id from the list."""

        # Read all records from CSV as a list or rows and headers.
        # Tuple at index 0 returns header and at index 1 list of patient's.
        csv_data = FileHandlerUtility().read_all_records()

        # Print the details as table.
        TableView.Table().print_table(csv_data[0], csv_data[1])

        # Flag for continue input. Set to false in case user taps on enter,
        # in which case it would exist the current module.
        prompt_for_detail_format = True
        while prompt_for_detail_format:  # Keep prompting if valid patient id
            patient_id_str = input(PrintFlowHandler.PRINT_INPUT_MESSAGE)
            if len(patient_id_str.strip()) == 0:  # Empty input entered.
                prompt_for_detail_format = False  # Exit the current flow
                continue
            else:  # Non empty input entered, use patient id to print record.
                # Print patient record.
                self.print_a_patient_record(patient_id_str)

    def print_a_patient_record(self, patient_id_str):
        """Print a specific record for provided patient id.
        If the patient id does not match with the one in the list an error
        message is displayed.

        It prints both patient specific details as well as questionnaire
        answers of the patient.

        """
        # Read all records as Patient object from teh CSV file.
        csv_rows = FileHandlerUtility().read_all_records_row_data()

        # Filter to get a unique patient object matching the patient id.
        patient_row_filter = filter(
            lambda patient: patient.get_patient_id() == patient_id_str,
            csv_rows)  # filter to search for patient id

        # Convert filter object to list, to get the patient object
        patient_row_result_list = list(patient_row_filter)  # result list.

        if len(patient_row_result_list) == 1:  # Found unique match
            # Get one and only one patient at index 0
            patient_result = patient_row_result_list[0]

            # Get questionnaire with answers, answered for the patient id.
            questionnaire = Questionnaire().get_questionnaire_to_print(
                patient_result.get_questionnaire_as_list())

            # Print patient record and questionnaire.
            print(PrintFlowHandler.PRINT_PATIENT_RESULT.format(patient_result,
                                                               questionnaire))
        else:  # Unable to find patient for the provided patient id.
            print(
                PrintFlowHandler.INVALID_PATIENT_ID_FOR_PRINT.format(
                    patient_id_str))


# Unit Tests
if __name__ == "__main__":
    # There are no test case for the current file as methods don't return a
    # specific value, its about printing values and FileHandlerUtility has
    # required test cases.
    pass
