class Solution(object):
    @staticmethod
    def sortVowels(s):
        box, res, vowels, ls = "", "", "AEIOUaeiou", []

        for i in s:
            if i in vowels:
                ls.append(i)
                box += "_"
            else:
                box += i
        ls.sort()
        for i in box:
            if i == "_":
                res += ls[0]
                ls.pop(0)
            else:
                res += i
        return res
