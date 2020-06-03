#impeliment a Q using list. get n and add data to q and print them in order.
def q_list(n):
    my_q = []
    for i in range(0,n):
        item = input("insert items for q \n")
        my_q.append(item)
    for i in range(0,len(my_q)):
        print(my_q.pop(0))


q_list(5)
