import time
import pyads
from datetime import datetime

# connect to the PLC
plc = pyads.Connection('10.18.120.42.1.1', 851)

# open the connection
plc.open()

while True:
    bTmp = plc.read_by_name('MAIN.bBlinker_1000ms', pyads.PLCTYPE_BOOL)
    rReferenceName = plc.read_by_name('GVL_Reference.sReferenceActive', pyads.PLCTYPE_STRING)
    plc.write_by_name('GVL_Reference.sReferenceNextToActive',"fajnie to dziala")
    for i in range(10):
        print("Potega {0}: {1}".format(i,i**2))
        variable = 'GVL_Reference.sReferenceNames[{0}]'.format(i)
        print(variable)
        plc.write_by_name(variable,"Potega {0}: {1}".format(i,i**2))
    timenow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # print the timestamp and the value of bTmp
    print(timenow + '  bTmp value is ' + str(bTmp))
    print("Referencja: ", rReferenceName)

    # sleep for 1 seconds
    time.sleep(1)