class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        best = max(nums)
        return sum(i for i in range(best, best + k))
            