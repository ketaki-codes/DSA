class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
class LQueue:
    def __init__(self):
        self.front=self.rear=None
    def  enqueue(self,new_node):
        if self.rear :
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node
    def dequeue(self):
        if self.front:
            temp=self.front
            self.front=self.front.next
            if self.front==None:
               self.rear=None
               temp=None
               print("Now Queue is empty")
        else:
            print("Queue is empty")           

    def print(self):
        temp=self.front
        while temp:
            print(temp.data,end =" ")
            temp=temp.next 
        print()    

qu=LQueue()
qu.enqueue(Node(10))  
qu.enqueue(Node(50))  
qu.enqueue(Node(25))  
qu.enqueue(Node(31))  
qu.enqueue(Node(14))  
qu.print()
qu.dequeue()
qu.dequeue()
qu.dequeue() 
qu.print()
qu.dequeue()
qu.enqueue(Node(91))  
qu.enqueue(Node(64)) 
qu.print()


