import argparse

class BaseAdvCmd(argparse.ArgumentParser):
    def __init__(self):
        super().__init__(description="sqlgo")

    def add_arguments(self, action):
        action.add_argument(
            '--hh',
            dest='advanced_help',
            action='store_true',
            default=False,
            help='Show the helping menu'
        )
        super().add_argument(action)

class AdvCmd(BaseAdvCmd):
    def __init__(self):
        super(AdvCmd, self).__init__()



