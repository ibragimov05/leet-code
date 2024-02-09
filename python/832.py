class Solution(object):
    def flipAndInvertImage(self, image):
        res = []
        for arr in image:
            ls = []
            for num in arr:
                if num == 1:
                    ls.append(0)
                else:
                    ls.append(1)
            res.append(reversed(ls))
        return res
