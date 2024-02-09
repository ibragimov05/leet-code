class Solution(object):
    def checkIfPangram(self, sentence):
        sentence, alphabet = sentence.upper(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in alphabet:
            if i not in sentence:
                return False
        return True
