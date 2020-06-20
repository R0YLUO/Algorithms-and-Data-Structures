"""Implementation of a queue using a python list"""
from typing import Generic, TypeVar
T = TypeVar('T')


class Queue(Generic[T]):

    def __init__(self) -> None:
        """Instantiates an empty list"""
        self.len = 0
        self.list = []

    def __len__(self) -> int:
        """Length of our queue"""
        return self.len

    def append(self, item: T) -> None:
        """Add item to rear of queue"""
        self.list.append(item)
        self.len += 1

    def serve(self) -> T:
        """Remove item at front of queue and return it"""
        if self.len > 0:
            self.len -= 1
            return self.list.pop(0)
        else:
            raise Exception("Queue is empty")

    def peek(self) -> T:
        """Look at item at front of queue removing"""
        if len(self) > 0:
            return self.list[0]
        else:
            raise Exception("Queue is empty")

    def __str__(self) -> str:
        """Prints contents in Queue from front to rear."""
        n = len(self)
        output = ""
        if self.length == 0:
            return output
        else:
            output += '['
            output += str(self.list[0])
            for i in range(1, n):
                output += ", " + str(self.list[i])
            output += ']'
            return output
