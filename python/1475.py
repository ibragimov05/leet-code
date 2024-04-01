class Solution(object):
    @staticmethod
    def finalPrices(prices):
        res = []
        for i in range(len(prices)):
            lamp = False
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    res.append(prices[i] - prices[j])
                    lamp = True
                    break
            if not lamp:
                res.append(prices[i])
        return res
