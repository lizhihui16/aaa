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
    for i,d in enumerate(L):
        if d['name']==a:
            del L[i]
            print("删除成功")
            return



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
def read_from_file():
    L=[]
    try:
        f=open('si.txt','r')
        for line in f:
            line=line.strip()#去掉'\n'
            lines=line.split(',')
            n,a,s=lines
            a=int(a)
            s=int(s)
            L.append(dict(name=n,
                          age=a,
                          score=s))
        f.close()
        print("读取文件成功")
    except OSError:
        print('打开文件失败')
    return L

def save_to_file(L):
    try:
        f=open('si.txt','w')
        for d in L:
            f.write(d['name'])
            f.write(',')
            f.write(str(d['age']))
            f.write(',')
            f.write(str(d['score']))
            f.write('\n')
        f.close()
        print("保存文件成功")
    except OSError:
        print('保存文件失败')
