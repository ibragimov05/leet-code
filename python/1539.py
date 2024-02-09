class Solution(object):
    @staticmethod
    def findKthPositive(arr, k):
        for each in arr:
            if each <= k:
                k += 1
            else:
                return k
        return k