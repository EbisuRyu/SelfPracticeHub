class MyStack:
    """
    A class representing a stack data structure with a fixed capacity.
    """

    def __init__(self, capacity):
        """
        Initializes a new instance of MyStack with a specific capacity.

        Args:
            capacity (int): The maximum number of elements the stack can hold.
        """
        self.__capacity = capacity
        self.__elements = []  # Internal list to store stack elements

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self.__elements) == 0

    def is_full(self):
        """
        Checks if the stack is full.

        Returns:
            bool: True if the stack is full, False otherwise.
        """
        return len(self.__elements) == self.__capacity

    def pop(self):
        """
        Removes and returns the top element of the stack. Prints a message if the stack is empty.

        Returns:
            The top element of the stack if not empty. None if the stack is empty.
        """
        if self.is_empty():
            print('Stack is empty')
        else:
            return self.__elements.pop()

    def push(self, value):
        """
        Adds an element to the top of the stack if there is space available. Prints a message if the stack is full.

        Args:
            value: The element to be added to the stack.
        """
        if self.is_full():
            print('Stack is full')
        else:
            self.__elements.append(value)

    def top(self):
        """
        Returns the top element of the stack without removing it. Prints a message if the stack is empty.

        Returns:
            The top element of the stack if not empty. None if the stack is empty.
        """
        if self.is_empty():
            print('Stack is empty')
        else:
            return self.__elements[-1]


# Example usage of MyStack
stack1 = MyStack(capacity=5)
stack1.push(1)
stack1.push(2)
print(stack1.is_full())   # Expected output: False
print(stack1.top())       # Expected output: 2
print(stack1.pop())       # Expected output: 2
print(stack1.top())       # Expected output: 1
print(stack1.pop())       # Expected output: 1
print(stack1.is_empty())  # Expected output: True
