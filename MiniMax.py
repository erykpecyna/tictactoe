import copy

def minicheck(gameboard):
        for row in gameboard:
            if row.count("X") == 3:
                return "X"
            if row.count("O") == 3:
                return "O"

        currCheck = []

        for i in range(3):
            for j in range(3):
                currCheck.append(gameboard[j][i])
            if currCheck.count("X") == 3:
                return 'X'
            if currCheck.count("O") == 3:
                return 'O'
            currCheck = []

        for i in range(3):
            currCheck.append(gameboard[i][i])
        if currCheck.count("X") == 3:
            return 'X'
        if currCheck.count("O") == 3:
            return 'O'

        currCheck = []
        for i in range(3):
            currCheck.append(gameboard[2-i][i])
        
        if currCheck.count("X") == 3:
            return 'X'
        if currCheck.count("O") == 3:
            return 'O'

        return 'T'

def minimax(game, turn):
        moves = set()
        for i in range(3):
            for j in range(3):
                if game[i][j]=="":
                    moves.add((i, j))

        if len(moves) is 0:
            if minicheck(game) == 'X':
                return 1
            elif minicheck(game) == 'O':
                return -1
            else:
                return 0
        else:
            if turn == 'X':
                value = -2
                for move in moves:
                    testboard = copy.deepcopy(game)
                    testboard[move[0]][move[1]] = 'X'
                    value = max(value, minimax(testboard, "O"))
            else:
                value = 2
                for move in moves:
                    testboard = copy.deepcopy(game)
                    testboard[move[0]][move[1]] = 'O'
                    value = min(value, minimax(testboard, "X"))
            return value
