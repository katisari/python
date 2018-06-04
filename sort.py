# Selection Sort


def selectSort(arr):
    for i in range(len(arr)):
        min=arr[i]
        minidx=i
        for j in range(i+1, len(arr)):
            if arr[j] < min:
                min=arr[j]
                minidx=j
        temp = arr[minidx]
        arr[minidx]=arr[i]
        arr[i]=temp
    return arr

print(selectSort([1,6,3,7]))

# Insertion Sort
def insertSort(arr):
    if(len(arr) <= 1):
        return arr
    for count in range(1, len(arr)):
        comparewith = arr[count]
        currentidx=count-1
        # shift
        while comparewith < arr[currentidx] and currentidx >= 0:
            arr[currentidx+1]=arr[currentidx]
            currentidx-=1
        arr[currentidx+1]=comparewith

    return arr

print(insertSort([1,-1]))

