class Solution:
    def minimumDeletions(self, s: str) -> int:
        count = {'a': 0, 'b': 0}
        for c in s:
            count[c] += 1
            
        a = b = 0
        min_del = float('inf')
        for i in range(len(s)):
            if s[i] == 'a':
                min_del = min(min_del, b + count['a'] - a - 1)
                a += 1
            else:
                min_del = min(min_del, b + count['a'] - a)
                b += 1

        return min_del