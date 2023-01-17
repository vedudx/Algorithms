
import math
#input is an array
#[1,2,3,6,7]
#Building Max Heap
#A[2j] is left child
#A[2j+1] is right child and A[j/2] is parent child


def BuildMaxHeap(array):
#this function makes max heap
    heapSize = len(array)
    for i in range(math.floor(heapSize//2), -1, -1):
        maxHeapify(array, i, heapSize)
    

def maxHeapify(array, i, heapSize):
#this 
    newParent = i
    if 2*i < heapSize:
        if array[2*i] > array[newParent]:
            newParent = 2*i
    if 2*i + 1 < heapSize:
        if array[2*i + 1] > array[newParent]:
            newParent = 2*i + 1
    array[newParent], array[i] = array[i], array[newParent]
    if newParent != i:
        maxHeapify(array, newParent, heapSize)


def heapSort(array, heapSize):
    BuildMaxHeap(array)

    for i in range(len(array)):
        MaxElement = array[0]
        array[0], array[heapSize - 1] = array[heapSize - 1], array[0]
        heapSize -= 1
        maxHeapify(array, 0 , heapSize)


def main():

    array = list(map(int, input().split()))
    BuildMaxHeap(array)

    heapSort(array, len(array))
    print(*array)








if __name__ == '__main__':
    main()