def input_student():
    '''此函数返回用户输入的学生信息的列表
    返回的列表格式写之前完全相同
    '''
    L = []  # 创建一个列表，用来保存所有学生的字典
    # 读取学生数据放入列表中
    while True:
        n = input("请输入学生姓名: ")
        if not n:  # 如果学生姓名为空则结束输入
            break
        a = int(input("请输入学生年龄: "))
        s = int(input("请输入学生成绩: "))
        # 把上述n, a, s 所表示的信息形成字典，并加入到列表
        d = {}  # 创建一个新字典，准备存入学生信息数据
        d['name'] = n
        d['age'] = a
        d['score'] = s
        L.append(d)  # 把字典存入列表中
    return L

def output_student(L):
    '''此函数把传入的列表L 打印成为表格'''
    # 第二步，显示所有学生的信息
    print("+---------------+----------+----------+")
    print("|      name     |    age   |  score   |")
    print("+---------------+----------+----------+")
    # 此处打印所有学生的信息
    for d in L:  # 把每个学生的数据取出来，用d绑定对应的字典
        center_name = d['name'].center(15)
        str_age = str(d['age'])  # 先将年龄转为字符串
        center_age = str_age.center(10) # 生成居中的字符串
        center_score = str(d['score']).center(10)
        line = "|%s|%s|%s|" % (center_name,
                              center_age,
                              center_score)
        print(line)
    print("+---------------+----------+----------+")


def del_student(L):  # 删除学生信息
    name = input("请输入要删除学生的姓名: ")
    print('删除成功')

def modify_student_score(L):  # 删除学生信息
    name = input("请输入要修改学生的姓名:")
    # 查找name 是不是在列表L里
    # 如果name在L里
    score = int(input("请输入要修改的成绩: "))
    # ...


def show_student_by_score_desc(L):
    lst = sorted(L,
                 key=lambda d: d['score'],
                 reverse=True)
    output_student(lst)

def show_student_by_score_asc(L):
    lst = sorted(L,
                 key=lambda d: d['score'])
    output_student(lst)

def show_student_by_age_desc(L):
    lst = sorted(L,
                 key=lambda d: d['age'],
                 reverse=True)
    output_student(lst)

def show_student_by_age_asc(L):
    lst = sorted(L,
                 key=lambda d: d['age'])
    output_student(lst)



def show_menu():
    print("+---------------------------------+")
    print("| 1)  添加学生信息                |")
    print("| 2)  显示学生信息                |")
    print("| 3)  删除学生信息                |")
    print("| 4)  修改学生成绩                |")
    print("| 5)  按学生成绩高-低显示学生信息 |")
    print("| 6)  按学生成绩低-高显示学生信息 |")
    print("| 7)  按学生年龄高-低显示学生信息 |")
    print("| 8)  按学生年龄低-高显示学生信息 |")
    print("| q)  退出程序                    |")
    print("+---------------------------------+")

def main():
    docs = []
    while True:
        show_menu()
        s = input("请选择: ")
        if s == '1':
            docs += input_student()
        elif s == '2':
            output_student(docs)
        elif s == '3':
            del_student(docs)  # 删除学生信息
        elif s == '4':
            modify_student_score(docs)  # 删除学生信息
        elif s == '5':
            show_student_by_score_desc(docs)
        elif s == '6':
            show_student_by_score_asc(docs)
        elif s == '7':
            show_student_by_age_desc(docs)
        elif s == '8':
            show_student_by_age_asc(docs)
        elif s == 'q':
            break  # 退出循环




main()
