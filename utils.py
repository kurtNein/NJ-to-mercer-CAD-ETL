import arcpy as ap
import regex as re
from objects import *

path = r"C:\Users\kcneinstedt\OneDrive - mercercounty.org\Documents\FME\Workspaces\NG911\NJ_NG911_2023_12_26.gdb\DATA" \
       r"\RoadCenterlines"


functions = {0: (Bool0(), 'OID'),
             1: (Bool1(), 'Integer'),
             2: (ExternalStreetKey(), 'String'),
             69: (Shape(), 'String')
             }


def field_check_template(cursor):
    iterations = 0
    for row in cursor:
        i = 0
        while i < 70:
            try:
                #print(i)
                function = functions[i][0]
                print(function(row[i]))

            except KeyError as e:
                print(e)

            finally:
                i += 1

        iterations += 1
        continue

    print(iterations)


def search_cursor(feature_class: str):
    fields_index = {}
    i = 0
    for each in ap.ListFields(feature_class):
        fields_index[i] = (each.name, each.type)
        i += 1
    for each in fields_index:
        fields_wrong_type = []
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
        field_check_template(cursor)


search_cursor(path)
