import arcpy as ap
import regex as re
from objects import *

path = r"C:\Users\kcneinstedt\OneDrive - mercercounty.org\Documents\FME\Workspaces\NG911\NJ_NG911_2023_12_26.gdb\DATA" \
       r"\RoadCenterlines"


functions = {0: Bool0(),
             1: Bool1()
             }


def field_check_template(cursor):
    iterations = 0
    for row in cursor:
        i = 0
        while i < 2:
            try:
                #print(i)
                function = functions[i]
                print(function(row[i]))
                i += 1

            except KeyError as e:
                #print(e)
                continue
        iterations += 1
        continue
    print(iterations)


def search_cursor(feature_class: str):
    fields_index = {}
    i = 0
    for each in ap.ListFields(feature_class):
        fields_index[i] = each.name
        i += 1
    for each in fields_index:
        print(each, fields_index[each])

    with ap.da.SearchCursor(feature_class, "*") as cursor:
        field_check_template(cursor)


search_cursor(path)
