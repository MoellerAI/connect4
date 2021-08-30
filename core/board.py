from helper import clear

import time

ROWS = 6
COLUMNS = 7


class Board():

    def __init__(self):
        self.board = [[0, 0, 0, 0, 0, 0, 0],
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
                    print('|', self.player_icons[self.board[row][column]], '', end = '')
                else:
                    print('|', self.player_icons[self.board[row][column]], '|', end = '\n')
            print('-   -   -   -   -   -   -   -')
            
    def reset_game(self):
        self.board = [[0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0]]
    
    def make_move(self, player, column):
        for row in range(ROWS - 1):
            if self.board[ROWS-1][column] == 0:
                self.board[ROWS-1][column] = player
                break  
            elif self.board[row][column] == 0 and self.board[row + 1][column] != 0:
                self.board[row][column] = player
                break
    
    def validate_move(self, column: int) -> bool:
        if self.board[0][column] != 0:
            return False
        else:
            return True

    def change_player(self):
        while True:
            yield 1
            yield 2
        
    def game_over(self, player) -> bool:
        # check for horizontal win
        for column in range(COLUMNS-3):
            for row in range(ROWS):
                if self.board[row][column] == player and self.board[row][column+1] == player and self.board[row][column+2] == player and self.board[row][column+3] == player:
                    return True

        # check for vertical win
        for column in range(COLUMNS):
            for row in range(ROWS-3):
                if self.board[row][column] == player and self.board[row+1][column] == player and self.board[row+2][column] == player and self.board[row+3][column] == player:
                    return True

        # check negative slope win
        for column in range(COLUMNS-3):
            for row in range(ROWS-3):
                if self.board[row][column] == player and self.board[row+1][column+1] == player and self.board[row+2][column+2] == player and self.board[row+3][column+3] == player:
                    return True

        # check positive slope win
        for column in range(COLUMNS-3):
            for row in range(3, ROWS):
                if self.board[row][column] == player and self.board[row-1][column+1] == player and self.board[row-2][column+2] == player and self.board[row-3][column+3] == player:
                    return True
        return False
    
    def play(self, start_player = 1):
        self.reset_game()
        game_over = False
        self.print_board()
        player_turn = self.change_player()
        start_player = next(player_turn)

        while game_over == False:
            while True:
                column = input(f'Player {self.player_icons[start_player]} choose a column:')
                if self.validate_move(column = int(column)-1): break
            self.make_move(player = start_player, column = int(column)-1)
            clear()
            game_over = self.game_over(player = start_player)
            start_player = next(player_turn)
            self.print_board()
            


        

game = Board()
game.play()