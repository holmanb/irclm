import subprocess

import pytest


@pytest.mark.parametrize(
    ("command", "rc"),
    (
        (["--version"], 0),
        (["--help"], 0),
        (["---version"], 1),
        (["-", "pwd"], 0),
    ),
)
def test_commands(command, rc):
    assert rc == subprocess.run(["irclm/irclm.py", *command]).returncode
