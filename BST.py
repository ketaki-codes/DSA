#BST using Linked List
class Node:
    def __init__(self, value):
        self.left=None
        self.data=value
        self.right=None
class BST: 
    def __init__(self):
        self.root=None       
    def insert(self, new_node):
        if self.root is None: #BST is empty
            self.root=new_node
        else:
            temp=self.root
            while True:
                if new_node.data<temp.data:
                    if temp.left is None:
                        temp.left=new_node
                        return
                    else:
                        temp=temp.left
                else:
                    if temp.right is None:
                        temp.right=new_node
                        return
                    else:
                        temp=temp.right        
    def inorder(self, root):
        
        if root is None:
            return
        else:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
            
            if root is None:
                return
            else:               
                print(root.data, end=" ")
                self.preorder(root.left)
                self.preorder(root.right)

    def postorder(self, root): 
                if root is None:
                    return
                else:               
                    
                    self.postorder(root.left)
                    self.postorder(root.right)
                    print(root.data, end=" ")
    def findminmax(self):
        temp=self.root
        while temp.left:
            temp=temp.left 
        print("\nMininum :",temp.data)  
        temp=self.root
        while temp.right:
            temp=temp.right 
        print("\nMaxinum :",temp.data)                              
            

b1=BST()
b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(0))
b1.insert(Node(65))
b1.insert(Node(5))
b1.inorder(b1.root)
print("\nInorder:")
b1.preorder(b1.root)
print("\nPreorder:")
b1.postorder(b1.root)
print("\nPostorder:")
b1.findminmax()


