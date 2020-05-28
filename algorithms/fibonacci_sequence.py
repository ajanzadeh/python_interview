0, 1, 1, 2, 3, 5, 8, 13, 21,

def sequence(a,b,n):
    arr = []
    arr.append(a)
    arr.append(b)
    for i in range(0,n):
        c = a+b
        arr.append(c)
        a = b
        b = c
        c = 0

    resutl = " ,".join(map(str,arr))
    return resutl


print(sequence(0,1,20))
