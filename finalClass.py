class App2048:
    #initializing board
    def __init__(self):
        self.board = [[0] * 4] * 4

    def __repr__(self):
        print(*self.board, sep = " ")

    def right(self):
        for column in range(4):
            for row in range(4):
                if self.board[row][column] == 0:
                    for num in range(row,-1):
                        if num != 0:



                

game1 = App2048()
print(game1)