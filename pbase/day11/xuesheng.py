def input1():
    L=[]

    while True:
        a=input("姓名:")
        if not a:
            break
        else:           
            b=int(input("年龄:"))
            c=int(input("成绩:"))
            d={}
            d['name']=a
            d['age']=b 
            d['score']=c
            L.append(d)
    return L


    
def print1(L):
    print('+---------------+----------+----------+')
    print('|      name     |    age   |  score   |')
    print('+---------------+----------+----------+')
    for d in L:
  
        line='|'+d['name'].center(15)+'|'+str(d['age']).center(10)+'|'+str(d['score']).center(10)+'|'
        print(line)
    print('+---------------+----------+----------+')

def sc(L):
    a=input("姓名:")
    for d in L:
        if d['name']==a:
            L.remove(d)
    print("删除成功")



def xg(L):
    a=input("姓名")
    b=int(input("年龄:"))
    c=int(input("成绩:"))
    for d in L:
        if d['name']==a:
            d['name']=a
            d['age']=b
            d['score']=c


def cjg(L):
    L= sorted(L,key=lambda d: d['score'],
               reverse=True)
    print1(L)
def cjd(L):
    # def 
    for d in L:
        L.sort(key=lambda d:d["score"])
def nlg(L):
    for d in L:
        L.sort(key=lambda d:d["age"],reverse=True)
def nld(L):
    for d in L:
        L.sort(key=lambda d:d["age"])

def main():
    infos = []  # 用于保存学生信息的列表
    while True:
        # 打印菜单:
        # show_menu()
        print("+---------------------------- -----+")
        print("| 1) 添加学生信息                  |")
        print("| 2) 显示学生信息                  |")
        print("| 3) 删除学生信息                  |")
        print("| 4) 修改学生信息                  |")
        print("| 5) 按学生成绩高-低显示学生信息   |")
        print("| 6) 按学生成绩低-高显示学生信息   |")
        print("| 7) 按学生年龄高-低显示学生信息   |")
        print("| 8) 按学生年龄低-高显示学生信息   |")
        print("| q) 退出                          |")
        print("+------------------------------- --+")

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
        elif s == 'q':
            break
main()