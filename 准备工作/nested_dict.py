# 嵌套
# 列表中存储字典
nums = {'one': 1, 'two': 2}
new_nums = [nums for i in range(3)]
print(new_nums)

# 字典中存储列表
numbers = [1, 2, 3]
age = [4, 5, 6]
new_numbers = {'name': numbers, 'age': age}
print(new_numbers)
for keys, values in new_numbers.items():
    new_sum = [i for i in values]
    print(sum(new_sum))

new_sum = [[i for i in values] for values in new_numbers.values()]
print(new_sum)

new_sum = [values for values in new_numbers.values()]
print(new_sum)

# 字典嵌套字典
# 在字典中，分清楚是处在第几层中，就比较好理解












