#10.12 标准异常
print("hello world")
short_list = [1, 2, 3]
while True:
    value = input('Position [a to quit]?')
    if 'q' == value:
        break
    try:
        postion = int(value)
        print(short_list[position])
    except IndexError as err:
        print('Bad index:', position)
    except Exception as other:
        print("Something else broke:", other)

