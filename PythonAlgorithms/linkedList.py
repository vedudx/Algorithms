class LLNode:

    def __init__(self, value=0, point=None):
        self.next=point
        self.val = value
    
class LinkedList:

    def __init__(self):
        self.head = None
    

    def insert(self, value):
        if not self.head:
            self.head = LLNode(value)
        else:
            start = self.head
            while start.next != None:
                start = start.next
            start.next = LLNode(value)

    def find(self, value):

        start = self.head
        while start != None:
            if start.val == value:
                return 1
            start = start.next
        return None

    
    def print(self):
        start = self.head
        while start != None:
            print(start.val, '->', end = " ")
            start = start.next
            

    def remove(self, value):
        if not self.head:
            print('No element in LinkedList')
        else:
            
            if self.head.val == value:
                self.head = self.head.next
                return 1
            else:
                prev = self.head
                start = prev.next
                while start.next != None:
                    if start.val == value:
                        prev.next = start.next
                        return 1
                    prev = prev.next
                    start = start.next
        return None
                

                


        
    



