# @description:next函数使用以及读取文件内容的几种方法和编码格式显示的问题
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/14 22:27
# next方法有两个参数next(iterobject,default)
# iterobject为可迭代对象，default可省，如果可迭代对象取出完毕之后返回stopiteration；若写了default，则一直返回default

list = ['z', 'j', 'p']
list_item = iter(list)
print(next(list_item))
print(next(list_item))
print(next(list_item))
print(next(list_item, -1))
print("=============================================")
# 当用next方法读取文件时，若只执行一次，则默认读取第一行
# python3用next会出现报错'_io.TextIOWrapper' object has no attribute 'next'
# 解决办法：https://stackoverflow.com/questions/26967509/attributeerror-io-textiowrapper-object-has-no-attribute-next-python
#
# # 打开文件
# fo = open( "runoob.txt" , "r+" )
# print("文件名为: " , fo.name)
# for index in range( 5 ):
#     line = fo.next( )
#     print(   "第 %d 行 - %s" % (index , line))
# # 关闭文件
# fo.close( )

# 对于python3用readline而不用next
# 打开文件读取文件内容的readline方法
# with open( "E:\Python_language\pycharmProjects\Web_Crawler\day5\Function_next_txt.txt" , 'r+' ) as fo:
# 存在乱码问题，原因是由于chapter.txt是UTF-8编码，而系统默认是GBK，需要打开时转换成UTF-8编码才可以正常显示，即需要加上encoding='UTF-8'
# with open( "E:\Python_language\pycharmProjects\Web_Crawler\day4\QingYuNian_FirstChapter.txt" , 'r+' , encoding='UTF-8' ) as fo:
# with open( "E:\Python_language\pycharmProjects\Web_Crawler\day4\SanTi.txt" , 'r+' , encoding='UTF-8' ) as fo:
#     for index in range( 9 ):
#         line = fo.readline( )
#         print( "第 %d 行 - %s" % (index + 1 , line) )

# 打开文件读取文件内容的另一种循环方法
# index = 0
# with open( "E:\Python_language\pycharmProjects\Web_Crawler\day4\SanTi.txt" , 'r+' , encoding='UTF-8' ) as fo:
#     for line in fo:
#         print( "Line No:%d - %s " % (index , line) + '\n' )
#         index += 1
#         # 关闭文件

# 打开文件读取文件内容的枚举方法,注意Function_next_txt.txt是GBK编码，而系统默认是GBK，open打开的时候按照系统默认编码读取
# 因此这里可加可不加这句encoding='gbk'
fo = open("E:\Python_language\pycharmProjects\Web_Crawler\day5\Function_next_txt.txt", 'r+', encoding='gbk')
for index, line in enumerate(fo):
    print("Line No:%d - %s" % (index, line) + "\n")
fo.close()
# 出于对比，建立了一个刚才文件副本，保存成UTF-8格式，这里就得加上 encoding='UTF-8' ，否则就会乱码
# fo = open( "E:\Python_language\pycharmProjects\Web_Crawler\day5\Function_next_UTF8.txt" , 'r+' , encoding='UTF-8' )
# for index , line in enumerate( fo ):
#     print( "Line No:%d - %s" % (index , line) + "\n" )
# fo.close( )
