
def partition(arr,low,high):
    pivot=arr[high]
    i=low-1 # tracks last element smaller than pivot
    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1] # place pivot after last smallest element found
    return i+1 # index of pivot        


def fn(arr,low,high):
    if low<high: 
        p=partition(arr,low,high) # finds rightful position of pivot element
        fn(arr,low,p-1)
        fn(arr,p+1,high)
    return arr
    
    
print(fn([3,10,5,4,7,9,11,0],0,7)) 
# [0, 3, 4, 5, 7, 9, 10, 11]