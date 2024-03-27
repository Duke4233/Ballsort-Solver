from interface import make_game
from tubes import tube


def is_solved(tubes):
    solved_cnt = 0
    for cur_tube in tubes:
        if cur_tube.is_solved():
            solved_cnt += 1
        else:
            return False
    if solved_cnt == len(tubes):
        return True

    return False


def get_valid_moves(tubes, valid_move_list):
    for cur_tube in tubes:
        for tube_dest in tubes:
            if cur_tube == tube_dest:
                continue
            if not tube_dest.full and cur_tube.top.color == tube_dest.top.color:
                valid_move_list.append((cur_tube.id, tube_dest.id))


def apply_move(tubes: tube, cur_move):
    src_tube = tubes[cur_move[0]]
    target_tube = tubes[cur_move[1]]
    if not target_tube.full:
        if not target_tube.add_ball(src_tube.pop_top()):
            raise ValueError("Could not add a ball")
        return cur_move
    raise ValueError("apply_move tried to apply a move onto a full tube.")


def solve(tubes, move_list):
    lcl_move_list = move_list
    valid_move_list = []
    if is_solved(tubes):
        return tubes, move_list  # base case
    get_valid_moves(tubes, valid_move_list)
    for move in valid_move_list:
        # add for loop to loop through valid moves until retubes returns_issolve or run out then return.
        lcl_move_list.append(apply_move(tubes, move))
        re_tubes, re_move_list = solve(tubes, lcl_move_list)  # need to do stuff to handle not solved tubes.
        if re_tubes.solved:
            return re_tubes, move_list + re_move_list  #
    return tubes, move_list


def main():
    tubes = make_game()
    print(solve(tubes))
