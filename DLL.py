
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None


class DLL:
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
            new_node.prev = temp

    # Insert node at a given position
    def insert(self, new_node, pos):
        if pos == 1:
            new_node.next = self.head

            if self.head:
                self.head.prev = new_node

            self.head = new_node
        else:
            temp = self.head
            p = 1

            while p < pos - 1 and temp:
                temp = temp.next
                p += 1

            if temp is None:
                print("Invalid position")
                return

            new_node.next = temp.next
            new_node.prev = temp

            if temp.next:
                temp.next.prev = new_node

            temp.next = new_node

    # Delete node by value
    def delete(self, key):
        temp = self.head

        while temp and temp.data != key:
            temp = temp.next

        if temp is None:
            print("Value is not present in the list")
            return

        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next

        if temp.next:
            temp.next.prev = temp.prev

    # Print list in reverse order
    def printrev(self):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        while temp.next:
            temp = temp.next

        print("List elements in reverse order:", end=" ")

        while temp:
            print(temp.data, end=" ")
            temp = temp.prev

        print()

    # Count total nodes
    def countnum(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        return count

    # Reverse the linked list
    def reverse(self):
        temp = self.head
        prev_node = None

        while temp:
            next_node = temp.next
            temp.next = prev_node
            temp.prev = next_node

            prev_node = temp
            temp = next_node

        self.head = prev_node

    # Print the linked list
    def print(self):
        temp = self.head
        print("List elements:", end=" ")

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()


# Main program
list1 = DLL()

list1.append(Node(10))
list1.append(Node(20))
list1.append(Node(30))
list1.append(Node(40))
list1.append(Node(55))
list1.append(Node(65))

# Display original list
list1.print()

# Insert a node at position 3
list1.insert(Node(34), 3)
list1.print()

# Delete a node with value 30
list1.delete(30)
list1.print()

# Print in reverse order
list1.printrev()

# Reverse the actual linked list
list1.reverse()
list1.print()

# Count total nodes
print("Total nodes:", list1.countnum())
