import random

class GessNumberSimulator():
    def __init__(self):
        self.nameprogram = print('\033[1;34mGess Number Simulator\033[m')

    def Start(self):
        self.numbers = [random.choice(0,50)]

Choice = GessNumberSimulator()
Choice.nameprogram
