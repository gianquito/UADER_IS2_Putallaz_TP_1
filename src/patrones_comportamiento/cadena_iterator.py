import os
from collections.abc import Iterable, Iterator

class Iterator(Iterator):
    def __init__(self, collection, reverse=False):
        self._collection = collection
        self._reverse = reverse
        print("inicializa iterator")
        self._index = -1 if reverse else 0

    def __next__(self):
        try:
            result = self._collection[self._index]
            self._index += -1 if self._reverse else 1
            return result
        except IndexError:
            print("<eol>")
            raise StopIteration

class Collection(Iterable):
    def __init__(self):
        self._items = []

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __iter__(self):
        return Iterator(self._items)
    
    def get_reverse_iterator(self):
        return Iterator(self._items, True)

    def add_item(self, item):
        print("Agrega item %s" % (item))
        self._items.append(item)


#*--------- Crea colección
collection = Collection()
collection.add_item('Item 1')
collection.add_item('Item 2')
collection.add_item('Item 3')

#*-------- La recorre en sentido directo

for item in collection:
    print(item)

#*-------- La recorre en sentido reverso
print("\n".join(collection.get_reverse_iterator()), end="")

