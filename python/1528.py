class Solution(object):
    def restoreString(self, s, indices):
        d = (dict(sorted((dict(zip(indices, s))).items())))
        return "".join([val for i, val in d.items()])
