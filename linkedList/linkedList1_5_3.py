#!/sur/bin/python3
#1.5 引申: 将单链表向右旋转k个位置
#2019.08.29

from linkedList1_5_2 import LinkedList,makeList,\
	findLastK,printList

"""
方法功能: 将单链表向右旋转k个位置
输入参数: head:链表头结点; k:旋转位置
返回值:   newHead:旋转后的链表头结点
"""
def constructList(head,k):
	preKNode,lastNone=findLastK(head,k+1)
	head2=preKNode.next
	preKNode.next=None
	newHead=LinkedList("newHead")
	newHead.next=head2
	if head.next==None:
		return newHead
	else:
		lastNone.next=head.next
		return newHead

if __name__ == '__main__':
	head=makeList()
	print("链表",end=":")
	printList(head)
	k=1
	while k<7:
		head=makeList()
		print("将单链表向右旋转%s个位置后" % k, end=":")
		printList(constructList(head,k))
		k+=1