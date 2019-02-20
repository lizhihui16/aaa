# ２. 输入一个整数n，打印一个对应的正方形:
#   如：
#   　　请输入: 5
#   打印:
#     1 2 3 4 5
#     2 3 4 5 6
#     3 4 5 6 7
#     4 5 6 7 8
#     5 6 7 8 9
#   　　请输入: 3
#   打印:
#     1 2 3
#     2 3 4
#     3 4 5

# 打印一行
def print_a_line(line, n):
    for i in range(line + 1, line + 1 + n):
        print("%2d" % i, end=' ')
    print()  # 换行

def print_squqre(n):
    for line in range(n):
        # 打印一行
        print_a_line(line, n)


n = int(input("请输入行数:"))
print_squqre(n)

print('-----------------------------')
print_squqre(n + 2)