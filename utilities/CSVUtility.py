"""
Nikunj Upadhyay
Class: CS 521 - Fall 1
Date: 10/16/2021
Homework Problem # Project
Description of Problem (1-2 sentence summary in your own words):

CSV Utility helper which performs multiple operations like writing/appending
a new record to the file, deleting a patient entry, reading all records as
list of string or Patient object.
"""
import copy
import csv
import os
import time

from model.Patient import Patient

# CSV  file name holding the patient records.
INPUT_FILE_NAME = "PatientRecords.csv"

# CSV  file name holding the patient records,
# which can be used for testing.
TEST_FILE_NAME = "PatientRecordsTest.csv"


class FileHandlerUtility:
    """ File Handler Utility which helps to perform CRUD operations like
    add new patient, read patient records, update and delete patient record
    on a input file.
    """

    # Folder in which Input file name is present
    __INPUT_FOLDER_NAME = "InputFiles"  # Private static attribute

    # Encoding to be used while encoding or decoding the input file.
    __FILE_ENCODING = 'utf-8-sig'  # Private static attribute

    def __init__(self, file_name=INPUT_FILE_NAME):
        """Initialize the utility handler with a default file name. We can still
        initialize it with a different file name, usually we use it during
        Test."""
        self.__file_name = file_name

    def __get_input_file_path(self):
        """Get the path of the file with folder that it resides in, using
        a platform independent approach."""
        return os.path.join(self.__INPUT_FOLDER_NAME, self.__file_name)

    def read_all_records(self, rows_as_patient=False):
        """ Read records from a file and returns a tuple of header and rows.

        Header represent first row in the CSV file and rows are the ones
        which hold patient record. Returned Tuple at index 0 represents header
        and at index 1 its list of rows (as list of string values or list of
        Patient object)

        :param rows_as_patient: value should be True
        :return: Tuple of list representing header(0) and rows(1).
                In case the reading of file it returns tuple of empty list.
        """
        workbook_file = None  # Default to None

        try:
            # Open the .csv file with read only mode and utf-8 encoding.
            workbook_file = open(self.__get_input_file_path(), "r",
                                 encoding=FileHandlerUtility.__FILE_ENCODING)
        except IOError:
            print("Failed to read PatientRecords.csv")

        headers = []  # Default empty header list
        rows = []  # Default empty rows list

        if workbook_file is not None:  # Read only if file opening was success
            workbook_reader = csv.reader(workbook_file)  # Iterator to read line
            for row in workbook_reader:  # Iterate each row in CSV
                if len(headers) == 0:  # Set header only once at the start.
                    headers = row[:]  # Shallow copy row
                else:  # Rest of them are rows not headers.
                    if rows_as_patient:
                        rows.append(Patient(row))  # Row as Patient Object
                    else:
                        rows.append(row)  # Row as list of string.

            workbook_file.close()  # Close the opened file after processing.

        return headers, rows  # Return multiple results using Tuple

    def read_all_records_row_data(self):
        """It returns the list of rows as a Patient object rather than
        a string.

        :return: list of Patient objects.
        """
        csv_data = self.read_all_records(rows_as_patient=True)
        return csv_data[1]  # Tuple at index 1 has patient rows.

    def write_new_record(self, new_patient_data_list):
        """ Appends a new patient to the csv file.

        :param new_patient_data_list: List of entries represented in the
            columns of csv, starting from patient id to questionnaire.
        """
        workbook_file = None  # Default to None

        try:
            # Open the .csv file with append mode to add new record entry at
            # the end of the file and use utf-8 encoding.
            workbook_file = open(self.__get_input_file_path(), "a",
                                 encoding=FileHandlerUtility.__FILE_ENCODING,
                                 newline="")
        except IOError:
            print("Failed to read PatientRecords.csv")

        if workbook_file is not None:  # Append only if file opening was success
            # Get the writer object which converts user's data into delimited
            # strings.
            workbook_writer = csv.writer(workbook_file)
            # Write iterable object ex: list to the file.
            workbook_writer.writerow(new_patient_data_list)
            workbook_file.close()  # Close the opened file after processing.

    def update_a_record(self, new_patient_data_list, patient_id):
        """ Updates the demographic details for the provided patient id.

        :param new_patient_data_list: List of entries represented in the
            columns of csv, starting from patient id to questionnaire.
        :param patient_id: Patient id for which we need to update the record.
        """
        # Read all existing records to be re-written
        existing_records = self.read_all_records()
        workbook_file = None  # Default to None

        try:
            # Open the .csv file with write mode which clears the current file
            # content and helps to write new entries while replacing the
            # specified patient record and use utf-8 encoding.
            workbook_file = open(self.__get_input_file_path(), "w",
                                 encoding=FileHandlerUtility.__FILE_ENCODING,
                                 newline="")
        except IOError:
            print("Failed to read PatientRecords.csv")

        if workbook_file is not None:  # Update only if file opening was success
            # Get the writer object which converts user's data into delimited
            # strings.
            workbook_writer = csv.writer(workbook_file)
            header = existing_records[0]  # Get the header from existing records
            workbook_writer.writerow(header)  # Write the header first

            # Get all rows from existing records
            existing_rows = existing_records[1]
            for record in existing_rows:  # Iterate and write patient row.
                if record[0] == patient_id and len(new_patient_data_list) == 13:
                    # Patient id match found, so skip the current record
                    # and use new record entry to have updated value.
                    workbook_writer.writerow(new_patient_data_list)
                else:  # Patient id match not found, keep adding current record
                    workbook_writer.writerow(record)

            workbook_file.close()  # Close the opened file after processing.

    def delete_a_record(self, patient_id):
        """ Deletes the record for the provided patient id.

        :param patient_id: Patient for which csv row has to be deleted.
        :return: True if delete was success else default None.
        """
        existing_records = self.read_all_records()  # Records to be re-written
        workbook_file = None  # Default to None

        try:
            # Open file object with write mode, which clears the current file
            # content and helps to write existing entry while skipping the
            # entry which we want to delete and use utf-8 encoding.
            workbook_file = open(self.__get_input_file_path(), "w",
                                 encoding=FileHandlerUtility.__FILE_ENCODING,
                                 newline="")
        except IOError:
            print("Failed to read PatientRecords.csv")

        if workbook_file is not None:
            workbook_writer = csv.writer(workbook_file)
            header = existing_records[0]  # Get the header from existing records
            workbook_writer.writerow(header)  # Write the header first

            # Get all rows from existing records
            existing_rows = existing_records[1]
            for record in existing_rows:  # Iterate and write patient row.
                # Write back all records except the one to be deleted.
                if record[0] != patient_id:
                    workbook_writer.writerow(record)

            workbook_file.close()  # Close the opened file after processing.
            return True  # Delete was success.


