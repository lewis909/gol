from pprint import pprint


class Gol:

    def __init__(self, x, duration=None):
        self.x = x
        self.duration = duration
        self._game_board = self._build_board()

    def _build_board(self):
        return [[0 for i in range(self.x)] for i in range(self.x)]

    def set_start_position(self):
        self._game_board[3][5] = 1
        self._game_board[5][5] = 1

    def _game_logic(self):
        board = self._game_board
        for row in range(len(board)):
            for cell in range(len(board[row])):
                try:

                    neighbour_count = 0
                    if board[row][cell + 1] == 1:
                        neighbour_count += 1
                    if board[row][cell -1] == 1:
                        neighbour_count += 1
                    if board[row + 1][cell] ==1:
                        neighbour_count += 1
                    if board[row - 1][cell] == 1:
                        neighbour_count += 1
                    if board[row - 1][cell -1] == 1:
                        neighbour_count += 1
                    if board[row - 1][cell + 1] == 1:
                        neighbour_count += 1
                    if board[row + 1][cell -1] == 1:
                        neighbour_count += 1
                    if board[row + 1][cell + 1] == 1:
                        neighbour_count += 1

                    if neighbour_count == 2 or neighbour_count == 3:
                        board[row][cell] = 1
                    if neighbour_count >= 3:
                        board[row][cell] = 0

                except:
                    continue
            print(board[row])

    def run_sim(self):
        print("Run: 0")
        pprint(gol._game_board)
        run_num = 0
        while run_num < self.duration:
            print("Run: {}".format(run_num + 1))
            self._game_logic()
            run_num += 1

gol = Gol(10, 20)
gol.set_start_position()
gol.run_sim()
