class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        sum_half = sum(nums) // 2
        sub_sum = 0
        for index, element in enumerate(nums):
            sub_sum += element
            if sub_sum > sum_half:
                return nums[:index + 1]



        