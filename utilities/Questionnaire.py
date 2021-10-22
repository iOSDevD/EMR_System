"""
Nikunj Upadhyay
Class: CS 521 - Fall 1
Date: 10/16/2021
Homework Problem # Project
Description of Problem (1-2 sentence summary in your own words):
"""
from model.Question import Question


class Questionnaire:
    """ Helps to generate questionnaire summary or result, answers string which
    can be saved in the csv as well prompt message for a question while user
    enters input.
    """

    __question_1 = Question("Did you had covid any time before your visit?",
                            ["Yes", "No"])
    __question_2 = Question("Do you have insurance on file?", ["Yes", "No"])
    __question_3 = Question("Do you want us to reach out to you via SMS or "
                            "E-mail for further appointments", ["Yes", "No"])

    __question_4 = Question("Do you have migraine or had earlier?",
                            ["Yes", "No"])

    # questionnaire_list = [__question_1, __question_2, __question_3,
    #                       __question_4]

    YES_ANSWER_SET = {"Y", "YES"}
    NO_ANSWER_SET = {"N", "NO"}

    def __init__(self):
        # Public attribute questionnaire list
        self.questionnaire_list = [Questionnaire.__question_1,
                                   Questionnaire.__question_2,
                                   Questionnaire.__question_3,
                                   Questionnaire.__question_4]

    def get_questionnaire_to_print(self, answers):
        """ Generates a string which represents the list of questions along
        with its options and answer. Used to display result of a questionnaire.

        :param answers: list of answer values 1 for Yes, 0 for No and -1 for
                Not answered or skipped.
        :return: string representing question, options and hint part
        """

        # Defaults to -1 i.e not answered for empty list, helps to show
        # question was not answered or skipped.
        if answers is None or len(answers) == 0:
            answers = self.__get_all_answers_as_skipped()

        options_dict = {0: "No", 1: "Yes", -1: "Not answered or skipped"}

        result_map = map(
            lambda question, answer: "{}\nAnswer: {}".format(question,
                                                             options_dict[
                                                                 answer]),
            self.questionnaire_list, answers)

        result_list = list(result_map)

        return "\n".join(result_list)

    def get_formatted_answers_to_save(self, answers):
        """ Generates a string which represents the answers and which case be
        saved to the csv file. ex: list [-1,0,1,1] will be converted to
        string value '[-1,0,1,1]'.

        :param answers: list of answer values 1 for Yes, 0 for No and -1 for
                Not answered or skipped.
        :return: string representation of array.
        """
        answers_str_list = [str(answer_id) for answer_id in answers]
        return "[{}]".format(",".join(answers_str_list))

    def get_question_str_for_prompt(self, question):
        """Generates a string representation of question, it's options and hint
        on what to enter of yes or no option. The message is used as a prompt,
        so that they can enter appropriate value for a answer.
        :param question: Question object for which representation has to be
                    created.
        :return: a string representing the question,it's option followed by
        small hint after it.

        """
        return str(question) + "\nPlease enter y for Yes or n " \
                               "for No and enter to skip"

    def get_default_questionnaire_answers(self):
        """For new patient since the intake form will not be answered all
        answers should have value skipped. It returns string value of
        answers [-1,-1,-1,-1]"""
        default_answers_list = self.__get_all_answers_as_skipped()
        return self.get_formatted_answers_to_save(default_answers_list)

    def __get_all_answers_as_skipped(self):
        """Returns Default answers list for the questionnaire as skipped."""
        return [-1] * len(self.questionnaire_list)


# Unit Tests
if __name__ == "__main__":
    print("Started Executing test case in Questionnaire")

    questionnaire = Questionnaire()

    # 1. Test Questionnaire String representing, question, options and answer
    # is as expected.
    questionnaire_print_test_str = questionnaire.get_questionnaire_to_print(
        [-1, 0, 1, 1])

    assert questionnaire_print_test_str.count("Answer: Not "
                                              "answered or skipped") == 1, \
        ("Occurrence of Not answered should be only"
         " 1 as there is only one '-1' entry in the list")

    # Replacing Not required, as it will be counted because `Answer: No`
    # matches initial part of 'Answer: Not answered'.
    questionnaire_print_test_str = \
        questionnaire_print_test_str.replace("Answer: Not answered "
                                             "or skipped", "")

    assert questionnaire_print_test_str.count("Answer: No") == 1, \
        ("Occurrence of No answered should be only"
         " 1 as there is only one '0' entry in the list")

    assert questionnaire_print_test_str.count("Answer: Yes") == 2, \
        ("Occurrence of Yes answered should be 2 as "
         "there are two entries of '1' in the list")

    # 2. Test Case to check answers list to string formatting is correct
    assert questionnaire.get_formatted_answers_to_save([-1, 0, 1, 1]) == \
           "[-1,0,1,1]", ("String representation of list should "
                          "match exact values in the list")

    # 3. Test case to check message being created for prompt is correct or not.
    input_question = Question("Question 1", ["Yes", "No"])
    assert questionnaire.get_question_str_for_prompt(input_question). \
        startswith(str(input_question)), ("Question-Option part "
                                          "of the prompt is missing.")

    # 4. Test case for default answers to save, which will have all answers
    # as skipped i.e -1
    assert questionnaire.get_default_questionnaire_answers() == \
           "[-1,-1,-1,-1]", ("Default answers to save should all have default "
                             "answer as skipped i.e -1")

    print("Success! Completed Executing test case in Questionnaire")
