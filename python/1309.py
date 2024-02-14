class Solution(object):
    def freqAlphabets(self, s):
        alphabet, res, i = 'abcdefghijklmnopqrstuvwxyz', '', 0
        box = ['10#', '11#', '12#', '13#', '14#', '15#', '16#', '17#', '18#',
               '19#', '20#', '21#', '22#', '23#', '24#', '25#', '26#']
        while i < len(s):
            if s[i:i + 3] in box:
                res += alphabet[int(s[i:i + 2]) - 1]
                i += 2
            else:
                res += alphabet[int(s[i]) - 1]
            i += 1
        return res
