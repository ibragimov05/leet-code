class Solution(object):
    @staticmethod
    def decodeMessage(key, message):
        i, d, decoded_message, alpha = 0, {" ": " ", }, "", "abcdefghijklmnopqrstuvwxyz"
        for char in key:
            if char not in d:
                d[char] = alpha[i]
                i += 1
        for char in message:
            if char == " ":
                decoded_message += " "
            else:
                decoded_message += d[char]
        return decoded_message
