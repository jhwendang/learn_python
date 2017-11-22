#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther : Jianghao
# Date : 2017/11/3
import logging

logging.basicConfig(
                    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=10)

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error11')
logging.critical('critical')

logging.log(40,'log111')         #如果level=40,则只有logging.critical和loggin.error的日志会被打印