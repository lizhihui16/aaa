# import os
# from time import sleep

# pid=os.fork()

# if pid<0:
#     print('dgf')
# elif pid == 0:
#     sleep(3)
#     print('Cjild %d process exit'%os.getpid())
#     os._exit(2)
# else:
#     pid,status = os.wait()
#     print('child pid',pid)
#     #退出状态 *256
#     # print(status)
#     print(os.WEXITSTATUS(status))
#     print("Parent process")
#     while True:
#         pass


# import os
# from time import sleep

# pid=os.fork()

# if pid<0:
#     print('dgf')
# elif pid == 0:
#     sleep(3)
#     print('Cjild %d process exit'%os.getpid())
#     os._exit(2)
# else:
#     p,status = os.waitpid(-1,os.WNOHANG)
#     print('child pid',p)
#     print(os.WEXITSTATUS(status))
#     print("Parent process....")
#     while True:
#         pass






import os
from time import sleep

pid=os.fork()

if pid<0:
    print('dgf')
elif pid == 0:
    sleep(3)
    print('Cjild %d process exit'%os.getpid())
    os._exit(2)
else:
    while True:
        p,status = os.waitpid(-1,os.WNOHANG)
        print('child pid',p)
        print(os.WEXITSTATUS(status))
        if p!=0:
            break
        sleep(1)
    while True:    
        print("Parent process....")
        sleep(2)