class Solution(object):
    def countSymmetricIntegers(self, low, high):
        result = 0
        for i in range(low, high + 1):
            if len(str(i)) % 2 == 0:
                res1, res2 = 0, 0
                for j in range(len(str(i)) // 2):
                    res1 += int(str(i)[::-1][j])
                    res2 += int(str(i)[j])
                if res1 == res2:
                    result += 1
        return result
