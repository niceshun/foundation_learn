# dict字典，键值对
# 获取字典的键，就可以得到相应的值
"""nums = {'one': 1, 'two': 2, 'shree': 3, 'four': 4}
nums['five'] = 5
print(nums)
del nums['two']
print(nums)
num = nums.get('light', 'no value rollback')  # get方法获取字典中的值，没有相应的值则弹出后边设定的条件
print(num)"""

# 遍历字典
nums = {'one': 1, 'two': 2, 'shree': 3, 'four': 4}
for NUM, num in nums.items():  # 遍历字典中的键和值
    print(f'NUM:{NUM},num:{num}')
for NUM in nums.keys():  # 遍历字典中的键
    print(NUM)
for num in nums.values():  # 遍历字典中的值
    print(num)

























