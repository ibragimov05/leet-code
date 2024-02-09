class Solution(object):
    @staticmethod
    def findContentChildren(g, s):
        g.sort(), s.sort()
        i, j, res = 0, 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                res += 1
                i += 1
            j += 1
        return res
