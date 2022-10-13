'''This is an implementation of a basic Doubly Linked Lists

written by- Aman Agrawal
date - 12/10/2022

'''


class Node():
    def __init__(self,element):
        self.element = element
        self.next = None
        self.prev = None



class DoublyLinkedList():
    def __init__(self):
        self.head = Node("head")
        self.length = 0
        self.tail = Node("tail")
        self.head.next = None
        self.tail.prev = None
        self.tail.next = self.head
        self.head.prev = self.tail


    def addElementFront(self,element):
        node = Node(element)
        self.head.prev.next = node
        node.prev = self.head.prev
        self.head.prev = node
        node.next = self.head
        self.length += 1


    def addElementTail(self,element):
        node = Node(element)
        lastNode = self.tail
        lastNode.next.prev = node
        node.next = lastNode.next
        node.prev = lastNode
        self.tail.next = node
        self.length += 1


    def _size(self):
        return self.length


    def printAllNodes(self):
        cursor = self.tail
        while(cursor!=None):
            if(cursor.next==None):
                print(f'{cursor.element}',sep="",end="",flush=True)
            else:
                print(f'{cursor.element}',sep="",end="<->",flush=True)
            cursor = cursor.next
        print("\n")




anew = DoublyLinkedList()
anew.addElementFront(8)
anew.addElementFront(5)
anew.addElementFront(3)
anew.addElementTail(2)
anew.addElementTail(6)
anew.addElementTail(9)
anew.printAllNodes()
print("Size of list->",anew._size())


#Time Complexity till now without printAllNodes() is O(1)
#Total Time Complexity is O(n) 