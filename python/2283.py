class Solution:
    def digitCount(self, num: str) -> bool:
        i = 0
        for dig in num:
            box = num.count(str(i))
            if dig != str(box):
                return False
            i += 1
        return True
