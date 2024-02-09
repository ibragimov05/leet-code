class Solution(object):
    @staticmethod
    def squareIsWhite(coordinates) -> bool:
        black = ['a', 'c', 'e', 'g']
        white = ['b', 'd', 'f', 'h']

        if coordinates[0] in black:
            if int(coordinates[1]) % 2 == 0:
                return True
            else:
                return False
        elif coordinates[0] in white:
            if int(coordinates[1]) % 2 == 0:
                return False
            else:
                return True