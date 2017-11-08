class Node(object):
    """docstring for Node."""
    def __init__(self, data):
        super(Node, self).__init__()
        self.data = data
        self.next = None


class LinkedList(object):
    """docstring for LinkedList."""
    def __init__(self):
        super(LinkedList, self).__init__()
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, position, new_data):
        if(position==0):
            self.push(new_data)
            return

        prev_node = self.head
        while(prev_node.next and position-1!=0):
            prev_node = prev_node.next
            position -= 1

        if(position-1!=0):
            print("No suffiecient Element")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while(last.next):
            last = last.next

        last.next = new_node

    def delete(self, data):
        temp = self.head
        if(temp):
            if(temp.data==data):
                self.head = temp.next
                temp = None
                return

        while(temp):
            if(temp.data==data):
                break
            prev = temp
            temp = temp.next

        if(not temp):
            print("Data to be deleted not present")
            return

        prev.next = temp.next
        temp = None

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next



if __name__=='__main__':
    sll = LinkedList()
    sll.append(6)
    sll.push(7)
    sll.push(1)
    sll.append(4)
    sll.insertAfter(2,8)
    sll.delete(9)

    print ('Created linked list is:')
    sll.print_list()
