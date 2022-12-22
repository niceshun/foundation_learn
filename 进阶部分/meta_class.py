# 元类：type
# 利用元类去定义类是不推荐的
"""class Mytype(type):
    pass

class People(metaclass=Mytype):
    pass"""

# 利用__new__实现单例模式
class Student:
    _isinstance = None

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        if not cls._isinstance:
            cls._isinstance = super().__new__(cls)  # 返回一个空对象
        return cls._isinstance

stu1 = Student("shun")
stu2 = Student("xiaoming")

print(stu2.name)

# 再写装饰器
import time

def outer(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        now_time = end - start
        print(now_time)
    return inner

@outer
def foo(x, y):
    time.sleep(2)
    print(x + y)

foo(1, 3)

























