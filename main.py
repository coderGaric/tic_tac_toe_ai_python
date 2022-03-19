import re
from click import clear
from modules.game import Game


def main():
    game = Game()
    board = game.board
    ai = game.ai
    
    while game.running:
        # player choice
        get_tuple = True
        
        while get_tuple:
            choice = input(f"Player {game.player} choose(row,column): ")
            pattern = re.compile(r"\d")
            a, b = pattern.findall(choice)
            extract_tuple = tuple([int(a), int(b)])
            
            while extract_tuple not in board.get_empty_sqrs():
                choice = input(f"Player {game.player} move not valid, choose again: ")
                pattern = re.compile(r"\d")
                a, b = pattern.findall(choice)
                extract_tuple = tuple([int(a), int(b)])
                
            if extract_tuple in board.get_empty_sqrs():
                get_tuple = False
            
        row = extract_tuple[0]
        col = extract_tuple[1]
        
        if board.empty_sqr(row, col) and game.running:
            game.make_move(row, col)

        # ai mode
        if game.gamemode == "ai" and game.player == ai.player and game.running:
            if not game.isover():
                row, col = ai.evaluate(board)
                game.make_move(row, col)

        if game.isover():
            print(game.result())
                
            game.running = False

            print("\n" + "-" * 50 + "\n")
            
            if input("Play again('y' to continue)? ").lower() == "y":
                clear()
                game = Game()
                board = game.board
                ai = game.ai


main()