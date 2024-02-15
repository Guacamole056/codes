class SaleData:
    def __init__(self, myID, qty):
        self.id = myID
        self.quantity = qty


CircularQueue = []
for x in range(5):
    CircularQueue.append(SaleData("", -1))

head = 0
tail = 0
NumberOfItems = 0


def Enqueue(new_record):
    global tail
    global NumberOfItems
    if NumberOfItems == 5:
        return -1
    CircularQueue[tail] = new_record
    tail = tail + 1
    NumberOfItems = NumberOfItems + 1
    if tail == len(CircularQueue):
        tail = 0
    return 1


def Dequeue():
    global head
    global NumberOfItems
    if NumberOfItems == 0:
        return ""
    else:
        return_record = CircularQueue[head]
        head = head + 1
        NumberOfItems = NumberOfItems - 1
    if head == 5:
        head = 0
    return return_record


def EnterRecord():
    id = input("enter your sale ID : ")
    quantity = int(input("enter your sale quantity : "))
    myrecord = SaleData(id, quantity)
    if Enqueue(myrecord) == 1:
        print("Stored")
    else:
        print("Full")


for x in range(6):
    EnterRecord()

removal = Dequeue()
if removal.id == "":
    print("Queue is Empty")
else:
    print(removal.id, "", removal.quantity)
EnterRecord()
for x in range(5):
    print(CircularQueue[x].id, "", CircularQueue[x].quantity)
