"""This script works for feature classes of variable number of fields. One at a time fields are queried for nulls.
If nulls are in the field, they are selected. If they are string fields, they are calculated to empty string.
If they are not string fields, this does not work and nulls remain."""


import arcpy as ap
from objects import *


ap.env.workspace = r"C:\Users\kcneinstedt\Downloads\MercerCo_export_Aug2_2024\MercerCo_export_20241010.gdb"

layer = "AddressPoints_CS"


def SQL_calc(sql_expression, feature_class, field_name, calculation, language="PYTHON3"):
    print(sql_expression)

    nulls = ap.SelectLayerByAttribute_management(feature_class,
                                                 selection_type='NEW_SELECTION',
                                                 where_clause=sql_expression
                                                 )

    ap.CalculateField_management(nulls, field_name, calculation, language)

def nulls_to_empty_string(feature_class):
    fields_index = {}
    i = 0
    for each in ap.ListFields(feature_class):
        fields_index[i] = (each.name, each.type)
        # This print has a use: it formats the index and field name into dictionary format for easy copy/paste.
        # Updating this file, you could copy+paste the standard output into the functions dict.
        print(f"{i}: {each.name}(), {each.type}")
        i += 1
    for each in fields_index:
        field_name = fields_index[each][0]
        sql_expression = f'{field_name} IS NULL'
        calculation = "''"

        try:
            SQL_calc(sql_expression, feature_class, fields_index[each][0], calculation)

        except Exception as e:
            print(f"Could not calculate {field_name} to be {calculation}")
            print(e)
            continue


if __name__ == '__main__':
    nulls_to_empty_string(layer)
