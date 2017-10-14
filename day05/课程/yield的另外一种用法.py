#yield的语句形式： yield 1
#yield的表达式形式： x=yield



#协程函数

def deco(func):
    def wrapper(*args,**kwargs):
        res=func(*args,**kwargs)
        next(res)
        return res
    return wrapper

@deco
def eater(name):
    print('%s ready to eat' %name)
    food_list=[]
    while True:
        food=yield food_list
        food_list.append(food)
        print('%s start to eat %s' %(name,food))


g=eater('alex')
# print(g)
# next(g) #等同于 g.send(None)

#

g.send('手指头')
# g.send('脚指头')
# g.send('别人的手指头')
# g.send('别人的脚指头')

# print(g)
# print(g.send('脚趾头1'))
# print(g.send('脚趾头2'))
# print(g.send('脚趾头3'))




#x=yield
#g.send('1111'),先把1111传给yield，由yield赋值给x
# 然后再往下执行，直到再次碰到yield，然后把yield后的返回值返回







