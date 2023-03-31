"""
A container class that takes as an argument any regular tkinter widget
as well as the method you would like it rendered to the screen.

You specify how you want it rendered to the screen by choosing pack, grid, or place
and setting it equal to a dictionary of regular tkinter variable for that respective
method. If you choose more than one you will receive an error

widget = any tkinter widget you would normally use

pack = tkinter pack method, submit a dictionary of pack method variables

grid = tkinter grid method, submit a dictionary of pack method variables

place = tkinter place method, submit a dictionary of pack method variables

"""

__all__ = [
    'SingWidgets',
]

from .PGP_Render import PGP_Renderer


class SingWidgets:
    def __init__(self, widget: object = None, pack: dict = {}, grid: dict = {}, place: dict = {}) -> object:
        if widget is None:
            raise Exception("Please specify a tkinter widget when creating a SingKinter widget")

        self.widget = widget
        self.pack = pack
        self.grid = grid
        self.place = place

    def render(self):
        PGP_Renderer(self.widget, self.pack, self.grid, self.place)

# todo allow the ability to change the method of render

# todo allow the ability to change the wrapped widget

