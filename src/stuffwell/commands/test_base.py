from .commands_dict import commands_dict
from .command_definitions.sleep import Sleep


def test_choose_command():
    sleep = commands_dict.get("!sleep")
    assert sleep == Sleep
