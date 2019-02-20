# defualt_args.py

# 此程序示意函数的缺省参数

def info(name, age=1, address="未填写"):
    print(name, "今年", age, "岁, 住在:", address)

# info()  # 出错,至少得给一个实参给name绑定
info('小李')
info('tarena', 15)
info('小魏', 3, '北京市朝阳区')
