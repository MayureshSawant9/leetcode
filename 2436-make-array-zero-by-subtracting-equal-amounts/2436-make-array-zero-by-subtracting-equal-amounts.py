class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        large = nums[-1]
        min_ops = 0
        curr_min = 0
        for num in nums:
            if num > curr_min:
                min_ops += 1
                curr_min = num

        return min_ops