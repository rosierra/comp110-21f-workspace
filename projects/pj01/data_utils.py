"""Utility functions."""

__author__ = "730365963"

# Define your functions below
from csv import DictReader


def read_csv_rows(DATA_FILE_PATH: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(DATA_FILE_PATH, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result 


def column_values(data_rows: list[dict[str, str]], combined: str) -> list[str]:
    """Produce a list of values in a single column."""
    subject_age: list[str] = []
    for row in data_rows:
        item: str = row[combined]
        subject_age.append(item)
    return subject_age


def columnar(data_cols: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    new_table: dict[str, list[str]] = {}
    first_row: dict[str, str] = data_cols[0]
    for column in first_row:
        new_table[column] = column_values(data_cols, column)
    return new_table


def head(data_cols: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produce a column-based table with only a certain number of rows of data per column."""
    returning: dict[str, list[str]] = {}
    for key in data_cols:
        minimize: list[str] = []
        for n in range(rows):
            minimize.append(data_cols[key][n])
            if rows >= len(data_cols):
                return data_cols
        returning[key] = minimize
    return returning


def select(data_cols: dict[str, list[str]], copy: list[str]) -> dict[str, list[str]]:
    """Produce a column-based table with only a specific subset of the original columns."""
    data_column: dict[str, list[str]] = {}
    for key in copy:
        data_column[key] = data_cols[key]
    return data_column 


def concat(data_cols_head: dict[str, list[str]], additional_table: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a column-based table with two column-based tables combined."""
    combined: dict[str, list[str]] = {}
    for key in data_cols_head:
        combined[key] = data_cols_head[key]
    for key in additional_table:
        if key in combined:
            combined[key] = additional_table[key] 
    return combined 


def count(selected_data: list[str]) -> dict[str, int]:
    """Counts the number of times a value appears in the input list."""
    counted: dict[str, int] = {}
    for item in selected_data: 
        if item in counted:
            counted[item] += 1
        else:
            counted[item] = 1
    return counted
