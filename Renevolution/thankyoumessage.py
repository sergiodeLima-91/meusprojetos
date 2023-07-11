class ThankYouMessage:
    def __init__(self):
        pass

    def message(self):
        print('\033[35mThanks for use this program!\033[m 😀')

closed_message = ThankYouMessage()
closed_message.message()
