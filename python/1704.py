class Solution(object):
    @staticmethod
    def halvesAreAlike(s):
        part1, part2 = s[:len(s) // 2].lower(), s[len(s) // 2:].lower()
        vowels_in_part1, vowels_in_part2 = 0, 0

        for i in range(len(part1)):
            if part1[i] in "aeiou":
                vowels_in_part1 += 1
            if part2[i] in "aeiou":
                vowels_in_part2 += 1
        return vowels_in_part1 == vowels_in_part2
