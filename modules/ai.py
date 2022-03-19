import random
import copy


class AI:
    def __init__(self, level=2, player=2):
        """level 1 - random pick
           level 2 - minimize ai
        """
        self.level = level
        self.player = player

    def random_pick(self, board):
        empty_sqrs = board.get_empty_sqrs()
        return random.choice(empty_sqrs)

    def minimax(self, board, maximizing):
        #terminal case
        case = board.final_state()

        # player 1 wins
        if case == 1:
            return 1, None # evaluate, move

        # player 2 wins
        if case == 2:
            return -1, None  # evaluate, move

        # draw
        elif board.isfull():
            return 0, None  # evaluate, move

        if maximizing:
            max_eval = -100
            best_move = None
            empty_sqrs = board.get_empty_sqrs()

            for (row, col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_sqr(row, col, 1)
                evaluate = self.minimax(temp_board, False)[0]

                if evaluate > max_eval:
                    max_eval = evaluate
                    best_move = (row, col)
            return max_eval, best_move

        elif not maximizing:
            min_eval = 100
            best_move = None
            empty_sqrs = board.get_empty_sqrs()

            for (row, col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_sqr(row, col, self.player)
                evaluate = self.minimax(temp_board, True)[0]

                if evaluate < min_eval:
                    min_eval = evaluate
                    best_move = (row, col)
            return min_eval, best_move

    def evaluate(self, main_board):
        if self.level == 1:
            # random choice
            evaluate  ="random"
            move = self.random_pick(main_board)
        else:
            # minimize algo choice
            evaluate, move = self.minimax(main_board, False)

        print("AI chose...")

        return move





