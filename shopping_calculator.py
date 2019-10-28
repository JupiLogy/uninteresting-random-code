names = ['rice portions', 'chicken portions', 'bread loaves', 'vegetable portions']
prices = [0.3, 2.5, 1, 0.5]
quantity = []

for item in range(len(names)):
    print('\n' + names[item] + ' cost $%.2f' % prices[item])
    quantity.append(int(input('How many ' + names[item] + ' would you like? ')))
    print('The ' + names[item] + ' will cost you $%.2f' % (prices[item] * quantity[item]))

total = sum({prices[item] * quantity[item] for item in range(len(names))})
print('\nThe total is $%.2f' % total)
