#Node class that makes up the basic structure of a single linked list
class Node:
    def __init__(self, newData):
        self.data = newData        #data contained in node
        self.next = None           #pointer to next node
        
#function to print data via traversing linked list iteratively
def iTraverse(head):
    
    #while not through full list print data of each node
    while head is not None:
        print(head.data)
        head = head.next