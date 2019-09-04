#!/usr/bin/python3

"""
测试结点地址何时会发生变化
"""

from linkedList1_5_2 import LinkedList,printList

if __name__ == '__main__':
	head=LinkedList("head")
	print(id(head)) #记录head内存地址
	head.data=0
	print(id(head)) #查看改变数据后内存地址是否变化
	head=None
	print(id(head)) #查看变量数据类型变了之后,内存地址是否发生变化