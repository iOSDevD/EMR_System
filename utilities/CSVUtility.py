"""
Nikunj Upadhyay
Class: CS 521 - Fall 1
Date: 10/16/2021
Homework Problem # Project
Description of Problem (1-2 sentence summary in your own words):
"""
import copy
import csv
import os
import time

from model.Patient import Patient


class FileHandlerUtility:
    """ File Handler Utility which helps to perform CRUD operations like
    add new patient, read patient records, update and delete patient record
    on a input file.
    """

    __INPUT_FILE_NAME = "PatientRecords.csv"
    __INPUT_FOLDER_NAME = "InputFiles"
    __FILE_ENCODING = 'utf-8-sig'

    def __get_input_file_path(self):
        return os.path.join(self.__INPUT_FOLDER_NAME, self.__INPUT_FILE_NAME)

    def read_all_records(self, rows_as_patient=False):
        """ Read records from a file and returns a tuple of header and rows.

        Header represent first row in the CSV file and rows are the ones
        which hold patient record.

        :param rows_as_patient: value should be True
        :return: Tuple of list representing rows or header. In case the reading
                of file it  returns tuple of empty list.
        """
        workbook_file = None  # Default to None

        try:
            # Open the .csv file with read only mode and utf-8 encoding.
            workbook_file = open(self.__get_input_file_path(), "r",
                                 encoding=self.__FILE_ENCODING)
        except IOError:
            print("Failed to read PatientRecords.csv")

        headers = []  # Default empty header list
        rows = []  # Default empty rows list

        if workbook_file is not None:
            workbook_reader = csv.reader(workbook_file)
            for row in workbook_reader:
                if len(headers) == 0:  # Set header only once at the start.
                    headers = row[:]  # Shallow copy row
                else:  # Rest of them are rows not headers.
                    if rows_as_patient:
                        rows.append(Patient(row))
                    else:
                        rows.append(row)

            workbook_file.close()  # Close the opened file after processing.

        return headers, rows  # Return multiple results using Tuple

    def read_all_records_row_data(self):
        """It returns the list of rows as a Patient object rather than
        a string.

        :return: list of Patient objects.
        """
        csv_data = self.read_all_records(rows_as_patient=True)
        return csv_data[1]

    def write_new_record(self, new_patient_data_list):
        """ Appends a new patient to the csv file.

        :param new_patient_data_list: List of entries represented in the
            columns of csv, starting from patient id to questionnaire.
        """
        workbook_file = None

        try:
            workbook_file = open(self.__get_input_file_path(), "a",
                                 encoding=self.__FILE_ENCODING,
                                 newline="")
        except IOError:
            print("Failed to read PatientRecords.csv")

        if workbook_file is not None:
            workbook_writer = csv.writer(workbook_file)
            workbook_writer.writerow(new_patient_data_list)
            workbook_file.close()

    def update_a_record(self, new_patient_data_list, patient_id):
        """ Updates the demographic details for the provided patient id.

        :param new_patient_data_list: List of entries represented in the
            columns of csv, starting from patient id to questionnaire.
        :param patient_id: Patient id for which we need to update the record.
        """
        existing_records = self.read_all_records()
        workbook_file = None

        try:
            workbook_file = open(self.__get_input_file_path(), "w",
                                 encoding=self.__FILE_ENCODING,
                                 newline="")
        except IOError:
            print("Failed to read PatientRecords.csv")

        if workbook_file is not None:
            workbook_writer = csv.writer(workbook_file)
            header = existing_records[0]
            workbook_writer.writerow(header)
            existing_rows = existing_records[1]
            for record in existing_rows:
                if record[0] == patient_id and len(new_patient_data_list) == 13:
                    workbook_writer.writerow(new_patient_data_list)
                else:
                    workbook_writer.writerow(record)

            workbook_file.close()

    def delete_a_record(self, patient_id):
        """ Deletes the record for the provided patient id.

        :param patient_id: Patient for which csv row has to be deleted.
        :return: True if delete was success else default None.
        """
        existing_records = self.read_all_records()  # Records to be re-written
        workbook_file = None

        try:
            # Open file object with write mode, so as to clear the existing
            # file content and re-write rows.
            workbook_file = open(self.__get_input_file_path(), "w",
                                 encoding=self.__FILE_ENCODING,
                                 newline="")
        except IOError:
            print("Failed to read PatientRecords.csv")

        if workbook_file is not None:
            workbook_writer = csv.writer(workbook_file)
            header = existing_records[0]
            workbook_writer.writerow(header)
            existing_rows = existing_records[1]
            for record in existing_rows:
                if record[0] != patient_id:
                    workbook_writer.writerow(record)

            workbook_file.close()  # Close file object
            return True


if __name__ == "__main__":
    print("Started Executing test case in FileHandlerUtility")

    # Move to one step up from utilities dir to get
    # InputFiles/PatientRecords.csv
    parent = os.path.dirname(os.getcwd())
    os.chdir(parent)

    # FileHandlerUtility to test
    utility = FileHandlerUtility()

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
    fake_patient_id = "12346789TestPatientid"
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
