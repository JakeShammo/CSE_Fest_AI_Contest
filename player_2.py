import time
import random
import numpy as np


def read_file(player_no):
    with open("shared_file.txt") as f:
        lines = f.readlines()
    if len(lines) == 0:
        return None
    if lines[0].strip('\n') == str(player_no):
        temp_grid = []
        for line in lines[1:]:
            temp_grid.append(line.strip('\n').split(" ")[:-1])
        return np.transpose(np.flip(temp_grid, 0)).tolist()
    return None


def select_move(grid, player_color):
    while True:
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        if grid[x][y] == 'No' or grid[x][y][0] == player_color:
            return x, y


def write_move(move):
    str_to_write = '0\n' + str(move[0]) + " " + str(move[1])
    with open("shared_file.txt", 'w') as f:
        f.write(str_to_write)


def main():
    player_no = 2
    player_color = 'G'
    while True:
        while True:
            grid = read_file(player_no)
            if grid is not None:
                break
            time.sleep(.01)
        move = select_move(grid, player_color)
        write_move(move)


if __name__ == "__main__":
    main()