from typing import Generic, TypeVar
T = TypeVar('T')


class MaxHeap(Generic[T]):

    def __init__(self, lst: list = None) -> None:
        if lst is None:
            self.list = [None]
            self.count = 0
        else:
            self.count = len(lst)
            self.list = lst
            self.__build_heap()

    def __len__(self) -> int:
        return self.count

    def is_empty(self) -> bool:
        return len(self) == 0

    def __build_heap(self) -> None:
        self.list.append(None)
        self.__swap(0, len(self))
        self.__build_heap_aux(len(self) // 2)  # len(lst) // 2 is the index of first non-leaf node

    def __build_heap_aux(self, k):
        """Creating a heap with item at index k as the root of the heap"""
        if k >= 1:
            self.__sink(k)
            self.__build_heap_aux(k - 1)

    def __sink(self, k: int) -> None:
        while 2*k <= len(self):
            larger_child_index = self.__get_larger_child(k)
            if self.list[larger_child_index] > self.list[k]:  # sink
                self.__swap(k, larger_child_index)
                k = larger_child_index
            else:
                return

    def __swap(self, index1, index2) -> None:
        self.list[index1], self.list[index2] = self.list[index2], self.list[index1]

    def __get_larger_child(self, k) -> int:
        """Returns index of larger child"""
        if 2*k == len(self) or self.list[2*k] > self.list[2*k + 1]:
            return 2*k
        else:
            return 2*k + 1

    def add(self, item: T) -> None:
        self.count += 1
        self.list.append(item)
        self.__rise(len(self))

    def __rise(self, k: int) -> None:
        while k > 1 and self.list[k] > self.list[k // 2]:
            self.__swap(k, k // 2)
            k = k // 2

    def get_max(self) -> T:
        item = self.list[1]
        self.list[1] = self.list[self.count]
        self.__sink(1)
        self.count -= 1
        return item

    def __str__(self) -> str:
        if not self.is_empty():
            output = '[' + str(self.list[1])
            for i in range(2, len(self) + 1):
                output += ', '
                output += str(self.list[i])
            output += ']'
        else:
            output = "[]"
        return output
