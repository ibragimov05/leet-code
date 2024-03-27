class Solution:
    def maximumValue(self, strs: list[str]) -> int:
        return max([int(i) if i.isdigit() else len(i) for i in strs])
