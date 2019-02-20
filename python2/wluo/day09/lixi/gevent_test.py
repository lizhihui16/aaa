import gevent

def foo(a,b):
    print('事件１',a,b)
    gevent.sleep(2)
    print('Running foo again')

def bar():
    print('事件２')
    gevent.sleep(3)
    print("Running bar again")

f = gevent.spawn(foo,1,2)
g = gevent.spawn(bar)

gevent.joinall([f,g])