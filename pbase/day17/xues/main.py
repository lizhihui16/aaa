
from menu import *
from student_info import *


def main():
    infos = []  # 用于保存学生信息的列表
    while True:
        show_menu()
        s = input('请选择: ')
        if s == '1':
            infos +=input1()
        elif s == '2':
            print1(infos)
        elif s=='3':
            sc(infos)
        elif s=='4':
            xg(infos)
        elif s=='5':
            cjg(infos)
        elif s=="6":
            cjd(infos)
        elif s=='7':
            nlg(infos)
        elif s=='8':
            nld(infos)
        elif s=='9':
            infos==read_from_file()
        elif s=='10':
            save_to_file(infos)
        elif s == 'q':
            break
main()