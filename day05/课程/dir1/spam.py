#spam.py
print('from the spam.py')
__all__=['money']
money=1000

def read1():
    print('spam->read1->money',money)

def read2():
    print('spam->read2 calling read')
    read1()

def change():
    global money
    money=0


#spam.py当做脚本执行，__name__='__main__'
#spam.py当做模块导入，__name__=模块名
# print('当前文件的用途是: ',__name__)

if __name__ == '__main__':
    print('当做脚本执行')
    change()
    print(money)