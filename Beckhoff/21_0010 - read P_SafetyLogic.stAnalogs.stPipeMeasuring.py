import time
import pyads
from datetime import datetime

# connect to the PLC
plc = pyads.Connection('192.168.1.50.1.1', 851)

# open the connection
plc.open()

while True:
    rAngle = plc.read_by_name('P_SafetyLogic.stAnalogs.stPipeMeasuring.rAngle', pyads.PLCTYPE_ARR_LREAL(361))
    rAngleFiltered = plc.read_by_name('P_SafetyLogic.stAnalogs.stPipeMeasuring.rAngleFiltered', pyads.PLCTYPE_ARR_LREAL(361))
    rAngleInterpolation = plc.read_by_name('P_SafetyLogic.stAnalogs.stPipeMeasuring.rAngleInterpolation', pyads.PLCTYPE_ARR_LREAL(361))


    # print the timestamp and the value of bTmp
    print("rAngle:\n " + str(rAngle) + "\n")
    print("rAngleFiltered:\n " + str(rAngleFiltered) + "\n")
    print("rAngleInterpolation:\n " + str(rAngleInterpolation) + "\n")

    # sleep for 1 seconds
    time.sleep(5)