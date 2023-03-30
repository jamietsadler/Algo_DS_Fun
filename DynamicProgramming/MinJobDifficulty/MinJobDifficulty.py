from typing import List

class Solution:
    def __init__(self):
        self.memo = {}

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)

        # check for edge cases (must be at least as many jobs as days)
        if n < d:
            return -1
        if n == d:
            return sum(jobDifficulty)

        max_job_remaining = jobDifficulty[:]

        for i in range(n -2, -1, -1):
            max_job_remaining[i] = max(jobDifficulty[i], max_job_remaining[i+1])

        #@cache
        def recurse(i , days_remaining):
            if days_remaining == 1:
                return max_job_remaining[i]

            if (i, days_remaining) in self.memo:
                return self.memo[(i, days_remaining)]

            res = float("inf")
            max_diff_today = 0

            for j in range(i, n - days_remaining + 1):
                max_diff_today = max(max_diff_today, jobDifficulty[j])
                res = min(res, max_diff_today + recurse(j+1, days_remaining - 1))
            self.memo[(i, days_remaining)] = res
            return res

        return recurse(0, d)

class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        n = len(jobDifficulty)
        dp = [[float("inf")] * n + [0] for _ in range(d + 1)]

        for days_remaining in range(1, d + 1):
            for i in range(n - days_remaining + 1):
                daily_max_job_diff = 0
                for j in range(i+1, n - days_remaining + 2):
                    daily_max_job_diff = max(daily_max_job_diff, jobDifficulty[j - 1])
                    dp[days_remaining][i] = min(dp[days_remaining][i],
                                                      daily_max_job_diff + dp[days_remaining - 1][j])

        if dp[d][0] == float('inf'):
            return -1
        print(dp)
        return dp[d][0]     
            