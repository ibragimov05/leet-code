class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        res = arrivalTime + delayedTime
        if res < 24:
            return res
        return res - 24