# Unit Tests
if __name__ == "__main__":
    print("Started Executing test case in FileHandlerUtility")

    # Move to one step up from utilities dir to get
    # InputFiles/PatientRecords.csv
    parent = os.path.dirname(os.getcwd())
    os.chdir(parent)

    # FileHandlerUtility to test
    utility = FileHandlerUtility(TEST_FILE_NAME)

    # 1. Test Case to check fetch of rows as string.
    all_rows_with_header = utility.read_all_records()
    patient_rows_count = len(all_rows_with_header[1])
    assert all_rows_with_header is not None, (
        "Records should be available after reading")

    assert len(all_rows_with_header[0]) == 13, (
        "Should match the column in csv starting from patient id"
        " to Questionnaire")

    assert patient_rows_count > 0, (
        "There should be more than one patient rows with string values")

    # 2. Test case to read all patient rows as Patient object
    row_data_as_patient = utility.read_all_records_row_data()
    assert len(row_data_as_patient) == patient_rows_count, (
        "There should be more than one patient rows with patient object")

    # 3. Test case to Add new Patient
    fake_patient_id = "12346789"
    dummyPatient = Patient()
    dummyPatient.set_patient_id(fake_patient_id)
    utility.write_new_record(dummyPatient.get_list_template_to_save())
    row_count_on_adding_new_patient = len(utility.read_all_records_row_data())
    assert row_count_on_adding_new_patient == patient_rows_count + 1, \
        ("After adding new patient the count of "
         "rows should be incremented by 1")

    # 4. Test case to Update Patient
    # Get any the existing patient from the list
    patient_before_update = row_data_as_patient[0]

    dummyPatient = copy.copy(patient_before_update)
    # Add time stamp so that its unique every time we run the test case,
    # if we don't have timestamp string to expected address it would not
    # be unique and assert will throw error as if it did not update the address.
    expected_address_after_updated = "1 Rose Drive " + str(time.time())
    dummyPatient.set_address_line_1(expected_address_after_updated)
    # Main Test of Update address in the file. Important call this one!
    utility.update_a_record(dummyPatient.get_list_template_to_save(),
                            patient_before_update.get_patient_id())
    # After update, check if it was success by reading back details of
    # the updated patient id.
    patient_rows_after_update = utility.read_all_records_row_data()
    patient_list = [e for e in patient_rows_after_update if e.get_patient_id()
                    == patient_before_update.get_patient_id()]
    address_after_update = patient_list[0].get_address_line_1()
    assert patient_before_update.get_address_line_1() != address_after_update, (
        "Update did not work! Expected address is '{}' but found '{}'".format(
            expected_address_after_updated,
            patient_before_update.get_address_line_1()))

    # 5. Test case to delete a patient
    row_count_before_delete = len(utility.read_all_records_row_data())
    utility.delete_a_record(fake_patient_id)
    row_count_after_delete = len(utility.read_all_records_row_data())
    assert row_count_after_delete == row_count_before_delete - 1, \
        ("After adding deleting the patient the count of "
         "rows should be decremented by 1, found {} expected {}".
         format(row_count_after_delete, row_count_before_delete - 1))

    print("Success! Completed Executing test case in FileHandlerUtility")
