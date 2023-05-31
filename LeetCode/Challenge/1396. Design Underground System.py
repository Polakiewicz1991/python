class UndergroundSystem:
    def __init__(self):
        self.stationTimes = {}
        self.customers = {}

    def __str__(self):
        return f"customers: {self.customers} \n stationTimes: {self.stationTimes}"
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # if id not in self.customers:
        self.customers[id] = {
            "stationName" : stationName,
            "checkInTime" : t
            }
        # else:
        #     self.customers[id]["stationName"] = stationName
        #     self.customers[id]["checkInTime"].append(t)
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        customerStationName = self.customers[id]["stationName"]
        if customerStationName not in self.stationTimes:
            self.stationTimes[customerStationName] = {} #{stationName : [t - self.customers[id]["checkInTime"]]}
        #else:
        if stationName not in self.stationTimes[customerStationName]:
            self.stationTimes[customerStationName][stationName] = [] #[t - self.customers[id]["checkInTime"]]
        #else:
        self.stationTimes[customerStationName][stationName].append(t - self.customers[id]["checkInTime"])

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        print(startStation," ",endStation, " ", self.stationTimes[startStation])
        if endStation in self.stationTimes[startStation]:
            print(sum(self.stationTimes[startStation][endStation])/len(self.stationTimes[startStation][endStation]))
            return sum(self.stationTimes[startStation][endStation])/len(self.stationTimes[startStation][endStation])
        else:
            print(0)
            return 0
undergroundSystem = UndergroundSystem()
# undergroundSystem.checkIn(45, "Leyton", 3)
# undergroundSystem.checkIn(32, "Paradise", 8)
# undergroundSystem.checkIn(27, "Leyton", 10)
# undergroundSystem.checkOut(45, "Waterloo", 15)
# undergroundSystem.checkOut(27, "Waterloo", 20)
# undergroundSystem.checkOut(32, "Cambridge", 22)
# undergroundSystem.getAverageTime("Paradise", "Cambridge")
# undergroundSystem.getAverageTime("Leyton", "Waterloo")
# undergroundSystem.checkIn(10, "Leyton", 24)
# undergroundSystem.getAverageTime("Leyton", "Waterloo")
# undergroundSystem.checkOut(10, "Waterloo", 38)
# undergroundSystem.getAverageTime("Leyton", "Waterloo")

undergroundSystem.checkIn(37043,"K2618O72",29)#null[37043,"K2618O72",29]
undergroundSystem.checkOut(37043,"U1DTINDT",39)#null[37043,"U1DTINDT",39]
undergroundSystem.getAverageTime("K2618O72","U1DTINDT")#10.00000["K2618O72","U1DTINDT"]
undergroundSystem.checkIn(779975,"K2618O72",112)#null[779975,"K2618O72",112]
undergroundSystem.checkOut(779975,"CN3K6CYM",157)#null[779975,"CN3K6CYM",157]
undergroundSystem.getAverageTime("K2618O72","U1DTINDT")#10.00000["K2618O72","U1DTINDT"]
undergroundSystem.checkIn(706901,"K2618O72",221)#null[706901,"K2618O72",221]
undergroundSystem.getAverageTime("K2618O72","U1DTINDT")#45.00000["K2618O72","CN3K6CYM"],
undergroundSystem.checkIn(18036,"K2618O72",258)#null[18036,"K2618O72",258]
undergroundSystem.getAverageTime("K2618O72","U1DTINDT")#10.00000["K2618O72","U1DTINDT"]
undergroundSystem.getAverageTime("K2618O72","CN3K6CYM")#45.00000["K2618O72","CN3K6CYM"]
undergroundSystem.checkOut(18036,"U1DTINDT",293)#null[18036,"U1DTINDT",293]

print(undergroundSystem)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)