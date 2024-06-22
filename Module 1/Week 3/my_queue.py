class MyQueue:
    """
    A class that implements a queue data structure with fixed maximum capacity.

    Attributes:
        __capacity (int): The maximum number of elements the queue can hold.
        __elements (list): Internal list to store elements of the queue.
    """

    def __init__(self, capacity):
        """
        Initializes a new instance of MyQueue with a specified capacity.

        Args:
            capacity (int): The maximum number of elements the queue can hold.
        """
        self.__capacity = capacity  # Sets the maximum number of items that can be stored in the queue
        self.__elements = []  # Initializes the list to store queue elements

    def is_empty(self):
        """
        Determines whether the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self.__elements) == 0

    def is_full(self):
        """
        Determines whether the queue is full.

        Returns:
            bool: True if the queue is full, False otherwise.
        """
        return len(self.__elements) == self.__capacity

    def dequeue(self):
        """
        Removes and returns the front element of the queue. Issues a message if the queue is empty.

        Returns:
            Any: The front element of the queue if the queue is not empty, otherwise None.
        """
        if self.is_empty():
            print('Queue is empty')
            return None
        else:
            # Removes and returns the first item in the list, which is the front of the queue
            return self.__elements.pop(0)

    def enqueue(self, value):
        """
        Adds an element to the rear of the queue if there is space available. Issues a message if the queue is full.

        Args:
            value (Any): The element to be added to the rear of the queue.
        """
        if self.is_full():
            print('Queue is full')
        else:
            # Appends the new element to the end of the list
            self.__elements.append(value)

    def front(self):
        """
        Retrieves the front element of the queue without removing it. Issues a message if the queue is empty.

        Returns:
            Any: The front element of the queue if the queue is not empty, otherwise None.
        """
        if self.is_empty():
            print('Queue is empty')
            return None
        else:
            # Returns the first element of the list without removing it
            return self.__elements[0]


# Example usage of MyQueue
queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
queue1.enqueue(2)
print(queue1.is_full())  # Expected output: False
print(queue1.front())    # Expected output: 1
print(queue1.dequeue())  # Expected output: 1
print(queue1.front())    # Expected output: 2
print(queue1.dequeue())  # Expected output: 2
print(queue1.is_empty())  # Expected output: True
