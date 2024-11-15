import arcpy
from null_sweep import SQL_calc, nulls_to_empty_string


class NJ_RCL():
    # Class inside which all action on the New Jersey Address Point data happens.
    def __init__(self, workspace, layer):
        self.workspace = workspace
        self.layer = layer

    def transform(self):
        # Method inside which all field calculations happen. Maintain one field at a time for readability.
        try:
            arcpy.CheckGeometry_management(self.layer, r'result_outputs/NJ_RCL_check_geometry')
            SQL_calc(f'StreetName IS NULL', self.layer, 'StreetName', "''")
            SQL_calc(f'LeftFromAd IS NULL OR LeftFromAd < 0', self.layer, 'LeftFromAd', 0) # Get node at [0], get LeftToAddr from intersecting line feature?
            SQL_calc(f'LeftToAddr IS NULL OR LeftToAddr < 0', self.layer, "LeftToAddr", 0) # Get node at [-1], get LeftFromAd?
            SQL_calc(f'RightFromA IS NULL OR RightFromA < 0', self.layer, "RightFromA", 0)
            SQL_calc(f'RightToAdd IS NULL OR RightToAdd < 0', self.layer, "RightToAdd", 0)
            SQL_calc(f'LeftCityCo IS NULL', self.layer, "LeftCityCo", 0)
            SQL_calc(f'RightCityC IS NULL', self.layer, "RightCityC", 0)
            SQL_calc(f'OneWayCode IS NULL OR OneWayCode = ""', self.layer, "OneWayCode", "B")
            SQL_calc(f'FromElevat IS NULL', self.layer, "FromElevat", 0)
            SQL_calc(f'ToElevatio IS NULL', self.layer, "ToElevatio", 0)
            SQL_calc(f'FromElevat IS NULL', self.layer, "FromElevat", 0)
            SQL_calc(f'FromElevat IS NULL', self.layer, "FromElevat", 0)
            SQL_calc(f'LocationNa IS NULL', self.layer, "LocationNa", "")

            SQL_calc(f'ZipCode IS NULL', self.layer, 'ZipCode', calculation='First(Intersects($feature, FeatureSetByName($datastore,"Census_ZIP_Code"))).ZCTA5', language='ARCADE')
        except Exception as e:
            print(e)
        finally:
            nulls_to_empty_string(self.layer)

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

