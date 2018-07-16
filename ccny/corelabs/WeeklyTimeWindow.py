

class WeeklyTimeWindow:
    """
    Represents a time window in a week.
    Time measured in week minutes with Monday being the first day in a week.
    WeeklyTimeWindow(0,60) represents Mon 12 am - Mon 1 am
    """

    MAX_END = 10080

    def __init__(self, start, end):
        assert (0 <= start <= self.MAX_END), "Start value of our range"
        assert (0 <= end <= self.MAX_END), 'End value of our range'
        assert (start < end), 'Start must be less then end'

        self.start = start
        self.end = end
