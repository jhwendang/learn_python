#!/usr/bin/python
# -*- coding:utf-8 -*-

import re

# print(re.findall('\w','abc123d_ef * | - ='))
# print(re.findall('\W','abc123d_ef * | - ='))
# print(re.findall('\s','abc1\n23\td_ef * | - ='))
# print(re.findall('\S','abc1\n23\td_ef * | - ='))
# print(re.findall('\d','abc1\n23\td_ef * | - ='))
# print(re.findall('\D','abc1\n23\td_ef * | - ='))
# print(re.findall('^a','abc1\n23\tad_efa * | - ='))
# print(re.findall('a$','abc1\n23\tad_efa * | - ='))
# print(re.findall('\n','abc1\n\n23\tad_efa * | - ='))
# print(re.findall('\t','abc1\n\n23\tad_efa * | - ='))
# print(re.findall('a.c','abc1\nn2a\nc3\tad_efa * | - =',re.S))
# print(re.findall('a[^-.\n]c','a.c1\nn2a\nc3\tad_efa * | - ='))
#
#
# # * + ? {n,m}
#
# print(re.findall('ab*','a'))
# print(re.findall('ab*','abbbbbbbbbbbbbbbbbbbbbbbbb'))
# print(re.findall('ab+','abbbbb'))
# print(re.findall('ab?','a'))
# print(re.findall('ab?','ab'))
# print(re.findall('ab?','abb'))
# print(re.findall('ab?c','abbc')) #ac  abc
# print(re.findall('ab?c','ac')) #ac  abc
# print(re.findall('ab?c','abc')) #ac  abc

# print(re.findall('ab{2}','123123123abbbbbbbb')) #abb
# #123123123abbbbbbbb
# #         abb
# print(re.findall('ab{2}c','123123123abbbbbbbbc')) #abb
# print(re.findall('ab{1,}c','123123123abbbbbbbbc')) #abc  abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbc
#

#
# print(re.findall('company|companies','all companies will be done,my company is already done'))
# print(re.findall('compan(y|ies)','all companies will be done,my company is already done')) #['ies', 'y']
# print(re.findall('compan(?:y|ies)','all companies will be done,my company is already done')) #['ies', 'y']
#
#
# print(re.findall('al(?:e)x','alex make love'))
#
#
# print(re.findall(r'a\\c','a\c'))

#
# print(re.findall('a.*b','a123b456789b'))
# print(re.findall('a.*?b','a123b456789b'))

# print(re.search('e','alex make love'))
# print(re.search('^e','alex make love'))
# print(re.search('e','alex make love'))
# print(re.match('e','alex make love'))
# print(re.match('a','alex make love').group())
# print(re.search('al(e)x\smak(e)','alex make love').group(0))
# print(re.findall('al(?:e)x\smak(?:e)','alex make love'))
# print(re.search('e','alex make love').group()) #e
# print('===>', re.sub('^(\w+)(\s+)(\w+)(\s+)(\w+)(.*)$', r'\5\2\3\4\1\6', 'alex   make love  111aa'))

# print(re.split('[ab]','abcd'))

# print(re.sub('^a','A','alex make love'))
# print(re.sub('a','A','alex make love'))
# print(re.sub('^(\w+)(\s)(\w+)(\s)(\w+)',r'\5\2\3\4\1','alex make love'))
# print(re.sub('^(\w+)(\s+)(\w+)(\s+)(\w+)',r'\5','alex    make       love'))
# print(re.sub('^(\w+)(\W+)(\w+)(\W+)(\w+)',r'\5\2\3\4\1','alex " \ + = make ----/==     love'))


# print(re.findall('companies|company','my company is already done,all companies will be done'))


# print(re.findall(r'\-?\d+\.?\d*',"1-12*(60+(-40.35/5)-(-4*3))"))
# print(re.findall(r'\-?\d+\.\d*',"1-2*(60+(-40.35/5.3+1.2)-(-4*3))"))


# print(re.findall(r'\-?\d+\.\d+|(\-?\d+)',"1-2*(60+(-40.35/5.3+1.2)-(-4*3))"))

s='''
你好啊 alex 大傻逼
alex的邮箱是3781231123@qq.com
010-18211413111
378533872

'''

print(re.findall(r"[1-9][0-9]{4,}",s))