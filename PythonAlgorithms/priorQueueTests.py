from priorityQueue import priorityQueue





def main():
    myQueue = priorityQueue()
    for i in range(0, 10, 2):
        myQueue.insert(i)

    while myQueue.getSize() != 0:
        print(myQueue.getMax())







if __name__ == '__main__':
    main()