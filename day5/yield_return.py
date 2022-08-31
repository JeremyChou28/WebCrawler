# @description:yield和return的对比
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/12 15:53
# return方式是将所有的数据一次性处理
# yield将方法转换成生成器，可以理解为一种特殊的return方法
# 返回生成器，每构造一个items就用yield提升效率，可以减少服务器的资源
def f1():
    alist = []
    for i in range(10):
        alist.append(i)
    return alist


def f2():
    for i in range(10):
        yield i


print(f1())
index = f2()
print(next(index))
print(next(index))
print(next(index))
print(next(index))
print(next(index))
print(next(index))
