class Solution(object):
    @staticmethod
    def finalString(s):
        ls = []
        for letter in s:
            if letter == 'i':
                ls.reverse()
            else:
                ls.append(letter)
        return "".join(ls)
