import time
def consumer(item):
    # print(item)
    x=111111
    y=22222222222
    z=3333333
    a='abasdfasdfasdfasdfasdf'
    b='123213asdfasdfsadfasdf'
    pass

def producer(target,seq):
    for item in seq:
        target(item)

start_time=time.time()
producer(consumer,range(100000000))
stop_time=time.time()
print('run time is %s' %(stop_time-start_time))






import time
def consumer():
    # print(item)
    x=111111
    y=22222222222
    z=3333333
    a='abasdfasdfasdfasdfasdf'
    b='123213asdfasdfsadfasdf'
    while True:
        item=yield

def producer(target,seq):
    for item in seq:
        target.send(item)

g=consumer()
next(g)
start_time=time.time()
producer(g,range(100000000))
stop_time=time.time()
print('run time is %s' %(stop_time-start_time))