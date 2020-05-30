
class Node:
    """
    A node in a singly-linked list.
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    """
    Create a new singly-linked list.
    """
    def __init__(self):
        self.head = None

    def insert(self, data):
        """
        Insert a new element at the end of the singly-linked list.
        """
        new_node = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def __str__(self):
        """
        string representation of the singly-linked list.
        """
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return '[' + ', '.join(nodes) + ']'

    def reverse(self):
        """
        reverse  singly-linked list

        """
        def _reverse_recursive(current, previous):

            if not current: # base case check
                return  previous

            next = current.next # next node place holder
            current.next = previous # reverse the link
            previous = current  # move previous one step ahead
            current = next  # set current to next

            return _reverse_recursive(current, previous)

        self.head = _reverse_recursive(current=self.head, previous=None)



