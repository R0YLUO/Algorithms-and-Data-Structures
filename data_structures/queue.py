"""Implementation of a queue using a python list"""
from typing import Generic, TypeVar
T = TypeVar('T')


class Queue(Generic[T]):

    def __init__(self) -> None:
        """Instantiates an empty list"""
        self.length = 0
        self.list = []

    def __len__(self) -> int:
        """Length of our queue"""
        return self.length

    def is_empty(self) -> bool:
        return len(self) == 0

    def append(self, item: T) -> None:
        """Add item to rear of queue"""
        self.list.append(item)
        self.length += 1

    def serve(self) -> T:
        """Remove item at front of queue and return it"""
        if not self.is_empty():
            self.length -= 1
            return self.list.pop(0)
        else:
            raise Exception("Queue is empty")

    def peek(self) -> T:
        """Look at item at front of queue removing"""
        if not self.is_empty():
            return self.list[0]
        else:
            raise Exception("Queue is empty")

    def __str__(self) -> str:
        """Prints contents in Queue from front to rear."""
        n = len(self)
        output = ""
        if n == 0:
            return output
        else:
            output += '['
            output += str(self.list[0])
            for i in range(1, n):
                output += ", " + str(self.list[i])
            output += ']'
            return output
