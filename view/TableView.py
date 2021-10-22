"""
Nikunj Upadhyay
Class: CS 521 - Fall 1
Date: 10/16/2021
Homework Problem # Project
Description of Problem (1-2 sentence summary in your own words):

The program acts as view to show data in Tabular format.
MACRON character are added below the header to show a separation
between header and rows. Max character column size is 20, for
characters more than 20 it will show ellipsis at the end.

"""


class Table:
    """Table which helps to present data in tabular format on to the console.
    """

    # Column Format with column width as 20 and center aligned.
    COLUMN_FORMAT = "{:^20}"

    # Special underscore like character "_" which appears
    # below the text and acts like a separator.
    COMBINING_MACRON_BELOW = "\u0331"

    def print_table(self, headers, rows):
        """Prints the provided header list as column header and rows
        representing list of each individual row (as list)."""

        # Create string column format, which will be replaced with
        # header values using variable args. For two column header it would
        # be "{:^20}{:^20}"
        table_layout_format = Table.COLUMN_FORMAT * len(headers)

        # Prepare list of formatted header strings with COMBINING_MACRON_BELOW
        # ex:  ̱ ̱ ̱ ̱ ̱P̱a̱ṯi̱e̱ṉṯ ̱I̱ḏ ̱ ̱ ̱ ̱
        headers_with_macron = [
            Table.COMBINING_MACRON_BELOW.join(Table.COLUMN_FORMAT.format(e)) for
            e in
            headers]

        # Print with the help of layout format and set the values from the list.
        print(table_layout_format.format(*headers_with_macron))

        for row in rows:  # Start working on rows.
            formatted_row = []  # List for formatting ex: More than 20 chars.

            # Prepare row list to be set as variable args to the column format.
            for e in row:   # Iterate, each row data as it's a list
                if len(e) > 20:  # Show ellipsis if more than 20 characters.
                    # slice to show few characters with ellipsis
                    e = e[0:15] + "..."
                formatted_row.append(e)

            # Use the precalculated layout format, just like headers and print.
            print(table_layout_format.format(*formatted_row))
