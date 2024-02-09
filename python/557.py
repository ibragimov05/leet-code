class Solution(object):
    def reverseWords(self, s):
        box, s = '', s.split()
        for i in s:
            box += i[::-1] + ' '
        return box[:-1]
