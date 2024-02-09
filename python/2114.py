class Solution(object):
    def mostWordsFound(self, sentences):
        box = []
        for i in sentences:
            box.append(i.count(" "))
        return max(box) + 1
