import pandas as pd


class CommsIssueFilter:
    def __init__(self):
        self.comms_issue: bool = False

    def filter(self, window):
        pass


def run():
    x = pd.Series()
    comms_issue_filter = CommsIssueFilter()
    x.window().rolling(comms_issue_filter)
