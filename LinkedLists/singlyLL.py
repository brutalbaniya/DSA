'''This is an implementation of a Basic Linked List 

written by- Aman Agrawal
date - 12/10/2022

'''


class LNode():
    def __init__(self, element):
        self.element = element
        self.next = None

class LinkedList():

    def __init__(self):
        self.head = LNode("head")
        self.length = 0


    def addElement(self,element):
        node = LNode(element)
        node.next = self.head.next
        self.head.next = node
        self.length += 1


    def removeElement(self):
        print("[-]Removing First Element")
        removed = self.head.next
        self.head.next = self.head.next.next
        self.length -= 1
        self.printNodes()
        return(removed)


    def printNodes(self):
        cursor = self.head
        while(cursor!=None):
            print(cursor.element)
            cursor = cursor.next



anew=LinkedList()
anew.addElement(5)
anew.addElement(6)
anew.addElement(8)
anew.printNodes()
anew.removeElement()


#Time Complexity till now without printNodes() is - O(1)
#Total Time Complexity- O(n)