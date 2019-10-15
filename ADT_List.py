"""
    coding      : UTF-8
    Environment : Python 3.6
    Author      : Benjamin142857
    Data        : 10/3/2019
    Remark      : ADT_List
"""


# 1.1 单链表-结点
class SingleNode(object):
    def __init__(self, item):
        self.item = item
        self._next = None

    def __repr__(self):
        return '<SingleNode: {}>'.format(self.item)

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node):
        if isinstance(node, (SingleNode, type(None))):
            self._next = node
        else:
            raise ValueError('后继结点必须为单结点')


# 1.2 单链表-链
class SingleLinkList(object):
    def __init__(self, *args):
        self._length = len(args)
        self._head = None
        self._tail = None
        self._node = SingleNode
        
        for i, v in enumerate(args[::-1]):
            if i == 0:
                self.tail = self._node(v)
                last_node = self.tail
            elif i == self.length - 1:
                self.head = self._node(v)
                self.head.next = last_node
            else:
                this_node = self._node(v)
                this_node.next = last_node
                last_node = this_node

    def __repr__(self):
        ret_str = '{{'
        for i in range(self.length):
            if i == 0:
                node = self.head
                ret_str += node.item.__repr__() + ', '
            else:
                node = node.next
                ret_str += node.item.__repr__() + ', '
        ret_str = ret_str[:-2] + '}}' if self.length > 0 else '{{}}'
        return ret_str

    def __len__(self):
        return self._length

    def __getitem__(self, i):
        if not (isinstance(i, int) and i >= 0):
            raise ValueError('索引必须为自然数')
        elif i > self.length-1:
            raise ValueError('索引超出链表最大长度')

        for idx in range(i+1):
            node = self.head if idx == 0 else node.next

        return node.item

    @property
    def length(self):
        """只读属性"""
        return self._length

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, node):
        if isinstance(node, (self._node, type(None))):
            self._head = node
        else:
            raise ValueError('链表头必须为单结点')

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, node):
        if isinstance(node, (self._node, type(None))):
            self._tail = node
        else:
            raise ValueError('链表尾必须为单结点')

    def is_empty(self):
        """链表是否为空"""
        return self.head is None

    def travel(self):
        """遍历链表"""
        return self.__repr__()

    def add(self, item):
        """头插元素"""
        if self.head:
            node = self._node(item)
            node.next = self.head
            self.head = node
            self._length += 1
        else:
            node = self._node(item)
            self.head = node
            self.tail = node
            self._length += 1

    def append(self, item):
        """尾插元素"""
        if self.head:
            node = self._node(item)
            self.tail.next = node
            self.tail = node
            self._length += 1
        else:
            node = self._node(item)
            self.head = node
            self.tail = node
            self._length += 1

    def insert(self, idx, item):
        """插入元素"""
        if not (isinstance(idx, int) and idx >= 0):
            raise ValueError('索引必须为自然数')
        elif idx == 0:
            self.add(item)
        elif idx >= self.length:
            self.append(item)
        else:
            node = self.head
            # 找出索引的前一个结点
            for i in range(idx-1):
                node = node.next
            ins_node = self._node(item)
            ins_node.next = node.next
            node.next = ins_node
            self._length += 1

    def remove(self, item):
        """删除首个值为item的元素, 若不存在则报错"""
        pass

    def removeall(self, item):
        """删除所有值为item的元素, 返回int: 删除个数"""
        pass

    def search(self, item):
        """查询值为item的元素是否存在，存在则返回首个值的索引，不存在则返回None"""
        pass

    def searchall(self, item):
        """查询所有值为item的元素，返回list: [所有索引]"""
        pass

    def delete(self, idx_or_idxLst):
        """删除对应索引的元素，不返回"""
        pass


# 2.1 双向链表-结点
class DoubleNode(object):
    def __init__(self, item):
        self.item = item
        self._next = None
        self._prev = None

    def __repr__(self):
        return '<DoubleNode: {}>'.format(self.item)

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, node):
        if isinstance(node, (DoubleNode, type(None))):
            self._prev = node
        else:
            raise ValueError('前驱结点必须为双向结点')

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node):
        if isinstance(node, (DoubleNode, type(None))):
            self._next = node
        else:
            raise ValueError('后继结点必须为双向结点')


# 2.2 双向链表-链
class DoubleLinkList(SingleLinkList):
    def __init__(self, *args):
        self._length = len(args)
        self._head = None
        self._tail = None
        self._node = DoubleNode

        for i, v in enumerate(args[::-1]):
            if i == 0:
                self.tail = self._node(v)
                last_node = self.tail
            elif i == self.length - 1:
                self.head = self._node(v)
                self.head.next = last_node
            else:
                this_node = self._node(v)
                this_node.next = last_node
                last_node = this_node


if __name__ == '__main__':
    # lklst = SingleLinkList(3, 4, '5545', "Benjamin142857")
    # print(lklst.length)
    lklst = DoubleLinkList(3, 5, '5545', "Benjamin142857")
    print(lklst.length)