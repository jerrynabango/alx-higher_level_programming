#!/usr/bin/python3
"""Singly linked list"""


class Node:
    """Defines a node of singly linked list"""

    def __init__(self, data, next_node=None):
        """Initilization of a node.
        instance: self.data, self.next_node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        @property: Defines the method(Getter for specific attribute).
        private attribute: __data
        """
        return self.__data

    @property
    def next_node(self):
        """
        Returns:
            Node: instance of Node
        """
        return self.__next_node

    @data.setter
    def data(self, value):
        """
        setter for data attribute.
        private attribute: __data
        """
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError('data must be an integer')

    @next_node.setter
    def next_node(self, value):
        """
        setter for the next node.
        private attribute: __next_node
        """
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')


class SinglyLinkedList:
    """Defines a list of singly linked lists"""
    def __init__(self):
        """Initialization function.
        private attribute: __head
        """
        self.__head = None

    def sorted_insert(self, value):
        """Insertion into the node.
        private attribute: __head
        """
        linked_list = self.__head
        insert_node = None
        if linked_list is None or linked_list.data >= value:
            self.__head = Node(value, linked_list)
        else:
            while linked_list is not None and value > linked_list.data:
                insert_node = linked_list
                linked_list = linked_list.next_node
            insert_node.next_node = Node(value, linked_list)

    def __str__(self):
        """ Conversion to node.
        private attribute: __head
        """
        node = []
        linked_list = self.__head
        while linked_list is not None:
            node.append(str(linked_list.data))
            linked_list = linked_list.next_node
        if len(node) > 0:
            return '\n'.join(node)
        return ""
