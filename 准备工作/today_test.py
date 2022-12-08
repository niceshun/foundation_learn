"""给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。
请返回 nums 的动态和~

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/running-sum-of-1d-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""



num = [1, 1, 2, 3, 9, 6]
class Solution:
    def runningSum(nums: list[int]) -> list[int]:
        sums = []
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            sums.append(sum)
        return sums


print(Solution.runningSum(num))





