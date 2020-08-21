"""
File: my_drawing
Name: Kai Cheng
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GArc
from campy.graphics.gwindow import GWindow


def main():
    """
    This program is to create a drawing of Pokemon first generation.
    Last Saturday I went to Adidas with Alan, and spotted their new Pokemon pixel t-shirt.
    I decided to create a drawing of Pokemon, because I'm poor and have no money to purchase the t-shirt.
    Therefore, I like to paint a drawing which is full of my favorite cartoon in my childhood.
    """

    window = GWindow(width=700, height=400, title="Pokemon")

    # Create a white background.
    cover = GRect(700, 400)
    cover.color = "white"
    cover.fill_color = "white"
    cover.filled = True
    window.add(cover)

    # Draw pixels to create Bulbasaur.
    # Column 1
    b = GRect(5, 5, x=150, y=220)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=150, y=225)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=150, y=230)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b4 = GRect(5, 5, x=150, y=235)
    b4.filled = True
    b4.fill_color = "lightgreen"
    window.add(b4)

    b4 = GRect(5, 5, x=150, y=240)
    b4.filled = True
    b4.fill_color = "limegreen"
    window.add(b4)

    bb = GRect(5, 5, x=150, y=245)
    bb.filled = True
    bb.fill_color = "black"
    window.add(bb)

    # Column 2

    b = GRect(5, 5, x=155, y=205)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=155, y=210)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=155, y=215)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=155, y=220)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=155, y=225)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=155, y=230)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=155, y=235)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=155, y=240)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=155, y=245)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=155, y=250)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    # Column 3

    b = GRect(5, 5, x=160, y=200)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=160, y=205)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=160, y=210)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=160, y=215)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=160, y=220)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=160, y=225)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=160, y=230)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=160, y=235)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=160, y=240)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=160, y=245)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=160, y=250)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    # Column 4

    b = GRect(5, 5, x=165, y=205)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=165, y=210)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=165, y=215)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=165, y=220)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=165, y=225)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=165, y=230)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=165, y=235)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=165, y=240)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=165, y=245)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=165, y=250)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=165, y=255)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    # Column 5

    b = GRect(5, 5, x=170, y=205)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=170, y=210)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=170, y=215)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=170, y=220)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=170, y=225)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=170, y=230)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=170, y=235)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=170, y=240)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=170, y=245)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=170, y=250)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=170, y=255)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    # Column 6

    b = GRect(5, 5, x=175, y=200)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=175, y=205)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=175, y=210)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=175, y=215)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=175, y=220)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=175, y=225)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=175, y=230)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=175, y=235)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=175, y=240)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=175, y=245)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=175, y=250)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=175, y=255)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    # Column 7

    b = GRect(5, 5, x=180, y=195)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=180, y=200)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=180, y=205)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=180, y=210)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=180, y=215)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=180, y=220)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=180, y=225)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=180, y=230)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=180, y=235)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=180, y=240)
    b.filled = True
    b.fill_color = "tomato"
    window.add(b)

    b = GRect(5, 5, x=180, y=245)
    b.filled = True
    b.fill_color = "tomato"
    window.add(b)

    b = GRect(5, 5, x=180, y=250)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=180, y=255)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    # Column 8

    b = GRect(5, 5, x=185, y=195)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=185, y=200)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=185, y=205)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=185, y=210)
    b.filled = True
    b.fill_color = "green"
    window.add(b)

    b = GRect(5, 5, x=185, y=215)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=185, y=220)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=185, y=225)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=185, y=230)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=185, y=235)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=185, y=240)
    b.filled = True
    b.fill_color = "white"
    window.add(b)

    b = GRect(5, 5, x=185, y=245)
    b.filled = True
    b.fill_color = "white"
    window.add(b)

    b = GRect(5, 5, x=185, y=250)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=185, y=255)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    # Column 9

    b = GRect(5, 5, x=190, y=190)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=190, y=195)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=190, y=200)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=190, y=205)
    b.filled = True
    b.fill_color = "green"
    window.add(b)

    b = GRect(5, 5, x=190, y=210)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=190, y=215)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=190, y=220)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=190, y=225)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=190, y=230)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=190, y=235)
    b.filled = True
    b.fill_color = "lightgreen"
    window.add(b)

    b = GRect(5, 5, x=190, y=240)
    b.filled = True
    b.fill_color = "white"
    window.add(b)

    b = GRect(5, 5, x=190, y=245)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=190, y=250)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=190, y=255)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    # Column 10

    b = GRect(5, 5, x=195, y=190)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=195, y=195)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=195, y=200)
    b.filled = True
    b.fill_color = "green"
    window.add(b)

    b = GRect(5, 5, x=195, y=205)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=195, y=210)
    b.filled = True
    b.fill_color = "green"
    window.add(b)

    b = GRect(5, 5, x=195, y=215)
    b.filled = True
    b.fill_color = "green"
    window.add(b)

    b = GRect(5, 5, x=195, y=220)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=195, y=225)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=195, y=230)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=195, y=235)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=195, y=240)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=195, y=245)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=195, y=250)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=195, y=255)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    # Column 11

    b = GRect(5, 5, x=200, y=185)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=200, y=190)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=200, y=195)
    b.filled = True
    b.fill_color = "green"
    window.add(b)

    b = GRect(5, 5, x=200, y=200)
    b.filled = True
    b.fill_color = "green"
    window.add(b)

    b = GRect(5, 5, x=200, y=205)
    b.filled = True
    b.fill_color = "green"
    window.add(b)

    b = GRect(5, 5, x=200, y=210)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=200, y=215)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=200, y=220)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=200, y=225)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=200, y=230)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=200, y=235)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=200, y=240)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=200, y=245)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=200, y=250)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=200, y=255)
    b.filled = True
    b.fill_color = "white"
    window.add(b)

    b = GRect(5, 5, x=200, y=260)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    # Column 12

    b = GRect(5, 5, x=205, y=180)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=205, y=185)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=205, y=190)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=205, y=195)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=205, y=200)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=205, y=205)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=205, y=210)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=205, y=215)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=205, y=220)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=205, y=225)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=205, y=230)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=205, y=235)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=205, y=240)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=205, y=245)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=205, y=250)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=205, y=255)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=205, y=260)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    # Column 13

    b = GRect(5, 5, x=210, y=180)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=210, y=185)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=210, y=190)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=210, y=195)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=210, y=200)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=210, y=205)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=210, y=210)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=210, y=215)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=210, y=220)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=210, y=225)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=210, y=230)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=210, y=235)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=210, y=240)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=210, y=245)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=210, y=250)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=210, y=255)
    b.filled = True
    b.fill_color = "white"
    window.add(b)

    b = GRect(5, 5, x=210, y=260)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    # Column 14'

    b = GRect(5, 5, x=215, y=180)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=215, y=185)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=215, y=190)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=215, y=195)
    b.filled = True
    b.fill_color = "green"
    window.add(b)

    b = GRect(5, 5, x=215, y=200)
    b.filled = True
    b.fill_color = "green"
    window.add(b)

    b = GRect(5, 5, x=215, y=205)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=215, y=210)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=215, y=215)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=215, y=220)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=215, y=225)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=215, y=230)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=215, y=235)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=215, y=240)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=215, y=245)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=215, y=250)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=215, y=255)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    # Column 15

    b = GRect(5, 5, x=220, y=185)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=220, y=190)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=220, y=195)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=220, y=200)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=220, y=205)
    b.filled = True
    b.fill_color = "green"
    window.add(b)

    b = GRect(5, 5, x=220, y=210)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=220, y=215)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=220, y=220)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=220, y=225)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=220, y=230)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=220, y=235)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=220, y=240)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    # Column 16

    b = GRect(5, 5, x=225, y=195)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=225, y=200)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=225, y=205)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=225, y=210)
    b.filled = True
    b.fill_color = "green"
    window.add(b)

    b = GRect(5, 5, x=225, y=215)
    b.filled = True
    b.fill_color = "green"
    window.add(b)

    b = GRect(5, 5, x=225, y=220)
    b.filled = True
    b.fill_color = "green"
    window.add(b)

    b = GRect(5, 5, x=225, y=225)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=225, y=230)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=225, y=235)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=225, y=240)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    # Column 17

    b = GRect(5, 5, x=230, y=195)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=230, y=200)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=230, y=205)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=230, y=210)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=230, y=215)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=230, y=220)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=230, y=225)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=230, y=230)
    b.filled = True
    b.fill_color = "limegreen"
    window.add(b)

    b = GRect(5, 5, x=230, y=235)
    b.filled = True
    b.fill_color = "white"
    window.add(b)

    b = GRect(5, 5, x=230, y=240)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    # Column 18

    b = GRect(5, 5, x=235, y=200)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=235, y=205)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=235, y=210)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=235, y=215)
    b.filled = True
    b.fill_color = "lawngreen"
    window.add(b)

    b = GRect(5, 5, x=235, y=220)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=235, y=225)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=235, y=230)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=235, y=235)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    # Column 19

    b = GRect(5, 5, x=240, y=205)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=240, y=210)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    b = GRect(5, 5, x=240, y=215)
    b.filled = True
    b.fill_color = "black"
    window.add(b)

    # # Draw pixels to create Charmander.
    # Column 1
    """
    c = GRect(5, 5, x=300, y=260)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)
    """
    c = GRect(5, 5, x=300, y=200)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=300, y=205)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=300, y=210)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    # Column 2

    c = GRect(5, 5, x=305, y=195)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=305, y=200)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=305, y=205)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=305, y=210)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=305, y=215)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    # Column 3

    c = GRect(5, 5, x=310, y=185)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=310, y=190)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=310, y=195)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=310, y=200)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=310, y=205)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=310, y=210)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=310, y=215)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=310, y=220)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    # Column 4

    c = GRect(5, 5, x=315, y=180)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=315, y=185)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=315, y=190)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=315, y=195)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=315, y=200)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=315, y=205)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=315, y=210)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=315, y=215)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=315, y=220)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    # Column 5

    c = GRect(5, 5, x=320, y=175)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=320, y=180)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=320, y=185)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=320, y=190)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=320, y=195)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=320, y=200)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=320, y=205)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=320, y=210)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=320, y=215)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=320, y=220)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=320, y=225)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=320, y=240)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    # Column 6

    c = GRect(5, 5, x=325, y=175)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=325, y=180)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=325, y=185)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=325, y=190)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=325, y=195)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=325, y=200)
    c.filled = True
    c.fill_color = "white"
    window.add(c)

    c = GRect(5, 5, x=325, y=205)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=325, y=210)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=325, y=215)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=325, y=220)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=325, y=225)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=325, y=230)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=325, y=235)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=325, y=240)
    c.filled = True
    c.fill_color = "white"
    window.add(c)

    c = GRect(5, 5, x=325, y=245)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    # Column 7

    c = GRect(5, 5, x=330, y=175)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=330, y=180)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=330, y=185)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=330, y=190)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=330, y=195)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=330, y=200)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=330, y=205)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=330, y=210)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=330, y=215)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=330, y=220)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=330, y=225)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=330, y=230)
    c.filled = True
    c.fill_color = "honeydew"
    window.add(c)

    c = GRect(5, 5, x=330, y=235)
    c.filled = True
    c.fill_color = "yellow"
    window.add(c)

    c = GRect(5, 5, x=330, y=240)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=330, y=245)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    # Column 8

    c = GRect(5, 5, x=335, y=175)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=335, y=180)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=335, y=185)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=335, y=190)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=335, y=195)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=335, y=200)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=335, y=205)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=335, y=210)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=335, y=215)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=335, y=220)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=335, y=225)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=335, y=230)
    c.filled = True
    c.fill_color = "yellow"
    window.add(c)

    c = GRect(5, 5, x=335, y=235)
    c.filled = True
    c.fill_color = "yellow"
    window.add(c)

    c = GRect(5, 5, x=335, y=240)
    c.filled = True
    c.fill_color = "yellow"
    window.add(c)

    c = GRect(5, 5, x=335, y=245)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    # Column 9

    c = GRect(5, 5, x=340, y=180)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=340, y=185)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=340, y=190)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=340, y=195)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=340, y=200)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=340, y=205)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=340, y=210)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=340, y=215)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=340, y=220)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=340, y=225)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=340, y=230)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=340, y=235)
    c.filled = True
    c.fill_color = "yellow"
    window.add(c)

    c = GRect(5, 5, x=340, y=240)
    c.filled = True
    c.fill_color = "yellow"
    window.add(c)

    c = GRect(5, 5, x=340, y=245)
    c.filled = True
    c.fill_color = "yellow"
    window.add(c)

    c = GRect(5, 5, x=340, y=250)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    # Column 10

    c = GRect(5, 5, x=345, y=185)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=345, y=190)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=345, y=195)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=345, y=200)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=345, y=205)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=345, y=210)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=345, y=215)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=345, y=220)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=345, y=225)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=345, y=230)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=345, y=235)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=345, y=240)
    c.filled = True
    c.fill_color = "yellow"
    window.add(c)

    c = GRect(5, 5, x=345, y=245)
    c.filled = True
    c.fill_color = "yellow"
    window.add(c)

    c = GRect(5, 5, x=345, y=250)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=345, y=255)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    # Column 11

    c = GRect(5, 5, x=350, y=195)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=350, y=200)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=350, y=205)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=350, y=210)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=350, y=215)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=350, y=220)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=350, y=225)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=350, y=230)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=350, y=235)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=350, y=240)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=350, y=245)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=350, y=250)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=350, y=255)
    c.filled = True
    c.fill_color = "white"
    window.add(c)

    c = GRect(5, 5, x=350, y=260)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    # Column 12

    c = GRect(5, 5, x=355, y=205)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=355, y=210)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=355, y=215)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=355, y=220)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=355, y=225)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=355, y=230)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=355, y=235)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=355, y=240)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=355, y=245)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=355, y=250)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=355, y=255)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=355, y=260)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    # Column 13

    c = GRect(5, 5, x=360, y=215)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=360, y=220)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=360, y=225)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=360, y=230)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=360, y=235)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=360, y=240)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=360, y=245)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=360, y=250)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=360, y=255)
    c.filled = True
    c.fill_color = "white"
    window.add(c)

    c = GRect(5, 5, x=360, y=260)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    # Column 14

    c = GRect(5, 5, x=365, y=220)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=365, y=225)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=365, y=230)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=365, y=235)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=365, y=240)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=365, y=245)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=365, y=250)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=365, y=255)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    # Column 15

    c = GRect(5, 5, x=370, y=220)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=370, y=225)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=370, y=230)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=370, y=235)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=370, y=240)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=370, y=245)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    # Column 16

    c = GRect(5, 5, x=375, y=195)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=375, y=200)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=375, y=215)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=375, y=220)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=375, y=225)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=375, y=230)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=375, y=235)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=375, y=240)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    # Column 17

    c = GRect(5, 5, x=380, y=180)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=380, y=185)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=380, y=190)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=380, y=195)
    c.filled = True
    c.fill_color = "tomato"
    window.add(c)

    c = GRect(5, 5, x=380, y=200)
    c.filled = True
    c.fill_color = "tomato"
    window.add(c)

    c = GRect(5, 5, x=380, y=205)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=380, y=210)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=380, y=215)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=380, y=220)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=380, y=225)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=380, y=230)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=380, y=235)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    # Column 18

    c = GRect(5, 5, x=385, y=175)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=385, y=180)
    c.filled = True
    c.fill_color = "tomato"
    window.add(c)

    c = GRect(5, 5, x=385, y=185)
    c.filled = True
    c.fill_color = "tomato"
    window.add(c)

    c = GRect(5, 5, x=385, y=190)
    c.filled = True
    c.fill_color = "tomato"
    window.add(c)

    c = GRect(5, 5, x=385, y=195)
    c.filled = True
    c.fill_color = "tomato"
    window.add(c)

    c = GRect(5, 5, x=385, y=200)
    c.filled = True
    c.fill_color = "tomato"
    window.add(c)

    c = GRect(5, 5, x=385, y=205)
    c.filled = True
    c.fill_color = "yellow"
    window.add(c)

    c = GRect(5, 5, x=385, y=210)
    c.filled = True
    c.fill_color = "yellow"
    window.add(c)

    c = GRect(5, 5, x=385, y=215)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=385, y=220)
    c.filled = True
    c.fill_color = "orange"
    window.add(c)

    c = GRect(5, 5, x=385, y=225)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=385, y=230)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    # Column 19

    c = GRect(5, 5, x=390, y=180)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=390, y=185)
    c.filled = True
    c.fill_color = "tomato"
    window.add(c)

    c = GRect(5, 5, x=390, y=190)
    c.filled = True
    c.fill_color = "tomato"
    window.add(c)

    c = GRect(5, 5, x=390, y=195)
    c.filled = True
    c.fill_color = "yellow"
    window.add(c)

    c = GRect(5, 5, x=390, y=200)
    c.filled = True
    c.fill_color = "yellow"
    window.add(c)

    c = GRect(5, 5, x=390, y=205)
    c.filled = True
    c.fill_color = "yellow"
    window.add(c)

    c = GRect(5, 5, x=390, y=210)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=390, y=215)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=390, y=220)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    # Column 20

    c = GRect(5, 5, x=395, y=185)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=395, y=190)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=395, y=195)
    c.filled = True
    c.fill_color = "tomato"
    window.add(c)

    c = GRect(5, 5, x=395, y=200)
    c.filled = True
    c.fill_color = "yellow"
    window.add(c)

    c = GRect(5, 5, x=395, y=205)
    c.filled = True
    c.fill_color = "tomato"
    window.add(c)

    c = GRect(5, 5, x=395, y=210)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    # Column 21

    c = GRect(5, 5, x=400, y=195)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=400, y=200)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    c = GRect(5, 5, x=400, y=205)
    c.filled = True
    c.fill_color = "black"
    window.add(c)

    # Draw pixels to create Squirtle.
    # Column 1

    s = GRect(5, 5, x=460, y=200)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=460, y=205)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=460, y=210)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    # Column 2

    s = GRect(5, 5, x=465, y=190)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=465, y=195)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=465, y=200)
    s.filled = True
    s.fill_color = "peru"
    window.add(s)

    s = GRect(5, 5, x=465, y=205)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=465, y=210)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=465, y=215)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    # Column 3

    s = GRect(5, 5, x=470, y=185)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=470, y=190)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=470, y=195)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=470, y=200)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=470, y=205)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=470, y=210)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=470, y=215)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=470, y=220)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=470, y=225)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    # Column 4

    s = GRect(5, 5, x=475, y=180)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=475, y=185)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=475, y=190)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=475, y=195)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=475, y=200)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=475, y=205)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=475, y=210)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=475, y=215)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=475, y=220)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=475, y=225)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=475, y=230)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    # Column 5

    s = GRect(5, 5, x=480, y=180)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=480, y=185)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=480, y=190)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=480, y=195)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=480, y=200)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=480, y=205)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=480, y=210)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=480, y=215)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=480, y=220)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=480, y=225)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=480, y=230)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=480, y=240)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    # Column 6

    s = GRect(5, 5, x=485, y=180)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=485, y=185)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=485, y=190)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=485, y=195)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=485, y=200)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=485, y=205)
    s.filled = True
    s.fill_color = "white"
    window.add(s)

    s = GRect(5, 5, x=485, y=210)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=485, y=215)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=485, y=220)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=485, y=225)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=485, y=230)
    s.filled = True
    s.fill_color = "#F0E68C"
    window.add(s)

    s = GRect(5, 5, x=485, y=235)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=485, y=240)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=485, y=245)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    # Column 7

    s = GRect(5, 5, x=490, y=180)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=490, y=185)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=490, y=190)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=490, y=195)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=490, y=200)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=490, y=205)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=490, y=210)
    s.filled = True
    s.fill_color = "peru"
    window.add(s)

    s = GRect(5, 5, x=490, y=215)
    s.filled = True
    s.fill_color = "peru"
    window.add(s)

    s = GRect(5, 5, x=490, y=220)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=490, y=225)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=490, y=230)
    s.filled = True
    s.fill_color = "#F0E68C"
    window.add(s)

    s = GRect(5, 5, x=490, y=235)
    s.filled = True
    s.fill_color = "#F0E68C"
    window.add(s)

    s = GRect(5, 5, x=490, y=240)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=490, y=245)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    # Column 8

    s = GRect(5, 5, x=495, y=185)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=495, y=190)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=495, y=195)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=495, y=200)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=495, y=205)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=495, y=210)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=495, y=215)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=495, y=220)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=495, y=225)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=495, y=230)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=495, y=235)
    s.filled = True
    s.fill_color = "#F0E68C"
    window.add(s)

    s = GRect(5, 5, x=495, y=240)
    s.filled = True
    s.fill_color = "#F0E68C"
    window.add(s)

    s = GRect(5, 5, x=495, y=245)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    # Column 9

    s = GRect(5, 5, x=500, y=185)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=500, y=190)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=500, y=195)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=500, y=200)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=500, y=205)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=500, y=210)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=500, y=215)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=500, y=220)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=500, y=225)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=500, y=230)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=500, y=235)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=500, y=240)
    s.filled = True
    s.fill_color = "#F0E68C"
    window.add(s)

    s = GRect(5, 5, x=500, y=245)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=500, y=250)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    # Column 10

    s = GRect(5, 5, x=505, y=190)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=505, y=195)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=505, y=200)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=505, y=205)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=505, y=210)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=505, y=215)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=505, y=220)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=505, y=225)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=505, y=230)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=505, y=235)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=505, y=240)
    s.filled = True
    s.fill_color = "#F0E68C"
    window.add(s)

    s = GRect(5, 5, x=505, y=245)
    s.filled = True
    s.fill_color = "#F0E68C"
    window.add(s)

    s = GRect(5, 5, x=505, y=250)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=505, y=255)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    # Column 11

    s = GRect(5, 5, x=510, y=190)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=510, y=195)
    s.filled = True
    s.fill_color = "peru"
    window.add(s)

    s = GRect(5, 5, x=510, y=200)
    s.filled = True
    s.fill_color = "peru"
    window.add(s)

    s = GRect(5, 5, x=510, y=205)
    s.filled = True
    s.fill_color = "white"
    window.add(s)

    s = GRect(5, 5, x=510, y=210)
    s.filled = True
    s.fill_color = "white"
    window.add(s)

    s = GRect(5, 5, x=510, y=215)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=510, y=220)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=510, y=225)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=510, y=230)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=510, y=235)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=510, y=240)
    s.filled = True
    s.fill_color = "#F0E68C"
    window.add(s)

    s = GRect(5, 5, x=510, y=245)
    s.filled = True
    s.fill_color = "#F0E68C"
    window.add(s)

    s = GRect(5, 5, x=510, y=250)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=510, y=255)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=510, y=260)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    # Column 12

    s = GRect(5, 5, x=515, y=195)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=515, y=200)
    s.filled = True
    s.fill_color = "peru"
    window.add(s)

    s = GRect(5, 5, x=515, y=205)
    s.filled = True
    s.fill_color = "peru"
    window.add(s)

    s = GRect(5, 5, x=515, y=210)
    s.filled = True
    s.fill_color = "peru"
    window.add(s)

    s = GRect(5, 5, x=515, y=215)
    s.filled = True
    s.fill_color = "white"
    window.add(s)

    s = GRect(5, 5, x=515, y=220)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=515, y=225)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=515, y=230)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=515, y=235)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=515, y=240)
    s.filled = True
    s.fill_color = "#F0E68C"
    window.add(s)

    s = GRect(5, 5, x=515, y=245)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=515, y=250)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=515, y=255)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=515, y=260)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    # Column 13

    s = GRect(5, 5, x=520, y=195)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=520, y=200)
    s.filled = True
    s.fill_color = "peru"
    window.add(s)

    s = GRect(5, 5, x=520, y=205)
    s.filled = True
    s.fill_color = "peru"
    window.add(s)

    s = GRect(5, 5, x=520, y=210)
    s.filled = True
    s.fill_color = "peru"
    window.add(s)

    s = GRect(5, 5, x=520, y=215)
    s.filled = True
    s.fill_color = "peru"
    window.add(s)

    s = GRect(5, 5, x=520, y=220)
    s.filled = True
    s.fill_color = "white"
    window.add(s)

    s = GRect(5, 5, x=520, y=225)
    s.filled = True
    s.fill_color = "white"
    window.add(s)

    s = GRect(5, 5, x=520, y=230)
    s.filled = True
    s.fill_color = "white"
    window.add(s)

    s = GRect(5, 5, x=520, y=235)
    s.filled = True
    s.fill_color = "white"
    window.add(s)

    s = GRect(5, 5, x=520, y=240)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=520, y=245)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=520, y=250)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=520, y=255)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=520, y=260)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    # Column 14

    s = GRect(5, 5, x=525, y=200)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=525, y=205)
    s.filled = True
    s.fill_color = "peru"
    window.add(s)

    s = GRect(5, 5, x=525, y=210)
    s.filled = True
    s.fill_color = "peru"
    window.add(s)

    s = GRect(5, 5, x=525, y=215)
    s.filled = True
    s.fill_color = "peru"
    window.add(s)

    s = GRect(5, 5, x=525, y=220)
    s.filled = True
    s.fill_color = "peru"
    window.add(s)

    s = GRect(5, 5, x=525, y=225)
    s.filled = True
    s.fill_color = "peru"
    window.add(s)

    s = GRect(5, 5, x=525, y=230)
    s.filled = True
    s.fill_color = "peru"
    window.add(s)

    s = GRect(5, 5, x=525, y=235)
    s.filled = True
    s.fill_color = "peru"
    window.add(s)

    s = GRect(5, 5, x=525, y=240)
    s.filled = True
    s.fill_color = "white"
    window.add(s)

    s = GRect(5, 5, x=525, y=245)
    s.filled = True
    s.fill_color = "white"
    window.add(s)

    s = GRect(5, 5, x=525, y=250)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=525, y=255)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    # Column 15

    s = GRect(5, 5, x=530, y=190)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=530, y=195)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=530, y=200)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=530, y=205)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=530, y=210)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=530, y=215)
    s.filled = True
    s.fill_color = "peru"
    window.add(s)

    s = GRect(5, 5, x=530, y=220)
    s.filled = True
    s.fill_color = "peru"
    window.add(s)

    s = GRect(5, 5, x=530, y=225)
    s.filled = True
    s.fill_color = "peru"
    window.add(s)

    s = GRect(5, 5, x=530, y=230)
    s.filled = True
    s.fill_color = "peru"
    window.add(s)

    s = GRect(5, 5, x=530, y=235)
    s.filled = True
    s.fill_color = "peru"
    window.add(s)

    s = GRect(5, 5, x=530, y=240)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=530, y=245)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    # Column 16

    s = GRect(5, 5, x=535, y=185)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=535, y=190)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=535, y=195)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=535, y=200)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=535, y=205)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=535, y=210)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=535, y=215)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=535, y=220)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=535, y=225)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=535, y=230)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=535, y=235)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    # Column 16

    s = GRect(5, 5, x=540, y=180)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=540, y=185)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=540, y=190)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=540, y=195)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=540, y=200)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=540, y=205)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=540, y=210)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=540, y=215)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    # Column 17

    s = GRect(5, 5, x=545, y=180)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=545, y=185)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=545, y=190)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=545, y=195)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=545, y=200)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=545, y=205)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=545, y=210)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    # Column 18

    s = GRect(5, 5, x=550, y=180)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=550, y=185)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=550, y=190)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=550, y=195)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=550, y=200)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=550, y=205)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=550, y=210)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    # Column 18

    s = GRect(5, 5, x=555, y=185)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=555, y=190)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=555, y=195)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=555, y=200)
    s.filled = True
    s.fill_color = "sky blue"
    window.add(s)

    s = GRect(5, 5, x=555, y=205)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    # Column 19

    s = GRect(5, 5, x=560, y=190)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=560, y=195)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    s = GRect(5, 5, x=560, y=200)
    s.filled = True
    s.fill_color = "black"
    window.add(s)

    label = GLabel("Pokémon", x=200, y=80)   # Create the name of Pokémon.
    label.font = "Helvetica-50-italic-bold"
    window.add(label)

    label = GLabel("Bulbasaur", x=120, y=130)   # Create the name of Bulbasaur.
    label.font = "Helvetica-20-bold"
    window.add(label)

    label = GLabel("Charmander", x=275, y=130)   # Create the name of Charmander.
    label.font = "Helvetica-20-bold"
    window.add(label)

    label = GLabel("Squirtle", x=465, y=130)   # Create the name of Squirtle.
    label.font = "Helvetica-20-bold"
    window.add(label)

    choose_sign1 = GLabel("▲", x=170, y=330)   # Create the sign of "▲".
    choose_sign1.font = "-20"
    window.add(choose_sign1)

    choose_sign2 = GLabel("▲", x=337, y=330)   # Create the sign of "▲".
    choose_sign2.font = "-20"
    window.add(choose_sign2)

    choose_sign2 = GLabel("▲", x=500, y=330)   # Create the sign of "▲".
    choose_sign2.font = "-20"
    window.add(choose_sign2)


if __name__ == '__main__':
    main()
