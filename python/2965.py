class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        box_ls = []
        for i in grid:
            for j in i:
                box_ls.append(j)

        box_ls, repeat_val, missed_val, = sorted(box_ls), 0, 0

        for i in range(min(box_ls), max(box_ls) + 1):
            if i not in box_ls:
                missed_val = i
            cnt = box_ls.count(i)
            if cnt > 1:
                repeat_val = i

        if missed_val == 0 and min(box_ls) == 1:
            missed_val = max(box_ls) + 1
        elif missed_val == 0 and min(box_ls) == 2:
            missed_val = min(box_ls) - 1
        return [repeat_val, missed_val]
