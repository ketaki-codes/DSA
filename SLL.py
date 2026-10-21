
# Singly Linear Linked List

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    # Append node at the end
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = new_node

    # Insert node at a given position
    def insert(self, new_node, pos):
        if pos < 1:
            print("Invalid position")
            return

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        p = 1

        while temp and p < pos - 1:
            temp = temp.next
            p += 1

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node

    # Delete node by value
    def delete(self, value):
        temp = self.head
        prev = None

        while temp and temp.data != value:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value is not present in the list")
            return

        if prev is None:
            self.head = temp.next
        else:
            prev.next = temp.next

        temp = None

    # Reverse the linked list
    def reverse(self):
        curr = self.head
        prev = None

        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode

        self.head = prev

    # Find the middle node
    def find_middle(self):
        if self.head is None:
            print("List is empty")
            return

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print("Middle node:", slow.data)

    # Find and delete the middle node
    def findmid_del(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        temp1 = self.head
        prev = None

        while temp1 and temp1.next:
            prev = temp
            temp = temp.next
            temp1 = temp1.next.next

        print("Middle Node:", temp.data)

        if prev is None:
            self.head = None
        else:
            prev.next = temp.next

        temp = None

    # Delete the first and last nodes
    def delfirst_last(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        # Delete first node
        self.head = self.head.next

        # Find last node
        temp = self.head
        prev = None

        while temp.next:
            prev = temp
            temp = temp.next

        # Delete last node
        prev.next = None

    # Print the linked list
    def print(self):
        print("List elements:")

        temp = self.head

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()


# Main program
list1 = SLL()

n1 = Node(10)
n2 = Node(20)

list1.append(n1)
list1.append(n2)
list1.append(Node(30))
list1.append(Node(40))
list1.append(Node(55))
list1.append(Node(65))

# Display original list
list1.print()

# Insert a node
list1.insert(Node(34), 3)
list1.print()

# Delete a node
list1.delete(30)
list1.print()

# Reverse the list
list1.reverse()
list1.print()

# Find the middle node
list1.find_middle()

# Delete the middle node
list1.findmid_del()
list1.print()

# Delete first and last nodes
list1.delfirst_last()
list1.print()




               

