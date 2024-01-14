import argparse

class BaseAdvCmd(argparse.ArgumentParser):
    def __init__(self):
        super().__init__(description="advsqlgo")

    def add_arguments(self,action):
        action.append(argparse._StoreTrueAction(
        option_strings=['--hh'],
        dest='advaned_help',
        default=False,
        help='Show the helping menu'
        ))
        super().add_arguments(action)

class AdvCmd(BaseAdvCmd):
    def __init__(self):
        super().__init__()
        self.add_argument("--shell",help="execute sqlgo in shell environment",required=False)
        self.add_argument("--update",help="update sqlgo",required=False)
        self.add_argument("--beep",help="beep when vulnerability info appeared.",required=False)
        self.add_argument("--no-prompt",help="do not show user any prompt unless found important info.",required=False)
        
        