
from menu import *
from Student import *


def main():
    infos = []  # 用于保存学生信息的列表
    while True:
        show_menu()
        s = input('请选择: ')
        if s == '1':
            infos =Student.input1()
        elif s == '2':
            Student.print1()
        elif s=='3':
            Student.sc()
        elif s=='4':
            Student.xg()
        elif s=='5':
            Student.cjg()
        elif s=="6":
            Student.cjd()
        elif s=='7':
            Student.nlg()
        elif s=='8':
            Student.nld()
        elif s=='9':
            infos=Student.read_from_file()
        elif s=='10':
            Student.save_to_file()
        elif s == 'q':
            break
main()