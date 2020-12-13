
import chess
import copy

from mesh import *
layer_sizes = [68, 120, 100, 50, 25, 10, 1] # 64 + 4 

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

        self.mesh.setInputValues([])
        # Input Fen to numeric and then push forward
        root.evaluation = 0


class Unit:

    def __init__(self, ID, position):
        self.ID = ID
        self.position = position
        
p = Position(0, None)
p.generate_move_tree(p, 2)

print('Done')