# 列表的定义最好以复数的形式
"""my_likes = ['learn', 'money', 'talk_with_someboby', '张熠女神']
print(my_likes[3])
print(my_likes[-1])  # 负数代表从列表最后一个元素开始检索,当列表元素为空时，此索引会引发索引错误
print(f'my favorite {my_likes[-1]}!!')"""  # 终极暗恋史，要加油啊

# 增、删、改、查在列表与字典中都是相当重要的
"""my_likes = ['learn', 'money', 'talk_with_someboby', '张熠女神']
my_likes[2] = '旅游'   # 直接修改列表元素即可更改列表
print(my_likes)
my_likes.append('job')  # 添加元素最简单的方法就是直接append在最后边
print(my_likes)
my_likes.insert(2, 'water')  # insert方法可在指定位置添加元素
print(my_likes)

del my_likes[0]  # del语句直接删除掉列表中相应位置的元素，可去除任意位置的一个元素
print(my_likes)
my_like = my_likes.pop(-2)  # pop语句弹出列表中的元素，可接收，可去除任意位置的一个元素
print(my_like)
print(my_likes)
nums = [1, 1, 1, 2, 3]
num = 1
nums.remove(num)  # remove语句弹出对应值的元素，只能一次弹出列表中最前边的一个
print(nums)"""

# 对列表对象进行排序
"""letters = ['b', 'w', 'f', 's', 'l']
letters.sort()  # sort函数对列表的排序是永久的
print(letters)
letters.sort(reverse=True)  # reverse可使列表按字母倒叙排列
print(letters)
nums = [1, 1, 2, 3, 9, 6]
nums.sort()  # 也可对数字列表进行排列
print(nums)
new_nums = sorted(nums, reverse=True)  # sorted函数可临时排序列表
print(new_nums)
print(nums)
nums.reverse()  # reverse函数永久性的颠倒列表的顺序，再次调用reverse函数也可重新调整回来
print(nums)
print(len(nums))  # len函数确定长度，之后用到的地方很多"""
















