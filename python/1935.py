class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        res = 0
        for word in text.split():
            lamp = True
            for letter in brokenLetters:
                if letter in word:
                    lamp = False
                    break
            if lamp:
                res += 1
        return res
