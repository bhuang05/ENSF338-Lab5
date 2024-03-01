import random

"""
Discussion of Results for #5:

"""

# Implementing a queue using Python arrays
class QueueArray:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        # Insert item at the head (start of the list)
        self.queue.insert(0, item)

    def dequeue(self):
        # Check if the queue is empty
        if not self.queue:
            print("Queue is empty")
            return None
        return self.queue.pop()

# Implementing a queue using a Linked List 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        # Create a new node
        newNode = Node(value)
        # Check if the queue is empty
        if self.head is None and self.tail == None:
            self.head = newNode
            self.tail = newNode
        else:
            # If not empty, add the new node at the head
            newNode.next = self.head
            self.head = newNode

    def dequeue(self):
        # Check if the queue is empty
        if self.head == None:
            print("dequeue None")
            return None

        if self.head == self.tail:
            # Queue has only one element
            value = self.head.value
            self.head = None
            self.tail = None
            return value

        # Traverse from head to the second-last node
        current = self.head
        while current.next != self.tail:
            current = current.next
        
        # Update the tail and remove the last node
        value = self.tail.value
        self.tail = current
        self.tail.next = None
        return value

# Function that generates random lists of 10000 tasks. 
# ChatGPT was used to write this function.

def generate_task_list(n=10000, enqueue_prob=0.7):
    tasks = []
    for _ in range(n):
        if random.random() < enqueue_prob:
            # Generate an enqueue task
            tasks.append(('enqueue', random.randint(1, 100)))  # Random value for enqueue
        else:
            # Generate a dequeue task
            tasks.append(('dequeue', None))
    return tasks

# Generate the list
task_list = generate_task_list()
