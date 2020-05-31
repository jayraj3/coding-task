
class Node:
    """
    A node in a singly-linked list.
    """
    def __init__(self, data=None, next=None):
        self.data = data    # linked list node data
        self.next = next    # reference to next node

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
        if (self.head): # check null head
            current = self.head
            while (current.next):   # iterate till node exists
                current = current.next
            current.next = new_node # add new node
        else:
            self.head = new_node    # add head node

    def __str__(self):
        """
        string representation of the singly-linked list.
        """
        nodes = []  # placeholder for node data
        current = self.head #placeholder for head
        while current:  # iterate over all node
            nodes.append(str(current.data)) # append node data  to list
            current = current.next  # get next node
        return '[' + ', '.join(nodes) + ']' # join list data to string

    def reverse(self):
        """
        reverse  singly-linked list

        """
        def _reverse_recursive(current, previous):

            if not current: # base case check
                return  previous

            next = current.next # next node placeholder
            current.next = previous # reverse the link
            previous = current  # move previous one step ahead
            current = next  # set current to next

            return _reverse_recursive(current, previous)

        self.head = _reverse_recursive(current=self.head, previous=None)



