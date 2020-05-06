# write a binary search.

def search(item_list, item, end=None, start=0 ):
    item_list = sorted(item_list)
    if end is None:
      end = len(item_list) - 1

    middle_index = (start + end) //2
    middle = item_list[middle_index]
    print(item_list)
    print(middle)

    if middle == item:
       return middle_index
    elif item > middle:
       return search(item_list, item, end, middle+1)
    else:
       return search(item_list, item, middle-1, 0)


print(search([1,5,2,4,9,10,11,12,14,18,7],7))
