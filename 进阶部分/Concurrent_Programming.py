# 多进程(效率最低)
"""import time
from multiprocessing import Process

def wait():
    print("start")
    time.sleep(2)
    print("end")

if __name__ == '__main__':
    ps = []
    for _ in range(2):
        p = Process(target=wait)
        p.start()
        ps.append(p)
    for i in ps:
        i.join()

    print("主进程结束!")"""

# p.daemon守护进程,保证主进程结束相应的子进程也会结束
# 子进程之间内存空间相互隔离
# 进程的互斥锁

"""from multiprocessing import Lock, Process
import json, time, random

# 查票
def search(i):
    with open('data.txt', 'r', encoding='utf8') as f:
        dic = json.load(f)
    print('用户%s查询余票：%s' % (i, dic.get('ticket_num')))

def buy(i, lock):
    search(i)		# 先查票
    # 再买票
    lock.acquire()  # 抢锁
    time.sleep(random.randint(1, 2))
    with open('data.txt', 'r', encoding='utf8') as f:
        dic = json.load(f)
    if dic.get('ticket_num') > 0:
        dic['ticket_num'] -= 1
        with open('data.txt', 'w', encoding='utf8') as f:
            json.dump(dic, f)
        print('用户%s买票成功' % i)
    else:
        print('用户%s买票失败' % i)
    lock.release()  # 释放锁

if __name__ == '__main__':
    lock = Lock()
    for i in range(1, 11):
        p = Process(target=buy, args=(i, lock))
        p.start()"""

# 多线程(每个进程都自带一个控制线程)
# 线程相对进程来说资源消耗小很多（进程相当于车间，线程相当于车间中的流水线）
"""from threading import Thread
import time

def say():
    time.sleep(2)
    print("say...")

p = Thread(target=say)
p.start()
p.join()  # 主线程等待子线程结束
print("what...")"""
# 线程共享内存空间,也有互斥锁

# 协程：同一线程内通过操作不同代码块来实现协程，全力压榨CPU
import asyncio  # 协程包

# 快速排序
def quick_sort(lists, i, j):
    if i >= j:
        return lists
    pivot = lists[i]
    low = i
    high = j
    while i < j:
        while i < j and lists[j] >= pivot:
            j -= 1
        lists[i], lists[j] = lists[j], lists[i]
        while i < j and lists[i] <= pivot:
            i += 1
        lists[i], lists[j] = lists[j], lists[i]
    # lists[j] = pivot
    quick_sort(lists, low, i-1)
    quick_sort(lists, i+1, high)
    return lists

"""if __name__=="__main__":
    lists=[30,24,5,18,36,12,42,39]
    print("排序前的序列为：")
    for i in lists:
        print(i,end =" ")
    print("\n排序后的序列为：")
    for i in quick_sort(lists,0,len(lists)-1):
        print(i,end=" ")"""



def shun_sort(lists, i, j):
    if i >= j:
        return lists
    pivot = lists[i]
    low = i
    high = j
    while i < j:
        while i < j and lists[j] >= pivot:
            j -= 1
        lists[i], lists[j] = lists[j], lists[i]
        while i < j and lists[j] <= pivot:
            i += 1
        lists[i], lists[j] = lists[j], lists[i]

    shun_sort(lists, low, j-1)
    shun_sort(lists, j+1, high)
    return lists


if __name__=="__main__":
    lists=[30,24,5,18,36,12,42,39]
    print("排序前的序列为：")
    for i in lists:
        print(i,end =" ")
    print("\n排序后的序列为：")
    for i in shun_sort(lists,0,len(lists)-1):
        print(i,end=" ")




























