class Solution:
    def numTeams(self, rating: List[int]) -> int:

        res = 0

        for m in range(1, len(rating) - 1):
            m_rating = rating[m]

            left_less = sum(1 for i in range(m) if rating[i] < m_rating)
            right_greater = sum(1 for i in range(m + 1, len(rating)) if rating[i] > m_rating)
            left_greater = m - left_less
            right_less = len(rating) - m - right_greater - 1

            res += left_less * right_greater
            res += left_greater * right_less

        return res