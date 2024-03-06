import random
import timeit
import matplotlib.pyplot as plt


"""
Discussion of Results for #5:

After running the code multiple times it showed that the QueueArray implementation showed consistently faster results than the QueueLinkedList implementation.

Some possible explanations were that dequeuing from a linked list was slower, with an O(n) complexity because you needed to traverse through all the elements to delete through the tail node. As for the arrays, dequeuing was super fast through the tail.
"""

# Implementing a queue using Python arrays. Insertion @ head and Deletion @ tail.
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

# Implementing a queue using a Linked List. Insertion @ head and Deletion @ tail.
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
# ChatGPT was used to write these functions.

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

# Generate the list of 10000 tasks
task_list = generate_task_list()

# Function to measure the performance of both implementations and plotting the results of the data:
def measure_performance_and_plot():
    times_array = []
    times_linked_list = []

    for _ in range(100):
        task_list = generate_task_list()

        # Measure performance for QueueArray
        queue_array = QueueArray()
        start_time = timeit.default_timer()
        for task in task_list:
            if task[0] == 'enqueue':
                queue_array.enqueue(task[1])
            else:
                queue_array.dequeue()
        times_array.append(timeit.default_timer() - start_time)

        # Measure performance for QueueLinkedList
        queue_linked_list = QueueLinkedList()
        start_time = timeit.default_timer()
        for task in task_list:
            if task[0] == 'enqueue':
                queue_linked_list.enqueue(task[1])
            else:
                queue_linked_list.dequeue()
        times_linked_list.append(timeit.default_timer() - start_time)

    # Plotting both distributions overlayed in the same plot
    plt.figure(figsize=(10, 6))
    plt.hist(times_array, bins=20, alpha=0.5, label='QueueArray')
    plt.hist(times_linked_list, bins=20, alpha=0.5, label='QueueLinkedList')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Frequency')
    plt.title('Performance Comparison between QueueArray and QueueLinkedList')
    plt.legend()
    plt.show()

# Call the function to measure performance and plot the results
measure_performance_and_plot()
