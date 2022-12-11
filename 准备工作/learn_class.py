class shun:
    def __init__(self, like, want):
        self.like = like
        self.want = want

    def do(self, do_something):
        print(f'shun like {self.like},like {do_something}!')

shun = shun('water', 'money')
shun.do('swim')


class shun1:
    def __init__(self):
        self.num = 20   # 内部定义的默认值在外部是不可调用的，需要经过类内部转化

    def read_num(self):
        print(f'shun like number is {self.num}')

    def do(self, do_something):
        print(f'shun like {do_something}!')

    def change_num(self, new_num):
        self.num = new_num

shun = shun1()  # 类得先实例化才能调用方法
shun.do('swim')
shun.change_num(30)
shun.read_num()




























