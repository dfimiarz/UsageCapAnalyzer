from WeeklyTimeWindow import WeeklyTimeWindow
from types import StringType


class RateTimeSpan(WeeklyTimeWindow):
    """ Weekly time span for a particular rate

        duration -- duration of time span in minutes
        start    -- start time in week minutes

    """
    DUR_ONE_MINUTE = 1
    DUR_ONE_HOUR = 60
    DUR_HALF_DAY = 60 * 12
    DUR_DAY = 60 * 24
    DUR_WEEK = 60 * 24 * 7

    def __init__(self, rateid, start, duration):
        assert type(rateid) is StringType, 'rateid must be a string'
        WeeklyTimeWindow.__init__(self, start, start + duration)
        self.rateid = rateid

    def __repr__(self):
        return 'Rate: %s, start: %s end: %s' % (self.rateid, self.start, self.end)
