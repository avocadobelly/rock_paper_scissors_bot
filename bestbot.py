import random


class MyBot:
    global random

    def __init__(self):
        self.available_moves = ['R', 'P', 'S']
        self.opponent_used_moves = {'R': 0, 'P': 0, 'S': 0, 'D': 0, 'W': 0}
        self.dynamite_supply = 100

    def make_move(self, gamestate):
        rounds = gamestate['rounds']
        if rounds:
            opponents_previous_move = rounds[- 1]['p2']
            my_bot_previous_move = rounds[- 1]['p2']

            # Add/update opponents last move in a dictionary:
            self.track_opponents_move(opponents_previous_move)
            # Sort the used moves dictionary by frequency of move:
            self.sort_by_frequency(self.opponent_used_moves)
            if str(opponents_previous_move) == str(my_bot_previous_move) and self.dynamite_supply >= 1:
                self.use_dynamite()

            choice = random.choice(self.available_moves)
        else:
            choice = self.use_dynamite()
        return choice

    def dynamite_supply_tracker(self):
        if self.dynamite_supply > 0:
            self.dynamite_supply = self.dynamite_supply - 1
        return self.available_moves

    def use_dynamite(self):
        dynamite = 'D'
        self.dynamite_supply_tracker()
        return dynamite

    def track_opponents_move(self, move):
        self.opponent_used_moves[move] += 1

    def sort_by_frequency(self, moves):
        used_moves = moves.items()
        sorted_moves = sorted(used_moves, key= lambda item: item[1])
        most_frequent_move = sorted_moves[0]
        return most_frequent_move

