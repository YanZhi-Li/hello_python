def get_description():
    '''Return random weather, just like the pros'''
    from random import choice
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knowns']
    return choice(possibilities)

#上面的例子等价于
def get_description1():
    import random
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knowns']
    return random.choice(possibilities)
