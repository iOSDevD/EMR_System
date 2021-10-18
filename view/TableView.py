"""
Nikunj Upadhyay
Class: CS 521 - Fall 1
Date: 10/16/2021
Homework Problem # Project
Description of Problem (1-2 sentence summary in your own words):
"""


class Table:
    # Column Format with column width as 20 and center aligned.
    COLUMN_FORMAT = "{:^20}"

    COMBINING_MACRON_BELOW = "\u0331"

    def printTable(headers, rows):
        table_layout_format = Table.COLUMN_FORMAT * len(headers)
        headers_with_macron = [
            Table.COMBINING_MACRON_BELOW.join(Table.COLUMN_FORMAT.format(e)) for e in
            headers]
        print(table_layout_format.format(*headers_with_macron))

        for row in rows:
            formatted_row = []
            for e in row:
                if len(e) > 20:  # Show ellipsis if more than 20 characters.
                    # slice to show few characters with ellipsis
                    e = e[0:15] + "..."
                formatted_row.append(e)

            print(table_layout_format.format(*formatted_row))
