class Node:
    def __init__(self,d,p,n):
        self.data=d;    self.prev=p;     self.next=n

class DoubleLinkedList:
    def __init__(self,h=None,t=None):
        self.head=h;     self.tail=t

    def addFirst(self,d):
        node=Node(d,None,self.head)
        if self.head!=None:
            self.head.prev=node
        if self.head==None:
            self.tail=node
        self.head=node
    
    def addLast(self,d):
        node=Node(d,self.tail,None)
        if self.tail!=None:
            self.tail.next=node
        if self.tail==None:
            self.head=node
        self.tail=node

    def deleteFirst(self):
        x=self.head.data;     self.head=self.head.next;    self.head.prev=None;   print("{d} is deleted".format(d=x));   return x

    def deleteLast(self):
        x=self.tail.data;     self.tail=self.tail.prev;    self.tail.next=None;   print("{d} is deleted".format(d=x));   return x

    def getElementsNo(self):
        temp=self.head;     elm=0
        while temp:
           elm+=1;      temp=temp.next
        print("Number of stack elements is: {e}".format(e=elm));      return elm

    def isEmpty(self):
        return self.head==None

    def getHead(self):
        if self.head!=None:
            print("Double Linked List Head is: {d}".format(d=self.head.data));   return self.head.data

    def getTail(self):
        if self.tail!=None:
            print("Double Linked List Tail is: {d}".format(d=self.tail.data));   return self.tail.data

    def clearDoubleLinkedList(self):
        while self.head!=None:
            self.head=self.head.next
        self.tail=None;    print("Double Linked List is cleared")

    def printDoubleLinkedList(self):
        temp=self.head
        print("Double Linked List=[ ",end="")
        while temp:
            print(temp.data,end=" <--> ");   temp=temp.next
        print("None ]",end="")
        return ""
    
l=DoubleLinkedList();    print(l.printDoubleLinkedList());  print("Is the DLL empty ? {t}".format(t=l.isEmpty()));  l.getElementsNo();  l.getHead();  l.getTail();  print("");
l.addFirst(13);          print(l.printDoubleLinkedList());  print("Is the DLL empty ? {t}".format(t=l.isEmpty()));  l.getElementsNo();  l.getHead();  l.getTail();  print("");
l.addFirst(12);          print(l.printDoubleLinkedList());  print("Is the DLL empty ? {t}".format(t=l.isEmpty()));  l.getElementsNo();  l.getHead();  l.getTail();  print("");
l.addFirst(999);          print(l.printDoubleLinkedList());  print("Is the DLL empty ? {t}".format(t=l.isEmpty()));  l.getElementsNo();  l.getHead();  l.getTail();  print("");
l.addLast(1000);         print(l.printDoubleLinkedList());  print("Is the DLL empty ? {t}".format(t=l.isEmpty()));  l.getElementsNo();  l.getHead();  l.getTail();  print("");
l.deleteFirst();         print(l.printDoubleLinkedList());  print("Is the DLL empty ? {t}".format(t=l.isEmpty()));  l.getElementsNo();  l.getHead();  l.getTail();  print("");
l.deleteLast();          print(l.printDoubleLinkedList());  print("Is the DLL empty ? {t}".format(t=l.isEmpty()));  l.getElementsNo();  l.getHead();  l.getTail();  print("");
l.clearDoubleLinkedList(); print(l.printDoubleLinkedList());  print("Is the DLL empty ? {t}".format(t=l.isEmpty()));  l.getElementsNo();  l.getHead();  l.getTail();  print("");