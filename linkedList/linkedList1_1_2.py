#!/sur/bin/python3
#1.1 如何实现链表的逆序
#方法2 递归法

class LinkedList:
	def __init__(self,x):
		self.data=x
		self.next=None

"""
方法功能: 对不带头结点的单链表进行逆序
输入参数: firstRef:链表头结点
"""
def RecursiveReverse(head):
	#如果链表为空或者链表中只有一个元素
	if head is None or head.next is None:
		return head
	else:
		#反转后面的结点
		newhead=RecursiveReverse(head.next)
		#把当前遍历的结点加到后面结点逆序后链表的尾部
		head.next.next=head
		head.next=None
	return newhead

"""
方法功能: 对带头结点的单链表进行逆序
输入参数: head:链表头结点
"""
def Reverse(head):
	if head is None or head.next is None:
		return
	# 获取链表第一个结点
	firstNode=head.next
	# 对链表进行逆序
	newhead=RecursiveReverse(firstNode)
	# 头结点指向逆序后链表的第一个结点
	head.next=newhead
	return newhead

if __name__=="__main__":
	#创建链表
	#创建链表头结点
	head=LinkedList("head")
	cur=head
	#不带头结点链表
	i=1
	while i<9:
		tmp=LinkedList(i)
		cur.next=tmp
		cur=tmp
		i+=1
	print("逆序前:",end="")
	cur=head.next
	while cur != None:
		print(cur.data,end="")
		cur=cur.next
	Reverse(head)
	print("\n逆序后:",end="")
	cur=head.next
	while cur != None:
		if cur.next!=None:
			print(cur.data,end="")
		else:
			print(cur.data)
		cur=cur.next