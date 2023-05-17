from random import choice

class DecideForMe:
    def __init__(self):
        self.answers = [
            'Yes! Do it!',
            'No! Don´t do this!',
            'I don´t know answer this question.',
            'I´m not in the mood to talk today.'
        ]
    
    def Start(self):
        input('What this your question? > ')
        print(choice(self.answers))

question = DecideForMe()
question.Start()