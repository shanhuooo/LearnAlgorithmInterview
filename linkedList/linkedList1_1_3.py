#!/sur/bin/python3
#1.1 如何实现链表的逆序
#方法2 递归法
#2019.08.23 

#链表类
class LinkedList:
	def __init__(self,x):
		self.data=x
		self.next=None

def Reverse(head):
	#判断链表是否为空
	if head is None or head.next is None:
		return
	cur=None #当前结点
	next=None #后继结点
	#设置当前节点
	cur=head.next.next
	#设置链表第一个结点为尾节点
	head.next.next=None
	# 把遍历到结点插入到头结点的后面
	while cur is not None:
		next=cur.next
		cur.next=head.next
		head.next=cur
		cur=next

if __name__ == '__main__':
	#创建链表
	#创建表头
	head=LinkedList("表头")
	cur=head
	#创建无头链表
	i=1
	while i<9:
		tmp=LinkedList(i)
		cur.next=tmp
		cur=tmp
		i+=1
	print("逆序前:",end="")
	cur=head
	while cur!=None:
		print(cur.data,end="")
		cur=cur.next
	Reverse(head)
	print("\n逆序后:",end="")
	cur=head
	while cur!=None:
		if cur.next!=None:
			print(cur.data,end="")
		else:
			print(cur.data)
		cur=cur.next