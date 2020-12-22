import numpy as np
from Bots import RandomBot
import random


class Board:
    def __init__(self, x, y, player_count):
        self.x = x
        self.y = y

        # number of players
        self.player_count = player_count

        # count of any troop at each board tile
        self.count_board = np.zeros((y, x))

        # id of player who controls each board tile. 0 is no one
        self.player_board = np.zeros((y, x))

        # id of player nexus at each board tile. Mostly empty.
        self.nexus_board = np.zeros((y, x))

        # turn number
        self.turn = 0

        for player_id in range(1, player_count + 1):
            while True:
                rand_x, rand_y = random.randint(0, y-1), random.randint(0, x-1)
                if self.player_board[rand_x, rand_y] == 0:
                    self.player_board[rand_x, rand_y] = player_id
                    self.nexus_board[rand_x, rand_y] = player_id
                    break

    def move(self, player_id, x_start, x_end, y_start, y_end):
        if player_id != self.player_board[y_start][x_start]:
            return
        if abs(x_start - x_end) + abs(y_start - y_end) > 1:
            return
        if not (0 <= x_start < self.x and 0 <= x_end < self.x and 0 <= y_start < self.y and 0 <= y_end < self.y):
            return
        if self.player_board[y_end][x_end] == player_id:
            movable_units = max(self.count_board[y_start][x_start] - 1, 0)
            self.count_board[y_end][x_end] += movable_units
            self.count_board[y_start][x_start] -= movable_units
        else:
            movable_units = max(self.count_board[y_start][x_start] - 1, 0)
            self.count_board[y_start][x_start] -= movable_units
            self.count_board[y_end][x_end] -= movable_units
            if self.count_board[y_end][x_end] < 0:
                self.player_board[y_end][x_end] = player_id
                self.count_board[y_end][x_end] *= -1
        return

    def increment_turn(self):
        nexus_locations = self.nexus_board != 0
        self.count_board[nexus_locations] += 1
        if self.turn % 20 == 0:
            player_controlled_board = self.player_board != 0
            self.count_board[player_controlled_board] += 1
        self.turn += 1

    def __str__(self):
        return str(self.count_board)

def main():
    board = Board(6, 5, 2)
    bot_1 = RandomBot(1)
    bot_2 = RandomBot(2)
    for i in range(20):
        board.increment_turn()
        print(bot_1.make_move(board))
        print(board)
        print("______________________________")
        print(bot_2.make_move(board))
        print(board)
        print("______________________________")


if __name__ == "__main__":
    main()
