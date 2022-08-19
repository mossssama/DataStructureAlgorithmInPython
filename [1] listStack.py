class ListStack:
    def __init__(self):
        global __ls;   self.ls=[]
        
    def push(self,d):
        self.ls.append(d);

    def pop(self): 
        print("{t} is poped".format(t=self.ls[len(self.ls)-1]));                return self.ls.pop()   

    def getElementsNo(self):
        print("Number of stack elements is: {t}".format(t=len(self.ls)));       return len(self.ls)

    def isEmpty(self):
        return len(self.ls)==0

    def getTop(self):
        if len(self.ls)>0:
            print("Stack Top is: {t}".format(t=self.ls[len(self.ls)-1]));       return self.ls[len(self.ls)-1]

    def clearStack(self):
        self.ls.clear(); print("Stack is cleared")

    def printStack(self):
        temp=len(self.ls)-1;  print("Stack=[",end=" ")   
        while temp>=0:
            print(self.ls[temp],end=" "); temp-=1
        print("]")

# For testing the stack
s=ListStack()
s.push(13);   s.push(12);    s.push(1999)
s.printStack();      s.getElementsNo()
s.getTop()
print("Is the stack empty ? {t}".format(t=s.isEmpty()))
s.pop()
s.getTop()
s.printStack();      s.getElementsNo()
s.clearStack();      s.printStack()