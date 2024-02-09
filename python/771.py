class Solution(object):
    @staticmethod
    def numJewelsInStones(jewels, stones):
        return sum(1 for let in stones if let in jewels)
