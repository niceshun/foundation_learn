# 重要的环节

"""# 遍历列表
nums = [1, 1, 2, 3, 9, 6]
for num in nums:  # 使用for循环遍历列表,使用for循环时，需注意缩进，冒号等，虽然pycharm都会提醒你。。
    print(num)
# 数值列表
numbers = list(range(1, 10))  # 使用range函数创建有序列表是相当快速的
print(numbers)
new_nums = list(range(1, 15, 3))  # range函数也可用于创建等差数列
print(new_nums)
lists_1 = []
for list_1 in range(1, 15, 3):
    lists_1.append(list_1**2)   # 可实现等差阶乘
print(lists_1)
lists_2 = [list_2**2 for list_2 in range(1, 15, 3)]  # 这种方式大大简化了代码量
print(lists_2)

num_1 = min(lists_1)  # min函数取列表中最小的值
print(num_1)
num_2 = max(lists_1)  # max函数取列表中最大的值
print(num_2)
num_3 = sum(lists_1)  # sum函数算出列表的总和
print(num_3)"""

"""# 使用列表的一部分
numbers = list(range(1, 10))
print(numbers)
print(numbers[3:])
# 使用切片复制列表
new_numbers = numbers[:]  # 切片复制会让两个列表指向不同的id，再次赋值则相互不干扰
new_numbers.append(11)
numbers.append(12)
print(id(new_numbers))
print(id(numbers))"""

"""new_numbers = numbers  # 直接赋值列表会导致两个列表同时指向同一个id，再次赋值则会相互干扰
new_numbers.append(11)
numbers.append(12)
print(id(new_numbers))
print(id(numbers))"""


















