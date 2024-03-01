import timeit
import random
import matplotlib.pyplot as plt

# Array stack implemntation from github examples on d2l (without unused methods)
class MyArrayStack:
    def __init__(self):
        self._storage = []
    def push(self, value):
        self._storage.append(value)
    def pop(self):
        if not self._storage:
            return None
        else:
            return self._storage.pop()

# Linked list stack implementation from github examples on d2l (without unused methods)  
class ListNode:
    def __init__(self, value):
        self._value = value
        self._next = None

    def getData(self):
        return self._value

    def getNext(self):
        return self._next

    def setNext(self, next):
        self._next = next

    
class MyListStack:
    def __init__(self):
        self._head = None
    def push(self, value):
        node = ListNode(value)
        node.setNext(self._head)
        self._head = node
    def pop(self):
        if self._head is None:
            return None
        else:
            retval = self._head.getData()
            self._head = self._head.getNext()
            return retval

        
# Creating random tasks
def generate_tasks():
    tasks = []
    for i in range(10000):
        if random.random() < 0.7:
            tasks.append(('enqueue', i)) 
        else:
            tasks.append(('pop', None))  
    return tasks

as_time = []
lls_time = []

# ArrayStack processing
def process_as(tasks):
    array_stack = MyArrayStack()
    for operation, task in tasks:  
        if operation == 'pop':  
            array_stack.pop()
        else:
            array_stack.push(task)

# LinkedListStack processing
def process_lls(tasks):
    linked_list_stack = MyListStack()
    for task, operation in tasks: 
        if operation == 'pop': 
            linked_list_stack.pop()
        else:
            linked_list_stack.push(task)

# Measuring times
for i in range(100):
    tasks = generate_tasks()
    
    as_time.append(timeit.timeit(lambda: process_as(tasks), number=1))
    lls_time.append(timeit.timeit(lambda: process_lls(tasks), number=1))

# Plotting apq_time and sllpq_time
plt.hist(as_time, bins=20, alpha=0.5, label='ArrayStack')
plt.hist(lls_time, bins=20, alpha=0.5, label='LinkedListStack') 

plt.xlabel('Time (s)')
plt.ylabel('Frequency')
plt.title('Distribution of Processing Times')
plt.legend()
plt.show()

"""
Question 5:
The ArrayStack implementation is faster than the LinkedListStack implementation. For arrays, insertion
and deletion at the tail is an O(1). For linked lists, insertion and deletion at the head is an O(1).
Thus, there should not be much of a difference, but due to the linked list memory overhead
(https://stackoverflow.com/questions/7477181/array-based-vs-list-based-stacks-and-queues), this can result in
an O(n) time complexity for the linked list implementation. One case where the linked list implementation would
be more efficient is if we are implementing a stack that were to be dynamically resized during the 
push operation. The time complexity would be O(n) instead of O(1) as the array would have to resize and copy.

"""






