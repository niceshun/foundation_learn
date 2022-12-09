# 给你一个二维整数数组 matrix， 返回 matrix 的 转置矩阵 。
# 矩阵的 转置 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引
"""
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

list_name = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]  # 这确实牛逼
print(list_name)

m, n = len(matrix), len(matrix[0])
ans = [[0]*m for _ in range(n)]
for i in range(m):
    for j in range(n):
        ans[j][i] = matrix[i][j]
print(ans)"""



"""有 n 个 (id, value) 对，其中 id 是 1 到 n 之间的一个整数，value 是一个字符串。不存在 id 相同的两个(id, value) 对。
设计一个流，以 任意 顺序获取 n个(id, value)对，并在多次调用时 按 id 递增的顺序 返回一些值。
实现 OrderedStream 类：
OrderedStream(int n) 构造一个能接收 n 个值的流，并将当前指针 ptr 设为 1 。
String[] insert(int id, String value) 向流中存储新的 (id, value) 对。存储后：
如果流存储有 id = ptr 的 (id, value) 对，则找出从 id = ptr 开始的 最长 id 连续递增序列 ，并 按顺序 返回与这些 id 关联的
值的列表。然后，将 ptr 更新为最后那个 id + 1。
否则，返回一个空列表。"""

class OrderedStream:

    def __init__(self, n: int):
        self.stream = [""] * (n + 1)
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> list[str]:
        stream_ = self.stream

        stream_[idKey] = value
        res = list()
        while self.ptr < len(stream_) and stream_[self.ptr]:
            res.append(stream_[self.ptr])
            self.ptr += 1

        return res
# name = OrderedStream.insert(["OrderedStream", "insert", "insert", "insert", "insert", "insert"],
# [[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]])
# nums = [[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
# obj = OrderedStream(6)
# name = obj.insert(6,
# ["ccccc", "aaaaa", "bbbbb", [5, "eeeee"], [4, "ddddd"]])
# print(name)

# 确实一脸蒙蔽，蒙圈了




