class Button:
    def __init__(self, command):
        self.command = command

    def click(self):
        self.command.execute()