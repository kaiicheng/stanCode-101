"""

stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120   # 120 frames per second.
NUM_LIVES = 3


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    while True:
        if lives <= 0:
            break
        else:
            pause(FRAME_RATE)
            graphics.move()
            graphics.reflect()
            graphics.remove()
            if graphics.ball.y >= graphics.window.height:
                lives -= 1
                graphics.reset_ball()
                graphics.switch_off()
            if lives <= 0:
                break
            finished = graphics.finished()
            if finished:
                break


if __name__ == '__main__':
    main()
