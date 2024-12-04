from null_sweep import SQL_calc, nulls_to_empty_string


class NJ_AP():
    """
    Class inside which all action on the New Jersey Address Point data happens.
    """
    def __init__(self, workspace, layer):
        self.workspace = workspace
        self.layer = layer

    def transform(self) -> None:
        """
        Method inside which all field calculations happen. Maintain one field at a time for readability.
        """
        try:
            SQL_calc(f'StreetName IS NULL', self.layer, 'StreetName', "''")
            SQL_calc(f'Address IS NULL', self.layer, 'Address', 0)
            SQL_calc(f'ZipCode IS NULL', self.layer, 'ZipCode', calculation='First(Intersects($feature, FeatureSetByName($datastore,"Census_ZIP_Code"))).ZCTA5', language='ARCADE')
        except Exception as e:
            print(e)
        finally:
            nulls_to_empty_string(self.layer)

class BC_AP():
    """
    Class inside which all action on the Bucks County Address Point data happens.
    """
    def __init__(self, workspace, layer):
        self.workspace = workspace
        self.layer = layer

    def transform(self) -> None:
        """
        Method inside which all field calculations happen on Bucks. Maintain one field at a time for readability.
        """
        try:
            SQL_calc(f'ExternalKey IS NULL', self.layer, 'StreetName', "''")
            SQL_calc(f'ZipCode IS NULL', self.layer, 'ZipCode', calculation='First(Intersects($feature, FeatureSetByName($datastore,"Census_ZIP_Code"))).ZCTA5', language='ARCADE')
        except Exception as e:
            print(e)
        finally:
            nulls_to_empty_string(self.layer)


if __name__ == '__main__':
    print("This file to be used as an imported module only. Did you mean to run main?")
