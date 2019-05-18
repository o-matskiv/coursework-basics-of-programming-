class Node:

    def __init__(self, item, next=None):
        """
        Produces a newly constructed empty node.
        __init__: Any -> Node
        Fields: item stores any value
            next points to the next node in the list
        """
        self.item = item
        self.next = next

    def __str__(self):
        """
        Prints the value stored in self.
        __str__: Node -> Str
        """
        return str(self.item)

    def __iter__(self):
        """
        Realization of iterarion
        """
        for element in self.item:
            yield element


class Array:
    def __init__(self):
        """
        Produces a newly constructed empty Array.
        """
        self._head = None

    def is_empty(self):
        """
        Checks emptiness of Array.
        (Array) -> Bool
        :return: True if Array is empty and False otherwise.
        """
        return self._head == None

    def __contains__(self, value):
        """
        Checks existence of value in the Array.
        (Array) -> Bool
        :param value: the value to be check.
        :return: True if Array is in the Array and False otherwise.
        """
        current = self._head
        while current != None:
            if current.item == value:
                return True
            else:
                current = current.next
        return False

    def add(self, value):
        """
        Adds the value to Array.
        :param value: the value to be added.
        """
        if self._head is None:
            self._head = Node(value)
        else:
            rest = self._head
            self._head = Node(value)
            self._head.next = rest

    def __str__(self):
        """
        :return: string representation of Array.
        """
        current = self._head
        str_list = []
        while current is not None:
            str_list.append(str(current))
            current = current.next
        return str(str_list)

    def __len__(self):
        """
        :return: a number of elements in Array.
        """
        if self._head == None:
            return 0
        current = self._head
        lngth = 0
        while current is not None:
            lngth += 1
            current = current.next
        return lngth

    def __iter__(self):
        """
        Realization of iterarion.
        (Array) -> generator
        """
        current = self._head
        while current is not None:
            yield current
            current = current.next

    def get_element(self, element):
        """
        Finds and returns element by its name.
        (Array, Any) -> Any
        """
        for i in self:
            if i.item == element:
                return i.item

    def __add__(self, other):
        """
        Extends self with elements from other.
        """
        for i in other:
            self.add(i)
