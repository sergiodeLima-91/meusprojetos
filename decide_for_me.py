from random import choice
import PySimpleGUI as sg

class DecideForMe:
    def __init__(self):
        self.answers = [
            'Yes! Do it!',
            'No! Don´t do this!',
            'I don´t know answer this question.',
            'I´m not in the mood to talk today.'
        ]
    def Start(self):
                                    
        layout = [
            [sg.Text('Your question:')],
            [sg.Input(size=(18,0), key='QuestionValue')],
            [sg.Button('Ask!')],
            [sg.Output(size=(20,10))]
        ]
                                    
        self.window = sg.Window('Decide for Me', layout=layout)

        try:
            while True:
                self.event, self.values = self.window.Read()
                self.ReceiveQuestion()
                if self.event == 'Ask!':
                    print(choice(self.answers))
        except:
             print('Please, enter a valid question.')
             self.Start()
             
    def ReceiveQuestion(self):
         input('What this your question? > ')
         


question = DecideForMe()
question.Start()