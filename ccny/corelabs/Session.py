from datetime import datetime

class Session:
    """
    Class captures the start and end time of equipment session in a fcility
    """

    def __init__(self,start,end):
        assert type( start ) is datetime, "Session start must be a valid dattime object"
        assert type( end ) is datetime, "Session end must be a valid dattime object"
        assert start <= end, "Start must be before end"
        self._start = start
        self._end = end

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, val):
        self._start = val
    
    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, val):
        self._end = val

    def __repr__(self):
        return 'Session start: %s, end: %s' % (self._start,self._end)
