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
             print("Poped Element :",temp.data)
             self.top=self.top.next
             temp=None
    def print(self):
           
            temp=self.top
            print("Stack elements...")
            while temp:
              print(temp.data)
              temp=temp.next
st=stack()
st.push(Node(10))  
st.push(Node(23))
st.push(Node(17))              
st.push(Node(36))
st.push(Node(40))
st.push(Node(70))
st.print()
st.pop()
st.print()

