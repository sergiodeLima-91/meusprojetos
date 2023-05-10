from random import Random, randint, choice
import PySimpleGUI as sg

class GessNumberSimulator():
    def __init__(self):
        self.nameprogram = print('\033[1;34mGess Number Simulator\033[m')
    
        self.layout = [
            [sg.Text('Insert your gess [1 to 60] > ')]
            [sg.Button('click here')]

        ]

    def Start():
        window = sg.Window('Guess Number Simulator',layout= layout)
        chosen = randint(1,60)
        numberofchances = 10
        print(f'')
        try:
            while numberofchances > 0:
                userchoice = int(input('Insert your gess [1 to 60] > '))
                if userchoice == chosen:
                    print('Congratulations! You ´ re right! ')
                    break
                elif userchoice < chosen:
                    print('Almost there! It´s a bigger number!')
                    numberofchances -= 1
                    if numberofchances != 0:
                        print(f'You can try more {numberofchances} time(s)')
                elif userchoice > chosen:
                    print('A little less!')
                    numberofchances -= 1
                    if numberofchances != 0:
                        print(f'You can try more {numberofchances} time(s)')
        except:
            print('There was an error receiving your reply.')
        print(f'What a shame, your chances is over! The number chosen is {chosen} Try again and good luck in the next time!')

GessNumberSimulator()
Guess1 = GessNumberSimulator.Start()
