#Node class that makes up the basic structure of a single linked list
class Node:
    def __init__(self, newData):
        self.data = newData        #data contained in node
        self.next = None           #pointer to next node
        
#function to print data via traversing linked list iteratively
#time complexity: O(n)
#space complexity: O(1)
def iTrav(head):
    
    cur = head
    
    #while not through full list print data of each node
    while cur != None:
        print(cur.data)
        cur = cur.next

#function to print data via recursive function
#time complexity: O(n)
#space complexity: O(n)
def rTrav(head):
    if head == None:
        return head
    else:
        print(head.data)
        rTrav(head.next)
        
#function to find element in linked list or lack there of iteratively
#time complexity: O(n)
#space complexity: O(1)
def iSearch(head, target):
    cur = head
    
    while cur != None:
        if cur.data == target:
            return True
        cur = cur.next
    return False

#function to find element in linked list or lack there of recursively
#time complexity: O(n)
#space complexity: O(n)
def rSearch(head, target):
    if(head == None):
        return False
    elif(head.data == target):
        return True
    return rSearch(head.next, target)