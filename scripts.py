from subprocess import run


def black():
    run(["python3", "-m", "black", "."])


def pytest():
    run(["python3", "-m", "pytest", "tests/"])


def flake():
    run(["python3", "-m", "flake8", "."])


def pylint():
    run(["python3", "-m", "pylint", "irclm/", "tests/"])


def isort():
    run(["python3", "-m", "isort", "."])


def tests():
    for test in (pytest,):
        test()


def format():
    for test in (black, isort, flake, pylint):
        test()


def all():
    tests()
    format()
