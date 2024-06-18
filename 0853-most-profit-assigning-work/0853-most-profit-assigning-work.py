class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        jobs = list(zip(difficulty, profit))
        jobs.sort()
        worker.sort()

        n = len(jobs)
        max_profit = 0
        job_index = 0
        best_profit = 0

        for ability in worker:
            while job_index < n and jobs[job_index][0] <= ability:
                best_profit = max(best_profit, jobs[job_index][1])
                job_index += 1

            max_profit += best_profit
            
        return max_profit

        