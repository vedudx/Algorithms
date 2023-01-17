
def binarySearch(start, end, value, A):
#prereq - sorted array A
    mid = (start + end)//2
    if start > end:
        return -1
    if A[mid] == value:
        return mid
    elif A[mid] < value:
        return binarySearch(mid+1, end, value, A)
    else:
        return binarySearch(start, mid - 1, value, A)



def main():

    #implementing loop based binary search
    array = list(map(int, input('Enter array seperated by space: ').split()))
    #sorting array just incase
    array.sort()
    value = int(input('Enter value to be found: '))
    print(*array)
    print(binarySearch(0, len(array), value, array))
    l = 0
    r = len(array) - 1
    found = False
    while l <= r:
        mid = (l+r)//2
        if array[mid] == value:
            found = True
            break
        elif array[mid] < value:
            l = mid + 1
        else:
            r = mid - 1
    

    if found:
        print('Found')
    else:
        print('Not found')
    

if __name__ == '__main__':
    main()

