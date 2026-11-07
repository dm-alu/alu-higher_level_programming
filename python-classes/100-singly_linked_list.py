#!/usr/bin/python3
"""This module defines a singly linked list that keeps itself sorted."""


class Node:
    """This class represents a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new node.

        Args:
            data (int): the integer stored in the node.
            next_node (Node): the next node of the list, or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get or set the data stored in the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data after checking that it is an integer.

        Raises:
            TypeError: if value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get or set the next node of the list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node after checking its type.

        Raises:
            TypeError: if value is neither None nor a Node.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This class represents a singly linked list of sorted integers."""

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.__head = None

    def __str__(self):
        """Return the list as a string with one node value per line."""
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """Insert a new Node at its sorted position in increasing order.

        Args:
            value (int): the integer stored in the new node.
        """
        new = Node(value)
        if self.__head is None or value < self.__head.data:
            new.next_node = self.__head
            self.__head = new
            return
        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node
        new.next_node = current.next_node
        current.next_node = new
