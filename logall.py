import os, io, re
from ADBTools import logADB, pullDUTADD

os.system('cls')
print("Walter's LogAll v3, ver.0.1\nAutomatically Connects to all ADB enabled devices and logs them.\nA Folder named with IMEI and timestamp is created for each connected device\n\n")

testCase = input("Test Case Number\n")

devCheck = 'n'
while devCheck == 'n' or devCheck == 'N':
    os.system('cls')
    os.system('.\\platform-tools\\adb devices')
    devCheck = input('\nAre all devices listed?(Y/N)\n')

print("\n\nstarting logging")

DUTadd = pullDUTADD()

logADB(DUTadd, testCase)
