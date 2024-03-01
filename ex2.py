import random
import timeit
import matplotlib.pyplot as plt

# ChatGPT gave the MergeSort implementation
class ArrayPriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        self.queue.append((item, priority))
        self._merge_sort(self.queue)

    def dequeue(self):
        if not self.queue:
            return None
        return self.queue.pop(0)[0]
    
    def print_queue(self):
        print("Current queue:")
        for item, priority in self.queue:
            print(f"Item: {item}, Priority: {priority}")

    def _merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            self._merge_sort(left_half)
            self._merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i][1] < right_half[j][1]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1


class Node:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority
        self.next = None


# ChatGPT gave the implementation of a SortedLinkedListPriorityQueue, because we did not have it in notes
class SortedLinkedListPriorityQueue:
    def __init__(self):
        self.head = None

    def enqueue(self, item, priority):
        new_node = Node(item, priority)
        
        if not self.head or priority < self.head.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.priority <= priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def dequeue(self):
        if not self.head:
            return None
        item = self.head.item
        self.head = self.head.next
        return item

    def print_queue(self):
        current = self.head
        print("Current queue:")
        while current:
            print(f"Item: {current.item}, Priority: {current.priority}")
            current = current.next

# Creating random tasks
def generate_tasks():
    tasks = []
    for i in range(1000):
        if random.random() < 0.7:
            tasks.append((f'Task {i + 1}', i+1))
        else:
            tasks.append(('dequeue', None))
    return tasks



apq_time = []
sllpq_time = []

# ArrayPriorityQueue processing
def process_apq(tasks):
    apq = ArrayPriorityQueue()
    for task in tasks:
        if task[0] == 'dequeue':
            apq.dequeue()
        else:
            apq.enqueue(task[0], int(task[1]))

# SortedLinkedListPriorityQueue processing
def process_sllpq(tasks):
    sllpq = SortedLinkedListPriorityQueue()
    for task in tasks:
        if task[0] == 'dequeue':
            sllpq.dequeue()
        else:
            sllpq.enqueue(task[0], int(task[1]))

# Measuring times
for i in range(100):
    tasks = generate_tasks()

    apq_time.append(timeit.timeit(lambda: process_apq(tasks), number=1))
    sllpq_time.append(timeit.timeit(lambda: process_sllpq(tasks), number=1))

# Plotting apq_time and sllpq_time
plt.plot(apq_time, label='ArrayPriorityQueue')
plt.plot(sllpq_time, label='SortedLinkedListPriorityQueue')
plt.xlabel('Iteration')
plt.ylabel('Time')
plt.legend()
plt.show()

"""
Question 5:
From the graph, it is easy to see that the Sorted Linked List Priority Queue is faster than the 
Array Priority Queue. If we compare the two implementations, we can see that although the dequeue method
for both of the queues is O(1) as there is no loop, the enqueue operation for the Sorted Linked List Priority 
Queue is O(n) in the worst case while the enqueue operation for the Array Priority Queue is O(nlog(n))
in the worst case due to having to implement the merge sort algorithm. Thus, the Sorted Linked List 
Priority Queue is more efficient thanks to its O(n) enqueue operation.
"""




