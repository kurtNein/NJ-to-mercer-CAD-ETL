"""Class definitions of small objects go here to be imported."""


class Bool0:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print("0 true")
        return bool(*args)


class Bool1:
    def __init__(self):
        pass

    def __call__(self, value, **kwargs):
        print("1 true")
        self.right_type = int(value) == value


def is_correct_type(value, desired_type: type) -> bool:
    return type(value) == desired_type


class FieldCheck:
    def __init__(self):
        self.desired_type = str
        self.allow_null = False

    def is_null(self, value) -> bool:
        return type(value) == type(None)

    def __call__(self, value):
        print(is_correct_type(value, self.desired_type))
        print(type(value))
        print("checked type")
        print(self.allow_null == self.is_null(value))
        print("checked null")
        return is_correct_type(value, self.desired_type)


class ExternalStreetKey(FieldCheck):
    def __init__(self):
        super().__init__()


class Shape(FieldCheck):
    def __init__(self):
        super().__init__()
        self.desired_type = tuple


class StreetName(FieldCheck):
    def __init__(self):
        super().__init__()
        self.desired_type = str


class LeftFromAddress(FieldCheck):
    def __init__(self):
        super().__init__()
        self.desired_type = int


class LeftToAddress(FieldCheck):
    def __init__(self):
        super().__init__()
        self.desired_type = int


class RightFromAddress(FieldCheck):
    def __init__(self):
        super().__init__()
        self.desired_type = int


class RightToAddress(FieldCheck):
    def __init__(self):
        super().__init__()
        self.desired_type = int


class LeftParity(FieldCheck):
    def __init__(self):
        super().__init__()
        self.desired_type = str


class RightParity(FieldCheck):
    def __init__(self):
        super().__init__()
        self.desired_type = str


class LeftCityCode(FieldCheck):
    def __init__(self):
        super().__init__()
        self.desired_type = str


class RightCityCode(FieldCheck):
    def __init__(self):
        super().__init__()
        self.desired_type = str


class LeftCountyCode(FieldCheck):
    def __init__(self):
        super().__init__()
        self.desired_type = str


class RightCountyCode(FieldCheck):
    def __init__(self):
        super().__init__()
        self.desired_type = str


class LeftState(FieldCheck):
    def __init__(self):
        super().__init__()
        self.desired_type = str


class RightState(FieldCheck):
    def __init__(self):
        super().__init__()
        self.desired_type = str


class FeatureTypeCode(FieldCheck):
    def __init__(self):
        super().__init__()
        self.desired_type = str


class SpeedLimit(FieldCheck):
    def __init__(self):
        super().__init__()
        self.desired_type = int


class LeftZipCode(FieldCheck):
    def __init__(self):
        super().__init__()
        self.desired_type = str


class RightZipCode(FieldCheck):
    def __init__(self):
        super().__init__()
        self.desired_type = str


class OneWayCode(FieldCheck):
    def __init__(self):
        super().__init__()
        self.desired_type = str


class ToElevation(FieldCheck):
    def __init__(self):
        super().__init__()
        self.desired_type = int


class FromElevation(FieldCheck):
    def __init__(self):
        super().__init__()
        self.desired_type = int


class LocationName(FieldCheck):
    def __init__(self):
        super().__init__()
        self.desired_type = str


class RoutingStreetExternalKey(FieldCheck):
    def __init__(self):
        super().__init__()
        self.desired_type = str


class LeftZipCod(FieldCheck):
    def __init__(self):
        super().__init__()
        self.desired_type = str

    def __call__(self, *args, **kwargs):
        import arcpy
        zip_code_layer = r"C:\Users\kcneinstedt\Downloads\CAD Output\RCL_CAD.gdb\Bucks_Zip_Codes"
        rcl_layer = r"C:\Users\kcneinstedt\Downloads\CAD Output\RCL_CAD.gdb\RCL_CAD_Dataset\Bucks_RCL_NJStatePlane"
        with arcpy.da.SearchCursor(zip_code_layer, ['SHAPE@', 'ZIP_CODE']) as cursor:
            for row in cursor:
                rcl_blank = arcpy.SelectLayerByAttribute_management(rcl_layer, 'NEW_SELECTION', "RightZipCo=''")
                zip_shape = row[0]
                zip_code = row[1]
                print(zip_code)
                rcl_to_edit = arcpy.SelectLayerByLocation_management(rcl_blank, 'INTERSECT', zip_shape, 'feet', 'SUBSET_SELECTION')
                print(arcpy.management.GetCount(rcl_to_edit))
                with arcpy.da.UpdateCursor(rcl_to_edit, ['RightZipCo']) as update_cursor:
                    for each in update_cursor:
                        each[0] = zip_code
                        update_cursor.updateRow(each)
                        print(f'RCL LeftZipCod updated to {zip_code}')