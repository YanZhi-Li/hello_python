test_str = '''I did said \"There was a Young Lady of Norway\",
    who casually sat in a d\toorway;
    When the door \nsqueezed her flat
    '''
print(test_str)
#int()
#float()
#str()


#实用*复制
start = 'Na' * 4 + '\n'
middle = 'Hey ' * 3 + '\n'
end = 'Goodbye'
print(start + middle + end)
a = 7
print(type(a))
print(True)
print(divmod(9, 5))
print(0x16)
print(int('12'))
print(int(1.0e4))
print("hello, world")

#[:] 提取从开头到结尾的整个字符串
#[start:] 从start提取到结尾
#[:end] 从开头提取到end-1
#[start:end] 从start提取到end-1
#[start:end:step]从start提取到end-1, 每step个字符提取一个
letters = 'abcedfghijklmnopqrstuvwxyz1234567890'
print(len(letters))
print(letters[:])
print(letters[10:])
print(letters[10:15])
print(letters[-3:])
print(letters[18:-3])
print(letters[-6:-2])
print(letters[::7])

