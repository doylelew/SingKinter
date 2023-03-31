# SingKinter
Tkinter wrapper with a single call paradigm for creating GUI elements and frames

## Widgets

SingKinter widgets just wrap regular tkinter widgets and allow you to pass in one of the three geometry methods (pack, grid, place) right there upon creation of the widget instead of elsewhere in your code.

The SingWidget class takes 2 parameters the first which is just a tkinter widget and the second that is a dictionary of geometry parameters set equal to the geometry type you would like tkinter to use to display the widget to the frame

The widget will not accept more than one geometry type in its constructor

```python
import SingKinter as sk

sk.SingWidgets(widget=tk.Label(root, text="Hello, World!", font=('courier', 25)),
                           pack={'padx': 20, 'pady': 20, 'side': 'tk.TOP', 'expand': True})

```
The geometry method can later be changed or updated as well as the actual widget that is wrapped allowing you to change the position of a widget on the screen on the fly or switch out a completely new tkinter widget into the same space.

(Code example to come once this is an implemented feature)

