import queue

def my_q(n):
    q = queue.Queue()
    for i in range(0,n):
        q.put(input("put stuff in Q\n"))

    print(q)

    for i in range(0,n):
        print(q.get())


my_q(5)
