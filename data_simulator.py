import random, PySimpleGUI as sg

class DataSimulator:
    def __init__(self):
        self.minimum_value = 1
        self.maximum_value = 6
        self.message = 'Would you like to generate new value? > '

        self.layout=  [
            [sg.Text('Playing the data?')],
            [sg.Button('yes'), sg.Button('no')]
        ]
    
    def Start(self):
        self.window = sg.Window('Data Simulator',layout=self.layout)
        self.events, self.values = self.window.Read()
        try:
            if self.events == 'yes' or self.events == 'y':
                self.GerateDataValue()
            elif self.events == 'no' or self.events == 'n':
                print('Thanks for playing!')
            else:
                print('Please, choice yes or no.')
        except:
            print('There was an error receiving your reply.')
    
    
    def GerateDataValue(self):
        print(random.randint(self.minimum_value,self.maximum_value))

Playing = DataSimulator()
Playing.Start()
