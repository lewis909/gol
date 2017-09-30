from random import randint
from pprint import pprint


class Gol:
    game_board = []

    def __init__(self, x, duration=None):
        self.x = x
        self.duration = duration
        self._game_board = self._build_board()

    def _build_board(self):
        matrix = [[0 for i in range(self.x)] for i in range(self.x)]
        return matrix

    def set_start_position(self):
        row = randint(0,9)
        col = randint(0,9)
        self._game_board[row][col] = 1

    def run_sim(self):
        run_num = 0
        while run_num < self.duration:
            print("Run: {}".format(run_num + 1))
            pprint(self._game_board)
            run_num += 1

gol = Gol(10, 3)
gol.set_start_position()
gol.run_sim()
