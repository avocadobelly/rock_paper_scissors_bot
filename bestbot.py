import random

class RandomBot:
    global random
    def __init__(self):
        self.available_moves = ['R', 'P', 'S', 'W', 'D']
        self.dynamite_supply = 100

    def make_move(self, gamestate):
        choice = random.choice(self.available_moves)
        if choice == 'D':
            self.dynamite_supply_tracker()
        return choice

    def dynamite_supply_tracker(self):
        if self.dynamite_supply > 0:
            self.dynamite_supply = self.dynamite_supply - 1
        if self.dynamite_supply == 0:
            self.available_moves.remove('D')
