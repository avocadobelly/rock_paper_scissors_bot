import random

class RandomBot:
    global random
    def __init__(self):
        self.available_moves = ['R', 'P', 'S', 'W', 'D']
        self.dynamite_supply = 100
        self.opponents_used_dynamite = 0
        self.opponent_used_moves = []

    def make_move(self, gamestate):
        #check if opponent has used all dynamite:

        rounds = gamestate['rounds']

        if rounds:
            opponents_previous_move = rounds[- 1]['p2']
            if opponents_previous_move == 'D':
                self.opponent_dynamite_tracker()
            self.opponent_used_moves.append(opponents_previous_move)

        #If opponent has used all thier dynamite, remove water from available moves
        if self.opponents_used_dynamite == 100 and 'W' in self.available_moves:
            self.available_moves.remove('W')

        choice = random.choice(self.available_moves)
        if choice == 'D':
            self.dynamite_supply_tracker()

        return choice

    def dynamite_supply_tracker(self):
        if self.dynamite_supply > 0:
            self.dynamite_supply = self.dynamite_supply - 1
        if self.dynamite_supply == 0:
            self.available_moves.remove('D')
        return self.available_moves

    def opponent_dynamite_tracker(self):
        if self.opponents_used_dynamite < 100:
            self.opponents_used_dynamite = self.opponents_used_dynamite + 1
