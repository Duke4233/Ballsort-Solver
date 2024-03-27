from balls import ball
from tubes import tube
from balls import ball
from common import colors


def make_game(filename: str):
    file = open(filename, "r")
    file_text = file.readlines()
    game_tubes = []
    for line in file_text:
        tube_num = 0

        text_colors = line.split(" ")
        new_tube = tube(len(text_colors), tube_num)  # TODO
        for color in text_colors:
            new_ball = ball(colors[color.strip('\n')])
            new_tube.add_ball(new_ball)
        tube_num += 1
        game_tubes.append(new_tube)

    return game_tubes
