class Node:
    def __init__(self,d=None,n=None):
        self.data=d 
        self.next=n

class LinkedStack:
    def __init__(self):
        self.head=None

    def push(self,d):
        node=Node(d,self.head)
        self.head=node

    def pop(self):
        x=self.head.data;      print("{d} is poped".format(d=x));         self.head=self.head.next

    def getElementsNo(self):
        temp=self.head;     elm=0
        while temp:
            elm+=1;      temp=temp.next;
        print("Number of stack elements is: {e}".format(e=elm))
        return elm

    def isEmpty(self):
        return self.head==None

    def getTop(self):
        if self.head!=None:
            print("Stack Top is: {d}".format(d=self.head.data));  return self.head.data

    def clearStack(self):
        while self.head:
            self.head=self.head.next      
        print("Stack is cleared")

    def printStack(self):
        temp=self.head
        print("Stack=[",end=" ")
        while temp:
            print(temp.data,end=" ");     temp=temp.next
        print("]")



# For testing the stack
s=LinkedStack()
s.push(13);   s.push(12);    s.push(1999)
s.printStack();      s.getElementsNo()
s.getTop()
print("Is the stack empty ? {t}".format(t=s.isEmpty()))
s.pop()
s.getTop()
s.printStack();      s.getElementsNo()
s.clearStack();      s.printStack()