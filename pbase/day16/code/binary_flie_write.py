try:
    f=open('0_255.bin','wb')  #二进制写
    b=bytes(range(256))
    f.write(b)
    f.close()
    print("写数据成功")
except:
    print('写失败')