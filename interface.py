from balls import ball
from tubes import tube
from common import *
def make_game():
    file = open(filename, "r")
    file_text = file.readlines()
    game_tubes = []
    for line in file_text:
        tube_num = 0
        new_tube = tube(4,)
        text_colors = line.split(" ")
        for color in text_colors:
            slot_num = 0
            new_ball = ball.ball(colors[color], tube_num, slot_num)

    return game_tubes

