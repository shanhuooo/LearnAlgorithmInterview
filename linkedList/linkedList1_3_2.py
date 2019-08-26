#!/usr/bin/python3
#1.3 计算两个单链表所代表的数之和
#方法2 链表相加法
#2019.08.26

from linkedList1_2_1 import printList

class LNode:
	def __init__(self,x):
		self.data=x
		self.next=None

"""
方法功能: 对两个带头结点的单链表所代表的数相加
输入参数: h1:第一个链表头结点; h2:第二个链表头结点
返回值: 相加后链表的头结点
"""
def add(h1,h2):
	if h1 is None or h1.next is None:
		return h2
	if h2 is None or h2.next is None:
		return h1
	c=0 #用来记录进位
	sums=0 #用来记录两个结点相加的值
	p1=h1.next #用来遍历h1
	p2=h2.next #用来遍历h2
	tmp=None   #用来指向新创建的存储相加和的结点
	resultHead=LNode("head") #相加后链表头结点
	resultHead.next=None
	p=resultHead #用来指向链表resultHead最后一个结点
	while p1 is not None and p2 is not None:
		tmp=LNode("head")
		tmp.next=None
		sums=p1.data+p2.data+c
		tmp.data=sums%10 #两结点相加和
		c=sums//10 #进位
		p.next=tmp
		p=tmp
		p1=p1.next
		p2=p2.next
	# 链表h2比h1长,接下来只需要考虑h2剩余结点的值
	if p1 is None:
		while p2 is not None:
			tmp=LNode("head")
			tmp.next=None
			sums=p2.data+c
			tmp.data=sums%10
			c=sums//10
			p.next=tmp
			p=tmp
			p2=p2.next
	# 链表h1比h2长,接下来只需要考虑h1剩余结点的值
	if p2 is None:
		while p1 is not None:
			tmp=LNode("head")
			tmp.next=None
			sums=p1.data+c
			tmp.data=sums%10
			c=sums//10
			p.next=tmp
			p=tmp
			p1=p1.next
	# 如果计算完成后还有进位,则增加新的结点
	if c==1:
		tmp=LNode()
		tmp.next=None
		tmp.data=1
		p.next=tmp
	return resultHead

#构建特定列表
def makeLists():
	head1=LNode("head1")
	head2=LNode("head2")
	tmp=None
	cur=head1
	addResult=None
	#构造第一个链表
	i=1
	while i<7:
		tmp=LNode(i)
		tmp.data=i+2
		cur.next=tmp
		cur=tmp
		i+=1
	cur=head2
	#构造第二个链表
	i=9
	while i>4:
		tmp=LNode(i)
		tmp.data=i
		cur.next=tmp
		cur=tmp
		i-=1
	return head1,head2

if __name__ == '__main__':
	head1,head2=makeLists()
	printList("Head1\t",head1)
	printList("head2\t",head2)
	addResult=add(head1,head2)
	printList("相加后\t",addResult)