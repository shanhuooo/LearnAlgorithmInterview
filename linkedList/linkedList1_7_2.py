#！/usr/bin/python3
#1.7 把链表相邻元素逆序
#方法2 快慢指针法
#2019.08.29

from linkedList1_5_2 import LinkedList,makeList,printList

"""
方法功能: 把链表相邻元素逆序
输入参数: head:链表头结点
返回值:   操作后链表的头结点
"""
def reverse(head):
	if head is None or head.next is None:
		return head
	pre=head
	cur1=pre.next
	cur2=cur1.next
	while cur1!=None and cur2!=None:
		next=cur2.next
		pre.next=cur2
		cur2.next=cur1
		cur1.next=next
		if next!=None:
			pre=cur1
			cur1=next
			cur2=next.next
	return head
			
if __name__ == '__main__':
	head=makeList()
	print("链表",end=":")
	printList(head)
	reverse(head)
	print("翻转后",end=":")
	printList(head)
