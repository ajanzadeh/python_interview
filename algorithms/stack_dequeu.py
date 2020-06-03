from collections import deque
def my_sta(n):
    stak = deque()
    for i in range(0,n):
        stak.append(input("put stuff in to stack\n"))


    print(stak)

    for i in range(0,len(stak)):
        print(stak.pop())


my_sta(6)
