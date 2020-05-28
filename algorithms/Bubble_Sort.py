#arr = [64, 34, 25, 12, 22, 11, 90]

def bubble_sort(arr):
    
    for i in range(0,len(arr)):
        for n in range(i+1,len(arr)):
            if arr[i] > arr[n]:
                arr[i],arr[n] = arr[n],arr[i]

    print(arr)
    return arr

print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
