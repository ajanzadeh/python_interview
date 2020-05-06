# write a binary search.

def search(item_list, item):
    item_list = sorted(item_list)
    start = 0
    end = len(item_list) -1

    while start < end:
        middle_index = (start + end) //2
        middle = item_list[middle_index]
        if middle == item:
           return middle_index
        elif item > middle:
            start = middle_index+1
        else:
            end = middle_index -1
    return middle_index

print(search([1,5,2,4,9,10,11,12,14,18,7],10))
