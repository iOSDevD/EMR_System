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

    def printAllRecored(self):
        csv_data = FileHandlerUtility().read_all_records()
        TableView.Table.printTable(csv_data[0], csv_data[1])
        prompt_for_detail_format = True
        while prompt_for_detail_format:
            input_patientId_str = input(
                "Would you like to print patient detail as summary? If yes please enter the patient id or simply press enter again to exit this option")
            if len(input_patientId_str.strip()) == 0:
                print("Exiting Print Records!!!!!")
                prompt_for_detail_format = False
                continue
            else:
                self.printPatientRecord(input_patientId_str)

    def printPatientRecord(self, patient_id_str):
        csv_rows = FileHandlerUtility().read_all_records_row_data()
        patient_row_filter = filter(
            lambda patient: patient.get_patient_id() == patient_id_str, csv_rows)
        patient_row_result_list = list(patient_row_filter)
        if len(patient_row_result_list) == 1:
            patient = patient_row_result_list[0]

            questionnaire = Questionnaire().get_questionnaire_to_print(patient.get_questionnaire_as_list())

            print("{}\nQuestionnaire Results:-\n{}".format(patient,questionnaire))
        else:
            print(
                "Could not find patient data for provided patient Id {}\nPlease try again with a valid patient id.".format(
                    patient_id_str))
