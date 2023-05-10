import random

class GessNumberSimulator():
    def __init__(self):
        self.nameprogram = print('\033[1;34mGess Number Simulator\033[m')

    def Start(self):
        numbers = [7,8,10,11,55,23,65,85,91,0,12,78]
        chosen = random.choice(numbers)
        numberoftimes = 1
        while numberoftimes < 3:
            userchoice = int(input('Insert your gess > '))
            if choice == chosen:
                print('Congratulations! You ´ re right! ')
            elif choice > chosen:
                print('Almost there! It´s a bigger number!')


