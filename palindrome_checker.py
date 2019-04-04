class Deque:
    def __init__(self, capacity):

        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.deque = [] * capacity
    def insertion(self,lower_case1):
        if self.capacity==self.rear:
            print("deque is full")
        else:
            for i in lower_case1:
                self.deque.append(i)
                self.rear = self.rear+1
    def display(self):
        if self.rear == self.front:
            print("deque is empty")
        else:
            for i in range(self.rear):
                print(self.deque[i])
                self.rear=self.rear-1
    def remove_from_front(self):
        if self.rear==self.front:
            print("it is empty")
        else:
            self.front=self.front+1
            return self.deque[self.front-1]
    def remove_from_rear(self):
        if self.rear== self.front:
            print("deque is full")
        else:
            self.rear=self.rear-1
            return self.deque[self.rear]
if __name__ == '__main__':
    element=input("enter the string")
    lower_case=element.lower()
    d=Deque(len(lower_case))
    d.insertion(lower_case)
    for i in range(len(lower_case)//2):
        if d.remove_from_front()==d.remove_from_rear():
            if i ==(len(lower_case)//2)-1:
                print("it is palindrome")
        else:
            print("it is not palindrome")
            break






