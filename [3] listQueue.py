class listQueue:
    def __init__(self):
        global __ls;   self.ls=[]

    def enqueue(self,d):
        self.ls.append(d); 

    def dequeue(self):
        print("{i} is poped".format(i=self.ls[0]));                          return self.ls.pop(0);

    def getElementsNo(self):
        print("Number of queue elements is: {l}".format(l=len(self.ls)));    return len(self.ls)

    def isEmpty(self):
        return len(self.ls)==0
        
    def getFront(self):
        if len(self.ls)>0:
            print("Queue front is: {f}".format(f=self.ls[0]));               return self.ls[0]

    def getRear(self):
        if len(self.ls)>0:
            print("Queue rear is: {r}".format(r=self.ls[len(self.ls)-1]));   return self.ls[len(self.ls)-1]
    
    def clearQueue(self):
        self.ls.clear();   print("Queue is cleared")
    
    def printQueue(self):
        temp=0;   print("Queue=[",end=" ")
        while temp<len(self.ls):
            print(self.ls[temp],end=" "); temp+=1
        print("]")


# For testing the queue
q=listQueue()
q.enqueue(13);        q.enqueue(12);    q.enqueue(1999)
q.printQueue();       q.getElementsNo()
q.getFront();         q.getRear()
print("Is the queue empty ? {t}".format(t=q.isEmpty()))
q.dequeue()
q.getFront();        q.getRear()
q.printQueue();      q.getElementsNo()
q.clearQueue();      q.printQueue()