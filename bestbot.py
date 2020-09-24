import random

class RandomBot:
    def __init__(self):
        self.available_moves = ['R', 'P', 'S', 'W', 'D']

    def make_move(self, gamestate):
        return random.choice(self.available_moves)
