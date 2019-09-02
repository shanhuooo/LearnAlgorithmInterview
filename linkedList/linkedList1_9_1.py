#!/usr/bin/python3
#1.4 把链表以K个结点为一组进行翻转
#2019.09.01

from linkedList1_5_2 import LinkedList,printList

"""
方法功能: 构造指定链表
输入参数: list:提供链表结点数据
返回值:   head:链表头结点
"""
def makeList(list):
	head=LinkedList("head")
	cur=head
	for i in list:
		tmp=LinkedList(i)
		cur.next=tmp
		cur=tmp
	return head

"""
方法功能: 合并两个有序链表
输入参数: head1,head2:两个链表的头结点
返回值:   head:合并后链表头结点
"""
def merge(head1,head2):
	if head1 is None or head1.next is None:
		return head2
	elif head2 is None or head2.next is None:
		return head1
	cur1=head1.next #记录链表1当前结点
	cur2=head2.next #记录链表2当前结点
	if cur1.data<=cur2.data:
		head=head1
	else:
		head=head2
	cur=head
	while cur1!=None and cur2!=None:
		if cur1.data<=cur2.data:
			cur.next=cur1
			cur1=cur1.next
		else:
			cur.next=cur2
			cur2=cur2.next
		cur=cur.next
	if cur1==None:
		cur.next=cur2
	elif cur2==None:
		cur.next=cur1
	return head

if __name__ == '__main__':
	head1=makeList([1,3,3,5])
	head2=makeList([2,4,5,6,7])
	print("head1",end=":")
	printList(head1)
	print("head2",end=":")
	printList(head2)
	head=merge(head1,head2)
	print("合并后的链表",end=":")
	printList(head)