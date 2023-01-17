from linkedList import LinkedList





def main():
    array = list(map(int, input().split()))
    

    myLinkedList = LinkedList()
    for i in array:
        myLinkedList.insert(i)

    value = int(input())
    print(myLinkedList.find(value))
    print(myLinkedList.remove(value))
    print(myLinkedList.find(value))


    myLinkedList.print()










if __name__ == '__main__':
    main()