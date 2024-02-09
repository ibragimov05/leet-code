class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        dct_val = {
            'type': 1,
            'color': 2,
            'name': 3,
        }
        x = dct_val.get(ruleKey)
        return sum(1 for i in items if ruleValue == i[x - 1])
