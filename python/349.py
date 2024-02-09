class Solution(object):
    @staticmethod
    def intersection(nums1, nums2):
        set1, set2 = set(nums1), set(nums2)
        res = []

        for num in set1:
            if num in set2:
                res.append(num)
        return res
