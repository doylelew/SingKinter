"""
A method that SingKinter classes use to draw the widgets and frames to the screen.
It checks that the class only has one render method assigned and then renders the wrapped
tkinter object with the chosen method and variables



widget = the wrapped tkinter object that needs to be rendered to the screen

packDict = the dictionary or variables associated with the pack method

gridDict = the dictionary or variables associated with the grid method

placeDict = the dictionary or variables associated with the place method

"""


def PGP_Renderer(widget, packDict,gridDict, placeDict):
    if packDict and gridDict or placeDict and gridDict or packDict and placeDict:
        raise Exception("Object has too many render methods")




