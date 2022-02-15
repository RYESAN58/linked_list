class SLNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class SList:
    def __init__(self):
        self.head= None
    def add_to_front(self, val):
        new_node= SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self
    def print_values(self):
        runner = self.head
        while runner != None:
            print(runner.val)
            runner = runner.next
            return self
    def add_to_the_back(self,val):
        pass

[1,3,5,10,5,6,7,8,9]

10


my_list = SList()

my_list.add_to_front(5)
my_list.print_values()
print(my_list)