
# Stack using Linked List
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class stack:
    def __init__(self):
        self.top=None 

    def isempty(self):
        return self.top is None    

    def push(self, new_node):
        new_node.next=self.top
        self.top=new_node

    def pop(self):
        if self.isempty():
            print("Stack is Empty")
        else: 
            temp=self.top
            poped_data=temp.data
            print("Poped Element :",temp.data)
            self.top=self.top.next
            temp=None
            return poped_data  
               
    def print(self):
        temp=self.top
        print("Stack elements...")
        while temp:
            print(temp.data)
            temp=temp.next


# Queue using Linked List
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LQueue:
    def __init__(self):
        self.front=self.rear=None

    def enqueue(self,new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node

    def dequeue(self):
        if self.front:
            temp=self.front
            dequed_data=temp.data
            self.front=self.front.next
            if self.front==None:
                self.rear=None
                print("Now Queue is empty")
            temp=None
            return dequed_data  
        else:
            print("Queue is empty") 
            
    def is_empty(self):
        return self.front is None                      

    def print(self):
        temp=self.front
        while temp:
            print(temp.data,end =" ")
            temp=temp.next 
        print()    


# Reverse Queue using Stack
def reverse_queue(q1):
    st1=stack()
    while not q1.is_empty():
        st1.push(Node(q1.dequeue()))

    while not st1.isempty():
        q1.enqueue(Node(st1.pop()))

    q1.print()


# Reverse Stack using Queue
def reverse_stack(s1):
    q1=LQueue()
    while not s1.isempty():
        q1.enqueue(Node(s1.pop()))

    while not q1.is_empty():
        s1.push(Node(q1.dequeue()))

    s1.print()


# Main Program
qu=LQueue()
st1=stack()

qu.enqueue(Node(10))  
qu.enqueue(Node(50))  
qu.enqueue(Node(25))  
qu.enqueue(Node(31))  
qu.enqueue(Node(14))  

qu.print()
reverse_queue(qu)

st1.push(Node(10))  
st1.push(Node(23))
st1.push(Node(17))              
st1.push(Node(36))
st1.push(Node(40))
st1.push(Node(70))

st1.print()
reverse_stack(st1)
