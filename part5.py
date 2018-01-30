#python盒子：模块、包和程序
#1.命令行参数
import sys
#print("Program arguments:", sys.argv)
##2. 倒入模块, 导入整个report模块，只要在名称前加上report. ,report.py的所有内容对本文件都是可见的
##通过模块名称限定模块的内容，可以避免命名冲突，不会被其他模块错误的调用
#import report
#
#description = report.get_description()
#print("Today's weather:", description)
##2.1 文件名report.py, 函数中的引用表示所有代码都在同一函数下，并且没有其他名称为choice的函数
#def get_description():
#    '''Return random weather, just like the pros'''
#    from random import choice
#    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knowns']
#    return choice(possibilities)
#
##上面的例子等价于
#def get_description1():
#    import random
#    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knowns']
#    return random.choice(possibilities)


##2.2 使用别名
#import report as wr
#print("weather:", wr.get_description())
##2.3 导入模块的某一部分
#from report import get_description
#print("Today's weather2:", get_description())
#
##2.4 模块的搜索路径
#for place in sys.path:
#    print(place)
#2.5 为了使Python应用更具有可扩展性，可以把多个模块组织称文件层次，称之为包
#from source import daily, weekly
#
#print("Daily forecast:", daily.forecast())
#print("Weekly forecast:", weekly.forecast())
#2.6 使用setdefault()和defaultdict()处理缺失的键
#如果原来的键不存在，新的默认值会添加进去，如果已经存在的键不会改变原来的值
periodic_table = {'Hydrogen':1, 'Helium':2}
carbon = periodic_table.setdefault('Carbon', 12)
print(carbon)
Helium = periodic_table.setdefault('Helium', 11)
print(Helium)
#2.7 defaultdict()用法同上，但是创建字典时对每个新的键都会指定默认值，他的参数是一个函数。
#参数为int()函数时，任何缺失的值都被赋为整数0, list()返回空列表，dict()返回空字典
from collections import defaultdict
periodic_table = defaultdict(int)
print(periodic_table['Helium'])
print(periodic_table['Lead'])
#参数为no_idea()函数时，任何缺失的值都被赋为'Huh?'
def no_idea():
    return 'Huh?'
bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable Snowman'
print(bestiary['B'])





