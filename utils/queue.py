from typing import List

class Queue:
    def __init__(self, items: List[str] = []) -> None:
        self.items = items

    def insert(self, item):
        self.items.insert(item)

    def remove(self):
        self.items.pop(0)

    def get(self, index) -> str:
        return self.items[index]