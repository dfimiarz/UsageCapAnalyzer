import json
import os.path
from ccny.corelabs.RateTimeSpan import RateTimeSpan

class RateScheduleReader:
    @staticmethod
    def loadRateSchedule(filepath):
        
        rateschedules = []

        fullPath = os.path.abspath(filepath)

        print( "Reading Rate Schedule from: '%s ...' " % fullPath) 

        if os.path.isfile( fullPath ) == False:
            return rateschedules

        with open(filepath, 'r') as file:
            datastore = json.load(file)
        
        for rateschedule in datastore["schedule"]:
            start = (rateschedule["day"] * RateTimeSpan.DUR_DAY) + (rateschedule["start"] * RateTimeSpan.DUR_ONE_HOUR)
            rid = rateschedule['rid'].encode('utf8')
            rateschedules.append(RateTimeSpan(rid,start,rateschedule["duration"] * RateTimeSpan.DUR_ONE_HOUR))

        return rateschedules
            
