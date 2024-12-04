"""
This file is uses classes from objects.py to apply a class-specific transformation on fields inside an UpdateCursor.
This is from a previous programming paradigm which has since changed, and this file is deprecated.
"""

import arcpy as ap
import regex as re
from objects import *

# This is the dataset taken as input.
path = r"C:\Users\kcneinstedt\OneDrive - mercercounty.org\Documents\FME\Workspaces\NG911\NJ_NG911_2023_12_26.gdb\DATA" \
       r"\RoadCenterlines"

# This functions dict will match field indexes with the right function to assess that field.
# Dict key is the int of the index the field is found in during arcpy.ListFields()
# Dict value is a tuple of the correct function to check the field, and a string of the desired data type.
# Rewiring of the field index to the right function should all occur within this dict.
functions = {0: (Bool0(), 'OID'),
             1: (Bool1(), 'Integer'),
             2: (ExternalStreetKey(), 'String'),
             69: (Shape(), 'String')
             }


def field_check_template(row):
    # Readjusted this function to take row as arg, so that it can return and make a correction before next the row.
    # Takes the row object iterated through by a cursor from SearchCursor() or UpdateCursor()
    # This function should always be preceded by a SearchCursor() or UpdateCursor() initialization.
    # for row in cursor:
    i = 0
    while i < 70:
        try:
            # print(i)
            function = functions[i][0]
            print(function(row[i]))

        except KeyError as e:
            print(e)

        finally:
            i += 1


def search_cursor(feature_class: str):
    fields_index = {}
    i = 0
    print("{")
    for each in ap.ListFields(feature_class):
        fields_index[i] = (each.name, each.type)
        # This print has a use: it formats the index and field name into dictionary format for easy copy/paste.
        # Updating this file, you could copy+paste the standard output into the functions dict.
        print(f"{i}: {each.name}(),")
        i += 1
    print("}")
    for each in fields_index:
        fields_wrong_type = []
        # The following try-except block is to assess the data type of each field once, rather than once for every row.
        try:
            actual_type = fields_index[each][1]
            desired_type = functions[each][1]
            print(each, actual_type, desired_type)

            if actual_type != desired_type:
                fields_wrong_type.append(f"Field at index {each} is {actual_type} but should be {desired_type}")

        except Exception as e:
            print(e)

        finally:
            for field in fields_wrong_type:
                print(field)

    with ap.da.SearchCursor(feature_class, "*") as cursor:
        for row in cursor:
            field_check_template(row)


search_cursor(path)
