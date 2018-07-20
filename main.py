from ccny.corelabs.RateTimeSpan import RateTimeSpan
from ccny.corelabs.RateScheduleReader import RateScheduleReader
from ccny.corelabs.Session import Session
import sys

from datetime import datetime
from datetime import timedelta

def findFirstRateTimeSpan(ratewindows, session):
    """
        ratewindows  List of RateTimeSpans
        session Session
    """
    assert isinstance(session,Session)
    #TODO assert that ratewindows is an array

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
    print("UsageCapAnalyzer starting...")
    rateSchedules = RateScheduleReader.loadRateSchedule('.\\RateSchedule.json')
    
    if( len(rateSchedules) == 0):
        print("Empty rate schedule. Exiting")
        sys.exit(0)

    print("Rate Schedule Loaded with %s entries" % (len(rateSchedules)))
    s = Session(datetime(2018,7,15,23,59),datetime(2018,7,19,11)  )
    print s.start
    windowIndex = findFirstRateTimeSpan(rateSchedules,s)
    print windowIndex



if __name__ == "__main__":
    analyze_usage()
