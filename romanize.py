# romanize returns the Romans representation of the given number.
def romanize(number: int):
    if number <= 0 or number > 399:
        raise Exception('Number should be in [1, 399] range')
    conv = [(100, 'C'),
            (50, 'L'), (10, 'X'),
            (5, 'V'), (1, 'I')]
    result = [0] * len(conv)
    is_positive = [True] * len(conv)
    for i, (value, _) in enumerate(conv):
        result[i] = number // value
        number -= result[i] * value
        if result[i] == 4:
            result[i] = 1
            if result[i-1] == 0:
                result[i-1] += 1
                is_positive[i-1] = False
            else:
                result[i-2] += 1
                result[i-1] = 0
                is_positive[i-2] = False
    s = ''
    for i, (_, c) in enumerate(conv):
        if is_positive[i]:
            s += c * result[i]
        else:
            if result[i+1] == 0:
                s += (result[i]-1) * c + conv[i+2][1] + c
                result[i+2] = 0
            else:
                s += (result[i]-1) * c + conv[i+1][1] + c
                result[i+1] = 0
    return s


while True:
    a = int(input())
    if a == -1:
        break
    romanized = romanize(a)
    print(romanized)
