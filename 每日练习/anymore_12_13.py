"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
给你一个可能存在重复元素值的数组numbers，它原来是一个升序排列的数组，并按上述情形进行了一次旋转。
请返回旋转数组的最小元素。例如，数组[3,4,5,1,2] 为 [1,2,3,4,5] 的一次旋转，该数组的最小值为 1。
"""

numbers = [0, 0, 2, 3]
print(min(numbers))  # 利用python自带函数寻找最小值的方法

low, high = 0, len(numbers) - 1
while low < high:
    pivot = low + (high - low) // 2
    if numbers[pivot] < numbers[high]:
        high = pivot
    elif numbers[pivot] > numbers[high]:
        low = pivot + 1
    else:
        high -= 1
print(numbers[low])  # 利用二分法寻找最小值

left, right = 0, len(numbers) - 1
while left < right:
    mid = left + (right - left) // 2
    if numbers[mid] < numbers[right]:
        right = mid
    elif numbers[mid] > numbers[right]:
        low = mid + 1
    else:
        right -= 1















