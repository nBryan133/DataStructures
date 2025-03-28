import SingleLinkedList
from SingleLinkedList import Node

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

SingleLinkedList.iTraverse(head)