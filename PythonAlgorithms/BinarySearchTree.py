def main():
    tree = BinarySearchTree()
    tree.put(2, 'a')
    tree.put(7, 'a')
    tree.put(3, 'a')
    tree.put(4, 'a')
    tree.put(9, 'a')
    tree.put(11, 'a')
    tree.put(1, 'a')
    tree.Inorder()
    print(tree)
    tree.delete(7)
    print(tree)
    tree.delete(1)
    print(tree)
class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.__key = key
        self.__value=val
        self.__left = left
        self.__right = right
        self.__parent = parent
    def getKey(self):
        return self.__key
    def getValue(self):
        return self.__value
    def getLeft(self):
        return self.__left
    def getRight(self):
        return self.__right
    def getParent(self):
        return self.__parent
    def setKey(self, key):
        self.__key = key
    def setValue(self, val):
        self.__value = val
    def setLeft(self,leftChild):
        self.__left = leftChild
    def setRight(self,rightChild):
        self.__right = rightChild
    def setParent(self,newParent):
        self.__parent=newParent
    def __str__(self):
        return str(self.__key)+str(self.__value)

class BinarySearchTree:
    def __init__(self):
        self.__root = None
        self.__size =0

    def getSize(self):
        return self.__size

    def getRoot(self):
        return self.__root

    def Inorder(self):
        self._Inorder(self.__root)
    
    def _Inorder(self, node):
        if node:
            self._Inorder(node.getLeft())
            print(node.getKey(), node.getValue())
            self._Inorder(node.getRight())

    def get(self,key):
    # to retrieve the value associated with the given key
        return self._get(key,self.__root)

    def _get(self,key,currentNode):
    # helper method to get the key’s value of a node
        if not currentNode: # the node is empty
            return None
        elif key == currentNode.getKey(): # the key is the one we look for
            return currentNode.getValue()
        elif key < currentNode.getKey():
            return self._get(key,currentNode.getLeft()) # search left
        else:
            return self._get(key,currentNode.getRight())

    def put(self,key,val):
    # to insert a key-value pair
        if not self.__root: # root is None
            self.__root = TreeNode(key,val) # create a new tree node
            self.__size += 1 # increment the cached size
        else:
            self._add(key,val,self.__root) 

    def _add(self,key,val,currentNode): # add at a given node
        if key < currentNode.getKey():
            if not currentNode.getLeft(): # left doesn’t exist, create a node
                currentNode.setLeft(TreeNode(key,val,parent=currentNode))
                self.__size += 1
            else:
                self._add(key,val,currentNode.getLeft()) # add to the left

        elif key == currentNode.getKey(): # key already exists
            currentNode.setValue(val) # update value
        else:
            if not currentNode.getRight(): # right doesn’t exist, create a node
                currentNode.setRight(TreeNode(key,val,parent=currentNode))
                self.__size += 1
            else:
                self._add(key,val,currentNode.getRight())
    def delete(self,key):
        if self.__size > 1: # there is more than just the root
            nodeToRemove = self._locate(key,self.__root)
            if nodeToRemove: # we located the node to remove – not NONE
                self._remove(nodeToRemove)
                self.__size = self.__size-1
            else:
                raise KeyError('Error, key not in tree')
        elif self.__size == 1 and self.__root.getKey() == key:
            self.__root = None
            self.__size = self.__size - 1
        else: # we have one node and it is not the key, or tree is empty
            raise KeyError('Error, key not in tree')

    def _locate(self, key, currentNode):
        if currentNode:
            if currentNode.getKey() == key:
                return currentNode
            elif key < currentNode.getKey():
                return self._locate(key, currentNode.getLeft())
            else:
                return self._locate(key, currentNode.getRight())

    def _remove(self,currentNode):
        parentNode = currentNode.getParent()
        leftNode = currentNode.getLeft()
        rightNode = currentNode.getRight()
        # first case: the node to be deleted has no children
        if leftNode ==None and rightNode == None:
            if currentNode == parentNode.getLeft():
                parentNode.setLeft(None)
            else:
                parentNode.setRight(None)
        elif leftNode and not rightNode:
            if parentNode == None:
                self.__root = leftNode
            elif currentNode == parentNode.getLeft():
                parentNode.setLeft(leftNode)
            else:
                parentNode.setRight(leftNode)
            leftNode.setParent(parentNode)

        elif not leftNode and rightNode:
            if parentNode == None:
                self.__root = rightNode
            elif currentNode == parentNode.getLeft():
                parentNode.setLeft(rightNode)
            else:
                parentNode.setRight(rightNode)
            rightNode.setParent(parentNode)
        else:
            
            # finding the smallest key (extreme left) of the right subtree
            swap = self._findSmallest(currentNode.getRight())
            # copying the key and value
            currentNode.setKey(swap.getKey())
            currentNode.setValue(swap.getValue())
            # removing the node we copied
            self._remove(swap)

    def _findSmallest(self,currentNode):
        if currentNode.getLeft(): # there is someone smaller
            return self._findSmallest(currentNode.getLeft())
        else:
            return currentNode

    def _strHelper(self, node):
        """Returns list of strings,  total width of the tree, position of the middle node and the height"""
        # Base case, no child.
        if node.getLeft() == None and node.getRight() == None:
            row = '%s' % node.getKey()
            width = len(row)
            middle = width // 2
            height = 1
            return [row], width, middle, height 

        keyStr = '%s' % node.getKey()
        keyStrLength = len(keyStr)
        # Case 1: only have left child
        if node.getLeft() != None and node.getRight() == None:
            leftRows, leftWidth, leftMiddle, leftHeight = self._strHelper(node.getLeft())
            firstRow = (leftMiddle + 1) * ' ' + (leftWidth - leftMiddle - 1) * '_' + keyStr
            secondRow = leftMiddle * ' ' + '/' + (leftWidth - leftMiddle - 1 + keyStrLength) * ' '
            shiftedRows = [row + keyStrLength * ' ' for row in leftRows]
            return [firstRow, secondRow] + shiftedRows, leftWidth + keyStrLength,leftWidth + keyStrLength // 2, leftHeight + 2

        # Case 2: only have right child
        elif node.getLeft() == None and node.getRight() != None:
            rightRows, rightWidth, rightMiddle, rightHeight = self._strHelper(node.getRight())
            firstRow = keyStr + rightMiddle * '_' + (rightWidth - rightMiddle) * ' '
            secondRow = (keyStrLength + rightMiddle) * ' ' + '\\' + (rightWidth - rightMiddle - 1) * ' '
            shiftedRows = [keyStrLength * ' ' + row for row in rightRows]
            return [firstRow, secondRow] + shiftedRows, rightWidth + keyStrLength,keyStrLength // 2, rightHeight + 2, 

        # Two children.
        else:
            leftRows, leftWidth, leftMiddle, leftHeight = self._strHelper(node.getLeft())
            rightRows, rightWidth, rightMiddle, rightHeight = self._strHelper(node.getRight()) 
          
    
            firstRow = (leftMiddle + 1) * ' ' + (leftWidth - leftMiddle - 1) * '_' + keyStr + rightMiddle * '_' + (rightWidth - rightMiddle) * ' '
            secondRow = leftMiddle * ' ' + '/' + (leftWidth - leftMiddle - 1 + keyStrLength + rightMiddle) * ' ' + '\\' + (rightWidth - rightMiddle - 1) * ' '
            #append a few rows to fill in the blanks in the bottom, so that left and right lists are of the length
            if leftHeight < rightHeight:
                leftRows += [leftWidth * ' '] * (rightHeight - leftHeight)
            else:
                rightRows += [rightWidth * ' '] * (leftHeight - rightHeight)
            pairedRows = zip(leftRows, rightRows)
            rows = [firstRow, secondRow] + [i + keyStrLength * ' ' + j for i, j in pairedRows]
            return rows, leftWidth + rightWidth + keyStrLength,  leftWidth + keyStrLength // 2,max(leftHeight, rightHeight) + 2
    
    
    def __str__(self):
        rows, _, _, _ = self._strHelper(self.__root)
        result = ''
        for row in rows:
            result += row + "\n"
        return result
main()