class Solution(object):
    def countKeyChanges(self, s):
        st = s.lower()
        return sum(1 for i in range(len(st) - 1) if st[i] != st[i + 1])
