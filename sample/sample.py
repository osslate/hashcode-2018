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
def is_valid_slice(sliceSizeData,formalSliceData,ruleData,ingData, numSlice):
    bucket = []
    # checking ingredients in the slice row
    for iSlice in (0, numSlice):
        for ingredient in sliceSizeData[iSlice]:
            countT = 0
            countM = 0
            if ingredient == 'T':
                countT+= 1
            elif ingredient == 'M':
                countM += 1
        x = ruleData['ing_per_slice']
        if countT >= x and countM >= x:
            bucket.append([formalSliceData])
    print('this is here so the outlin of this function dose not break everything')
    return bucket

# scoring (bradley)

# RUN FILE

data = parse_data("example.in")
