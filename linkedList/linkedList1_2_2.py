#!/usr/bin/python3
#1.2 从无序链表中移除重复项
#方法2 递归法
#2019.08.25

from linkedList1_2_1 import makeList,printList

def removeDupRecursion(head):
	if head.next is None:
		return head
	pointer=None
	cur=head
	#对以head.next为首的子链表删除重复的结点
	head.next=removeDupRecursion(head.next)
	pointer=head.next
	#找出以head.next为首的子链表中与head节点相同的结点并删除
	while pointer is not None:
		if head.data == pointer.data:
			cur.next = pointer.next
			pointer = cur.next
		else:
			pointer = pointer.next
			cur = cur.next
		return head

	"""
	方法功能: 对带头结点的单链表删除重复结点
	输入参数: head:链表头结点
	"""
def removeDup(head):
	if (head is None):
		return
	head.next = removeDupRecursion(head.next)

if __name__ == '__main__':
	head=makeList()
	printList("删除重复结点前",head)
	removeDup(head)
	printList("删除重复结点后",head)