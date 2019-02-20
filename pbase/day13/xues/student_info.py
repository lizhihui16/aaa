def input1():
    L=[]

    while True:
        a=input("姓名:")
        if not a:
            break
        try:           
            b=int(input("年龄:"))
            c=int(input("成绩:"))
        except ValueError:
            print("您输入有误，请重新输入")
            continue
        d={}
        d['name']=a
        d['age']=b 
        d['score']=c
        L.append(d)
    return L
# print(input1())

    
def print1(L):
    print('+---------------+----------+----------+')
    print('|      name     |    age   |  score   |')
    print('+---------------+----------+----------+')
    for d in L:
        # line='|'+d['name'].center(15)
        # line='|'+str(d['age']).center(11)
        # line='|'+str(d['score']).center(9)+'|'
        line='|'+d['name'].center(15)+'|'+str(d['age']).center(10)+'|'+str(d['score']).center(10)+'|'
        print(line)
    print('+---------------+----------+----------+')
# L=input1()
# print(L)
# print1(L)

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
    for d in L:
        L.sort(key=lambda d:d["score"])
    print1(L)

def nlg(L):
    for d in L:
        L.sort(key=lambda d:d["age"],reverse=True)
    print1(L)

def nld(L):
    for d in L:
        L.sort(key=lambda d:d["age"])
    print1(L)
