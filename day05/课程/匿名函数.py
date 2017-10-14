# def func(x,y):
#     return x+y
#
# func(1,2)


#匿名函数
# f=lambda x,y:x+y
# print(f)
#
# print(f(1,2))
#
# lambda x,y:x+y


#max,min,zip,sorted的用法
salaries={
'egon':3000,
'alex':100000000,
'wupeiqi':10000,
'yuanhao':2000
}

# print(max(salaries))
# res=zip(salaries.values(),salaries.keys())
#
# # print(list(res))
# print(max(res))

# def func(k):
#     return salaries[k]

# print(max(salaries,key=func))
# print(max(salaries,key=lambda k:salaries[k]))
# print(min(salaries,key=lambda k:salaries[k]))

# print(sorted(salaries)) #默认的排序结果是从小到到
# print(sorted(salaries,key=lambda x:salaries[x])) #默认的排序结果是从小到到
# print(sorted(salaries,key=lambda x:salaries[x],reverse=True)) #默认的排序结果是从小到到
#




# x=1000
# def f1():
#     # global x
#     x=0
#
# f1()
# print(x)




'''
4. 内置函数
    map
    reduce
    filter
'''


# def func(f):
#     return f
#
# res=func(max)
# print(res)


# l=['alex','wupeiqi','yuanhao']
#
#
# res=map(lambda x:x+'_SB',l)
#
# print(res)
#
# print(list(res))
#
# nums=(2,4,9,10)
#
# res1=map(lambda x:x**2,nums)
#
# print(list(res1))

# from functools import reduce
#
# l=[1,2,3,4,5]
# print(reduce(lambda x,y:x+y,l,10))


# l=['alex_SB','wupeiqi_SB','yuanhao_SB','egon']
#
# res=filter(lambda x:x.endswith('SB'),l)
# print(res)
# print(list(res))






