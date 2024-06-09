from math import comb

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        pre_sum = 0
        count = {}
        count[0] = 1
        result = 0

        for element in nums:
            pre_sum = (pre_sum + element) % k 

            if count.get(pre_sum):
                result += count[pre_sum]
                count[pre_sum] += 1

            else:
                count[pre_sum] = 1
          
        return result