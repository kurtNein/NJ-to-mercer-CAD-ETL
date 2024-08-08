import arcpy

def select_nulls_and_calculate(feature_class, field):
    #Goal is to find which fields are null, select those, and do a calculation on them
    for field in arcpy.ListFields(feature_class):
        #Selects certain features out of the entire feature class based on a WHERE clause
        #Logic that changes which features would pass the filter goes in the WHERE clause, blank clause selects all
        arcpy.SelectLayerByAttribute_management(feature_class,
                                                selection_type='NEW_SELECTION',
                                                where_clause=rf'')

        #If SelectLayerByAttribute was called on feature class, calling CalculateField will calculate that selection.
        #All logic to determine what value those selected fields receive has to go in the code_block attribute.
        #There are multiple options for expression type e.g. 'PYTHON3', 'SQL', 'ARCADE', see documentation on this func
        arcpy.CalculateField_management(feature_class,
                                        field=field,
                                        expression=None,
                                        expression_type='',
                                        code_block=''
                                        )

if __name__ == '__main__':
    select_nulls_and_calculate(r'full path to feature class', 'field')





"""eventually, to run on every field,

for field in arcpy.ListFields(feature_class):
    select_nulls_and_calculate(feature_class, field)


and even more eventually to-do, run on every field, but the calculation for each field is unique to the field
"""