class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        win_size = nums.count(1)
        nums.extend(nums[:win_size])
        max_ones = float('-inf')
        one_count = 0
        for i in range(win_size):
            if nums[i]:
                one_count += 1

        print()

        i, j = 0, win_size

        while j < len(nums):
                
            if not nums[i] and nums[j]:
                one_count += 1
            elif nums[i] and not nums[j]:
                one_count -= 1
            max_ones = max(max_ones, one_count)
            i += 1
            j += 1

        return win_size - max_ones