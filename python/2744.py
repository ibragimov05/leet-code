class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        return sum(1 for i in range(len(words)) for j in range(i) if words[i] == words[j][::-1])
