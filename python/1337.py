class Solution(object):
    @staticmethod
    def kWeakestRows(mat, k):
        ls, res = [], []
        for i in range(len(mat)):
            ls.append(mat[i].count(1))
        for i in range(k):
            num_ind = ls.index(min(ls, key=lambda x: x if x != -1 else float('inf')))
            res.append(num_ind)
            ls[num_ind] = -1
        return res
