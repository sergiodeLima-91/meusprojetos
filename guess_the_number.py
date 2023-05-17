import random
import PySimpleGUI as sg

class GessNumberSimulator():
    def __init__(self):
        self.randon_value = 0
        self.min_value = 1
        self.max_value = 60
        self.number_chances = 10

    def Start(self):
        # Layout
        '''layout = [
            [sg.Text('Your guess',size=(20,0))],
            [sg.Input(size=(18,0),key='GuessValue')],
            [sg.Button('Guess!')],
            [sg.Output(size=(20,10))]
        ]'''
        # create a window
        self.window = sg.Window('Guess Number Simulator')
        

        self.GenerateNumber()
        self.RequestNumber()
        try:
            while True:
                # receive the values
                self.event, self.values = self.window.Read()
            if self.event == 'Guess!':
                self.guess_value = self.values['GuessValue']
                while self.number_chances != 0:
                    if int(self.guess_value) > self.randon_value:
                        print(f'\033[1;32mA little less! (Number of chances: {self.number_chances})\033[m')
                        self.number_chances -= 1
                        self.RequestNumber()
                    elif int(self.guess_value) < self.randon_value:
                        print(f'\033[1;31mA little more! (Number of chances: {self.number_chances})\033[m')
                        self.number_chances -= 1
                        self.RequestNumber()
                    if int(self.guess_value) == self.randon_value:
                        self.try_again = False
                        print(f'\033[1;34m🎉🎉🎉 CONGRATULATIONS! The number chosen is {self.randon_value}! You ´ re right! 🎉🎉🎉\033[m')
                        break
                    if self.number_chances == 0:
                        print(f'\033[1;35m😢😢😢 What a shame! Your chances is over! This number chosen was {self.randon_value}! More luck in the next time!\033[m')
        except:
            print('\033[1;031mPlease insert only integers numbers!\033[m')

    def RequestNumber(self):
        self.guess_value = int(input('Guess any number: '))
    
    def GenerateNumber(self):
        self.randon_value = random.randint(self.min_value, self.max_value)
        

Guess1 = GessNumberSimulator()
Guess1.Start()