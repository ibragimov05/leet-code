class Solution(object):
    def finalValueAfterOperations(self, operations):
        return sum((1 if each == '++X' or each == 'X++' else -1) for each in operations)
