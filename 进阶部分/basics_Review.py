# 判断内存地址是否相同用 is
# 小整数池：预先开辟一块内存空间，存放一部分整数（范围：-5 ~ 256）
# 字符串驻留：与小整数池类似，存储一部分常用的字符串
# 垃圾回收机制：利用计算引用计数来回收垃圾（计数回收效率低），标记回收、分代回收效率会高一些
# 迭代器的优点：惰性取值，每次取一个数值，不占内存； 缺点：每次只能取一个值
# while循环适合做条件循环，for循环适合做迭代器循环
# for循环的本质就是while循环去循环迭代器，只是for循环底层帮我们做了这一部分工作
# 例如：
"""
ll = [1, 2, 3, 4]
ll_iter = iter(ll)  # 生成迭代对象
while True:
    try:
        print(next(ll_iter))  # 利用next函数取值
    except StopIteration:
        break
# 等同于
for i in ll:
    print(i)
"""
"""
from itertools import chain

a = [1, 2, 3]
b = [1, 3, 5]
c = [1, 2]
for i in chain(a, b, c):  # chain函数利用迭代器原理，惰性取值a和b中的数，内存消耗会更小
    print(i)

d = [[1, 2, 3], [1, 3, 5], [1, 2]]
print(*d)  # *d 表示把列表拆开
for i in chain(*d):
    print(i)
"""


































