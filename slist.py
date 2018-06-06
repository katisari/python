class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Slist:
    def __init__(self, value):
        node = Node(value)
        self.head = node

    def addNode(self, value):
        node = Node(value)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = node
        return self

    def printAllValues(self, msg=""):
        runner = self.head
        print('Head is', id(runner), msg)
        while(runner.next != None):
            print(runner.value)
            runner = runner.next
        print(runner.value)
        return self


    def removeNode(self, value):
        # node you want to remove is head
        if self.head.value == value:
            if self.head.next == None:
                self.head = None
            else:
                self.head = self.head.next
        # node you want to remove is in middle
        elif self.head.next != None:
            prev = self.head
            runner = prev.next
            while(runner.next != None):
                if runner.value == value:
                    prev.next = runner.next
                    break
                prev = runner
                runner = prev.next
            # remove last element
            if runner.next == None:
                prev.next = None

    def insertNode(self, value, index):
        runner = self.head
        node = Node(value)
        counter = 0
        # first node
        if index == counter:
            self.head = node
            self.head.next = runner
        else:
            prev = self.head
            runner = prev.next
            count = 1
            # middle
            while (runner.next and index != counter):
                prev = runner
                runner = prev.next
                counter += 1
            prev.next = node
            node.next = runner


list = Slist(5)
list.addNode(3)
list.addNode(1)
list.insertNode(7, 0)
list.printAllValues("Attempt 1")
