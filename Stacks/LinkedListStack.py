'''This is an implementation of a Stack Data Structure using Singly Linked Lists

written by- Aman Agrawal
date - 11/10/2022

'''


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



anew = Stack()
anew.push(6)
anew.push(8)
anew.push(11)
anew.pop()


#Time Complexity till now without printStack() is - O(1)
#Total Time Complexity- O(n)