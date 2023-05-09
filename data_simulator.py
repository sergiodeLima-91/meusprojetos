import random

class DataSimulator:
    def __init__(self):
        self.minimum_value = 1
        self.maximum_value = 6
        self.message = 'Would you like to generate new value? > '
    
    def Start(self):
        answer = input(self.message)
        try:
            if answer == 'yes' or answer == 's':
                self.GerateDataValue()
            elif answer == 'no' or answer == 'n':
                print('Thanks for playing!')
            else:
                print('Please, choice yes or no.')
        except:
            print('There was an error receiving your reply.')
    
    
    def GerateDataValue(self):
        print(random.randint(self.minimum_value,self.maximum_value))

Playing = DataSimulator()
Playing.Start()

