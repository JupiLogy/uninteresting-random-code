def str_to_int(input):
    dict = {
        '1' : 1,
        '2' : 2,
        '3' : 3,
        '4' : 4,
        '5' : 5,
        '6' : 6,
        '7' : 7,
        '8' : 8,
        '9' : 9,
        '0' : 0
    }
    num = 0
    split_in = input.split('.')
    for char in range(len(split_in[0])):
        num += dict.get(split_in[0][char]) * (10 ** (len(split_in[0]) - char - 1))
    if len(split_in) > 1:
        for char in range(len(split_in[1])):
            num += dict.get(split_in[1][char]) * (10 ** (- char - 1))
    return num
