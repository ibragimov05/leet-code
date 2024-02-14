class Solution(object):
    def similarPairs(self, words):
        return sum(1 for i in range(len(words)) for j in range(i) if set(words[i]) == set(words[j]))
