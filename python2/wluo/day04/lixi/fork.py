import os
from time import sleep
pid = os.fork()

if pid<0:
    print("Create process failend")
elif pid == 0:
    sleep(2)
    print('The new process')
else:
    sleep(3)
    print('the new process')
print('fork test over')







# import os
# pid = os.fork()

# if pid<0:
#     print("Create process failend")
# elif pid == 0:
#     print('The new process')
# else:
#     print('the new process')
# print('fork test over')