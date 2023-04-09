from typing import Any


class FixedQueue:
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: int = 256) -> None:
        self.que = [None] * capacity
        self.capacity = capacity
        self.front = self.rear = 0

    def __len__(self) -> int:
        return self.capacity

    def is_empty(self) -> bool:
        return self.front == self.rear

    def is_full(self) -> bool:
        return self.front == (self.rear + 1) % self.capacity

    def enqueue(self, value: Any) -> None:
        if self.is_full():
            raise FixedQueue.Full

        self.que[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity

    def dequeue(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty

        x = self.que[self.front]
        self.front = (self.front + 1) % self.capacity

        return x

    def peek(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty

        return self.que[self.front]

    def find(self, value: Any) -> Any:
        for i in range(self.front, self.rear):
            if self.que[i] == value:
                return i

        return -1

    def count(self, value: Any) -> bool:
        c = 0

        for i in range(self.front, self.rear):
            if self.que[i] == value:
                c += 1

        return c

    def __contains__(self, value: Any) -> bool:
        return self.count(value)

    def clear(self) -> None:
        self.front = self.rear = 0

    def dump(self) -> None:
        if self.is_empty():
            print('큐가 비어있습니다.')
        else:
            print(self.que[self.front:self.rear])