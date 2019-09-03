#!/usr/bin/python3
#1.8 把链表以K个结点为一组进行翻转
#2019.09.01

from linkedList1_5_2 import LinkedList,makeList,printList

"""
方法功能: 翻转无头结点的链表
输入参数: firstNode:第一个结点
返回值: 首末结点
"""
def reverse(firstNode):
	if firstNode is None or firstNode.next is None:
		return firstNode,firstNode
	newHead,lastNode=reverse(firstNode.next)
	lastNode.next=firstNode
	firstNode.next=None
	return newHead,firstNode

"""
方法功能: 把链表以K个结点为一组进行翻转 
输入参数: head:链表头结点; k:每组结点个数
返回值: head:链表头结点
"""
def reverseK(head,k):
	if head is None or head.next is None or k==0 or k==1:
		return head
	pre=head
	cur=head.next
	while cur!=None:
		for i in range(k-1):
			cur=cur.next
			if cur==None:
				return head
		next=cur.next
		cur.next=None
		firstNode,lastNode=reverse(pre.next)
		pre.next=firstNode
		lastNode.next=next
		pre=lastNode
		cur=next
	return head


if __name__ == '__main__':
	head=makeList()
	print("链表",end=":")
	printList(head)
	k=0
	while k<10:
		head=makeList()
		print("以%s个结点为一组进行翻转" % k, end=":")
		reverseK(head,k)
		printList(head)
		k+=1