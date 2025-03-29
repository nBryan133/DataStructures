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

#function to find the length of the linked list iteratively
#time complexity: O(n)
#space complexity O(1)
def iLength(head):
    l = 0
    while(head != None):
        l = l + 1
        head = head.next
    return l

#function to find the length of the linked list recursively
#time complexity: O(n)
#space complexity O(n)
def rLength(head):
    if(head == None):
        return 0
    else:
        return rLength(head.next) + 1
    
#function to insert new element at the beginning of a linked list
#time complexity: O(1)
#space complexity O(1)
def insertAF(head, newData):
    
    newNode = Node(newData)
    
    if(head != None):
        buf = head
        head = newNode
        head.next = buf
    else:
        head = newNode
        
    return head

#function to insert new element at the end of a linked list
#time complexity: O(n)
#space complexity O(1)
def insertAE(head, newData):
    
    newNode = Node(newData)
    
    if(head != None):
        last = head
        
        while(last.next != None):
            last = last.next
        
        last.next = newNode
    else:
        head = newNode
    
    return head

#function to insert new element at any position of a linked list
#time complexity: O(n)
#space complexity O(1)
def insertAP(head, target, newData):
    
    if(target == 0):
        return insertAF(head, newData)
        
    newNode = Node(newData)
    #iTrav(newNode)
        
    pos = head
        
    for i in range(target - 1):
        if(pos == None):
            print("Target does not existt")
            return head
        pos = pos.next
        
    newNode.next = pos.next
    pos.next = newNode
    #iTrav(pos)
       
    return head
        
    