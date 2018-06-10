import os, time, io

os.system('cls')
print("Walter's LogAll v3, ver.0.1\n\n")

'''This is pretty fast and nasty, I need to make some of these if blocks into real functions, lol'''

testCase = input("Test Case Number\n")

devCheck = 'n'
while devCheck == 'n' or devCheck == 'N':
    os.system('cls')
    os.system('adb devices')
    devCheck = input('\nAre all devices listed?(Y/N)\n')



print("\n\nstarting logging")

ADBrawInput = str(io.StringIO(os.popen(".\\platform-tools\\adb devices").read()).read())
DUT1add = ADBrawInput[(ADBrawInput.find('\n') + 1):ADBrawInput.find('\t')]
DUT1Folder = "{}_{}".format(DUT1add, testCase)
DUT2add = ADBrawInput[(ADBrawInput.find(DUT1add) + 2):ADBrawInput.find('\t')]
DUT2Folder = "{}_{}".format(DUT2add, testCase)


os.mkdir('{}'.format(DUT1Folder))
#os.mkdir('{}'.format(DUT2Folder))


os.popen("start cmd /C adb -s {} logcat -b radio -v threadtime ^>^>{}/logradio.txt".format(DUT1add, DUT1Folder))
os.popen("start cmd /C adb -s {} logcat -b main -v threadtime ^>^>{}/logmain.txt".format(DUT1add, DUT1Folder))
os.popen("start cmd /C adb -s {} logcat -b kernel -v threadtime ^>^>{}/logkernel.txt".format(DUT1add, DUT1Folder))
os.popen("start cmd /C adb -s {} logcat -b events -v threadtime ^>^>{}/logevents.txt".format(DUT1add, DUT1Folder))
os.popen("start cmd /C adb -s {} logcat -b system -v threadtime ^>^>{}/logsystem.txt".format(DUT1add, DUT1Folder))
os.popen("start cmd /C adb -s {} logcat -b all -v threadtime ^>^>{}/logall.txt".format(DUT1add, DUT1Folder))

os.popen("start cmd /C adb -s {} logcat -b radio -v threadtime ^>^>{}/logradio.txt".format(DUT2add, DUT2Folder))
os.popen("start cmd /C adb -s {} logcat -b main -v threadtime ^>^>{}/logmain.txt".format(DUT2add, DUT2Folder))
os.popen("start cmd /C adb -s {} logcat -b kernel -v threadtime ^>^>{}/logkernel.txt".format(DUT2add, DUT2Folder))
os.popen("start cmd /C adb -s {} logcat -b events -v threadtime ^>^>{}/logevents.txt".format(DUT2add, DUT2Folder))
os.popen("start cmd /C adb -s {} logcat -b system -v threadtime ^>^>{}/logsystem.txt".format(DUT2add, DUT2Folder))
os.popen("start cmd /C adb -s {} logcat -b all -v threadtime ^>^>{}/logall.txt".format(DUT2add, DUT2Folder))
