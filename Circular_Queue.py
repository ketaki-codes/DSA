class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
class CQueue:
    def __init__(self):
        self.front=self.rear=None
    def  enqueue(self,new_node):
        if self.rear :
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node
        self.rear.next=self.front    #added for cqueue
    def dequeue(self):
        if self.front:
            temp=self.front
            if self.front==self.rear: #updated for cqueue
               self.front=self.rear=None
               print("Now Queue is empty")

            else:
                self.front=self.front.next
                self.rear.next=self.front # added for cqueue
            temp=None
            
        else:
            print("Queue is empty")           

    def print(self):
        temp=self.front
        while True :
            print(temp.data,end =" ")
            temp=temp.next 
            if temp==self.front:
                break
        print()    

qu=CQueue()
qu.enqueue(Node(11))  
qu.enqueue(Node(55))  
qu.enqueue(Node(25))  
qu.enqueue(Node(31))  
qu.enqueue(Node(14))  
qu.print()
qu.dequeue()
qu.print()
qu.dequeue()
qu.print()
qu.dequeue()
qu.print()
qu.dequeue()
qu.print()



 


