class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parkingSpace = [big, medium, small]
        self.parkingSpaceFill = [0, 0, 0]

    def addCar(self, carType: int) -> bool:
        # print("carType", carType)
        # print(self.parkingSpaceFill[carType - 1])
        # print(self.parkingSpace[carType - 1])

        if self.parkingSpaceFill[carType - 1] < self.parkingSpace[carType - 1]:
            self.parkingSpaceFill[carType - 1] += 1
            return True
        return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)