class Solution(object):
    def totalMoney(self, n):
        box, cnt, ls = 0, 0, []
        for i in range(1, n + 1):
            box += 1
            ls.append(box)
            if i % 7 == 0:
                cnt += 1
                box = cnt
        return sum(ls)
