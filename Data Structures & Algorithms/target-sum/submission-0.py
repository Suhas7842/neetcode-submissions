class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        dp = [defaultdict(int) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(n):
            for cur_sum,count in dp[i].items():
                dp[i+1][cur_sum+nums[i]]+=count
                dp[i+1][cur_sum-nums[i]]+=count
        return dp[n][target]