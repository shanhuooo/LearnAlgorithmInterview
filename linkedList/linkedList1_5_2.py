#!/sur/bin/python3
#1.5 找出单链表中的倒数第k个元素
#方法2 快慢指针法
#2019.08.29

#链表类
class LinkedList:
	def __init__(self,x):
		self.data=x
		self.next=None

#创建特定链表(head->1->2->3->4->5->6->7)
def makeList():
	head=LinkedList("head")
	i=1
	cur=head
	while i<8:
		tmp=LinkedList(i)
		cur.next=tmp
		cur=tmp
		i+=1
	return head

#屏幕打印链表
def printList(head,type=0):
	#type==0,  带头结点
	if type==0:
		cur=head.next
	#type==1, 不带头结点
	elif type!=0:
		cur=head
	while cur is not None:
		if cur.next is not None:
			print(cur.data,end=" ")
		else:
			print(cur.data)
		cur=cur.next

"""
方法功能: 找出链表倒数第k个结点
输入参数: head:链表头结点
返回值:   倒数第k个结点
"""
def findLastK(head,k):
	if head is None or head.next is None:
		return LinkedList("None"),LinkedList("None")
	slow=head
	fast=head
	i=0
	while i<k:
		fast=fast.next
		i+=1
		if fast.next==None:
			if i==k:
				return head.next,fast
			return LinkedList("None"),fast
	while fast is not None:
		slow=slow.next
		last=fast
		fast=fast.next
	return slow,last

if __name__ == '__main__':
	head=makeList()
	print("链表",end=":")
	printList(head)
	k=1
	while k<9:
		kNode,last=findLastK(head,k)
		print("链表倒数第%s个元素为:%s" % (k,kNode.data))
		k+=1