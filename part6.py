#1.1 对象既包含数据（变量，或者称为特性）， 也包含代码（函数，或者称为方法）。是某一类具体事物的特殊实例。
class Person():
    def __init__(self, name):
        self.name = name
huter = Person("Tom")
print("name:", huter.name)

