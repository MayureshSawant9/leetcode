class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        idx = 0
        required = 1
        size = len(nums)
        
        while required <= n:
            if idx < size and nums[idx] <= required:
                required += nums[idx]
                idx += 1
            else:
                patches += 1
                required += required
                
        return patches







        