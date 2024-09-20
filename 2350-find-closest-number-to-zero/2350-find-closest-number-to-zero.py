class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        minimum = float('inf')
        res = 0

        for num in nums:
            if abs(num) < minimum:
                res = num
                minimum = abs(num)

            elif abs(num) == minimum:
                res = max(num, res)

        return res    