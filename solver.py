from interface import make_game


def is_solved(tubes):
    solved_cnt = 0
    for tube in tubes:
        if tube.is_solved():
            solved_cnt += 1
        else:
            return False
    if solved_cnt == len(tubes):
        return True

    return False

def get_valid_moves(tubes,valid_move_list):
    for tube in tubes:
        for tube_dest in tubes:
            if tube == tube_dest:
                continue
            if not tube_dest.full and tube.top.color == tube_dest.top.color:
                valid_move_list.append((tube.id, tube_dest.id))


def solve(tubes,move_list):
    move_list = []
    valid_move_list = []
    if is_solved(tubes):
        return move_list, tubes
    else:
        get_valid_moves(tubes,valid_move_list)
def main():
    tubes = make_game()
    print(solve(tubes))
