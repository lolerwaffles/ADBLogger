import os,io,re,datetime

def pullDUTADD():
    ADBrawInput = str(io.StringIO(os.popen(".\\platform-tools\\adb devices").read()).read())
    pattern = re.compile('\\n((?!\\n|\\t).*?)\\t')
    return pattern.findall(ADBrawInput)

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

def pullIMEI(DUTadd, i):

    IMEIraw = str(io.StringIO(os.popen( r'''.\\platform-tools\\adb -s {} shell "service call iphonesubinfo 1 | toybox cut -d \"'\" -f2 | toybox grep -Eo '[0-9]' | toybox xargs | toybox sed 's/\ //g'"'''.format(DUTadd[i])).read()).read())
    IMEIPattern = re.compile('[?!\\n]*(.*.)[\\t]*')
    return IMEIPattern.findall(IMEIraw)[0]
