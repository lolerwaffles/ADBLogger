import os,io,re,datetime
from pullIMEI import pullIMEI

def logADB(DUTadd, testCase):

    for i in range(len(DUTadd)):

        DUTFolder = "{}_{}_{}".format(pullIMEI(DUTadd,i), testCase , datetime.datetime.now().strftime("%H-%M-%S"))

        os.mkdir('{}'.format(DUTFolder))

        os.popen("start cmd /C .\\platform-tools\\adb -s {} logcat -b radio -v threadtime ^>^>{}/logradio.txt".format(DUTadd[i], DUTFolder))
        os.popen("start cmd /C .\\platform-tools\\adb -s {} logcat -b main -v threadtime ^>^>{}/logmain.txt".format(DUTadd[i], DUTFolder))
        os.popen("start cmd /C .\\platform-tools\\adb -s {} logcat -b kernel -v threadtime ^>^>{}/logkernel.txt".format(DUTadd[i], DUTFolder))
        os.popen("start cmd /C .\\platform-tools\\adb -s {} logcat -b events -v threadtime ^>^>{}/logevents.txt".format(DUTadd[i], DUTFolder))
        os.popen("start cmd /C .\\platform-tools\\adb -s {} logcat -b system -v threadtime ^>^>{}/logsystem.txt".format(DUTadd[i], DUTFolder))
        os.popen("start cmd /C .\\platform-tools\\adb -s {} logcat -b all -v threadtime ^>^>{}/logall.txt".format(DUTadd[i], DUTFolder))
