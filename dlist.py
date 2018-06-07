class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        node.prev = node
        node.next = node 

    def add_node(self, value):
        # for every node
        node = Node(value)
        self.tail.next = node
        node.prev = self.tail
        node.next = self.head
        self.tail = node
        self.head.prev = self.tail
        return self

    def printAll(self, msg=""):
        runner = self.head
        print("\n\n head points to", id(self.head))
        print("*"*80, msg)
        while(runner.next!=self.head):
          print(id(runner), runner.value, id(runner.next))
          runner = runner.next
        print(id(runner), runner.value, id(runner.next))


    def remove_node(self, value):
        # remove first value
        previous_node = self.head
        runner = previous_node.next
        if self.head.value == value:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
        
        # middle node
        elif runner != self.head:
            while runner.next != self.head:
                if runner.value == value:
                    runner.next.prev = previous_node
                    previous_node.next = runner.next
                    runner = previous_node
                previous_node = runner
                runner = previous_node.next
            # end
            if runner.value == value:
                runner.next.prev = previous_node
                previous_node.next = runner.next
            
        return self
    def insert_node(self, value, index):
        counter = 0
        node = Node(value)
        if index == 0:
            node.next = self.head
            node.prev = self.tail
            self.head.prev = node
            self.head = node
            return self
        else:
            counter = 1
            runner = self.head.next
            while runner.next != self.head:
                if counter == index:
                    node.prev = runner.prev
                    node.next = runner
                    node.prev.next = node
                    runner.prev = node
                    return self
                counter += 1
                runner = runner.next
            node.prev = runner
            node.next = runner.next
            runner.next = node
            self.head.prev = node
            self.tail = node

    # def insert_node(self, value, index):
    #     counter = 0
    #     node = Node(value)
    #     if counter == index:
    #         node.next = self.head
    #         node.prev = self.tail
    #         self.head.prev = node
    #         self.head = node
    #     # insert beginning
    #     else: 
    #         counter = 1
    #         previous_node = self.head
    #         runner = previous_node.next
    #         while runner != self.head:
    #             if counter == index:
    #                 previous_node.next = node
    #                 node.prev = previous_node
    #                 node.next = runner
    #                 runner.prev = node
    #             counter += 1
    #             previous_node = runner
    #             runner = previous_node.next
    #         # if counter == index:

                    
        # middle
list = DoublyLinkedList(5)
list.add_node(3)
list.add_node(7)
list.add_node(4)
list.insert_node(7,3)
list.printAll()
