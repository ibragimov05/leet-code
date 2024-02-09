class Solution(object):
    @staticmethod
    def sortSentence(s):
        s = s[::-1]
        sentence = sorted(s.split())
        box, res = "", ""
        for i in sentence:
            box += i[::-1]
        for i in box:
            if not i.isdigit():
                res += i
            else:
                res += " "
        return res[:-1]
