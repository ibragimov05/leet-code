class Solution:
    def reverseWords(self, s: str) -> str:
        box = s.split()
        box.reverse()
        return " ".join(s.split())
