class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dct = {}
        for name, height in zip(names, heights):
            dct[height] = name
        dct = dict(sorted(dct.items(), reverse=True))
        res = []
        for val in dct.items():
            res.append(val[1])
        return res
