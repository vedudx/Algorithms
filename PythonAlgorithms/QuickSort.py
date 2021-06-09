
def main():
    listi = list(map(int, input().split()))
    listi2 = [50, 20, 90, 30, 80, 40]
    quickSort(listi)
    quickSort(listi2)
    print(listi)

def partition(data,first,last): #not the same as in the slides

    pivotValue = data[first]  # choosing the pivot as the first element in the list
    leftMark = first + 1  # leftMark indicates the end of the first partition (+1)
    rightMark = last  # rightMark indicates the beginning of the second partition
    done = False
    print('Before partition: ', data)
    while not done:
        while leftMark <= rightMark and data[leftMark] <= pivotValue:
            leftMark = leftMark + 1  # shifting the pointer to the right
        while rightMark >= leftMark and data[rightMark] >= pivotValue:
            rightMark = rightMark - 1  # shifting the pointer to the left
        if rightMark < leftMark:  # the partitioning is done
            done = True
        else:  # elements blocking the partitioning need to be swapped around pivot
            temp = data[leftMark]
            data[leftMark] = data[rightMark]
            data[rightMark] = temp

    temp = data[first]  # putting pivot in place
    data[first] = data[rightMark]
    data[rightMark] = temp
    print('Right mark: ', rightMark)
    print('After Partition: ', data, '\n\n')

    return rightMark    

def quickSort(data):
# Sort myself using a quick sort.
    quickSort_helper(data,0,len(data)-1)

def quickSort_helper(data,first,last):
    if first<last:
        pivot=partition(data,first,last) # partition around a pivot
        quickSort_helper(data,first,pivot-1) #sort 1st half
        quickSort_helper(data,pivot+1,last) 

main()