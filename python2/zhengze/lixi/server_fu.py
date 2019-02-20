
import re
import sys

def get_address(port):
    f = open('/home/tarena/aid1808/python2/zhengze/lixi/1.txt')
    print(f)
    while True:
        data = ''
        for line in f:
            if line !='\n':
                data +=line
            else:
                break

        if not data:
            return "Not found the port"

        try:
            PORT = re.match(r'\S+',data).group()
        except Exception as e:
            print(e)
            continue
    
        if port == PORT:
            # pattern = r'address is (\w{4}\.\w{4}\.\w{4})'
            pattern = r'address is ((\d{1,3}\.){3}\d{1,3}/\d+|Unknow)'

            address = re.search(pattern,data).group(1)
            return address

if __name__=="__main__":
    port = sys.argv[1]
    print(get_address(port))










# data = f.read()
# lists = data.split('')
# p1 = sys.argv[1]

# if pi == list[0]
# p2 = r'address is(\S)'

# l = re.findall(p,data)

