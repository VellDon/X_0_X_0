class S21_minmaks:
    def __init__(self, id, type):
        self.player = type
        self.game = 
        self.id = id
        self.matrix = ["", "", "", ""]
        self.win_line = [[0, 1], [1, 2], [2, 3]]



def WinLine(matrix):
    win_line = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [2, 4, 6],
    [0, 4, 8],
    ]
    for a, b, c in win_line:
        if matrix[a] != "" and matrix[a] == matrix[b] == matrix[c]:
            return matrix[a]
    return False

def MinMaks(matrix, type, number):
    
    matrix[number] = type
    newType = WinLine(matrix)

    if(newType):


    for i in range(len(matrix)):
        if(matrix[i] == ''):
            MinMaks(matrix, type, i)


class MinMaks:
    def __init__(self, flag, id, number):
        self.player = True
        self.id_game = id
        self.move = number
        self.matrix = ['', '', '', '']
        self.best_score = 0

    def Score(self, state):
        flag = False
        score = 0
        win_line = [[0, 1], [1, 2], [2, 3]]
        for a, b in win_line:
            if state[a] == state[b] != "":
                score = 10 if state[a] == '0' else -10
                return score
        for i in state:
            if i == "":
                flag = True
        if flag:
            return False
        else:
            return score
        
    def Recurs(self, move, flag):
        flag = not flag
        self.matrix[move] = 'x' if flag else '0'
        score = self.Score(self.matrix)
        if score != False:
            self.matrix[move] = ""
            return score
        
        best_score = float('inf') if flag else float('-inf')

        for i in range(len(self.matrix)):
            if self.matrix[i] == "":
                score = self.Recurs(i, flag)
                if flag:
                    if score < best_score:
                        best_score = score
                else:
                    if score > best_score:
                        best_score = score
        self.matrix[move] = ""
        return best_score

    def Main(self):
        best = float('-inf')
        index = -1
        for i in range(len(self.matrix)):
            if self.matrix[i] == "":
                score = self.Recurs(i, self.player)
                if score > best:
                    best = score
                    index = i
        return index
    
    def PlayerMove(self, move):
        if(self.matrix[move] == ""):
            self.matrix[move] = "x"
        else:
            print("error")

                    


        