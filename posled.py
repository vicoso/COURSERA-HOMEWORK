a = int(input())
aMax = a
kolvo = 0
while a != 0:
    if aMax == a:
        kolvo += 1
        a = int(input())
    elif aMax < a:
        kolvo = 0
        aMax = a
        kolvo += 1
        a = int(input())
    elif aMax > a:
        a = int(input())
print(kolvo)
