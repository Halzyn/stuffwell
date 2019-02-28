class CommandBase:
    def __init__(self, client, message):
        self.client = client
        self.message = message
