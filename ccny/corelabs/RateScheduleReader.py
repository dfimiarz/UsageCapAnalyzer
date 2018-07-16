import json
import os.path
from ccny.corelabs.RateTimeSpan import RateTimeSpan

class RateScheduleReader:
    @staticmethod
    def loadRateSchedule(filepath):
        
        rateschedules = []

        print os.path.abspath(filepath)

        if os.path.isfile( filepath ) == False:
            return rateschedules;

        # print( "%s is file" % filepath)

        with open(filepath, 'r') as file:
            datastore = json.load(file)
        
        for rateschedule in datastore["schedule"]:
            start = (rateschedule["day"] * RateTimeSpan.DUR_DAY) + (rateschedule["start"] * RateTimeSpan.DUR_ONE_HOUR)
            rid = rateschedule['rid'].encode('utf8')
            rateschedules.append(RateTimeSpan(rid,start,rateschedule["duration"] * RateTimeSpan.DUR_ONE_HOUR))

        return rateschedules;
            
