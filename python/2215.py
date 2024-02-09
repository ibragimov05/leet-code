class Solution(object):
    def findDifference(self, nums1, nums2):
        res = []
        ls = []
        for i in nums1:
            if i not in nums2:
                ls.append(i)
        res.append(set(ls))
        ls = []
        for i in nums2:
            if i not in nums1:
                ls.append(i)
        res.append(set(ls))
        return res
