#!/usr/bin/python3
#1.3 计算两个单链表所代表的数之和
#方法1 整数相加法
#2019.08.26

import math
from linkedList1_2_1 import LinkedList,printList
from linkedList1_3_2 import makeLists

"""
方法功能: 计算两个单链表所代表的数之和
输入参数: head1:链表1头结点 head2:链表2头结点
输出参数: addHead:相加后和所对应链表的头结点
"""
#求链表所代表的数
def headNum(head):
	if head is None or head.next is None:
		return 0
	num=0 #存放链表代表的数
	i=0 #记录位数
	cur=head.next #记录当前结点
	while cur!=None:
		num=num+cur.data*int(math.pow(10,i))
		cur=cur.next
		i+=1
	return num
#求数字所代表的不带头结点的单链表(使用递归)
def numToNoHead(num):
	cur=LinkedList("None")
	if (num//10)==0:
		cur.data=num
		return cur
	cur.data=num%10
	cur.next=numToNoHead(num//10)
	return cur
#给单链表添加头结点
def numToHead(num):
	head=LinkedList("HEAD")
	head.next=numToNoHead(num)
	return head
#求和所对应的链表
def addList(head1,head2):
	sum=headNum(head1)+headNum(head2)
	addHead=numToHead(sum)
	return addHead

if __name__ == '__main__':
	head1,head2=makeLists()
	printList("head1",head1)
	printList("head2",head2)

	printList("相加后",addList(head1,head2))