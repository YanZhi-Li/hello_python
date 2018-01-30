
#代码结构
#1.使用#注释 可以代码和注释在同一行
#seconds_per_day = 86400 #60 sec/min * 60 min/hr * 24 hr/day
##2.使用\连接
#print("hello " + \
#      "world")
##3.实用if、elif、else进行比较
##  (5 < x) and (x < 10)
##  (5 < x) or (x < 10)
##  (5 < x) and not (x > 10)
##  5 < x < 10 python是允许的
#color = 'puce'
#if color == 'red':
#    print("It's a tomato")
#elif color == 'green':
#    print("It's a green pepper")
#else :
#    if color == 'bee purple':
#        print("I don't know what it is, but only bees can see it")
#    else :
#        print("I've never heard of the colot", color)
#
##4.什么是真值
##以下情况会被认为是False
##------------------
##布尔       False
##null类型   None
##整型       0
##浮点型      0.0
##空字符串    ''
##空列表     []
##空元组    （）
##空字典     {}
##空集合     set()
#
##5.while 循环 和 break/continue的使用
##while True:
##    stuff = input("String to capitalize [type q to quit]:")
##    if stuff == 'q':
##        break
##    else:
##        print(stuff.capitalize())
##        continue
#numbers = [1, 3, 5]
#position = 0
#print(len(numbers))
#while position < len(numbers):
#    number = numbers[position]
#    if number%2 == 0:
#        print("Found even num")
#        break
#    else:
#        print(number)
#    position += 1
#else: #循环外使用else, 没有执行break
#    print("No even numver found")
##6.使用for迭代
#test_dict = {'Groucho':'banjo', 'Chico':'piano', 'Harpo':'harp'}
#for item in test_dict.items():
#    print(item)
#for type, name in test_dict.items():
#    print("card:", type, "'s name is", name)
##7.zip()的并行迭代, 最短的序列用完为止
#days = ['Monday', 'Tuesday', 'Wednesday']
#fruits = ['banana', 'orange', 'peach']
#drinks = ['coffee', 'tea', 'beer']
#deserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
#for day, fruit, drink, desert in zip(days, fruits, drinks, deserts):
#    print(day, ": drink", drink, "- eat", fruit, "- enjoy", desert)
##8.range()生成自然数序列
#for x in range(0, 3):
#    print(x)
#for x in range(2, -1, -1):
#    print(x)
#list( range(2, -1, -1))
#9.推导式
#列表推导式 [ expression for item in iterable ]
#number_list = [num for num in range(0, 6)]
#print(number_list)
#a_list = [num for num in range(0, 6) if num % 2 == 0]
#print( a_list )
#b_list = [(row, col, cell) for row in range(1, 4) for col in range(1, 3) for cell in range(1, 4)]
#print( b_list )
##字典推导式 { key_expression : value_expression for expression in iterable }
#world = 'letters'
#letters_count = { letter : world.count(letter) for letter in world }
#print( letters_count )
##集合推导式 { expression for expression in iterable }
#a_set = { num for num in range(1, 6) if num % 2 == 1 }
#print( a_set )
##生成器推导式 元组没有推导式 圆括号之间的是生成器推导式返回的是一个生成器对象
##一个生成器智能运行一次， 列表/集合/字符串/字典都存储在内存中， 但生成器仅在运行中产生值，不会被保存下来
#number_list = ( num for num in range(1, 6) )
#print( type(number_list) )
#print( number_list )

##10. 函数
##传入到函数中的称为参数，当调用该函数时， 这些参数的值会被复制给函数中的对应参数
#def do_nothing():
#    pass
##10.1 函数可以接受任何数量（包括0）的任何类型的值作为入参， 并且返回任何数量（包括0）的任何类型的结果。默认返回None.
#def commentary( color ):
#    if color == 'red':
#        print("It's a tomato")
#    elif color == 'green':
#        print("It's a green pepper")
#    else :
#        if color == 'bee purple':
#            print("I don't know what it is, but only bees can see it")
#        else :
#            print("I've never heard of the color", color)
#commentary( 'blue' )
##10.2 0值的整型/浮点型、空字符串（‘’）、空列表（[]）、空元组（（，））、空字典（{}）、空集合（set()）都等价于False, 但是不等于None.
#def is_none( thing ):
#    if thing is None:
#        print( "It's None" )
#    elif thing:
#        print( "It's True" )
#    else:
#        print( "It's False" )
#is_none([])
#is_none({})
#is_none(())
#is_none(None)
##10.3 实用*收集位置参数, 无参数调用函数，什么也不返回，给函数传入所有参数都会以元组的形式返回
#def print_args(req1, req2='test2222', *args):
#    print( "Positional argument req1:", req1, "req2:", req2, "tuple:", args)
#print_args(req1="test111")
#print_args('test1')
#print_args('test1', 'test2')
#print_args('test1', 'test2', 'test3', 'test4', 'test5')
##使用**收集关键字参数， 可以将参数收集到一个字典中，参数的名字就是字典的键， 对应的参数值就是字典的值
#def print_kwargs(**kwargs):
#    print('Keyword arguments:', kwargs)
#print_kwargs(wine='merlot', entree='mutton', dessert="macaroon")

