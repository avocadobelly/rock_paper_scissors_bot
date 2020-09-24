# class PaperBot:
#     def __init__(self):
#         pass
#
#     def make_move(self, gamestate):
#         return 'P'

class RandomBot:
    def __init__(self):
        available_moves = ['R', 'P', 'S', 'W', 'D']
    def make_random_move(self, available_moves):
        return available_moves.choice()
