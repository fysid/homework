from romanize import romanize


while True:
    a = int(input())
    if a == -1:
        break
    romanized = romanize(a)
    print(romanized)
