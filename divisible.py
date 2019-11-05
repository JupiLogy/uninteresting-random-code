print('Is x divisible by y?')
x = int(input('x = '))
y = int(input('y = '))

if x % 4 == 0:
    print(str(x) + ' is divisible by 4.')
elif x % 2 == 0:
    print(str(x) + ' is even.')

if x % y == 0:
    print('Yes! %.0f' % x + ' is divisible by %.0f.' % y)
else:
    print('No! %.0f' % x + ' is not divisible by %.0f.' % y)
