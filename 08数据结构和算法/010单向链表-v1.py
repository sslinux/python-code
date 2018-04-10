"""
单向链表也叫单链表，是链表中最简单的一种形式，它的每个节点包含两个域，一个信息域（元素域）和一个链接域。
这个链接指向链表中的下一个节点，而最后一个节点的链接域则指向一个空值。

表元素域elem用来存放具体的数据。
链接域next用来存放下一个节点的位置（python中的标识）
变量p指向链表的头节点（首节点）的位置，从p出发能找到表中的任意节点。

"""

# 单向链表节点实现：

# 03_single_link_list.py
class Node(object):
    """节点"""
    def __init__(self,elem):
        # elem属性存储元素；
        self.elem = elem
        # next是下一个节点的标识；
        self.next = None



# node = Node(100)
class SingleLinkList(object):
    """单链表"""

    def __init__(self,node=None):
        self._head = node

    def is_empty(self):
        """链表是否为空"""
        return self._head == None

    def length(self):
        """链表长度"""
        # cur游标，用来移动遍历节点
        cur = self._head
        # count记录数量；
        count = 0
        while cur is not None:  # 建议不要使用 ！= None
            count += 1
            cur = cur.next
        return count


    def travel(self):
        """遍历整个链表"""
        cur = self._head
        while cur is not None:
            print(cur.elem,end=" ")
            cur = cur.next

    def add(self, item):
        """链表头部添加元素"""
        pass

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        pass

    def remove(self, item):
        """删除节点"""
        pass

    def search(self, item):
        """查找节点是否存在"""
        pass

if __name__ == "__main__":
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)

    ll.travel()

