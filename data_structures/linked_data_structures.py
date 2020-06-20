"""Implementation of simple data structures using linked nodes."""
from typing import Generic, TypeVar
T = TypeVar('T')


class LinkedNode(Generic[T]):

    def __init__(self, item: T) -> None:
        self.item = item
        self.link = None


class LinkedList(Generic[T]):

    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def is_empty(self) -> bool:
        return self.head is None

    def clear(self) -> None:
        self.head = None
        self.length = 0

    def __len__(self) -> int:
        return self.length

    def __getitem__(self, index: int) -> T:
        return self.__node_at_index(index)

    def __setitem__(self, index: int, item: T) -> None:
        node_at_index = self.__node_at_index(index)
        node_at_index.item = item

    def __delitem__(self, index: int) -> None:
        if self.is_empty():
            raise ValueError("List is empty")
        if index == 0:
            self.head = self.head.link
        else:
            node_before_index = self.__node_at_index(index - 1)
            node_before_index.link = node_before_index.link.link
        self.length -= 1

    def __node_at_index(self, index: int) -> LinkedNode:
        if index < 0:  # if negative index is given, treat as indexing from the end of list
            index = self.length + index
        if index >= self.length:  # if given index is larger than list size
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.link
        return current

    def insert(self, index: int, item: T) -> None:
        new_node = LinkedNode(item)
        if index == 0:
            new_node.link = self.head
            self.head = new_node
        else:
            node_before_index = self.__node_at_index(index - 1)
            new_node.link = node_before_index.link
            node_before_index.link = new_node
        self.length += 1

    def index(self, item: T) -> int:
        current = self.head
        index = 0
        while current is not None:
            if current.item is item:
                return index
            else:
                current = current.link
                index += 1
        raise ValueError("Item not in list")

    def __str__(self) -> str:
        n = len(self)
        output = ""
        if self.length == 0:
            return output
        else:
            current = self.head
            output += '['
            output += str(current.item)
            for _ in range(n - 1):
                current = current.link
                output += ", " + str(current.item)
            output += ']'
            return output
