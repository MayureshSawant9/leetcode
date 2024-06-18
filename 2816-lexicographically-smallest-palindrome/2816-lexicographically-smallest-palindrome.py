class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        letter_list = list(s)
        while left <= right:
            if letter_list[left] < letter_list[right]:
                letter_list[right] = letter_list[left]
                
            elif letter_list[left] > letter_list[right]:
                letter_list[left] = letter_list[right]

            left += 1
            right -= 1        

        return ''.join(letter_list)