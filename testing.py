# class App2048:
#     def __init__(self): #initializing board
#         self.board = [[0] * 4, [2] * 4, [2] * 4,  [2] * 4] 

#     def __repr__(self):
#         string = f'''{self.board[0][0]} {self.board[0][1]} {self.board[0][2]} {self.board[0][3]}
# {self.board[1][0]} {self.board[1][1]} {self.board[1][2]} {self.board[1][3]} 
# {self.board[2][0]} {self.board[2][1]} {self.board[2][2]} {self.board[2][3]}
# {self.board[3][0]} {self.board[3][1]} {self.board[3][2]} {self.board[3][3]}
# '''

#         return string

#     def define(self, b):
#         self.board = b
    
#     def copy(self):
#         new_board = App2048()
#         return new_board
    
#     def check(self):
#         flat_board = [[cell for cell in row] for row in self.board]
#         for i in range(0,4):
#             for j in range(0,4):
#                 if flat_board[i][j] == 0:
#                     print('balls')
#                 if self.board[i][j] == 0:
#                     print('hi')

# def copying(boardnum):
#     new_board = boardnum.copy()
#     print(boardnum)
#     print(new_board)
#     if new_board == boardnum:
#         print('hi')
#     else:
#         print('balls')

# game1 = App2048()
# # copying(game1)
# game2 = game1.copy()
# print(game1.check())

controls = 'Game Controls:\n\
W:    Up\n\
A:    Left\n\
S:    Down\n\
D:    Right\n\
Q:    Quit'
sentences = [word for word in controls.splitlines()]
print(sentences)


