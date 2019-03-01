class CommandBase:
    def __init__(self, client, message):
        self.client = client
        self.message = message

    async def run_command():
        """Runs a command."""
        raise NotImplementedError()
