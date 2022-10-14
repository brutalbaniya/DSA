
'''This is an implementation of a Queue Data Structure using Singly Linked Lists

written by- Aman Agrawal
date - 13/10/2022

'''

class Node:
    def __init__(self,element):
        self.element = element
        self.next = None




class Queue():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0



    def isEmpty(self):
        return self.length==0



    def getFirstElement(self):
        return self.head.element



    def enqueue(self,element):
        node = Node(element)
        if(self.isEmpty()):
            self.head = node
        else:
            node.next = self.head.next
            self.head.next = node
        self.length += 1



    def dequeue(self):
        if(self.isEmpty()):
            print("Empty List!")
        else:
            dequeued = self.head.element
            self.head = self.head.next
            self.length -= 1
            return "dequeued-",dequeued



    def printAllNodes(self):
        if(self.isEmpty()):
           print("Empty List!")
        else:
            cursor = self.head
            while(cursor!=None):
                if(cursor.next==None):
                    print(f'{cursor.element}',sep="",end="",flush=True)
                else:
                    print(f'{cursor.element}',sep="",end="<-",flush=True)
                cursor = cursor.next
            print("\n")




anew = Queue()
anew.enqueue(1)
anew.enqueue(2)
anew.enqueue(3)
anew.enqueue(4)
anew.printAllNodes()
print("First Element->",anew.getFirstElement())
print("\n[-]Dequeuing....\n")
anew.dequeue()
anew.printAllNodes()
print("\nFirst Element->",anew.getFirstElement())



#Time Complexity of the implementation is O(1), without printAllNodes()
#Total Time Complexity will be O(n)
#Space Complexity will be O(n) , where n= Number of elements in the list

