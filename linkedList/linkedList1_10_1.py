#!/usr/bin/python3
#1.4 把链表以K个结点为一组进行翻转
#2019.09.02

from linkedList1_5_2 import LinkedList,printList
from linkedList1_9_1 import makeList

"""
方法功能: 返回指定链表的指定结点
输入参数: head:链表头结点; n:指定所要获取的结点序数
返回值: 链表结点
"""
def getNode(head,n):
	if head is None or head.next is None:
		return head
	if n==0:
		return LinkedList("结点溢出")
	i=0
	cur=head
	while i<n and cur is not None:
		cur=cur.next
		i+=1
	if cur is not None:
		return cur
	else:
		return LinkedList("结点溢出")

"""
方法功能: 在只给定单链表中某个结点的指针的情况下删除该结点
输入参数: 链表结点
返回值: True:删除成功; False:删除失败 (无法删除最后一个结点)
"""
def delNNode(nNode):
	if nNode is None or nNode.next is None:
		return False
	nNode.data=nNode.next.data
	nNode.next=nNode.next.next
	return True

if __name__ == '__main__':
	head=makeList([1,2,3,4,5,6,7])
	print("链表",end=":")
	printList(head)
	for n in range(9):
		print("所要删除的结点序数%s" %n ,end=",")
		head=makeList([1,2,3,4,5,6,7])
		nNode=getNode(head,n)
		if nNode.data!="结点溢出":
			print("删除'%s'后链表为" % nNode.data, end=":")
			result=delNNode(nNode)
			if result:
				printList(head)
			else:
				print("删除失败")
		else:
			print("结点溢出")