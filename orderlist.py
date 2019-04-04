class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head= None
        self.last_node=None
    def insert_sort(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
        elif self.head.data >= new_node.data:
            new_node.next=self.head
            self.head=new_node
        else:
            n= self.head
            while n is not None:
                if n.data > new_node.data:
                    new_node.next=n
                    self.pre_node.next=new_node
                    break
                self.pre_node = n
                n= n.next
                self.pre_node.next=new_node


    def search(self,element):
        current= self.head
        while current is not None:
            if current.data==element:
                return True
            current=current.next
        return False
    def delete(self,element):
        current=self.head
        while  current is not None:
            if current==element:
                current=current.next
            prev=None
            if current.data==element:
                prev=current
                current=current.next
                prev.next=current.next
                current=None
                break
            if self.last_node==current:
                current=current.next
    def print1(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next
    def print2(self):
        current=self.head
        while current is not None:
            return current.data
            current=current.next
    def poll_first(self):
        self.last_node=self.head
        self.head=self.head.next
        return self.last_node.data
    def size_node(self):
        current=self.head
        size=0
        while current:
            size=size+1
            current=current.next
        return size
if  __name__ == '__main__':
    arr=[]
    ll=linkedlist()
    fo=open("orderlist.txt","r")
    arr=fo.read()
    word=arr.strip().split(' ')
    fo.close()
    print(word)
    for i in word:
        ll.insert_sort(int(i))
    print("sorted array")
    ll.print1()
    print()
    print("enter the element to search")
    element=int(input())
    var= ll.search(element)
    if var:
        print("element is found and remove from list ")
        ll.delete(element)
    else:
        print("element not found so adding in list")
        ll.insert_sort(element)
    ll.print1()
    node_size=ll.size_node()
    array=[]
    for i in range(node_size):
        array.append(ll.poll_first())
    print()
    print(array)
    fo=open ("orderlist.py.txt","w")
    for i in array:
        fo.write(str(i)+ " ")
    fo.close()










