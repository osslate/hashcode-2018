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
def slice_area(d):
    rows = d['num_rows']
    cols = d['num_cols']
    maxSlice = d['cells_per_slice']

    sizeOfPizza = rows * cols
    numOfBigSlices = sizeOfPizza / maxSlice

    print(numOfBigSlices)


# can be used (alex)
def is_valid_slice(sliceSizeData,ruleData,ingData):
    # checking ingredients in the slice row
    print('this is here so the outlin of this function dose not break everything')

# scoring (bradley)

# RUN FILE

data = parse_data("example.in")
