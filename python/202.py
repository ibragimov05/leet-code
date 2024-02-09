class Solution(object):
    def isHappy(self, n):
        if n != 7 and n != 1 and len(str(n)) == 1:
            return False
        elif n == 1 or n == 7:
            return True

        while True:
            box = ''
            for i in str(n):
                box += i
            n = str(sum(pow(int(i), 2) for i in box))
            if n == '1':
                return True
            elif len(n) == 1 and n != '1' and n != '7':
                return False
