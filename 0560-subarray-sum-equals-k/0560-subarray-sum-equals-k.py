class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = 0
        count = {}
        count[0] = 1
        result = 0

        for num in nums:
            pre_sum += num
            
            if pre_sum - k in count:
                result += count[pre_sum - k]    

            if pre_sum not in count:
                count[pre_sum] = 1
            else:
                count[pre_sum] += 1            
                    
        return result