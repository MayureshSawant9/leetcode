class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        while l < r:
            print(f'{l} {r}')
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            
            elif target < nums[mid]:
                r = mid
            
            else:
                l = mid + 1

        return l