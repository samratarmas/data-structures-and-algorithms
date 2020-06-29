class Node():
    def __init__(self, data = None, previous = None, next = None):
        self.data = data
        self.previous = previous
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None
    
    # This function is flexible because it can insert a new node inbetween existing chain of linked nodes
    # Inserts data right after the given node: O(1), or at the end of the list if no node was passed as argument: O(n)
    def appendData(self, data, node = None):
        if not self.head:
            self.head = Node(data = data)
            return

        if isinstance(node, Node):
            node.next = Node(data = data, previous = node, next = node.next)
            return

        currentHead = self.head
        while currentHead.next:
            currentHead = currentHead.next
        self.appendData(data = data, node = currentHead)
    
    # Returns the first found node that matches the given key, or None if not found, O(n)
    def searchList(self, key):
        if not self.head:
            raise Exception("List is empty")
        maybeMatch = self.head
        while maybeMatch:
            if maybeMatch.data == key:
                return maybeMatch
            maybeMatch = maybeMatch.next
        else:
            raise Exception("Node was not found during search. "
            + "Note: This exception maynot be needed in a real world application "
            + "since it may be OK to have empty result set")

    def printListData(self):
        print('printing list data:')
        currentHead = self.head
        while currentHead:
            print(currentHead.data)
            currentHead = currentHead.next
        else:
            print('done printing!!')

myList: LinkedList = LinkedList()
myList.appendData(1)
myList.appendData(2)
myList.appendData(3)
myList.appendData(4, myList.searchList(2)) # Inserting in-between 2 and 3.
myList.printListData() # Expect 1,2,4,3 to be printed