from .logo import logo
from .board import Board
from .ai import AI


class Game:
    def __init__(self):
        self.logo = logo
        self.board = Board()
        self.ai = AI()
        self.player = 1 # 2 to let ai start first
        self.player_1 = "X"
        self.player_2 = "O"
        self.gamemode = "ai"
        self.running = True
        self.start_scene()

    def start_scene(self):
        print(logo)
        print("Have fun with tic tac toe!!!")
        
        self.show_board()
        self.setup()

    def setup (self):
        player_symbol = input("\nICON | 1 - 'X' | 2 - 'O': ").upper()
        
        while player_symbol != "1" and player_symbol != "2":
            player_symbol = input("Not valid. Please pick again: ")

        self.player_1 = "X" if player_symbol == "1" else "O"
        self.player_2 = "O" if player_symbol == "1" else "X"

        game_mode = input("\nMODE | 1 - player vs player | 2 - player vs ai: ")
        
        while game_mode != "1" and game_mode != "2":
            game_mode = input("Not valid. Please pick again: ")

        if game_mode == "1":
            self.gamemode = "pvp"
        elif game_mode == "2":
            self.gamemode = "ai"
            
            level = input("\nLEVEL | 1 - easy | 2 - difficult: ")
            
            while level != "1" and level != "2":
                level = input("Not valid. Please pick again: ")
                
            self.ai.level = int(level)
        
        print("\n" + "-" * 50 + "\n")

    def make_move(self, row, col):
        self.board.mark_sqr(row, col, self.player)
        self.show_board()
        
        print("\n" + "-" * 50 + "\n")
        
        self.next_turn()

    def show_board(self):
        print("\n-------------")
        
        for i in range(len(self.board.squares)):
            str = "|"
            for j in range(len(self.board.squares)):
                show = None
                if self.board.squares[i][j] == 0:
                    show = " "
                if self.board.squares[i][j] == 1:
                    show = self.player_1
                if self.board.squares[i][j] == 2:
                    show = self.player_2
                
                str += f" {show} |"
                
            print(str)
            print("-------------")

    def next_turn(self):
        self.player = self.player % 2 + 1

    def isover(self):
        return self.board.final_state() != 0 or self.board.isfull()

    def result(self):
        if self.board.final_state() == 1:
            return "Player 1 wins!!!" if self.gamemode == "pvp" else "You beated AI!!!"
        elif self.board.final_state() == 2:
            return "Player 2 wins!!!" if self.gamemode == "pvp" else "AI is unbeatable!!!"
        elif self.board.final_state() == 0:
            return "Both drew!!!"