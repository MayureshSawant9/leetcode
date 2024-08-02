class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        win_size = nums.count(1)
        # nums.extend(nums[:win_size])
        one_count = sum(nums[:win_size])
        max_ones = one_count
        n = len(nums)

        for i in range(1, n):
            
            one_count += nums[(i + win_size) % n - 1] - nums[i-1]
            max_ones = max(max_ones, one_count)
                    
        return win_size - max_ones