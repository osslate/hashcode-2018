# imports
import sys

# data import/export (fionn)
def parse_data(filename):
    with open(filename, "r") as f:
        file_rows = [line.rstrip("\n") for line in f]

        attributes = file_rows[0].split(" ")

        num_rows = attributes[0]
        num_cols = attributes[1]
        ing_per_slice = attributes[2]
        cells_per_slice = attributes[3]
        rows = file_rows[1:]

        return {
            "num_rows": num_rows,
            "num_cols": num_cols,
            "ing_per_slice": ing_per_slice,
            "cells_per_slice": cells_per_slice,
            "rows": rows
        }

# slide area, etc (jack)

# can be used (alex)

# scoring (bradley)

# RUN FILE

data = parse_data("example.in")
