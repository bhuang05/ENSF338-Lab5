# Implementing a circular queue based on a fixed-size Python array.
class CQArray:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.head = self.tail = -1
        self.size = 0
        self.capacity = capacity

    # Using isFull and isEmpty functions is inspired by ChatGPT
    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, item):
        # Check if the array is full or empty
        if self.isFull():
            print("enqueue None")
            return
        if self.isEmpty():
            self.head = 0
        
        # Using modulo for circular arrays.
        self.tail = (self.tail + 1) % self.capacity
        self.queue[self.tail] = item
        self.size += 1
        print(f"enqueue {item}")

    def dequeue(self):
        if self.isEmpty():
            print("dequeue None")
            return None
        item = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        if self.isEmpty():
            self.head = self.tail = -1
        print(f"dequeue {item}")
        return item

    def peek(self):
        if self.isEmpty():
            print("peek None")
            return None
        item = self.queue[self.head]
        print(f"peek {item}")
        return item

# Implementing a circular queue using a circular linked list.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class CQLinkedList:
    def __init__(self):
        self.head = self.tail = None
    
    def enqueue(self, item):
        # Create a new node
        newNode = Node(item)
        if self.tail == None:
            self.head = newNode
            self.tail = newNode
        else:
            # Readjust the tail pointer to point to the new node.
            self.tail.next = newNode
            self.tail = newNode

            # Loop back to the head pointer
            self.tail.next = self.head
        print(f"enqueue {item}")

    def dequeue(self):
        # Check if the tail is empty
        if self.tail == None:
            print("dequeue None")
            return None
        
        # Get the head value and delete the node
        item = self.head.value
        
        if self.head == self.tail:
            self.head = self.tail = None
        else: 
            self.head = self.head.next
            self.tail.next = self.head
        print(f"dequeue {item}")
        return item

    def peek(self):
        # Check if the list is empty.
        if self.head == None:
            print("peek None")
            return None
        item = self.head.value
        print(f"peek {item}")
        return item 

# Generating a list of 40 operations. ChatGPT was used to generate these 40 operations.

# Initialize queues
array_queue = CQArray(5)
linked_list_queue = CQLinkedList()

operations = [
    "array_queue.enqueue(1)",  # Expected: enqueue 1
    "array_queue.enqueue(2)",  # Expected: enqueue 2
    "array_queue.peek()",      # Expected: peek 1
    "array_queue.dequeue()",   # Expected: dequeue 1
    "array_queue.enqueue(3)",  # Expected: enqueue 3
    "array_queue.enqueue(4)",  # Expected: enqueue 4
    "array_queue.enqueue(5)",  # Expected: enqueue 5
    "array_queue.enqueue(6)",  # Expected: enqueue None (queue is full)
    "array_queue.dequeue()",   # Expected: dequeue 2
    "array_queue.dequeue()",   # Expected: dequeue 3
    "array_queue.peek()",      # Expected: peek 4
    "array_queue.dequeue()",   # Expected: dequeue 4
    "array_queue.dequeue()",   # Expected: dequeue 5
    "array_queue.dequeue()",   # Expected: dequeue None (queue is empty)
    "linked_list_queue.enqueue(10)",  # Expected: enqueue_10
    "linked_list_queue.enqueue(20)",  # Expected: enqueue_20
    "linked_list_queue.peek()",       # Expected: peek 10
    "linked_list_queue.dequeue()",    # Expected: dequeue 10
    "linked_list_queue.enqueue(30)",  # Expected: enqueue_30
    "linked_list_queue.enqueue(40)",  # Expected: enqueue_40
    "linked_list_queue.peek()",       # Expected: peek 20
    "linked_list_queue.dequeue()",    # Expected: dequeue 20
    "linked_list_queue.dequeue()",    # Expected: dequeue 30
    "linked_list_queue.dequeue()",    # Expected: dequeue 40
    "linked_list_queue.dequeue()",    # Expected: dequeue None (queue is empty)
    "array_queue.enqueue(7)",  # Back to array_queue for another round
    "array_queue.enqueue(8)",
    "array_queue.enqueue(9)",
    "array_queue.enqueue(10)",
    "array_queue.enqueue(11)",  # Queue should now be full again
    "array_queue.enqueue(12)",  # Expected: enqueue None (queue is full)
    "linked_list_queue.enqueue(50)",  # Switch back to linked_list_queue
    "linked_list_queue.enqueue(60)",
    "linked_list_queue.enqueue(70)",
    "linked_list_queue.peek()",       # Expected: peek 50
    "linked_list_queue.dequeue()",    # Expected: dequeue 50
    "linked_list_queue.dequeue()",    # Expected: dequeue 60
    "linked_list_queue.enqueue(80)",
    "linked_list_queue.peek()",       # Expected: peek 70
    "linked_list_queue.dequeue()",    # Expected: dequeue 70
]

# Execute operations
for op in operations:
    exec(op)
    
