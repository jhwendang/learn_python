#递归调用：在函数调用过程中，直接或间接地调用了函数本身，这就是函数的递归调用


#
# def f1():
#     print('from f1')
#     f1()
#
# f1()



# def f1():
#     print('f1')
#     f2()
#
# def f2():
#     f1()
#
# f1()

# import sys
# print(sys.getrecursionlimit())
# print(sys.setrecursionlimit(1000000))
#
# print(sys.getrecursionlimit())



# age(5)=age(4)+2
# age(4)=age(3)+2
# age(3)=age(2)+2
# age(2)=age(1)+2
# age(1)=18
#
#
#
#
# age(n)=age(n-1)+2       n>1
# age(n)=18    n=1

# def age(n):
#     if n == 1:
#         return 18
#     return age(n-1)+2
#
# print(age(5))


#二分法

l = [1, 2, 10,33,53,71,73,75,77,85,101,201,202,999,11111]

def search(find_num,seq):
    if len(seq) == 0:
        print('not exists')
        return
    mid_index=len(seq)//2
    mid_num=seq[mid_index]
    print(seq,mid_num)
    if find_num > mid_num:
        #in the right
        seq=seq[mid_index+1:]
        search(find_num,seq)
    elif find_num < mid_num:
        #in the left
        seq=seq[:mid_index]
        search(find_num,seq)
    else:
        print('find it')

# search(77,l)
# search(72,l)
# search(-100000,l)






