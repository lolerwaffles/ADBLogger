import os, io, re, subprocess, datetime


os.system('cls')
print("Walter's LogAll v3, ver.0.1\nAutomatically Connects to all ADB enabled devices and logs them.\nA Folder named with IMEI and timestamp is created for each connected device\n")


testCase = input("Test Case Number\n")

devCheck = 'n'
while devCheck == 'n' or devCheck == 'N':
    os.system('cls')
    os.system('.\\platform-tools\\adb devices')
    devCheck = input('\nAre all devices listed?(Y/N)\n')

print("\n\nstarting logging")

ADBrawInput = str(io.StringIO(os.popen(".\\platform-tools\\adb devices").read()).read())
pattern = re.compile('\\n.*?\\t')

DUTadd = pattern.findall(ADBrawInput)

for i in range(len(DUTadd)):
    DUTadd[i] = DUTadd[i][1:-1]

    IMEI = str(io.StringIO(os.popen( r'''.\\platform-tools\\adb -s {} shell "service call iphonesubinfo 1 | toybox cut -d \"'\" -f2 | toybox grep -Eo '[0-9]' | toybox xargs | toybox sed 's/\ //g'"'''.format(DUTadd[i])).read()).read())
    IMEI = IMEI[:-1:]

    DUTFolder = "{}_{}_{}".format(IMEI, testCase , datetime.datetime.now().strftime("%H-%M-%S"))

    os.mkdir('{}'.format(DUTFolder))

    os.popen("start cmd /C .\\platform-tools\\adb -s {} logcat -b radio -v threadtime ^>^>{}/logradio.txt".format(DUTadd[i], DUTFolder))
    os.popen("start cmd /C .\\platform-tools\\adb -s {} logcat -b main -v threadtime ^>^>{}/logmain.txt".format(DUTadd[i], DUTFolder))
    os.popen("start cmd /C .\\platform-tools\\adb -s {} logcat -b kernel -v threadtime ^>^>{}/logkernel.txt".format(DUTadd[i], DUTFolder))
    os.popen("start cmd /C .\\platform-tools\\adb -s {} logcat -b events -v threadtime ^>^>{}/logevents.txt".format(DUTadd[i], DUTFolder))
    os.popen("start cmd /C .\\platform-tools\\adb -s {} logcat -b system -v threadtime ^>^>{}/logsystem.txt".format(DUTadd[i], DUTFolder))
    os.popen("start cmd /C .\\platform-tools\\adb -s {} logcat -b all -v threadtime ^>^>{}/logall.txt".format(DUTadd[i], DUTFolder))


print("Logging started")
