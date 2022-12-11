list_num = [1, 6, 3]
num = list_num[0] - 1  # 列表的数值需要从第一个开始查起
res = 0
for i in list_num:
    num = max(num + 1, i)
    res += num - i

print(res)



































