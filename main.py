from address_points import NJ_AP
from road_centerlines import NJ_RCL
import arcpy

arcpy.env.workspace = r'C:\Users\kcneinstedt\Downloads\CAD Output\AddressPoints_CAD.gdb'

nj_ap_layer = r'NJAddressPoints'
nj_rcl_layer = r'NJ_RCL_NOT_NULL'

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = input(f"Transform address point layer {nj_ap_layer}? Y/N: ")
    if a == "Y":
        nj_ap = NJ_AP(arcpy.env.workspace, nj_ap_layer)
        nj_ap.transform()

    a = input(f"Transform road centerline layer {nj_rcl_layer}? Y/N: ")
    if a == "Y":
        nj_rcl = NJ_RCL(arcpy.env.workspace, nj_rcl_layer)
        nj_rcl.transform()
