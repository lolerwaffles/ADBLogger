import os, time, io

os.system('cls')
print("Walter's LogAll v3, ver.0.1\n\n")

'''This is pretty fast and nasty, I need to make some of these if blocks into real functions, lol'''

testCase = input("Test Case Number\n")

devCheck = 'n'
while devCheck == 'n' or devCheck == 'N':
    os.system('cls')
    os.system('.\\platform-tools\\adb devices')
    devCheck = input('\nAre all devices listed?(Y/N)\n')

print("\n\nstarting logging")

ADBrawInput = str(io.StringIO(os.popen(".\\platform-tools\\adb devices").read()).read())
NumDevices = ADBrawInput.count(r"device\n")

for i in range(NumDevices):
    if NumDevices == 1:
        DUTadd = ADBrawInput[(ADBrawInput.find('\n') + 1):ADBrawInput.find('\t')]
    else:
        DUTadd = ADBrawInput[(ADBrawInput.find(DUTadd) + 2):ADBrawInput.find('\t')]

    DUTFolder = "{}_{}".format(DUTadd, testCase)

    os.mkdir('{}'.format(DUTFolder))

    os.popen("start cmd /C .\\platform-tools\\adb -s {} logcat -b radio -v threadtime ^>^>{}/logradio.txt".format(DUTadd, DUTFolder))
    os.popen("start cmd /C .\\platform-tools\\adb -s {} logcat -b main -v threadtime ^>^>{}/logmain.txt".format(DUTadd, DUTFolder))
    os.popen("start cmd /C .\\platform-tools\\adb -s {} logcat -b kernel -v threadtime ^>^>{}/logkernel.txt".format(DUTadd, DUTFolder))
    os.popen("start cmd /C .\\platform-tools\\adb -s {} logcat -b events -v threadtime ^>^>{}/logevents.txt".format(DUTadd, DUTFolder))
    os.popen("start cmd /C .\\platform-tools\\adb -s {} logcat -b system -v threadtime ^>^>{}/logsystem.txt".format(DUTadd, DUTFolder))
    os.popen("start cmd /C .\\platform-tools\\adb -s {} logcat -b all -v threadtime ^>^>{}/logall.txt".format(DUTadd, DUTFolder))
