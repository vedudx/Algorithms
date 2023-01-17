from maxHeap import maxHeapify, BuildMaxHeap
import math
from collections import deque

class priorityQueue:

    def __init__(self):
        self.baseArray = list()
       

    def insert(self, value):
        self.baseArray.append(value)    
        BuildMaxHeap(self.baseArray)


    def getMax(self):
        maxElem = self.baseArray[0]
        self.baseArray[0], self.baseArray[self.getSize() - 1] = self.baseArray[self.getSize() - 1], -1
       
        self.baseArray.pop()
        if self.getSize() != 0:

            maxHeapify(self.baseArray, 0, self.getSize())
        return maxElem

    def getSize(self):
        return len(self.baseArray)






