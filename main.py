from ccny.corelabs.RateTimeSpan import RateTimeSpan
from ccny.corelabs.RateScheduleReader import RateScheduleReader


def analyze_usage():
    """Run the application"""
    print("UsageCapAnalyzer")
    rateSchedules = RateScheduleReader.loadRateSchedule('.\RateSchedule.json')
    print rateSchedules
    


if __name__ == "__main__":
    analyze_usage()
