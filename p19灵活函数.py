#  离散数学题，在1-1000000中有多少个数字包括0或者1
a = 0
c: int = 0
for i in range(1,1000000):
#while a < 1000000:
    a += 1
    b = str(a)
#    list(b)
#    print(list(b))
#    print('0' in b or '1' in b)
    if ('0' in b or '1' in b):
        c += 1
print(c)