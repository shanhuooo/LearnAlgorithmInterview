#!/usr/bin/python3
#1.4 对链表进行重新排序
#2019.08.28

from linkedList1_2_1 import LinkedList,printList

"""
方法功能: 找出链表Head的中间结点,把链表从中间断成两个子链表
输入参数: head:链表头结点
返回值: 链表中间结点
"""
def FindMiddleList(head):
	if head is None or head.next is None:
		return head
	fast=head #遍历链表的时候每次向前走两步
	slow=head #遍历链表的时候每次向前走一步
	slowPre=head
	#当fast到链表尾时,slow恰好指向链表的中间结点
	while fast is not None and fast.next is not None:
		slowPre=slow
		slow=slow.next
		fast=fast.next.next
		#把链表断开成两个独立的子链表
	slowPre.next=None
	return slow

"""
方法功能: 对不带头结点(无数据)的单链表翻转
输入参数: head:链表头结点(第一个数据结点)
"""
def Reverse(head):
	if head is None or head.next is None:
		return head
	cur=head #记录当前结点
	next=None #记录后继结点
	pre=None #记录前驱结点
	while cur.next!=None:
		next=cur.next
		cur.next=pre
		pre=cur
		cur=next
	cur.next=pre
	return cur

"""
方法功能: 对链表进行排序
输入参数: head:链表的头结点
"""
def Reorder(head):
	if head is None or head.next is None:
		return
	#前半部分链表第一个结点
	cur1=head.next
	mid=FindMiddleList(head.next)
	#后半部分链表逆序后的第一个结点
	cur2=Reverse(mid)
	tmp=None
	#合并两个链表
	while cur1.next is not None:
		tmp=cur1.next
		cur1.next=cur2
		cur1=tmp
		tmp=cur2.next
		cur2.next=cur1
		cur2=tmp
	cur1.next=cur2

if __name__ == '__main__':
	#链表头结点
	head = LinkedList("head")
	cur = head
	#构造单链表
	i=1
	while i < 9:
		tmp = LinkedList(i)
		cur.next = tmp
		cur = tmp
		i+=1
	printList("排序前",head)
	Reorder(head)
	printList("排序后",head)