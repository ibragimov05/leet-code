class Solution(object):
    def findWords(self, words):
        return [word for word in words if (set(word.lower()).issubset(set("qwertyuiop")) or set(word.lower()).issubset(
            set("asdfghjkl")) or set(word.lower()).issubset(set("zxcvbnm")))]