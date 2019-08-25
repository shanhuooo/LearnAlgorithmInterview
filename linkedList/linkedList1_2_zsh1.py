#!/usr/bin/python3
#1.2 从无序链表中移除重复项
#zsh方法1 尝试自己做
#2019.08.25

from linkedList1_2_1 import makeList,printList 

"""
方法功能: 删除无序链表中的重复项
输入参数: head:链表头结点
"""
def removeDup(head):
	if head==None or head.next==None:
		return
	List1=[]
	cur=head.next #当前结点
	next=cur.next #后续结点
	while next!=None:
		List1.append(cur.data)
		if next.data in List1:
			cur.next=next.next
		cur=cur.next
		next=cur.next

if __name__ == '__main__':
	head=makeList()
	printList("删除重复项前",head)
	removeDup(head)
	printList("删除重复项后",head)