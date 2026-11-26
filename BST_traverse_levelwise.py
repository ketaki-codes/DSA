
# BST using Linked List

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.cnt=0

    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root
            while True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right

    def del_node(self, root, value):
        if root is None:
            return root

        if value < root.data:
            root.left = self.del_node(root.left, value)

        elif value > root.data:
            root.right = self.del_node(root.right, value)

        else:
            # Node with right child  only
            if root.left is None:
                return root.right

            # Node with left child  only
            if root.right is None:
                return root.left

            # Node has both left and right children
            succ = self.get_successor(root)
            root.data = succ.data
            root.right = self.del_node(root.right, succ.data)

        return root

    def get_successor(self, temp):
        temp = temp.right
        while temp is not None and temp.left is not None:
            temp = temp.left
        return temp

    def inorder(self, root):
        if root is None:
            return
        else:
            self.inorder(root.left)
            if root.left is None and root.right is None:
                self.cnt+=1
            print(root.data, end=" ")
            self.inorder(root.right)

    def level_order(self, root):
        if root is None:
            print("BST is empty")
        arr=[]
        cnt=0
        arr.append(root)
        while(cnt<len(arr)):
            temp=arr[cnt]
            cnt+=1
            print(temp.data, end=" ")
            if temp.left:
                arr.append(temp.left)
            if temp.right:
                arr.append(temp.right)                    


b1 = BST()

b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(4))
b1.insert(Node(65))
b1.insert(Node(300))
b1.insert(Node(500))
b1.insert(Node(50))

print("Inorder:")
b1.inorder(b1.root)

# Find Minimum and Maximum
# b1.findminmax()

# Delete a node
b1.root = b1.del_node(b1.root, 4)

print("\nAfter Delete:")
b1.inorder(b1.root)


print("\nLevel Order:")
b1.level_order(b1.root)

    
