import time

ROWS = 6
COLUMNS = 7


class Board():

    def __init__(self):
        self.board_matrix = [[0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0]]
        self.player_icons = {0: ' ', 1: 'x', 2: 'o'}

    def print_board(self):
        print('')
        print('- 1 - 2 - 3 - 4 - 5 - 6 - 7 -')
        for row in range(ROWS):
            for column in range(COLUMNS):
                if column != COLUMNS-1:
                    print('|', self.player_icons[self.board_matrix[row][column]], '', end = '')
                else:
                    print('|', self.player_icons[self.board_matrix[row][column]], '|', end = '\n')
            print('-   -   -   -   -   -   -   -')
            
    def reset_game(self):
        self.board_matrix = [[0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0]]
    
    def make_move(self, player, column):
        for row in range(ROWS - 1):
            if self.board_matrix[row][column] == 0 and self.board_matrix[row + 1][column] != 0:
                self.board_matrix[row][column] = player
                break
            elif self.board_matrix[ROWS][column] == 0:
                self.board_matrix[row][column] = player
                break
    
    def play(self, start_player = 1):
        self.reset_game()
        




board = Board()
board.print_board()