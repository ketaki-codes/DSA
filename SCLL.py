
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class SCLL:
    def __init__(self):
        self.head = None

    # Append node at the end
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            temp.next = new_node
            new_node.next = self.head

    
    # Insert node at a given position
    def insert(self, new_node, pos):
        if pos < 1:
            print("Invalid position")
            return

        if self.head is None:
            if pos == 1:
                self.head = new_node
                new_node.next = self.head
            else:
                print("Invalid position")
            return

        if pos == 1:
            temp = self.head

            # Find the last node
            while temp.next != self.head:
                temp = temp.next

            new_node.next = self.head
            self.head = new_node
            temp.next = self.head
            return

        # Insert at any other position
        p = 1
        temp = self.head

        while p < pos - 1 and temp.next != self.head:
            temp = temp.next
            p += 1

        if p != pos - 1:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node

    # Delete node by value
    def delete(self, value):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        prev = None

        # Search for the value
        while True:
            if temp.data == value:
                break

            prev = temp
            temp = temp.next

            if temp == self.head:
                print("Value is not present in the list")
                return

        # If only one node exists
        if temp.next == self.head and temp == self.head:
            self.head = None

        # If deleting the first node
        elif temp == self.head:
            last = self.head

            while last.next != self.head:
                last = last.next

            self.head = self.head.next
            last.next = self.head

        # If deleting another node
        else:
            prev.next = temp.next

    # Display the list
    def print(self):
        print("\nList elements:")

        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while True:
            print(temp.data, end=" ")
            temp = temp.next

            if temp == self.head:
                break

        print()


# Main program
list1 = SCLL()

list1.append(Node(10))
list1.append(Node(20))
list1.append(Node(30))
list1.append(Node(40))
list1.append(Node(55))
list1.append(Node(65))

# Display original list
list1.print()

# Insert a node at position 3
list1.insert(Node(100), 3)
list1.print()

# Delete node with value 10
# 0
list1.delete(100)
list1.print()
