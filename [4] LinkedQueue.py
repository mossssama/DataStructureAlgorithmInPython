class Node:
    def __init__(self,d,n=None):
        self.data=d;       self.next=n;

class LinkedQueue:
    def __init__(self,f=None,r=None):
        self.front=f;      self.rear=r;

    def enqueue(self,d):
        node=Node(d,None)
        if self.front==None:
            self.front=node
        if self.rear!=None:
            self.rear.next=node
        self.rear=node
        

    def dequeue(self):
        x=self.front.data;       self.front=self.front.next; 
        print("{i} is poped".format(i=x));       return x

    def getElementsNo(self):
        temp=self.front;      elm=0
        while temp:
            elm+=1;          temp=temp.next
        print("Number of queue elements is: {l}".format(l=elm));   return elm
    
    def isEmpty(self):
        return self.front==None

    def getFront(self):
        if self.front!=None:
            print("Queue front is: {f}".format(f=self.front.data));       return self.front.data

    def getRear(self):
        if self.front!=None:
            print("Queue rear is: {r}".format(r=self.rear.data));         return self.rear.data

    def clearQueue(self):
        self.rear=None
        while self.front!=None:
            self.front=self.front.next
        print("Queue is cleared")

    def printQueue(self):
        temp=self.front;   print("Queue=[",end=" ")
        while temp:
            print(temp.data,end=" ");          temp=temp.next
        print("]")



# For testing the queue
q=LinkedQueue()
q.enqueue(13);        q.enqueue(12);    q.enqueue(1999)
q.printQueue();       q.getElementsNo()
q.getFront();         q.getRear()
print("Is the queue empty ? {t}".format(t=q.isEmpty()))
q.dequeue()
q.getFront();        q.getRear()
q.printQueue();      q.getElementsNo()
q.clearQueue();      q.printQueue()