##10.4 文档字符串
#def print_if_true(thing, check):
#    '''
#    Prints the first argument if a second argument is True.
#    The operation is:
#        1. Check whether the *second* argument is true.
#        2. If it is, print the *first* argument .
#    '''
#    if check:
#        print(thing)
#
##help(print_if_true)
#print(print_if_true.__doc__)
##10.5 内部函数:也称为闭包
#def outer(a, b):
#    def inner(c, d):
#        return c + d
#    return inner(a, b)
#print(outer(5, 6))
#
##需要注意两点，inner2直接使用外部的saying参数，而不是通过另一个参数获取。
##knights（）返回的是inner2函数，而不是调用它
#def knights(saying):
#    def inner2():
#        return "We are the knights who say:'%s'" % saying
#    return inner2
#a = knights("Duck")
#print(type(a))
#print(a)
#print(a())
##10.6 匿名函数：lambda()函数，用它来代替小的函数。该函数接收一个参数，在冒号和末尾圆括号之间的部分为函数的定义
#def edit_story(words, fun):
#    for word in words:
#        print(fun(word))
#
#stairs = ['thud', 'meow', 'thud', 'hiss']
#def enliven(word):
#    return word.capitalize() + '!'
#edit_story(stairs, enliven)
##以上函数等价于
#edit_story(stairs, lambda word: word.capitalize() + '!')
##10.7 生成器用来创建python序列的一个对象。通常，生成器是为迭代器产生数据的。生成器函数和普通函数的类似只是返回值使用yield而不是return
#def my_range(first = 0, last = 10, step = 1):
#    number = first
#    while number < last:
#        yield number
#        number += step
#ranger = my_range(1, 4)
#for x in ranger:
#    print(x)
##10.8 装饰器：在不改变原代码的情况下，修改已经存在的函数。实质是一个函数，它把一个函数作为输入并且返回另外一个函数
#def document_it(func):
#    def new_function(*args, **kwargs):
#        print('Running function:', func.__name__)
#        print('Positional arguments:', args)
#        print('Keyword arguments:', kwargs)
#        ret = func(*args, **kwargs)
#        print('Ret:', ret)
#        return ret
#    return new_function
#def add_int(a, b):
#    return a + b
#cooler_add_ints = document_it(add_int)
#可直接要在装饰的函数前添加装饰器的名字
#@document_it
#def add_ints(a, b):
#    return a + b
#add_ints(3, 5)


##10.9 同样一个函数可以有多个装饰器，靠近函数定义（def上面）的装饰器最先执行，然后一个执行上面的
#def square_it(func):
#    def new_function(*args, **kwargs):
#        result = func(*args, **kwargs)
#        return result * result
#    return new_function
#@square_it
#@document_it
#def add_ints(a, b):
#    return a + b
#add_ints(3, 5)

##10.10 命名空间和作用域,全局变量
#animal = "fruitbat"
#def change_print_global():
#    animal = 'dog'
##    global animal
##    animal = 'pig'
#    print("animal:", animal, id(animal))
#change_print_global()
##10.11 locals()返回一个局部命名空间内容的字典
##globals（） 返回一个全局命名空间的字典
#def change_local():
#    animal = 'wombat'
#    print('locals:', locals())
#change_local()
#print("globals:", globals())
#名称中的_和__的用法：以两个下划线__开头和结束的名称都是Python的保留用法。
#function.__name__ ：函数的名称
#function.__doc__  ：文档字符串
#主程序被赋值特殊的名字__main__















