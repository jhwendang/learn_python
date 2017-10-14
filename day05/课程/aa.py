#
# def func1():
#     print('func1')
#
#
# def func2():
#     print('func2')
#
#
#
# dic={
#     'func1':func1,
#     'func2':func2,
# }
#
# dic['func1']()

# x=0
# def f1():
#     # x=1
#     def f2():
#         # x=2
#         def f3():
#             # x=3
#             print(x)
#         f3()
#
#     f2()
#
# f1()
# del x


# if x ==0:
#     y=2



def f1():
    print('first')
    yield 1
    print('second')
    yield 2
    print('third')
    yield 3

g=f1()
res1=next(g)
print(res1)

res2=next(g)
print(res2)










