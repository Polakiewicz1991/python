class Device:
    def __init__(self,name,connected_by):
        self.name = name
        self.conneced_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device: {self.name} {self.conneced_by}"

    def disconnected(self):
        self.connected = False
        print("Disconneced")

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name,connected_by)
        self.capacity = capacity
        self.reamining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.reamining_pages} pages remaining)"

    def printing(self,pages):
        if not self.connected:
            print("Printer is not connected")
            return
        print(f"printing {pages} pages.")
        self.reamining_pages -= pages

myPrinter = Printer("Printer","USB",500)
myPrinter.printing(20)
print(myPrinter)

myPrinter.disconnected()
myPrinter.printing(50)