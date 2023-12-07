class LinkedList:

    ARROW = "->"

    class Node:

        def __init__(self, value, next=None) -> None:
            self.value = value
            self.next = next

    def __init__(self) -> None:
        self.head = None
        self.__len = 0
        self.__current_node = None

    def __iter__(self):
        if self.head:
            self.__current_node = self.head
        else:
            self.__current_node = None
        return self

    def __next__(self):
        if self.__current_node.next:
            value = self.__current_node.next.value
            self.__current_node = self.__current_node.next
        else:
            self.__current_node = None
            raise StopIteration
        return value

    def __str__(self) -> str:
        res = ""

        last = self.head
        while last.next:
            last = last.next
            res = f"{res}{LinkedList.ARROW}{last.value}"

        return res.strip(LinkedList.ARROW)
    
    def __eq__(self, other) -> bool:
        try:
            if len(self) != len(other):
                return False
            last_self = self.head
            last_other = other.head
            while last_self.next and last_other.next:
                if last_self.value != last_other.value:
                    return False
                last_self = last_self.next
                last_other = last_other.next

            return True
        except AttributeError:
            return False
        # return str(self) == str(other)

    # def __len__(self):
    #     res = 0
    #     last = self.head
    #     while last.next:
    #         res += 1
    #         last = last.next

    #     return res

    def __len__(self):
        return self.__len

    def push(self, value):
        if self.head == None:
            self.head = LinkedList.Node(value)

        last = self.head
        while last.next:
            last = last.next
        
        last.next = LinkedList.Node(value)
        self.__len += 1

    def remove(self, value):

        last = self.head
        if last.value == value:
            self.head = last.next
            return

        while last.next:
            if last.next.value == value:
                if last.next.next != None:
                    last.next = last.next.next
                else:
                    last.next = None
            last = last.next

    def __getitem__(self, key):
        if key > len(self) - 1:
            raise IndexError
        
    def __setitem__(self, key, value):
        if key > len(self) - 1:
            raise IndexError

       

l = LinkedList()
l.push(1)
l.push(2)
l.push(3)
l.push([1,2,3])
l.push(print)
print(l)

l2 = LinkedList()
l2.push(1)
l2.push(2)
l2.push(3)
print(f"{l} == {l2} : {l==l2}")
print(f"{l} == {l} : {l==l}")

print(len(l))

l.remove(2)
print(l)

for i in l:
    print(i)

print(l)

l[1]
l[2] = "test"