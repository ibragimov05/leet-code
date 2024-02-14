class Solution(object):
    def areOccurrencesEqual(self, s):
        strict = s.count(s[0])
        for i in s:
            if strict != s.count(i):
                return False
        return True
