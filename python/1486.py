class Solution(object):
    @staticmethod
    def xorOperation(n, start):
        box, ans = [], 0

        for i in range(n):
            box.append(start + 2 * i)
        for i in box:
            ans = ans ^ i
            print(ans)
        return ans
