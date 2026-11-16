class Node:
    def __init__(self, value, pr):
        self.data = value
        self.priority=pr
        self.next = None
class PriorityQueue:
    def __init__(self):
        self.front=self.rear=None
    def enqueue(self, new_node):
        if self.front==None:#first node to be inserted
            self.front=new_node
            return
        if self.front.priority>new_node.priority:#first position
            new_node.next=self.front
            self.front=new_node    
            return
        else:
            temp=self.front
            while temp:
                if new_node.priority<=temp.priority:
                    break
                else:
                    prev=temp
                    temp=temp.next
            prev.next=new_node
            new_node.next=temp
    def display(self):
        temp=self.front
        while temp:
            print(temp.data , end =" ")
            temp=temp.next
        print()
#create priority queue
pq =PriorityQueue()
pq.enqueue(Node(100,2))
pq.enqueue(Node(300,5))
pq.enqueue(Node(800,7))
pq.enqueue(Node(200,9))
pq.enqueue(Node(900,6))
pq.display()
                            
