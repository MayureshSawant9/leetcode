class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = [0] * 52
        length = 0

        for char in s:
            if count[ord(char) - ord('a')]:
                count[ord(char) - ord('a')] -= 1
                length +=2
            else:
                count[ord(char) - ord('a')] += 1

        return length + 1 if 1 in count else length
        