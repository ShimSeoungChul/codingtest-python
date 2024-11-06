class Solution(object):
    def maxVowels(self, s, k):
        targets = s[0:k]
        length = len(s)
        max_vowl_num = self.findVowlNum(targets)
        current_vowl_num = max_vowl_num

        for i in range(0, length - k):
            current_vowl_num = current_vowl_num - 1 if self.isVowlLetter(s[i]) is True else current_vowl_num
            current_vowl_num = current_vowl_num + 1 if self.isVowlLetter(s[k+i]) is True else current_vowl_num
            max_vowl_num = max(max_vowl_num, current_vowl_num)

        return max_vowl_num

    def findVowlNum(self, letters):
        vowl_num = 0
        for letter in letters:
            if self.isVowlLetter(letter):
                vowl_num += 1
        return vowl_num

    def isVowlLetter(self, letter):
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            return True
        return False


solution = Solution()
assert solution.isVowlLetter(letter="a") is True
assert solution.isVowlLetter(letter="e") is True
assert solution.isVowlLetter(letter="i") is True
assert solution.isVowlLetter(letter="o") is True
assert solution.isVowlLetter(letter="u") is True
assert solution.isVowlLetter(letter="s") is False

assert solution.findVowlNum(letters="abce") == 2

assert solution.maxVowels(s="aeiousdf", k=5) == 5
assert solution.maxVowels(s="abciiidef", k=3) == 3
assert solution.maxVowels(s="aeiou", k=2) == 2
assert solution.maxVowels(s="leetcode", k=3) == 2
