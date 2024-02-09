class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        return sum(1 for i in endTime if i >= queryTime)


s = Solution()
print(s.busyStudent([1, 2, 3], [3, 2, 7], 4))
# Example 1:
#
# Input: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
# Output: 1
# Explanation: We have 3 students where:
# The first student started doing homework at time 1 and finished at time 3 and wasn't doing anything at time 4.
# The second student started doing homework at time 2 and finished at time 2 and also wasn't doing anything at time 4.
# The third student started doing homework at time 3 and finished at time 7 and was the only student doing homework at time 4.
# Example 2:
#
# Input: startTime = [4], endTime = [4], queryTime = 4
# Output: 1
# Explanation: The only student was doing their homework at the queryTime.
