class SNode():
    def __init__(self,value):
       self.value = value
       self.next = None




class Stack():
    def __init__(self):
        self.head = SNode("head")
        self.length = 0
        self.tail = self.head


    def push(self,number):
        node = SNode(number)
        node.next = self.head.next
        self.head.next = node
        self.length += 1


    def pop(self):
        popped = self.head.next
        self.head.next = self.head.next.next
        self.length -= 1
        return popped


    def printStack(self):
        cursor = self.head.next
        while(cursor!=None):
            print(cursor.value)
            cursor = cursor.next



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



#anew = Stack()
#anew.push(6)
#anew.push(8)
#anew.push(11)
#anew.pop()


anew=LinkedList()
anew.addElement(5)
anew.addElement(6)
anew.addElement(8)
anew.printNodes()
anew.removeElement()


#Time Complexity till now without printNodes()&printStack() is - O(n)
#Total Time Complexity- O(n)