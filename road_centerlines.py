import arcpy
from null_sweep import SQL_calc, nulls_to_empty_string

# Function must be passed as string because arcpy.CalculateField needs the expression and the code block as strings.
uuid_expression = """def ID():
  import uuid
  return str(uuid.uuid4())
"""

class NJ_RCL():
    # Class inside which all action on the New Jersey Address Point data happens.
    def __init__(self, workspace, layer):
        self.workspace = workspace
        self.layer = layer

    def transform(self) -> None:
        # Method inside which all field calculations happen. Maintain one field at a time for readability.
        try:
            arcpy.CalculateField_management(self.layer, "StreetName", 'Proper($feature.StreetName)','ARCADE')
            SQL_calc(f'ExternalSt IS NULL', self.layer, 'ExternalSt', 'ID()', language='PYTHON3', code=uuid_expression)
            SQL_calc(f'StreetName IS NULL', self.layer, 'StreetName', "''")
            SQL_calc(f'LeftFromAd IS NULL OR LeftFromAd < 0', self.layer, 'LeftFromAd', 0) # Get node at [0], get LeftToAddr from intersecting line feature?
            SQL_calc(f'LeftToAddr IS NULL OR LeftToAddr < 0', self.layer, "LeftToAddr", 0) # Get node at [-1], get LeftFromAd?
            SQL_calc(f'RightFromA IS NULL OR RightFromA < 0', self.layer, "RightFromA", 0)
            SQL_calc(f'RightToAdd IS NULL OR RightToAdd < 0', self.layer, "RightToAdd", 0)
            SQL_calc(f'LeftCityCo IS NULL', self.layer, "LeftCityCo", 0)
            SQL_calc(f'RightCityC IS NULL', self.layer, "RightCityC", 0)
            SQL_calc(f'LeftZipCod IS NULL', self.layer, "LeftZipCod", 'First(Intersects($feature, FeatureSetByName($datastore,"Census_ZIP_Code"))).ZCTA5', language='ARCADE')
            SQL_calc(f'RightZipCo IS NULL', self.layer, "RightZipCo", 'First(Intersects($feature, FeatureSetByName($datastore,"Census_ZIP_Code"))).ZCTA5', language='ARCADE')
            SQL_calc(f'OneWayCode IS NULL', self.layer, "OneWayCode", "B")
            SQL_calc(f'FromElevat IS NULL', self.layer, "FromElevat", 0)
            SQL_calc(f'ToElevatio IS NULL', self.layer, "ToElevatio", 0)
            SQL_calc(f'FromElevat IS NULL', self.layer, "FromElevat", 0)
            SQL_calc(f'FromElevat IS NULL', self.layer, "FromElevat", 0)
            SQL_calc(f'LocationNa IS NULL', self.layer, "LocationNa", "")

        except Exception as e:
            print(e)

        finally:
            nulls_to_empty_string(self.layer, ['OBJECTID', 'StreetID'])

class BC_RCL():
    # Class inside which all action on the Bucks County Address Point data happens.
    def __init__(self, workspace, layer):
        self.workspace = workspace
        self.layer = layer

    def transform(self):
        # Method inside which all field calculations happen on Bucks. Maintain one field at a time for readability.
        try:
            SQL_calc(f'ExternalKey IS NULL', self.layer, 'StreetName', "''")
            SQL_calc(f'ZipCode IS NULL', self.layer, 'ZipCode', calculation='First(Intersects($feature, FeatureSetByName($datastore,"Census_ZIP_Code"))).ZCTA5', language='ARCADE')
        except Exception as e:
            print(e)
        finally:
            nulls_to_empty_string(self.layer)

