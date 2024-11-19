from address_points import NJ_AP
import arcpy

arcpy.env.workspace = r'C:\Users\kcneinstedt\Downloads\CAD Output\AddressPoints_CAD.gdb'

nj_ap_layer = r'NJAddressPoints'

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nj_ap = NJ_AP(arcpy.env.workspace, nj_ap_layer)
    nj_ap.transform()