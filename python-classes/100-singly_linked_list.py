#!/usr/bin/python3
"""Singly linked list module"""


class Node:
    """Node class"""

    def __init__(self, data, next_node=None):
        """Initializes a node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly Linked List class"""

    def __init__(self):
        """Initializes a singly linked list"""
        self.__head = None

    def __str__(self):
        """String representation of the list"""
        nodes = []
        current = self.__head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position"""
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        current = self.__head
        while (current.next_node is not None and
                current.next_node.data < value):
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node
