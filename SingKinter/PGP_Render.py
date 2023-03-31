"""
A method that SingKinter classes use to draw the widgets and frames to the screen.
It checks that the class only has one render method assigned and then renders the wrapped
tkinter object with the chosen method and variables



widget = the wrapped tkinter object that needs to be rendered to the screen

packDict = the dictionary or variables associated with the pack method

gridDict = the dictionary or variables associated with the grid method

placeDict = the dictionary or variables associated with the place method

"""

import tkinter as tk


# todo add the less widely used pack parameters
packVariables = [
    'padx',
    'pady',
    'ipadx',
    'ipady',
    'anchor',
    'side',
    'fill',
    'expand',
]

# todo add the grid parameters
gridVariables = [

]

# todo add the place parameters
placeVariables = [

]


def PGP_Renderer(widget: object, packDict: dict, gridDict: dict, placeDict: dict)-> None:
    if packDict and gridDict or placeDict and gridDict or packDict and placeDict:
        raise Exception("Object has too many render methods")

    function_variables = ''
    method = ''

    if packDict:
        method = "pack"
        for key in packDict:
            if key in packVariables:
                function_variables += f'{key}={packDict[key]}, '
            else:
                raise Exception(f"{key} is not a parameter for {method} method")

    if gridDict:
        method = "grid"
        for key in gridDict:
            if key in gridVariables:
                function_variables += f'{key}={gridDict[key]}, '
            else:
                raise Exception(f"{key} is not a parameter for {method} method")

    if placeDict:
        method = "place"
        for key in placeDict:
            if key in placeVariables.keys():
                function_variables += f'{key}={placeDict[key]}, '
            else:
                raise Exception(f"{key} is not a parameter for {method} method")

    exec(f"widget.{method}({function_variables})")


