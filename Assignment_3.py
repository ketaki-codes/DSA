
class Node:
    def __init__(self, pid, name, priority):
        self.pid = pid
        self.name = name
        self.priority = priority
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.front = None

    def enqueue(self, new_node):
        if self.front is None or new_node.priority < self.front.priority:
            new_node.next = self.front
            self.front = new_node
        else:
            temp = self.front
            while temp.next is not None and temp.next.priority <= new_node.priority:
                temp = temp.next

            new_node.next = temp.next
            temp.next = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            temp = self.front
            print("Executed:", temp.pid, temp.name)
            self.front = self.front.next

    def display_next(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            print("Next Process:", self.front.pid, self.front.name, self.front.priority)

    def display_all(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            temp = self.front
            while temp is not None:
                print(temp.pid, temp.name, temp.priority)
                temp = temp.next

    def count(self):
        c = 0
        temp = self.front
        while temp is not None:
            c = c + 1
            temp = temp.next
        print("Total Processes:", c)


q = PriorityQueue()

q.enqueue(Node(101, "Youtube", 3))
q.enqueue(Node(102, "Microsoft", 1))
q.enqueue(Node(103, "Notepad", 2))
q.enqueue(Node(104, "System", 4))
q.enqueue(Node(105, "Email", 5))


print("All Processes:")
q.display_all()

print("Next Process:")
q.display_next()

print("Execute Process:")
q.dequeue()

print("Remaining Processes:")
q.display_all()

print("Count:")
q.count()
