class Solution:
    def minimumSum(self, num: int) -> int:
        digits = [int(digit) for digit in str(num)]
        digits.sort(reverse=True)

        return (digits[0] + digits[1]) + (digits[2] + digits[3]) * 10        