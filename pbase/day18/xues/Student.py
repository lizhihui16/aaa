

class Student:
    L=[]

    def __init__(self,a,b,c):
        self.name=a
        self.age=b
        self.score=c

    @classmethod
    def input1(cls):
        while True:
            a=input("姓名:")
            if not a:
                break
            try:           
                b=int(input("年龄:"))
                c=int(input("成绩:"))
                cls.L.append(Student(a,b,c))
            except ValueError:
                print("您输入有误，请重新输入")
                continue

    @classmethod        
    def print1(cls):
        print('+---------------+----------+----------+')
        print('|      name     |    age   |  score   |')
        print('+---------------+----------+----------+')
        for d in cls.L:
            line='|'+d.name.center(15)+'|'+str(d.age).center(10)+'|'+str(d.score).center(10)+'|'
            print(line)
        print('+---------------+----------+----------+')

    @classmethod
    def sc(cls):
        a=input("姓名:")
        for i,d in enumerate(cls.L):
            if d.name==a:
                del cls.L[i]
                print("删除成功")
                return


    @classmethod
    def xg(cls):
        a=input("姓名")
        b=int(input("年龄:"))
        c=int(input("成绩:"))
        for d in cls.L:
            if d.name==a:
                d.name=a
                d.age=b
                d.score=c

    @classmethod
    def cjg(cls):
        cls.L= sorted(cls.L,key=lambda d: d.score,
                reverse=True)


    @classmethod
    def cjd(cls):
        for d in cls.L:
            cls.L.sort(key=lambda d:d.score)
   

    @classmethod
    def nlg(cls):
        for d in cls.L:
            cls.L.sort(key=lambda d:d.age,reverse=True)


    @classmethod
    def nld(cls):
        for d in cls.L:
            cls.L.sort(key=lambda d:d.age)


    @classmethod
    def read_from_file(cls):
        l=[]
        try:
            f=open('si.txt','r')
            for line in f:
                line=line.strip()#去掉'\n'
                lines=line.split(',')
                a,b,c,=lines
                b=int(b)
                c=int(c)
                l.append(dict(name=a,
                            age=b,
                            score=c))
            f.close()
            print("读取文件成功")
        except OSError:
            print('打开文件失败')
        return l

    @classmethod
    def save_to_file(cls):
        try:
            f=open('si.txt','w')
            for d in cls.L:
                f.write(d.name)
                f.write(',')
                f.write(str(d.age))
                f.write(',')
                f.write(str(d.score))
                f.write('\n')
            f.close()
            print("保存文件成功")
        except OSError:
            print('保存文件失败')


# Student.input1()
