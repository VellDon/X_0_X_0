class MinMaks:
    def __init__(self):
        self.win_line = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [2, 4, 6],
            [0, 4, 8],
        ]

    def Score(self, state):
        flag = False
        score = 0

        for a, b, c in self.win_line:
            if state[a] == state[b] == state[c] != "":
                score = 10 if state[a] == "0" else -10
                return score
        for i in state:
            if i == "":
                flag = True
        if flag:
            return "continue"
        else:
            return score

    def Recurs(self, move, flag, matrix):
        flag = not flag
        matrix[move] = "x" if flag else "0"
        score = self.Score(matrix)
        if score != "continue":
            matrix[move] = ""
            return score

        best_score = float("-inf") if flag else float("inf")

        for i in range(len(matrix)):
            if matrix[i] == "":
                score = self.Recurs(i, flag, matrix)
                if flag:
                    if score > best_score:
                        best_score = score
                else:
                    if score < best_score:
                        best_score = score
        matrix[move] = ""
        return best_score

    def Main(self, matrix):
        player = True
        best = float("-inf")
        index = -1
        for i in range(len(matrix)):
            if matrix[i] == "":
                score = self.Recurs(i, player, matrix)
                if score > best:
                    best = score
                    index = i
        print(f"ОТВЕТНЫЙ ХОД - {index}")
        
        return index

    def PlayerMove(self, domain_model):
        move = domain_model.index
        matrix = domain_model.matrix
        print(f"MATRIX START - {matrix}")
        print(f"Ход игрока индекс: {move}")
        if matrix[move] == "":
            matrix[move] = "x"
            result = self.Winer(matrix)
            if(result == "continue"):
                bot_move = self.Main(matrix)
                matrix[bot_move] = "0"
                domain_model.init_matrix(matrix)
                domain_model.bot(bot_move)
                result = self.Winer(matrix)
                domain_model.Win(result)
            else:
                domain_model.Win(result)
            print(f"MATRIX END - {matrix}")
            return 1
        else:
            print("error")
            return 0
        
    def Winer(self, state):
        for a, b, c in self.win_line:
            if state[a] == state[b] == state[c] != "":
                winner = "player" if state[a] == "x" else "bot"
                return winner
        flag = False 
        for i in state:
            if i == "":
                flag = True
                break
        if(not flag):
            winner = "draw"
            return winner
        else:
            return "continue"
