class Solution(object):
    @staticmethod
    def replaceDigits(s):
        let, res = 'abcdefghijklmnopqrstuvwxyz', ''
        for i in range(len(s)):
            if s[i].isdigit():
                res += let[let.index(s[s.index(s[i - 1])]) + int(s[i])]
            else:
                res += s[i]
        return res
