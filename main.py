from solver import solve
from interface import make_game


def main():
    solution, current_tubes = solve(make_game("sample_balls.txt"))

    print(solution)

if __name__ == "__main__":
    main()