class queue:
    def __init__(self):
        self.list1=[]
    def is_empty(self):
        return self.list1==[]
    def enqueue(self,list1):
        self.list1.insert(0,list1)
    def dequeue(self):
        return self.list1.pop()
    def size(self):
        return len(self.list1)
def cash():
    q=queue()
    bank_cash=1000
    try:
        people=int(input("enter the no of people"))
    except ValueError:
        print ("enter the data in number")
    for i in range(0,people):
        q.enqueue(i)
    try:
        for i in range(0,q.size()):
            print("deposit the ammount and withdraw the ammount")
            choice=int(input("enter the choice"))
            if choice==1:
                deposit= float(input("enter the value"))
                bank_cash = bank_cash + deposit
                q.dequeue()
            if choice==2:
                withdraw=int(input("enter the ammount"))
                if withdraw <= bank_cash:
                    bank_cash=bank_cash-withdraw
                    print("total ammount",bank_cash)
                    q.dequeue()
                if withdraw > bank_cash:
                    print("insufficient ammount")
                    print("re-enter the ammount and cancel")
                    choose=int(input("enter the choice"))
                    if choose==1:
                        if withdraw <= bank_cash:
                            bank_cash=bank_cash - withdraw
                            print("withdraw cash",withdraw)
                            q.dequeue()
                    if choose==2:
                        print("trasaction is cancel")
                        print("thank you")
                        q.dequeue()
            if i < q.size():
                print("next person/n")
            print("total cash in bank account",bank_cash)
    except ValueError:
        print("enter valid data")
if __name__  == '__main__':
    cash()