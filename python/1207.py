class Solution(object):
    def uniqueOccurrences(self, arr):
        result, unique_nums = [], set(arr)

        for num in unique_nums:
            number_count = arr.count(num)
            if number_count in result:
                return False
            result.append(arr.count(num))
        return True
