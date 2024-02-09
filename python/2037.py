class Solution(object):
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        res = 0
        for i in zip(seats, students):
            if i[0] > i[1]:
                res += i[0] - i[1]
            else:
                res += i[1] - i[0]
        return res
