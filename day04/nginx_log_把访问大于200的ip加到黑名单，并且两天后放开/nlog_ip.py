#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther : Jianghao
# Date : 2017/9/26
import os,time

def time_diff(func1):
    """
    blockips-day1.conf是当天的黑名单、blockips-day2.conf是前一天、blockips-day.conf是前两天，这样就能两天后再释放
    blockips-day2.conf --> blockips-day3.conf
    blockips-day1.conf --> blockips-day2.conf'
    """
    def wrapper2():
        filemt = time.localtime(os.stat('blockips-day1.conf').st_mtime)
        file_time = time.strftime("%Y-%m-%d",filemt)
        now_time = time.strftime("%Y-%m-%d",time.localtime(time.time()))
        # now_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        if file_time < now_time:
            #file_time比now_time小，就说明已经过了一天了，测试时改为==便于测试
            with open('blockips-day2.conf','r') as f_r2,open('blockips-day3.conf', 'w') as f_w3:
                    for line_r2 in f_r2.readlines():
                        f_w3.writelines(line_r2)
            with open('blockips-day1.conf', 'r') as f_r1,open('blockips-day2.conf', 'w') as f_w2:
                for line_r1 in f_r1.readlines():
                    f_w2.writelines(line_r1)
        func1()
    return wrapper2


def nginxlog_diff(func2):
    def wrapper1():
        with open('blockips-day1.conf',mode='r') as fr:
            num1 = len(fr.readlines())
        if num1 != os.system("cat /data/logs/nginx/access_o2o-80_log | grep /user/register/sms/ |awk '{print $1}'| sort |uniq -c | sort -n | awk '$1>200{print "'"deny "'" $2"'";"'"}'| wc -l "):
        # if num1 != 5: #由于不是linux，自设定一个判断
            func2()
    return wrapper1


@time_diff
@nginxlog_diff
def nginx_log():
    """
    #由于不是linux，自设定一个ip日志和写入ip到blockips-day1.conf
    """
    # with open('ip.txt','r') as test1,open('blockips-day1.conf','w') as test2:
    #     for test111 in test1.readlines():
    #         test2.writelines(test111)
    os.system("cat /data/logs/nginx/access_o2o-80_log | grep /user/register/sms/ |awk '{print $1}'| sort |uniq -c | sort -n | awk '$1>200{print "'"deny "'" $2"'";"'"}' > blockips-day1.conf")
    time.sleep(1)
    os.system("kill -HUP `ps -ef | grep nginx | grep 'master process'|grep -v grep | awk '{print $2}'`")
    # print ('ok')

nginx_log()


