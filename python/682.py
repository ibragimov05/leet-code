class Solution(object):
    def calPoints(self, operations):
        ls = []
        for i in range(len(operations)):
            if operations[i].isdigit() or (operations[i][0] == '-' and operations[i][1:].isdigit()):
                ls.append(int(operations[i]))
            elif operations[i] == "C":
                ls.pop()
            elif operations[i] == "D":
                ls.append(2 * int(ls[-1]))
            elif operations[i] == "+":
                ls.append(ls[-1] + ls[-2])
        return sum(i for i in ls)
