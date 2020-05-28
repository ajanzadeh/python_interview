#arr = [12,11,13,5,6]
#arr = [12,11,13,5,6]



def sort(arr,n):
    if n == None:
        n = len(arr)-1
    if n > 0:
        if arr[n-1] > arr[n]  :
            arr[0],arr[n] =arr[n],arr[0]
        return sort(arr,n-1)
    return arr


print(sort([12,11,13,5,6],n=None))
