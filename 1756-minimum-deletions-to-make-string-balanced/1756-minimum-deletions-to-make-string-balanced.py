class Solution:
    def minimumDeletions(self, s: str) -> int:
        t_a = sum(1 for c in s if c == 'a')             

        a = b = 0
        min_del = float('inf')
        for i in range(len(s)):
            if s[i] == 'a':
                min_del = min(min_del, b + t_a - a - 1)
                a += 1
            else:
                min_del = min(min_del, b + t_a - a)
                b += 1

        return min_del