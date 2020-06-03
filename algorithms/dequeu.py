from collections import deque

def my_q(n):
    q = deque()
    for i in range(0,n):
        q.append(input("put stuff in q\n"))


    print(q)

    for i in range(0,n):
        print(q.popleft())


my_q(5)
