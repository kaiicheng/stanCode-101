"""
File: draw_line
Name: Kai Cheng
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the pen stroke
SIZE = 10
window = GWindow()
obj = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw1)


def draw1(m):
    obj.x = m.x   # Get the x and y coordinates of the first point.
    obj.y = m.y
    obj.filled = True
    obj.color = "black"
    obj.fill_color = "white"
    onmouseclicked(draw2)
    window.add(obj, obj.x - obj.width / 2, obj.y - obj.height / 2)


def draw2(n):
    obj2 = GOval(SIZE, SIZE)   # Get the x and y coordinates of the second point.
    obj2.x = n.x
    obj2.y = n.y

    line = GLine(obj.x, obj.y, n.x, n.y)   # Draw a line.
    line.filled = True
    line.fill_color = "black"
    window.add(line)
    window.remove(obj)

    onmouseclicked(draw1)   # Go back to the beginning phase.


if __name__ == "__main__":
    main()
