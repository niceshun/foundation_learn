class Shun1:
    def __init__(self):
        self.num = 20   # 内部定义的默认值在外部是不可调用的，需要经过类内部转化

    def read_num(self):
        print(f'shun like number is {self.num}')

    def do(self, do_something):
        print(f'shun like {do_something}!')

    def change_num(self, new_num):
        self.num = new_num

class New_shun(Shun1):
    def __init__(self):
        super().__init__()
        self.age = 27

    def read_age(self):
        print(f'my age is {self.age}!')

    def change_age(self, new_age):
        self.age = new_age

    def do(self, do_something):  # 重写父类的方法，可覆盖掉父类的方法
        print(f'shun like {do_something}!')


from random import randint

num = randint(1, 10)
print(num)






















