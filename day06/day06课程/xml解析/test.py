#!/usr/bin/python
# -*- coding:utf-8 -*-

import xml.etree.ElementTree as ET

tree = ET.parse("a")
root = tree.getroot()

# for i in root.iter('year'):
#     print(i.tag,i.text,i.attrib)
#
# print(root.find('country'))   #找到一个
# print(root.find('country').attrib)  #显示属性



# for country in root:
#     print('=====>',country.attrib['name'])
#     for item in country:
#         print(item.tag,item.text,item.attrib)


# for year in root.iter('year'):
#     print(year.tag,year.text,year.attrib)



# for year in root.iter('year'):
#     year.text=str(int(year.text)+1)
#     year.set('update','yes')


# tree.write('b.xml')
# tree.write('a')

# #删除root下的country：
# for country in root.findall('country'):
#    rank = int(country.find('rank').text)
#    if rank > 50:
#      root.remove(country)
# tree.write('output.xml')

#删除country下的year
# for country in root:
#     # print(country)
#     # print('===>',country.find('year'))
#     year=country.find('year')
#     if int(year.text) > 2010:
#         country.remove(year)
#
# tree.write('d.xml')

# year2 = ET.Element('year2')


# for country in root:
#     print(country)
#     # print('===>',country.find('year'))
#     year=country.find('year')
#     if int(year.text) > 2010:
#         year2 = ET.Element('year2')
#         year2.text=str(int(year.text)+1)
#         year2.set('update','yes')
#         country.append(year2)
# tree.write('e.xml')

# import xml.etree.ElementTree as ET
#
# new_xml = ET.Element("namelist")
# name = ET.SubElement(new_xml, "name", attrib={"enrolled": "yes"})
# age = ET.SubElement(name, "age", attrib={"checked": "no"})
# sex = ET.SubElement(name, "sex")
# sex.text = '33'
# name2 = ET.SubElement(new_xml, "name", attrib={"enrolled": "no"})
# age = ET.SubElement(name2, "age")
# age.text = '19'
#
# et = ET.ElementTree(new_xml)  # 生成文档对象
# et.write("test.xml", encoding="utf-8", xml_declaration=True)
#
# ET.dump(new_xml)  # 打印生成的格式





#
# import xml.etree.ElementTree as ET
# tree = ET.parse("a.xml")
# root=tree.getroot()
#
# for country in root.findall('country'):
#     for year in country.findall('year'):
#         if int(year.text) > 2000:
#             year2=ET.Element('year2')
#             year2.text='111'
#             year2.attrib={'a':'111'}
#             country.append(year2)

# tree.write('bbb.xml',encoding="utf-8",xml_declaration=True)
# tree.write('bbb.xml')


#
# new_xml = ET.Element('namelist')  # 初始化一个namelist节点,获取一个对象new_xml
# name = ET.SubElement(new_xml, "name_s", attrib={"enrolled": "yes"})  # 初始化一个子节点

import xml.etree.ElementTree as ET

new_xml = ET.Element("namelist")  # 生成名叫namelist的子节点
name = ET.SubElement(new_xml, "name", attrib={"enrolled": "yes"})  # 在namelist下生成名叫name的子节点
age = ET.SubElement(name, "age", attrib={"checked": "no"})
sex = ET.SubElement(name, "sex")
sex.text = '33'
name2 = ET.SubElement(new_xml, "name", attrib={"enrolled": "no"})
age = ET.SubElement(name2, "age")
age.text = '19'

et = ET.ElementTree(new_xml)  # 生成文档对象
et.write("test.xml", encoding="utf-8", xml_declaration=True)  # 写到文件去，最后声明是xml格式

ET.dump(new_xml)  # 打印生成的
