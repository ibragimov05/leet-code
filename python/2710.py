class Solution(object):
    def removeTrailingZeros(self, num):
        num, ind = num[::-1], 0
        for i in num:
            ind += 1
            if i == "0":
                continue
            else:
                break
        return (num[ind-1:])[::-1]
