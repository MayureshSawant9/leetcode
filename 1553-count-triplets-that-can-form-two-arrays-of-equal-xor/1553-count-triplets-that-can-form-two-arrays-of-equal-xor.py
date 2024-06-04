class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        def defaultvalue():
            return 0
        count = collections.defaultdict(defaultvalue)
        idx_sum = collections.defaultdict(defaultvalue)
        count[0] = 1
        n = len(arr)
        ans = 0
        pre = 0

        for k in range(n):
            pre ^= arr[k]
            
          
            ans += count[pre] * k - idx_sum[pre]

            count[pre] += 1
            idx_sum[pre] += k + 1

        return ans