class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def feasible(curr_day):
            flowers = 0
            bouquets = 0
            for bloomday in bloomDay:
                if bloomday <= curr_day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
                
            return bouquets >= m

        if len(bloomDay) < m * k:
            return -1

        left = min(bloomDay)
        right = max(bloomDay)
        min_day = 0

        while left <= right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid - 1                
                min_day = mid
            else:
                left = mid + 1

        return min_day