"""
Nikunj Upadhyay
Class: CS 521 - Fall 1
Date: 10/16/2021
Homework Problem # Project
Description of Problem (1-2 sentence summary in your own words):

Question Object represents Question and options object/
"""


class Question:
    """Question class which represents question and options to be displayed
    to the user. String representation can be used to display the message
    appropriately"""

    def __init__(self, question_str, options_list):
        self.__question = question_str
        self.__options = options_list

    def __str__(self):
        options_formatted_list = ["({}). {}".format(e + 1, v) for (e, v)
                                  in enumerate(self.__options)]
        options_str = "\n".join(options_formatted_list)
        return "{}\n{}".format(self.__question, options_str)


# Unit Test for Question object
if __name__ == "__main__":
    print("Started Executing test case in Question")

    # Question object under test
    question = Question("Question1", ["Yes", "No"])

    # expected string representation of Question
    expected_question = "Question1\n(1). Yes\n(2). No"

    # Test case should work fine.
    assert str(question) == expected_question, (
        "String representation should match expected result")

    print("Success! Completed Executing test case in Question")
