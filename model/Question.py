"""
Nikunj Upadhyay
Class: CS 521 - Fall 1
Date: 10/16/2021
Homework Problem # Project
Description of Problem (1-2 sentence summary in your own words):

Question Object that represents Question and options object. The string
representation is as follows. For example:
'Is this the question 1?
(a) Option 1
(b) Option 2
'
"""


class Question:
    """Question class which represents question and options to be displayed
    to the user. String representation can be used to display the message
    appropriately."""

    def __init__(self, question_str, options_list):
        """Initialize question object with a question string and list of
        string options."""
        self.__question = question_str  # Private variable for question
        self.__options = options_list  # Private variable for options list

    def __str__(self):
        """Use magic method to print the Question formatted to show question
        and option with index using enumeration."""
        # Format options ex: (1). Option A
        options_formatted_list = ["({}). {}".format(e + 1, v) for (e, v)
                                  in enumerate(self.__options)]
        # Join all options with new line to show them on separate lines.
        options_str = "\n".join(options_formatted_list)
        return "{}\n{}".format(self.__question, options_str)


# Unit Test for Question object
if __name__ == "__main__":
    print("Started Executing test case in Question")

    # Question object under test
    question = Question("Question1", ["Yes", "No"])

    # expected string representation of Question
    expected_question_str = "Question1\n(1). Yes\n(2). No"

    # Test case should work fine.
    assert str(question) == expected_question_str, (
        "String representation should match expected result")

    print("Success! Completed Executing test case in Question")
