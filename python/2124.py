class Solution:
    def checkString(self, s: str) -> bool:
        box1, cnt = s[0], 0
        for i in range(len(s)):
            if box1 != s[i]:
                cnt += 1
                box1 = s[i]
                if cnt == 2 or box1 == 'a':
                    return False
        return True
