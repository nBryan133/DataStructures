import SingleLinkedList
from SingleLinkedList import Node

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

#head = SingleLinkedList.insertAF(head, 0)
#head = SingleLinkedList.insertAE(head, 5)
head = SingleLinkedList.insertAP(head, 4, 0)

#print(SingleLinkedList.iLength(head))
#print(SingleLinkedList.rLength(head))

SingleLinkedList.iTrav(head)
#SingleLinkedList.rTrav(head)

#if(SingleLinkedList.iSearch(head, 3)):
#    print("target found")
#else:
#    print ("target not found")
    
#if(SingleLinkedList.iSearch(head, 6)):
#    print("target found")
#else:
#    print ("target not found")

#if(SingleLinkedList.rSearch(head, 3)):
#    print("target found")
#else:
#    print ("target not found")
    
#if(SingleLinkedList.rSearch(head, 6)):
#    print("target found")
#else:
#    print ("target not found")