"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    average = (width - GRAPH_MARGIN_SIZE*2) // 12
    x_coordinate = GRAPH_MARGIN_SIZE + ((year_index - 1900)/10) * average
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################

    # Create two horizontal lines to the canvas.
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)

    # Add vertical lines to the canvas.
    for i in range(len(YEARS)):   # len(YEARS)-1
        x = int(get_x_coordinate(width=CANVAS_WIDTH, year_index=YEARS[i]))
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)

    # Add years caption to the canvas.
    for i in range(len(YEARS)):   # len(YEARS)-1
        x = int(get_x_coordinate(width=CANVAS_WIDTH, year_index=YEARS[i]))
        canvas.create_text(x, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW, font='times 10')


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################

    y_begin = int(GRAPH_MARGIN_SIZE)
    average = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE*2)/1000

    for i in range(len(lookup_names)):
        for j in range(len(YEARS)-1):   # len(YEARS)-1
            print("-----------------------")
            print(len(YEARS))

            ls = list(name_data[lookup_names[i]])
            print(ls)

            # Create a switch. When the rank of year isn't recorded, the switch will be changed into True.
            missed = False

            # Create a switch. When the rank of the next year isn't recorded, the switch will be changed into True.
            next_missed = False

            # Change switch into True, if the rank of the year isn't recorded.
            if str(YEARS[j]) in ls:
                print('yes, with record')   # PROCESSED!
            else:
                print('no, data missed!')
                missed = True

            # Change switch into True, if the rank of the next year isn't recorded.
            if str(YEARS[j+1]) in ls:
                print('yes, next year with record')   # PROCESSED!
            else:
                print('no, next year data missed!')
                next_missed = True

            # Adjust color of the line.
            color_num = i
            if color_num > len(COLORS)-1:
                color_num = color_num % len(COLORS)
            color = COLORS[color_num]

            if missed == True:   # The data of first year is missed.
                print('###################')
                print('This is missed-if')

                # X coordinate of the year.
                x = int(get_x_coordinate(width=CANVAS_WIDTH, year_index=YEARS[j]))
                print('x: ')
                print(x)

                # X coordinate of the next year.
                x_next = 0
                if j == (len(YEARS) - 1):
                    pass
                else:
                    x_next = int(get_x_coordinate(width=CANVAS_WIDTH, year_index=YEARS[j + 1]))
                print('x_next: ')
                print(x_next)   # 100

                if next_missed is True:   # Data in the first year is missed, and that of next year is missed.

                    # Create a line on the canvas.
                    canvas.create_line(x, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, x_next, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill=color)

                    # Add name and rank to the canvas.
                    name_and_rank = str(lookup_names[i] + ' * ')
                    print(name_and_rank)
                    canvas.create_text(x, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=name_and_rank, anchor=tkinter.SW, font='times 10', fill=color)

                else:   # Data in the first year is missed, but that of next year isn't missed.

                    # X coordinate of the year.
                    x = int(get_x_coordinate(width=CANVAS_WIDTH, year_index=YEARS[j]))

                    # X coordinate of the next year.
                    x_next = 0
                    if j == (len(YEARS) - 1):
                        pass
                    else:
                        x_next = int(get_x_coordinate(width=CANVAS_WIDTH, year_index=YEARS[j + 1]))

                    # Count the rank of the next year, and then compute y coordinate of the next year.
                    rank_of_next_year = 0
                    if j == (len(YEARS) - 1):
                        pass
                    else:
                        rank_of_next_year = int(name_data[lookup_names[i]][str(YEARS[j + 1])])

                    # Y coordinate of the next year.
                    y_next = int(y_begin + average * rank_of_next_year)

                    # Create the line on the canvas.
                    canvas.create_line(x, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, x_next, y_next, width=LINE_WIDTH, fill=color)

                    # Add name and rank to the canvas.
                    name_and_rank = str(lookup_names[i] + ' * ')
                    canvas.create_text(x, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=name_and_rank, anchor=tkinter.SW, font='times 10', fill=color)

            else:   # Data in the first year isn't missed.
                if next_missed is True:   # Data in the first year isn't missed, but that of next year is missed.

                    # X coordinate of the year.
                    x = int(get_x_coordinate(width=CANVAS_WIDTH, year_index=YEARS[j]))

                    # X coordinate of the next year.
                    x_next = 0
                    if j == (len(YEARS)-1):
                        pass
                    else:
                        x_next = int(get_x_coordinate(width=CANVAS_WIDTH, year_index=YEARS[j + 1]))

                    # Count the rank of the year, and then compute the y coordinate of the year.
                    rank_of_year = int(name_data[lookup_names[i]][str(YEARS[j])])

                    # Y coordinate of the year.
                    y = int(y_begin + average * rank_of_year)

                    # Adjust color of the line.
                    color_num = i
                    if color_num > len(COLORS) - 1:
                        color_num = color_num % len(COLORS)
                    color = COLORS[color_num]

                    # Add the line to the canvas.
                    canvas.create_line(x, y, x_next, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill=color)

                    # Add name and rank to the canvas.
                    name_and_rank = str(lookup_names[i] + ' ' + name_data[lookup_names[i]][str(YEARS[j])])
                    canvas.create_text(x+TEXT_DX, y, text=name_and_rank, anchor=tkinter.NW, font='times 10', fill=color)
                else:   # Data in the first year isn't missed, and that of next year isn't missed.

                    # X coordinate of the year.
                    x = int(get_x_coordinate(width=CANVAS_WIDTH, year_index=YEARS[j]))

                    # X coordinate of the next year.
                    x_next = 0
                    if j == (len(YEARS)-1):
                        pass
                    else:
                        x_next = int(get_x_coordinate(width=CANVAS_WIDTH, year_index=YEARS[j + 1]))

                    # Count the rank of the year, and then compute the y coordinate of the year.
                    rank_of_year = int(name_data[lookup_names[i]][str(YEARS[j])])

                    # Y coordinate of the year.
                    y = int(y_begin + average * rank_of_year)

                    # Count the rank of the next year, and then compute y coordinate of the next year.
                    rank_of_next_year = 0
                    if j == (len(YEARS)-1):
                        pass
                    else:
                        rank_of_next_year = int(name_data[lookup_names[i]][str(YEARS[j+1])])

                    # Y coordinate of the next year.
                    y_next = int(y_begin + average * rank_of_next_year)

                    # Adjust color of the line.
                    color_num = i
                    if color_num > len(COLORS) - 1:
                        color_num = color_num % len(COLORS)
                    color = COLORS[color_num]

                    # Add the line to the canvas.
                    canvas.create_line(x, y, x_next, y_next, width=LINE_WIDTH, fill=color)

                    # Add name and rank to the canvas.
                    name_and_rank = str(lookup_names[i] + ' ' + name_data[lookup_names[i]][str(YEARS[j])])
                    canvas.create_text(x+TEXT_DX, y, text=name_and_rank, anchor=tkinter.NW, font='times 10', fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
