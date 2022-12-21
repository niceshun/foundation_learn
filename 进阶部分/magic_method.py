# class foo:
#     def __del__(self):  # 析构方法，对象回收时触发
#         print("I am nice")
#
# print("----->")

"""class student:
    def __init__(self, name, age):
        print("init.....")
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        print("new.....")
        return super().__new__(cls)


stu = student("shun", 18)
print(stu.name)"""

# getattr魔法函数：访问不存在的属性时触发
# setattr魔法函数：变量或对象赋值时触发
# delattr魔法函数：执行对象或参数回收时触发




























