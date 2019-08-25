#!/usr/bin/python3
#1.2 从无序链表中移除重复项
#方法1 顺序删除
#2019.08.25

#链表类
class LinkedList():
	def __init__(self,x):
		self.data=x
		self.next=None

"""
**方法功能: 对带头结点的无序单链表删除重复的结点
**输入参数: head:链表头结点
"""
def removeDup(head):
	if head==None or head.next==None:
		return
	outerCur=head.next #用于外层循环,指向链表第一个结点
	innerCur=None #用于内层循环用来遍历outerCur后面的结点
	innerPre=None #innerCur的前驱结点
	while outerCur!=None:
		innerCur=outerCur.next
		innerPre=outerCur
		while innerCur!=None:
			#找到重复的结点并删除
			if outerCur.data==innerCur.data:
				innerPre.next=innerCur.next
				innerCur=innerCur.next
			else:
				innerPre=innerCur
				innerCur=innerCur.next
		outerCur=outerCur.next

"""
创建特定链表,无需输入参数
"""
def makeList():
	head=LinkedList("head")
	cur=head
	i=1
	while i<7:
		tmp=LinkedList(i)
		if i%2==0:
			tmp.data=i+1
		elif i%3==0:
			tmp.data=i-2
		else:
			tmp.data=i
		cur.next=tmp
		cur=tmp
		i+=1
	return head

"""
方法功能: 输出链表
输入参数: a:提示字符串;head:链表头结点
"""
def printList(a, head):
	print(a,end=":")
	cur=head.next
	while cur!=None:
		if cur.next!=None:
			print(cur.data,end=" ")
		else:
			print(cur.data)
		cur=cur.next

if __name__=="__main__":
	head=makeList()
	printList("删除重复项前",head)
	removeDup(head)
	printList("删除重复项后",head)
