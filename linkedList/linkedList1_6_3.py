#!/sur/bin/python3
#1.6 检测一个较大的单链表是否有环
#引申: 如果链表存在环,如何找出环的入口点
#快慢指针遍历法
#2019.08.29

from linkedList1_5_2 import LinkedList,printList

#定义有环链表
def makeLoopList():
	head=LinkedList("head")
	cur=head
	i=1
	while i<8:
		tmp=LinkedList(i)
		if i==3:
			LoopNode=tmp
		cur.next=tmp
		cur=tmp
		i+=1
	cur.next=LoopNode
	return head

"""
方法功能: 判断单链表是否有环
输入参数: head:链表头结点
返回值: None:无环, 否则返回slow与fast相遇点的结点
"""
def isLoop(head):
	if head is None or head.next is None:
		return None
	#初始化slow与fast都指向链表的第一个结点
	slow=head.next
	fast=head.next
	while fast is not None and fast.next is not None:
		slow=slow.next
		fast=fast.next.next
		if slow==fast:
			return slow
	return None

"""
方法功能: 找出环的入口点
输入参数: head:fast与slow相遇点
返回值: None:无环,否则返回slow与fast指针相遇的结点
"""
def findLoopList(head,meetNode):
	first=head.next
	second=meetNode
	while first!=second:
		first=first.next
		second=second.next
	return first

if __name__ == '__main__':
	head=makeLoopList()
	meetNode=isLoop(head)
	if meetNode is not None:
		print("链表有环,环的入口点%s" % findLoopList(head,meetNode).data)
	else:
		print("链表无环")