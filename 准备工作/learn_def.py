# 函数基本模式
"""def name():
    print("what is your name?")
name()

def anmial(name, anmial_type = 'dog'):
    print(f"my favorite {anmial_type} is {name}!")

anmial('bai')
anmial('bai', 'cat')"""

# 返回值
"""def rent(name, money, people=3):
    return(f'This home {name} your accept money is {money},'
          f'and accept people are {people}')

while True:
    print("home is 'no' or money is '0' to break")
    name = input("what do you like home name is?")
    if name == 'no':
        break
    money = input("how much can you accept?")
    if money == 0:
        break
    house = rent(name, money)
    print(house)"""

# 有时候需要禁止函数修改列表，而切片可有效的实现原列表被修改























