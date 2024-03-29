"""
Nikunj Upadhyay
Class: CS 521 - Fall 1
Date: 10/21/2021
Homework Problem # Project
Description of Problem (1-2 sentence summary in your own words):

Displays statistics of state and covid spread distribution. It also prints
details about gender distribution.

"""

from utilities.AppConstants import AppConstants
from utilities.CSVUtility import FileHandlerUtility
from view import TableView


class StatisticsFlowHandler:
    """Displays the statistics based on the content available in the
    CSV file."""

    # Helps to show data in percentage ex: 10%
    PERCENTAGE_FORMAT = "{:.0%}"

    # Message to be displayed if there is an error to show state and covid
    # spread.
    ERROR_NO_DISTRIBUTION_COVID = "There are no records to show distribution" \
                                  " of Covid spread with states"

    # State and Covid main Message to be shown if tabular data is available.
    STATE_COVID_MAIN_MESSAGE = "Below are the result for state vs COVID " \
                               "Distribution\n"

    # State and Covid additional Message will have details of total patient
    # affected by Covid and number of states where it has been found.
    STATE_COVID_ADDITIONAL_MESSAGE = "There are in total {} patients, who " \
                                     "had covid found in {} different states\n"

    # Headers use by Table View with state and covid percentage distribution.
    STATE_COVID_HEADER_ROWS = ["State", "Covid", "Percentage Distribution"]

    # Gender and percentage distribution main message.
    GENDER_DISTRIBUTION_MAIN_MESSAGE = "\nBelow are the results for gender " \
                                       "and its percentage distribution " \
                                       "with respect to total number of " \
                                       "patients.\n"

    # Headers used by Table view with gender and percentage distribution
    GENDER_HEADER_ROWS = ["Gender", "Percentage distribution"]

    def start_print_statistics(self):
        """Prints the statistical data with available with the CSV file"""
        self.__print_patient_covid_state()  # Print State and Covid distribution
        self.__print_gender_distribution()  # Print Gender distribution

    def __print_patient_covid_state(self):
        """Prints State,Gender and percentage distribution in tabular format
        of three columns"""
        # Get the patient list.
        patient_list = FileHandlerUtility().read_all_records_row_data()
        if len(patient_list) > 0:  # Patient list is not empty.
            state_covid_dict = dict()  # State and Covid count dictionary
            total_covid_patients = 0  # Total number of covid patients
            for patient in patient_list:  # Iterate the list of patients

                # Answers will be returned as list so that we can check
                # first question which is covid one is answered or not.
                answer_list = patient.get_questionnaire_as_list()
                if answer_list is not None and \
                        len(answer_list) > 0 and answer_list[0] == 1:
                    # Patient had covid
                    state = patient.get_address_state()

                    # Put it in a dictionary, state as key and value
                    # as number of covid patients. Default is 0, increment it
                    # by 1.
                    state_covid_dict[state] = state_covid_dict.get(state, 0) + 1
                    # Total number of covid patients in each state.
                    total_covid_patients += 1

            if len(state_covid_dict) > 0:  # Dict at least one value.
                state_list = list(state_covid_dict.keys())  # Get all state's
                state_list.sort()  # Sort it by  state

                percentage_format_str = StatisticsFlowHandler.PERCENTAGE_FORMAT
                # Create list of list of a row ex: [["MA","1","10%"]]
                covid_count_list = [[state, str(state_covid_dict[state]),
                                     percentage_format_str.format(
                                         state_covid_dict[state] /
                                         total_covid_patients)]
                                    for state in state_list]
                # Print Main message about distribution
                print(StatisticsFlowHandler.STATE_COVID_MAIN_MESSAGE)
                # Print overview of statistics
                print(StatisticsFlowHandler.STATE_COVID_ADDITIONAL_MESSAGE
                      .format(total_covid_patients, len(state_list)))
                # Print the Covid and State distribution in tabular format.
                TableView.Table().print_table(
                    StatisticsFlowHandler.STATE_COVID_HEADER_ROWS,
                    covid_count_list)
            else:  # Size of Sate and Covid dictionary is zero, Nothing to show.
                print(StatisticsFlowHandler.ERROR_NO_DISTRIBUTION_COVID)
        else:  # Empty patient list nothing to show
            print(StatisticsFlowHandler.ERROR_NO_DISTRIBUTION_COVID)

    def __print_gender_distribution(self):
        """Prints statistics of gender distribution in tabular format"""
        # Get the patient list.
        patient_list = FileHandlerUtility().read_all_records_row_data()
        if len(patient_list) > 0:  # Patient list is not empty.
            # Print main header message before printing Table
            print(StatisticsFlowHandler.GENDER_DISTRIBUTION_MAIN_MESSAGE)
            # Male patient count
            male_count = len([pt for pt in patient_list if
                              pt.get_gender() == "Male"])

            # Fe-Male patient count
            female_count = len([pt for pt in patient_list if
                                pt.get_gender() == "Female"])

            # Other patient count
            other_count = len([pt for pt in patient_list if
                               pt.get_gender() == "Other"])

            # Total Gender count - sum all count.
            total_patients = male_count + female_count + other_count

            rows = list()  # List of rows having row data.
            male_percentage = male_count / total_patients
            # Create list of list for male row data.ex[["Male","10%"]]

            rows.append([AppConstants.GENDER_VALUE_MALE,
                         StatisticsFlowHandler.PERCENTAGE_FORMAT.format(
                             male_percentage)])
            # Create list of list for female row data.ex[["Female","10%"]]
            rows.append(
                [AppConstants.GENDER_VALUE_FEMALE,
                 StatisticsFlowHandler.PERCENTAGE_FORMAT.format(
                     female_count / total_patients)])

            # Create list of list for other row data.ex[["Other","30%"]]
            rows.append(
                [AppConstants.GENDER_VALUE_OTHER,
                 StatisticsFlowHandler.PERCENTAGE_FORMAT.format(
                     other_count / total_patients)])

            # Print the Gender and percentage distribution in tabular format.
            TableView.Table().print_table(
                StatisticsFlowHandler.GENDER_HEADER_ROWS, rows)
