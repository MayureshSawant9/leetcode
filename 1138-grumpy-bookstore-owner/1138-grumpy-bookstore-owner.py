class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        not_satisfied = [cust * grump for cust, grump in zip(customers, grumpy)]
        
        max_sum = sum(not_satisfied[:minutes])
        curr_sum = max_sum

        for i in range(1, len(not_satisfied) - minutes + 1):
            curr_sum = curr_sum - not_satisfied[i - 1] + not_satisfied[i + minutes - 1]
            if curr_sum > max_sum:
                max_sum = curr_sum

        return sum(customers) - sum(not_satisfied) + max_sum
        