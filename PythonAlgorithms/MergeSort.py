def main():
    listi = list(map(int, input().split()))
    print(recursive_merge_sort(listi))

def recursive_merge_sort(data): 
    '''
    Use MergeSort to arrange the integers in a list (data) in descending order
    Inputs:  data (list) - list of integers to be sorted
    Returns: sorted data list
    '''

    # Set the base case 
    if len(data) <= 1:
        return data
    #Find the middle of the data list
    middle = len(data)//2
    #Recursively calling merge sort function for both halves of the data list
    left = recursive_merge_sort(data[:middle])
    right = recursive_merge_sort(data[middle:])
    
    # merge the two halves of the data list and return the data list
    return merge(left, right)
   
     
def merge(left, right):
    '''
    Helper function for merge sort which merges two list in descending order
    Inputs: left(list), right(list)
    Return: n\a
    '''
    sortedList =[]
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            sortedList.append(left[i])
            i+=1
        else:
            sortedList.append(right[j])
            j+=1
    
    sortedList += left[i:]
    sortedList += right[j:]
    return sortedList

main()