# read file
"""with open('学习小细节.txt', encoding='utf-8') as txt:  # 缺少encoding可能会编码错误
    # read_txt = txt.read()
    # lines = txt.readlines()


# print(read_txt.rstrip())

    for line in txt:
        print(line.strip())"""

# write file
"""name = 'shun'
age = 26
like = 'girl'
with open('file_test.txt', 'w') as file_test:
    file_test.write(name + '\n' + str(age) + '\n' + like)  # 传入文件中的必须是str类型，write模式会覆盖掉文件中的内容"""

# 读取模式（‘r‘），写入模式（‘w‘），附加模式（‘a‘），读写模式（‘r+‘）
"""with open('file_test.txt', 'a') as file_test:
    file_test.write('\n' + 'anderstand')"""

# try-except-else 用于执行错误模块很好用
# json.dump把数据用json格式写进文件中,json.load把数据读出来
# 重构函数：最终使每一个函数都执行单一而清晰的任务

























