class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:

        MOD = 10**9 + 7
        min_heap = [(num, index) for index, num in enumerate(nums)]
        heapq.heapify(min_heap)

        res = 0
        for i in range(right):
            num, index = heapq.heappop(min_heap)
            if i >= left - 1:
                res = (res + num) % MOD
            if index + 1 < n:
                pair = ((num + nums[index + 1]) % MOD, index + 1)
                heapq.heappush(min_heap, pair)

        return res