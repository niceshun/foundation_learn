# 变量赋值不是拷贝
# copy拷贝为浅拷贝
# deepcopy拷贝为深拷贝，会把内存地址全部改变
"""
由于 Python 内部引用计数的特性，对于不可变对象，浅拷贝和深拷贝的作用是一致的，就
相当于复制了一份副本，原对象内部的不可变对象的改变，不会影响到复制对象
浅拷贝的拷贝。其实是拷贝了原始元素的引用（内存地址），所以当拷贝可变对象时，原对象
内可变对象的对应元素的改变，会在复制对象的对应元素上，有所体现
深拷贝在遇到可变对象时，又在内部做了新建了一个副本。所以，不管它内部的元素如何变化，都不会影响到原来副本的可变对象
"""

# 推导式
nums = [i for i in range(10) if i % 2 == 0]  # 条件判断可以添加多个
num = {i : i * 2 for i in range(10)}  # 字典推导式
number = tuple(i for i in range(10))  # 元组推导式得添加tuple

# 有名元组（具体的用处在哪里？？）

# defaultdict 会给字典中的键、值赋予默认值

# deque（双向队列）
from collections import deque
dq = deque()
dq.append(1)
dq.append(2)  # 从左向右添加元素
dq.append(3)
dq.appendleft(100)  # 从右向左添加元素
# deque 也可把列表等数据类型直接转换成双向队列类型

# 二分查找

# 选择排序
def chioce_sort(ll):
    for i in range(len(ll) - 1):
        min_index = i
        for j in range(i + 1, len(ll)):
            if ll[j] < ll[min_index]:
                ll[j], ll[min_index] = ll[min_index], ll[j]


li = [5, 6, 5, 3, 1]
chioce_sort(li)
print(li)

# 列表内置函数升级用法
ll = [{"id": 5}, {"id": 3}, {"id": 1}]
ll.sort(key=lambda x: x["id"])  # 还可根据权重值来选择排序
print(ll)









































