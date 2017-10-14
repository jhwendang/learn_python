import re
# s='''
# http://www.baidu.com
# 1011010101
# egon@oldboyedu.com
# 你好
# 21213
# 010-3141
# egon@163.com
# '''
# # print("ab\nc")
#
# res=re.findall(r"[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?",s)
# print(res)


# print(re.findall('\w','as213df_*|'))
# print(re.findall('\W','as213df_*|'))
#
# print(re.findall('a\wb','a_b a3b aEb a*b'))

# print(re.findall('\s','a b\nc\td'))
# print(re.findall('\S','a b\nc\td'))

# print(re.findall('\d','a123bcdef'))
# print(re.findall('\D','a123bcdef'))


# print(re.findall('\n','a123\nbcdef'))
# print(re.findall('\t','a123\tbc\td\tef'))

# print(re.findall('^h','hello egon hao123'))
# print(re.findall('^h','ello egon hao123'))

# print(re.findall('3$','e3ll3o e3gon hao123'))
# print(re.findall('3$','e3ll3o e3gon hao123asdf'))

# print(re.findall('a.c','abc a1c a*c a|c abd aed ac'))



# print(re.findall('a.c','abc a1c a*c a|c abd aed a\nc',re.S)) #让点能够匹配到换行符
# print(re.findall('a[1,2\n]c','a2c a,c abc a1c a*c a|c abd aed a\nc'))
# print(re.findall('a[0-9]c','a2c a,c abc a1c a*c a|c abd aed a\nc'))
# print(re.findall('a[0-9a-zA-Z*-]c','a1c abc a*c a-c aEc'))


# print(re.findall('a[^0-9]c','a1c abc a*c a-c aEc'))



#* + ? {n,m} #重复


#ab* a ab abbbbbbbbbbbbbbbbbbbbbbbbbbb
# print(re.findall('ab*','a'))
# print(re.findall('ab*','abbbbbb'))
# print(re.findall('ab*','bbbbbb'))


# print(re.findall('ab+','a'))
# print(re.findall('ab+','abbbbbb'))
# print(re.findall('ab+','bbbbbb'))


#ab[123] ab1 ab2 ab3
# print(re.findall('ab[123]','abbbbb123'))
# print(re.findall('ab[123]','ab1 ab2 ab3 abc1'))

#ab[123] ab1+ ab2+ ab3+
# print(re.findall('ab[123]+','ab11111111 ab2 ab3 abc1'))

#ab[123] ab[123][123][123]
# print(re.findall('ab[123]+','ab1 ab2 ab3 ab4 ab122'))

#abbb
# print(re.findall('ab{3}','ab1 abbbbbbbb2 abbbbb3 ab4 ab122'))
# print(re.findall('ab{3,4}','ab1 abbb123 abbbb123 abbbbbt'))

# print(re.findall('ab{3,}','ab1 abbb123 abbbb123 abbbbbt'))
# print(re.findall('ab{0,}','a123123123 ab1 abbb123 abbbb123 abbbbbt'))
# print(re.findall('ab{1,}','a123123123 ab1 abbb123 abbbb123 abbbbbt'))


#ac abc
# print(re.findall('ab?c','ac abc aec a1c'))


#.* 贪婪匹配
# print(re.findall('a.*c','ac abc aec a1c'))

#.*？ 非贪婪匹配
# print(re.findall('a.*?c','ac abc aec a1c'))
# print(re.findall('a.*?c','ac abc a111111111c a\nc a1c',re.S))



# print(re.findall('compan(?:y|ies)',
#                  'Too many companies have gone bankrupt, and the next one is my company'))
#

# print(re.findall('ab+123','ababab123'))
# print(re.findall('(?:ab)+123','ababab123'))


print(re.findall(r'a\\c','a\c')) #r代表告诉解释器使用rawstring，即原生字符串，把我们正则内的所有符号都当普通字符处理，不要转义
# print(re.findall('a\\\\c','a\c')) #r代表告诉解释器使用rawstring，即原生字符串，把我们正则内的所有符号都当普通字符处理，不要转义

# print(re.findall(r'a\\c','a\c')) #r代表告诉解释器使用rawstring，即原生字符串，把我们正则内的所有符号都当普通字符处理，不要转义
# print(re.findall('a\\\\c','a\c')) #同上面的意思一样，和上面的结果一样都是['a\\c']
