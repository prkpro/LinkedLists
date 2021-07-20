# Linked List Implementation

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        tail = self.head
        while tail.next is not None:
            tail = tail.next

        tail.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        self.head, new_node.next = new_node, self.head
        return

    def insert(self, value, at):
        new_node = Node(value)
        if at < 1:
            return
        elif at == 1:
            self.head, new_node.next = new_node, self.head
        else:
            while at > 1:
                at -= 1
                pos = self.head
                pos = pos.next
            self.head, new_node.next = new_node, self.head
        return

    def delete(self, value):
        if self.head is None:
            return
        pos = self.head
        while pos is not None:
            prev = pos
            if pos.value == value:
                if pos.next is None:
                    prev.next = None
                    return
                else:
                    pos.value, pos.next = pos.next.value, pos.next.next
                    return
            pos = pos.next

    def __str__(self):
        tmp_list = []
        if self.head is None:
            return str(tmp_list)
        tmp = self.head
        while tmp is not None:
            tmp_list.append(tmp.value)
            tmp = tmp.next

        return str(tmp_list)


def test():
    ll = LinkedList()

    ll.append(23)
    print(ll)
    ll.prepend(14)
    print(ll)
    ll.insert(19, 1)
    print(ll)
    ll.delete(19)
    print(ll)


if __name__ == "__main__":
    test()
