import numpy as np
import random


class AbstractBot:
    def __init__(self, id):
        self.id = id

    def make_move(self, board):
        pass


class RandomBot(AbstractBot):
    def make_move(self, board):
        owned_tiles = board.player_board == self.id
        owned_tiles = owned_tiles.flatten()
        prob_tiles = np.zeros(board.y * board.x)
        prob_tiles[owned_tiles] = 1
        prob_tiles /= np.sum(prob_tiles)
        move = np.random.choice(board.y * board.x, p=prob_tiles)
        x_start = move % board.x
        y_start = int(move / board.x)
        x_end = x_start + random.randint(-1, 1)
        if x_end == x_start:
            y_end = y_start + random.randint(-1, 1)
        else:
            y_end = y_start
        board.move(self.id, x_start, x_end, y_start, y_end)
        return x_start, y_start, x_end, y_end
