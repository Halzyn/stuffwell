import hashlib
from ..base import CommandBase


class MarkovCommands(CommandBase):
    def __init__(self, client, message):
        super().__init__(client, message)

    async def run_command(self):
        completed_lines_hash = set()
        output_file = open("./markov/brain.txt", "w")
        for line in open("./markov/brain.txt", "r"):
            hashValue = hashlib.md5(line.rstrip().encode("utf-8")).hexdigest()
            if hashValue not in completed_lines_hash:
                output_file.write(line)
                completed_lines_hash.add(hashValue)
        output_file.close()
