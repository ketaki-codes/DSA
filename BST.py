
# BST using Linked List

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None

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
            # Node has no left child
            if root.left is None:
                return root.right

            # Node has no right child
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
        if self.root is None:
            print("BST is empty")
            return

        temp = self.root
        while temp.left:
            temp = temp.left
        print("\nMinimum:", temp.data)

        temp = self.root
        while temp.right:
            temp = temp.right
        print("Maximum:", temp.data)


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

print("\nPreorder:")
b1.preorder(b1.root)

print("\nPostorder:")
b1.postorder(b1.root)

# Find Minimum and Maximum
# b1.findminmax()

# Delete a node
b1.root = b1.del_node(b1.root, 4)

print("\nAfter Delete:")
b1.inorder(b1.root)
