class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counts_s = Counter(s)
        counts_t = Counter(t)
        
        return sum((counts_s - counts_t).values())