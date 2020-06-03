def my_stak(n):
    stak = []
    for i in range(0,n):
        stak.append(input("put stuff in stack: \n"))

    print(stak)

    for i in range(0,len(stak)):
        print(stak.pop())



my_stak(5)
