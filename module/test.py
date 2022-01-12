
from .Test.test import run_test
from .Test.test_lib import defineArguments, processInput

availableTests = {
    "buildmodel": run_test
}


def init():
    # DO NOT CHANGE FROM THIS POINT BELOW
    # UNLESS YOU KNOW WHAT YOUR DOING
    args = defineArguments(availableTests)

    processInput(args, availableTests)
