class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        prices.sort()
        mon = money - prices[0]
        if mon - prices[1] >= 0:
            return mon - prices[1]
        else:
            return money
