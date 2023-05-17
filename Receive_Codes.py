import random 
import PySimpleGUI as sg

class GuessTheNumber:
    def __init__(self):
        self.random_value = 0
        self.mininum_value = 1
        self.maximum_value = 100
        self.try_again = True
    
    def Start(self):
        layout = [
            [sg.Text('Your guess',size=(39,0))],
            [sg.Input(size=(18,0),key='GuessValue')],
            [sg.Button('Guess!')],
            [sg.Output(size=(39,10))]
        ]
        
        self.window = sg.Window('Guess the number!',layout=layout)
        self.GenerateRandomNumber()
        try:
            while True:
                self.event, self.values = self.window.Read()
                if self.event == 'Guess!':
                    self.guess_value = self.values['GuessValue']
                    while self.try_again == True:
                        if int(self.guess_value) > self.random_value:
                            print('A little less!')
                            break
                        elif int(self.guess_value) < self.random_value:
                            print('A little more!')
                            break
                        if int(self.guess_value) == self.random_value:
                            self.try_again = False
                            print('CONGRATULATIONS! You right!')
                            break
                if self.event == sg.WIN_CLOSED:
                    break
        except:
            print('Please, insert only numbers!')
            self.Start()
            

    def GenerateRandomNumber(self):
        self.random_value =  random.randint(self.mininum_value, self.maximum_value)

guess = GuessTheNumber()
guess.Start()
