"""
请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop 和 empty）。
实现 MyStack 类：
void push(int x) 将元素 x 压入栈顶。
int pop() 移除并返回栈顶元素。
int top() 返回栈顶元素。
boolean empty() 如果栈是空的，返回 true ；否则，返回 false
"""


import collections

class MyStack:
    def __init__(self):
        # 实例化两个队列
        self.que1 = collections.deque()
        self.que2 = collections.deque()

    def push(self, x: int) -> None:
        # 把元素压入que1队列中
        self.que1.append(x)
        while self.que2:
            self.que1.append(self.que2.popleft())
        self.que1, self.que2 = self.que2, self.que1

    def pop(self) -> int:
        return self.que2.popleft()

    def top(self) -> int:
        return self.que2[0]

    def empty(self) -> bool:
        return not self.que2


























