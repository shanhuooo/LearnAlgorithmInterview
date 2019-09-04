#!/sur/bin/python3
#1.11 判断两个单链表(无环)是否交叉
#方法3 尾结点法
#2019.09.04

from linkedList1_5_2 import LinkedList,printList
from linkedList1_9_1 import makeList
from linkedList1_10_1 import getNode

"""
方法功能: 给出无环单链表长度
输入参数: head:链表头结点
返回值: nodeNum:链表长度
"""
def getNodeNum(head):
	nodeNum=0
	if head is None or head.next is None:
		return nodeNum
	cur=head
	while cur.next!=None:
		cur=cur.next
		nodeNum+=1
	return nodeNum

"""
方法功能: 判断链表是否交叉
输入参数: head1:链表1头结点; head2:链表2头结点
返回值: sameFistNode:第一个相交结点 / None:表明链表不交叉
"""
def isIntersect(head1,head2):
	nodeNum1=getNodeNum(head1)
	nodeNum2=getNodeNum(head2)
	cur1=head1
	cur2=head2
	addStep=nodeNum2 - nodeNum1
	if addStep > 0:
		for i in range(addStep):
			cur2=cur2.next
	elif addStep < 0:
		for i in range(-addStep):
			cur1=cur1.next
	while cur1 is not None and cur2 is not None:
		cur1=cur1.next
		cur2=cur2.next
		if cur1==cur2:
			sameFistNode=cur1
			return sameFistNode
	return None

if __name__ == '__main__':
	# 构造链表并输出
	list1=[1,2,3,4]
	list2=[11,22,33,44,55]
	sameList=[5,6,7,8]
	sameHead=makeList(sameList)
	head1=makeList(list1)
	last1=getNode(head1,len(list1))
	last1.next=sameHead.next
	head2=makeList(list2)
	last2=getNode(head2,len(list2))
	last2.next=sameHead.next
	print("链表1",end=":")
	printList(head1)
	print("链表2",end=":")
	printList(head2)
	#判断链表是否交叉
	sameFistNode=isIntersect(head1,head2)
	if sameFistNode!=None:
		print("链表交叉的第一个结点为%s" % sameFistNode.data)
	else:
		print("链表无交叉结点")