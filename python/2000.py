class Solution(object):
    @staticmethod
    def reversePrefix(word, ch):
        if ch in word:
            ind = word.index(ch)
            box = word[ind::-1]
            word = box + word[ind + 1:]
            return word
        else:
            return word
