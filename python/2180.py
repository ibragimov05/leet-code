class Solution(object):
    def countEven(self, num):
        res = []
        for i in range(1, num + 1):
            num_sum = 0
            for j in str(i):
                num_sum += int(j)
            if num_sum % 2 == 0:
                res.append(i)

        return len(res)
