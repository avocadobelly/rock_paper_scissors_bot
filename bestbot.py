import random

class MyBot:
    global random
    def __init__(self):
        self.available_moves = ['R', 'P', 'S', 'D']
        self.dynamite_supply = 100
        # self.opponents_used_dynamite = 0
        self.opponent_used_moves = {}
        self.opponent_used_moves['R'] = 0
        self.opponent_used_moves['P'] = 0
        self.opponent_used_moves['S'] = 0
        self.opponent_used_moves['D'] = 0
        self.opponent_used_moves['W'] = 0


    def make_move(self, gamestate):

        rounds = gamestate['rounds']

        if rounds:
            opponents_previous_move = rounds[- 1]['p2']
            if opponents_previous_move == 'D':
                self.opponent_used_moves['D'] += 1

            # Only add water to available moves once opponent has used their first dynamite
            if self.opponent_used_moves['D'] == 20:
                self.available_moves.append('W')

            # If opponent has used all their dynamite, remove water from available moves
            if self.opponent_used_moves['D'] == 50 and 'W' in self.available_moves:
                self.available_moves.remove('W')

            choice = random.choice(self.available_moves)
            if choice == 'D':
                self.dynamite_supply_tracker()

        else:
            choice = 'D'
            self.dynamite_supply_tracker()
        return choice

    def dynamite_supply_tracker(self):
        if self.dynamite_supply > 0:
            self.dynamite_supply = self.dynamite_supply - 1
        if self.dynamite_supply == 0:
            self.available_moves.remove('D')
        return self.available_moves

    # def least_frequent_move(self, opponent_used_moves):
    #     # sort opponents moves by ascending frequency:
    #     opponent_moves = opponent_used_moves.items()
    #
    #     return least_frequent_move_made
