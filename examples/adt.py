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
        for element in self.item:
            yield element


class Array:
    def __init__(self):
        """
        Produces a newly constructed empty Array.
        """
        self._head = None

    def empty(self):
        """
        Checks emptiness of Array.
        (Array) -> Bool
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

    def delete(self, value):
        """
        :param value: value first occurrence of which should be deleted.
        """
        current = self._head
        previous = None
        while current is not None and current.item != value:
            previous = current
            current = current.next
        if current is not None:
            if previous is None:
                self._head = self._head.next
            else:
                previous.next = current.next

    def remove_all(self):
        """
        Removes all elements from Array
        (Array) -> list
        :return: list of the values
        """
        result = []
        current = self._head
        self._head = None
        while current is not None:
            result.append(str(current))
            self.delete(current)
            current = current.next
        return result

    def __str__(self):
        """
        String representation of Array
        """
        current = self._head
        str_list = []
        while current is not None:
            str_list.append(str(current))
            current = current.next
        return str(str_list)

    def __len__(self):
        """
        :return: a number of elements in Array
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
        current = self._head
        while current is not None:
            yield current
            current = current.next


class Ward():
    """docstring for Ward."""

    def __init__(self, name, schools, crimes, price):
        self.name = name
        self.schools = schools
        self.crimes = crimes
        self.price = price

    def get_name(self):
        """
        (Ward) -> str
        Return the name of Ward
        """
        return self.name

    def number_of_schools(self):
        """
        (Ward) -> int
        Return the number of schools in this Ward
        """
        return len(self.schools)

    def number_of_crimes(self):
        """
        (Ward) -> int
        Return the number of crimes in this Ward
        """
        return len(self.crimes)

    def get_price(self):
        """
        (Ward) -> int
        Return the average price for appartments in this Ward
        """
        return self.price

    def __str__(self):
        """
        String representation of Array
        """
        result = self.get_name()
        result += ':\n\tNumber of schools: ' + str(self.number_of_schools())
        result += '\n\tNumber of crimes: ' + str(self.number_of_crimes())
        result += '\n\tAverage price: ' + str(self.get_price())
        return result


def main():
    schools = Array()
    schools.add('School №1')
    schools.add('School №2')
    schools.add('School №3')

    crimes = Array()
    crimes.add('theft')
    crimes.add('murder')
    crimes.add('hijacking')
    price = 3000
    name = "Ward1"

    new_w = Ward(name, schools, crimes, price)
    print(new_w.number_of_crimes())
    print(new_w.number_of_schools())
    print(new_w.schools)
    print(new_w)


main()
