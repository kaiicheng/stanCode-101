"""
File: Bouncing ball
Name: Kai Cheng
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
start = False
window = GWindow(800, 500, title='bouncing_ball')


def main():
    """
    This program is to create a bouncing ball game as requested.
    Once user clicks mouse, the game starts.
    After bouncing out of the border for three times, the game is over.
    """
    # Create a white background.
    cover = GRect(800, 500)
    cover.color = "white"
    cover.fill_color = "white"
    cover.filled = True
    window.add(cover)

    # Create a timer to check times of ball bouncing out of the border.
    timer = 0
    global GRAVITY
    global start

    # Create a ball.
    oval = GOval(SIZE, SIZE)
    oval.filled = True
    oval.fill_color = "black"
    oval.color = "black"
    window.add(oval, START_X, START_Y)

    while True:
        # Click mouse once to change start into True.
        onmouseclicked(switch)
        if start:
            gravity = GRAVITY
            while True:
                oval.move(VX, gravity)
                if oval.y >= window.height:
                    gravity = gravity * REDUCE
                    gravity = -gravity
                if oval.x >= window.width:
                    oval.x = START_X
                    oval.y = START_Y
                    # Change start into False.
                    start = False
                    timer += 1
                    break
                gravity = gravity + 1
                pause(DELAY)
        pause(DELAY)

        # If timer is equal or bigger than 3, break the while loop/
        if timer >= 3:
            break


def switch(event):
    global start
    start = True


if __name__ == "__main__":
    main()
