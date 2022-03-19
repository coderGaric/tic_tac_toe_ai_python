class Board:
    rows = 3
    cols = 3
    
    def __init__(self):
        self.squares = [[0 for _ in range(self.rows)] for _ in range(self.cols)]
        self.empty_sqrs = self.squares
        self.marked_sqrs = 0

    def final_state(self):
        """ return 0 if there is no win yet
            return 1 if player 1 wins
            return 2 if player 2 wins
        """
        # vertical wins
        for col in range(self.cols):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                return self.squares[0][col]

        # row wins
        for row in range(self.rows):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                return self.squares[row][0]

        # desc diagonal
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            return self.squares[1][1]

        # asc diagonal
        if self.squares[0][2] == self.squares[1][1] == self.squares[2][0] != 0:
            return self.squares[1][1]

        # no win yet
        return 0

    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player
        self.marked_sqrs += 1

    def empty_sqr(self, row, col):
        return self.squares[row][col] == 0

    def get_empty_sqrs(self):
        empty_sqrs = []
        
        for row in range(self.rows):
            for col in range(self.cols):
                if self.empty_sqr(row, col):
                    empty_sqrs.append((row, col))
        return empty_sqrs

    def isfull(self):
        return self.marked_sqrs == 9

    def isempty(self):
        return self.marked_sqrs == 0