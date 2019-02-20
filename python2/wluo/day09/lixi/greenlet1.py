from greenlet import greenlet

def test1():
    print(12)
    gr2.switch() #去执行协程２
    print(24)
    gr2.switch()

def test2():
    print(34)
    gr1.switch()
    print(99)

#将两个函数变为协程
gr1 = greenlet(test1)
gr2 = greenlet(test2)

gr1.switch()#执行协程test1
