import arcpy
arcpy.SearchCursor()


def multiply_2(*args):
    # Use a breakpoint in the code line below to debug your script.
    list = []
    for each in args:
        list.append(each*2)
    return list


def print_bye(*args):
    return f"Hi, {args}"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list = [1, 2, 3]
    lists = [each for each in list]
    multiply_2(*lists)
