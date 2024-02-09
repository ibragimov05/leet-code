class Solution(object):
    @staticmethod
    def interpret(command):
        dct = {'G': 'G',
               '()': 'o',
               '(al)': 'al'
               }
        ls = []
        st = ""
        for i in command:
            st += i
            if st in dct:
                ls.append(dct[st])
                st = ""

        return ''.join(ls)