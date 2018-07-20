from ccny.corelabs.RateTimeSpan import RateTimeSpan
from ccny.corelabs.RateScheduleReader import RateScheduleReader
from ccny.corelabs.Session import Session

from datetime import datetime
from datetime import timedelta

def findFirstRateTimeSpan(ratewindows, session):
    """
        ratewindows  List of RateTimeSpans
        session Session
    """
    dayofweek = session.start.weekday()
    sessionTime = session.start.time()
    hour = sessionTime.hour
    minute = sessionTime.minute

    startMinute = dayofweek * RateTimeSpan.DUR_DAY + hour * RateTimeSpan.DUR_ONE_HOUR + minute * RateTimeSpan.DUR_ONE_MINUTE

    i = 0

    # Find the first RateTimeSpan for the session
    while i < len(ratewindows):
        rWindow = ratewindows[i]
        if rWindow.end >= startMinute:
            break
        i = i + 1
    #print "d %s, H %s, m %s, %s, window %s" %  ( dayofweek, hour, minute, startMinute,i)

    return i


def analyze_usage():
    """Run the application"""
    print("UsageCapAnalyzer")
    rateSchedules = RateScheduleReader.loadRateSchedule('.\RateSchedule.json')
    print rateSchedules
    s = Session(datetime(2018,7,15,23,59),datetime(2018,7,19,11)  )
    print s.start
    windowIndex = findFirstRateTimeSpan(rateSchedules,s)
    print windowIndex


if __name__ == "__main__":
    analyze_usage()
