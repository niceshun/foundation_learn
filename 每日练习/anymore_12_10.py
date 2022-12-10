"""给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
请必须使用时间复杂度为 O(log n) 的算法

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/search-insert-position
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""

# 用传统循环的方法解题
def chioce(list_num: list, num: int):
    i = 0
    j = 0
    if num < min(list_num):
        return i
    elif num > max(list_num):
        i = len(list_num)
        return i
    else:
        while list_num[j] <= num:
            if list_num[j] == num:
                return j
            j += 1
        return j

num = chioce([1, 3, 5, 7, 9], 20)
print(num)

# nums = [1, 3, 5, 7, 9], target = 20
def searchInsert(nums: list[int], target: int) -> int:
    right = len(nums)
    left = -1
    while left + 1 < right:
        mid = (right + left) >> 1  # 二进制向右移动1位
        if nums[mid] < target:
            left = mid
        else:
            right = mid
    return right
num = searchInsert([1, 3, 5, 7, 9], 20)
print(num)


def searchInsert(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2   # 左闭右开的方法
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left



















