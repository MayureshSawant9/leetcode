import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))

        max_heap = []
        n = len(profits)
        idx = 0

        for _ in range(k):
            while idx < n and projects[idx][0] <= w:
                heapq.heappush(max_heap, (-1) * projects[idx][1])
                idx += 1

            if not max_heap:
                return w
            
            w += heapq.heappop(max_heap) * (-1)

        return w
            
