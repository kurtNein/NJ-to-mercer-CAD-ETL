"""
This module is for helper functions which compute field values.
"""


import arcpy


arcpy.env.workspace = r"C:\Users\kcneinstedt\Downloads\MercerCo_export_Aug2_2024\MercerCo_export_20241010.gdb"

layer = "AddressPoints_CS"


def SQL_calc(sql_expression: str, feature_class: str, field_name: str, calculation: str, language="PYTHON3", code=None):
    arguments_string = f'Selecting {feature_class} WHERE {sql_expression}...'
    print(f'{arguments_string:-^128}')
    nulls = arcpy.SelectLayerByAttribute_management(feature_class,
                                                    selection_type='NEW_SELECTION',
                                                    where_clause=sql_expression
                                                    )
    rows_count = arcpy.management.GetCount(nulls)
    perform_calc = input(f"Selected {rows_count} rows\n{field_name} calculation:\n{calculation}\nEdit {field_name}? Y/N: ")
    if perform_calc == "Y":
        arcpy.CalculateField_management(nulls, field_name, calculation, language, code)
        print(f"Edited {rows_count} rows")
    else:
        print(f"Aborted editing {field_name} field\n")

def nulls_to_empty_string(feature_class: str, excluded_fields=None) -> None:
    if excluded_fields is None:
        excluded_fields = []
    fields_index = {}
    i = 0
    for each in arcpy.ListFields(feature_class):
        fields_index[i] = (each.name, each.type)
        # This print has a use: it formats the index and field name into dictionary format for easy copy/paste.
        # Updating this file, you could copy+paste the standard output into the functions dict.
        print(f"{i}: {each.name}(), {each.type}")
        i += 1
    for each in fields_index:
        field_name = fields_index[each][0]
        if field_name in excluded_fields:
            continue
        sql_expression = f'{field_name} IS NULL'
        calculation = "''"

        try:
            SQL_calc(sql_expression, feature_class, fields_index[each][0], calculation)

        except Exception as e:
            print(f"Could not calculate {field_name} to be {calculation}")
            print(e)
            continue


if __name__ == '__main__':
    print("This file to be used as an imported module only. Did you mean to run main?")
