class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None    
    def create(self, values):
        for value in values:
            self.insert_end(value)
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
    def insert_position(self, data, position):
        new_node = Node(data)
        if position < 1:
            print("Invalid position")
            return
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        count = 1
        while temp is not None and count < position - 1:
            temp = temp.next
            count += 1
        if temp is None:
            print("Invalid position")
            return
        new_node.next = temp.next
        temp.next = new_node
    def find_middle(self):
        slow = self.head
        fast = self.head

        if self.head is None:
            print("List is empty")
            return

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        print("Middle node:", slow.data)
    def delete_node(self, value):
        if self.head is None:
            print("List is empty")
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        temp = self.head

        while temp.next is not None:
            if temp.next.data == value:
                temp.next = temp.next.next
                return

            temp = temp.next

        print("Value not found")
    def reverse(self):
        previous = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous
    def consecutive_sum(self):
        temp = self.head

        while temp is not None and temp.next is not None:
            total = temp.data + temp.next.data
            print(temp.data, "+", temp.next.data, "=", total)
            temp = temp.next

ll = LinkedList()

n = int(input("Enter the number of nodes: "))

values = []

for i in range(n):
    value = int(input("Enter node value: "))
    values.append(value)

ll.create(values)
print("\nOriginal Linked List:")
ll.display()
print("\nMiddle Node:")
ll.find_middle()
position = int(input("\nEnter position to insert: "))
value = int(input("Enter value to insert: "))
ll.insert_position(value, position)
print("After insertion:")
ll.display()
value = int(input("\nEnter value to delete: "))
ll.delete_node(value)
print("After deletion:")
ll.display()
ll.reverse()
print("After reversing:")
ll.display()
print("Sum of consecutive nodes:")
ll.consecutive_sum()  




              

                  
       