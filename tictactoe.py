class TicTacToe:
    def __init__(self, size):
        self.size = size
        self.board = [["","",""], ["","",""], ["","",""]]

    def move(self, row, col, play):
        self.board[row][col] = play

    def clear(self):
        self.board = [["","",""], ["","",""], ["","",""]]

    def check(self):
        for row in self.board:
            if row.count("X") == 3:
                return True
            if row.count("O") == 3:
                return True

        currCheck = []

        for i in range(3):
            for j in range(3):
                currCheck.append(self.board[j][i])
            if currCheck.count("X") == 3:
                return True
            if currCheck.count("O") == 3:
                return True
            currCheck = []

        for i in range(3):
            currCheck.append(self.board[i][i])
        if currCheck.count("X") == 3:
            return True
        if currCheck.count("O") == 3:
            return True

        currCheck = []
        for i in range(3):
            currCheck.append(self.board[2-i][i])
        
        if currCheck.count("X") == 3:
            return True
        if currCheck.count("O") == 3:
            return True

        return False