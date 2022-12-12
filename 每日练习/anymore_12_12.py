"""数组的每个下标作为一个阶梯，第 i 个阶梯对应着一个非负数的体力花费值 cost[i]（下标从 0 开始）。
每当爬上一个阶梯都要花费对应的体力值，一旦支付了相应的体力值，就可以选择向上爬一个阶梯或者爬两个阶梯。
请找出达到楼层顶部的最低花费。在开始时，你可以选择从下标为 0 或 1 的元素作为初始阶梯。"""

def minCostClimbingStairs(cost: list[int]) -> int:
    n = len(cost)
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
    return dp[n]

cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

min_num = minCostClimbingStairs(cost)
print(min_num)
list_n = [0] * 5
print(list_n)

# 动态规划（滚动前进）
def min_test(cost: list[int]) -> int:
    n = len(cost)
    dp = [0] * (n + 1)   # [0]表示列表里的元素全为0
    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
    return dp[n]
min_num = min_test(cost)
print(min_num)























