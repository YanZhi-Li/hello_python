#列表
#weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
#list_create = []
#list_new = list()
#print(type(list_new))
#print(type(list_create))
#print(type(weekdays))
#
#list('cat')
#a_tuple = ('dog', 'cat', 'pig')
#print(list(a_tuple))
##split的用法
#splitme = 'a/b//c/d///f'
#print(splitme.split('/'))
##列表访问
#print(weekdays[2])
#print(weekdays[-5])
#print(weekdays[::2])
##利用切片可实现列表逆序
#print(weekdays[::-1])
##包含列表的列表
#small_birds = ['hummingbird', 'finch']
#extinct_birds = ['dodo', 'passenger', 'norwegian']
#carol_birds = [3, 'French', 2, 'turtledoves']
#all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]
#print(all_birds)
#print(all_birds[0])
#print(all_birds[3][3])
##列表的操作(尾部追加/指定位置添加/删除指定位置/按名称删除/)
#weekdays.append('HaHa')
#print(weekdays)
#weekdays.insert(6, 'Hello, world')
#print(weekdays)
#del weekdays[-1]
#print(weekdays)
#weekdays.remove('HaHa')
#print(weekdays)
##extend或+=合并/实用pop获取并删除指定位置元素,pop(0)和append可实现FIFO队列结构
#marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
#others = ['Gummo', 'Karl']
#print(marxes + others)
#marxes.extend(others)
#print(marxes)
#marxes.pop()
#print(marxes)
#marxes.pop(-2)
#print(marxes)
##列表的方法：index('Chico')获取指定位置元素， in 可判断是否存在 ， count('haha')特定值出现的次数
#marxes.insert(0, 'karl')
#print(marxes)
#print(others in marxes)
#print('Gummo' in marxes)
##实用join（）转换为字符串
#print(','.join(others))
##sorted()返回排好序的列表副本，原列表内容不变
#sorted_mares = sorted(marxes)
#print(marxes)
#print(sorted_mares)
##sort()对原列表重新排序，改变原来内容， 默认升序，reverse=True可改变为降序
#sorted_mares = marxes.sort(reverse=True)
#print(marxes)
#print(sorted_mares)
##实用=赋值， 实用copy()复制
#a = [1, 2, 3]
#b = a
#a.insert(2, 'surprise')
#print(a)
#print(b)
#b = a.copy()
#c = list(a)
#d = a[:]

####################     元组(一旦创建便无法修改)
##元组可以作为字典的键， 函数的参数是以元组形式传递的
#empty_tuple = ()
#one_tuple = ('Groucho', )
#marx_tuple = 'Groucho', 'Chico', 'Harpo', 'Zeppo'
#marx_tuple = ('Groucho', 'Chico', 'Harpo', 'Zeppo')
##元组解包
#a, b, c, d= marx_tuple
#print(b)
##元组转换
#marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
#print(tuple(marxes))


####################     字典
#使用{}，创建个元素拥有与之对应的互不相同的键
#empty_dict = {}
#bierce = {
#    'day':'A period of twenty-four hours',
#    'positive': "Mistaken at the top of one's open"
#}
#lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
#print(dict(lol))
#lot = [('a', 'b'), ('c', 'd'), ('e', 'f')]
#print(dict(lot))
#tol = (['a', 'b'], ['c', 'd'], ['e', 'f'])
#print(dict(tol))
#los = ['ab', 'cd', 'ef']
#print(dict(los))
#tos = ('ab', 'cd', 'ef')
#print(dict(tos))
#
#name_dict = {
#    'Chapman':'Graham',
#    'Cleese' : 'John',
#    'Idle': 'Eric',
#    'Jones': 'Terry',
#    'Plalin':'Michael',
#}
#print(name_dict['Jones'])
##使用update（）合并字典
#other_name = {
#    'Marx': 'Groucho',
#    'Howard': 'Moe'
#}
#name_dict.update(other_name)
#print(name_dict)
##使用del删除具有指定键的元素
#del name_dict['Cleese']
##使用clear()删除所有元素
#name_dict.clear()
##使用in判断某一个键是否存在
#print('Marx' in name_dict)
##字典的方法：[key]获取元素/keys获取所有键/使用values()获取所有值/使用=赋值copy()复制
#other_name['Marx']
#other_name.get('Howard')
#print(other_name.get('Jones', 'Have not this name'))
#print(other_name.keys())
#print(other_name.values())
#print(other_name.items())
#a = other_name;
#b = other_name.copy();
#other_name['Howard'] = 'test_name'
#print(a)
#print(b)


################## 集合
#集合就是舍弃了值的，仅剩下键的字典。集合是无序的。仅仅想知道某一个元素是否存在而不关心其他的，使用集合是非常好的选择
#empyt_set = set()
#even_num = {1, 2, 3, 4, 5}
##类型转换
#print(set('letters'))
#print(set(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']))
#print(set(('Groucho', 'Chico', 'Harpo', 'Zeppo')))
#print(set({'a':1, 'b':2, 'c':3}))
##使用in测试值是否存在 集合仅仅是一系列值组成的序列，字典是一个或多个键值对组成的序列
#drinks = {
#    'martini':{'vodka', 'vermouth'},
#    'black russian':{'vodka', 'kahlua'},
#    'white russian':{'cream', 'kahlua', 'vodka'},
#    'manhattan':{'rye', 'vermouth', 'bitters'},
#    'screwdirver':{'orange juice', 'vodka'}
#}
#for name, contents in drinks.items():
#    if 'vodka' in contents and not('vermouth' in contents or 'cream' in contents):
#        print(name)
#print(' ')
##合并及运算符 交集运算符&, 元素同时存在比较的两个集合中. 交集函数intersection()
#for name, contents in drinks.items():
#    if contents & {'orange juice', 'vermouth'}:
#        print(name)
#print(' ')
#for name, contents in drinks.items():
#    if 'vodka' in contents and not contents & {'orange juice', 'vermouth'}:
#        print(name)
#print(' ')
#a = {1, 2, 3, 4}
#b = {2, 4, 6, 8}
#print(a.intersection(b))
#print(a & b)
##并集 |或union()
#print(a | b)
#print(a.union(b))
##差集 -或difference()
#print(a - b)
#print(a.difference(b))
##异或集 ^或symmetric_difference()(仅在两个集合中出现一次)
#print(a ^ b)
#print(a.symmetric_difference(b))
##子集 <=或issubset()   (< 是真子集)
#print(b <= a)
#print(b <= b)
#print(b < a)
#print(a.issubset(b))
##超集 >=或issuperset()  (> 是真超集)
#print(a >= b)
#print(a > b)
#print(a.issuperset(b))


#总结
#1.列表(使用方括号创建)/元组（使用逗号创建）/字典（使用花括号创建） 都可以通过方括号对单个元素访问
marx_list = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
marx_tuple = 'Groucho', 'Chico', 'Harpo', 'Zeppo'
marx_dict = {'Groucho':'banjo', 'Chico':'piano', 'Harpo':'harp'}
print(marx_list[2])
print(marx_tuple[2])
print(marx_dict['Harpo'])
#2.创建自定义结构体，需要了解个内置数据类型的限制。 字典的键必须是不可变对象，因此列表、字典、集合均不能作字典的键但元组可以。






















