class Solution(object):
    @staticmethod
    def dayOfYear(date):
        dct = {
            0: 0,
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }

        year, month, day = date.split("-")
        year, box = int(year), 0

        for i in range(1, int(month)):
            box += dct[i]

        if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) and int(month) > 2:
            return box + int(day) + 1
        return box + int(day)
