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
        self.head.next = self.tail
        self.tail.prev = self.head


    def addElementFront(self,element):
        node = Node(element)
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head
        self.length += 1


    def addElementTail(self,element):
        node = Node(element)
        node.next = self.tail.prev
        self.tail.prev = node
        #bookmark--------------


    def traverse(self):
        cursor = self.head
        while(cursor.next!=None):
            cursor = cursor.next
        return cursor

    def printAllNodes(self):
        cursor = self.head
        while(cursor!=None):
            if(cursor.next==None):
                print(f'{cursor.element}',sep="",end="",flush=True)
            else:
                print(f'{cursor.element}',sep="",end="<->",flush=True)
            cursor = cursor.next
        print("\n")