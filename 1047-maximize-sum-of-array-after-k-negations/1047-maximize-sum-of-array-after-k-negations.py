class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        idx = 0
        for i in range(len(nums)):
            if k > 0 and nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1
                idx += 1
            else:
                break

        nums.sort()
        if k & 1:
            nums[0] = -nums[0]

        return sum(nums)
        