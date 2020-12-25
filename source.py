
import chess
import copy

from mesh import *
layer_sizes = [64, 120, 100, 50, 25, 10, 1] # 64 + 4 

class Position:

    def __init__(self, ID, board):
        self.ID = ID
        if(board):
            self.board = board
        else:
            self.board = chess.Board()

        self.children = []
        self.mesh = Net(layer_sizes)
        self.evaluation = 0

    def generate_move_tree(self, root, depth, count = 0):
        if(count == depth):
            return

        # Depth First
        '''
        for i, move in enumerate(root.board.legal_moves):
            child = Position(i, copy.copy(root.board))
            child.board.push_san(str(move))
            root.children.append(child)
            root.children[i].generate_move_tree(root.children[i], depth, count+1)
        '''

        # Breadth First
        for i, move in enumerate(root.board.legal_moves):
            child = Position(i, copy.copy(root.board))
            child.board.push_san(str(move))
            root.children.append(child)

        for i in range(len(root.children)):
            root.children[i].generate_move_tree(root.children[i], depth, count+1)

    def evaluate(self, root):

        input_values = self.fen_to_int_array(root.fen)
        self.mesh.setInputValues(input_values)
        self.mesh.pushForward()
        root.evaluation = self.mesh.outputs()

        print(root.evaluation)


    def fen_to_int_array(self, fen):
        master_count = 0
        arr_index = 0
        piece_ammounts = ['_', 'p','n','b','r','q','k','P','N','B','R','Q','K',]
        int_arr = [0 for _ in range(64)]
        FEN = str(fen).split('\'')[1]

        while(FEN[master_count] != ' '):
            char = FEN[master_count]

            if(char != '/'):
                if(char.isalpha()):
                    int_arr[arr_index] = piece_ammounts.index(char)
                    arr_index+=1
                else:
                    for _ in range(int(char)):
                        int_arr[arr_index] = 0
                        arr_index+=1
            
            master_count+=1

        return int_arr
        
    def int_array_to_fen(self, int_arr):
        return

class Unit:

    def __init__(self, ID, position):
        self.ID = ID
        self.position = position
        
p = Position(0, None)
p.generate_move_tree(p, 1)
p.evaluate(p.board)
p.evaluate(p.children[0].board)
print('Done')
