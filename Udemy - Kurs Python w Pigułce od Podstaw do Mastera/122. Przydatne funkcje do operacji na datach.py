import time
import math
import datetime

ticks = time.time()
timeData = time.localtime(0)
timeAct = time.localtime(ticks)
timeYesterday = time.localtime(ticks - 24 * 60 * 60)
# czas zapisywany w sekundach
roundTicks = math.floor(ticks)
timeAct2 = time.localtime(roundTicks)

print("ticks: ", ticks, roundTicks)
print("timeData ", timeData)
print("timeAct ", timeAct, '\ntimeAct',timeAct2)
print("timeYesterday ",timeYesterday)

#przydatne formatowanie czasu
asciiTime = time.asctime(timeAct)
patternTime = time.strftime("%y/%m/%d   %H:%M:%S")
print(asciiTime)
print(patternTime)

timeStr = " 8 March, 2025"
timeDataCalc = time.strptime(timeStr, "%d %B, %Y")
print(timeDataCalc)

i=0
while i < 3:
    time.sleep(1)
    # ticks = time.time()
    # timeAct = time.localtime(ticks)
    patternTime = time.strftime("%y/%m/%d   %H:%M:%S")
    print(patternTime)
    i += 1

#pomiar czasu pracy
tStart = time.perf_counter()
time.sleep(0.2)
tStop = time.perf_counter()
print(tStop - tStart)

dateTimeObj = datetime.datetime.now()
print(dateTimeObj)
print(type(dateTimeObj))
print("ilość sec od 1970:", dateTimeObj.timestamp())

dateTime1 = datetime.datetime(2023,10,6,12,7,2)
dateTime2 = datetime.datetime(2023,10,6,12,7,4)

print(dateTime1, dateTime2)
print(dateTime1 > dateTime2)
print(dateTime2 > dateTime1)

dateRozbiorPolski = datetime.timedelta(1795,10,25)
print(dateRozbiorPolski.seconds)