import os,io,re

dataTemp = str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell "service call iphonesubinfo 1 | toybox cut -d \"'\" -f2 | toybox grep -Eo '[0-9]' | toybox xargs | toybox sed 's/\ //g'"''').read()).read())
rePattern = re.compile('[?!\\n]*(.*.)[\\t]*')
print("IMEI:                 {}".format(rePattern.findall(dataTemp)[0]))

dataTemp = str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell "service call iphonesubinfo 11 | toybox cut -d \"'\" -f2 | toybox grep -Eo '[0-9]' | toybox xargs | toybox sed 's/\ //g'"''').read()).read())
rePattern = re.compile('[?!\\n]*(.*.)[\\t]*')
print("ICCID:                {}".format(rePattern.findall(dataTemp)[0]))

dataTemp = str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell "service call iphonesubinfo 19 | toybox cut -d \"'\" -f2 | toybox grep -Eo '[0-9]' | toybox xargs | toybox sed 's/\ //g'"''').read()).read())
rePattern = re.compile('[?!\\n]*(.*.)[\\t]*')
print("MDN:                  {}".format(rePattern.findall(dataTemp)[0]))

dataTemp = str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell "service call iphonesubinfo 8 | toybox cut -d \"'\" -f2 | toybox grep -Eo '[0-9]' | toybox xargs | toybox sed 's/\ //g'"''').read()).read())
rePattern = re.compile('[?!\\n]*(.*.)[\\t]*')
print("IMSI:                 {}".format(rePattern.findall(dataTemp)[0]))

dataTemp = str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell getprop ro.vendor.product.brand''').read()).read())
rePattern = re.compile('[?!\\n]*(.*.)[\\t]*')
print("Device Brand:         {}".format(rePattern.findall(dataTemp)[0]))

dataTemp = str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell getprop ro.vendor.product.name''').read()).read())
rePattern = re.compile('[?!\\n]*(.*.)[\\t]*')
print("Device Name:          {}".format(rePattern.findall(dataTemp)[0]))

dataTemp = str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell getprop ro.build.display.id''').read()).read())
rePattern = re.compile('[?!\\n]*(.*.)[\\t]*')
print("Firmware Version:     {}".format(rePattern.findall(dataTemp)[0]))

dataTemp = str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell getprop ro.build.version.release''').read()).read())
rePattern = re.compile('[?!\\n]*(.*.)[\\t]*')
print("Android Version:      {}".format(rePattern.findall(dataTemp)[0]))

dataTemp = str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell getprop ro.boot.hardware.revision''').read()).read())
rePattern = re.compile('[?!\\n]*(.*.)[\\t]*')
print("Hardware Version:     {}".format(rePattern.findall(dataTemp)[0]))

dataTemp = str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell getprop ro.boot.hardware.ddr''').read()).read())
rePattern = re.compile('[?!\\n]*(.*.)[\\t]*')
print("Memory Type:          {}".format(rePattern.findall(dataTemp)[0]))

dataTemp = str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell getprop ro.product.board''').read()).read())
rePattern = re.compile('[?!\\n]*(.*.)[\\t]*')
print("LTE/CDMA Chipset type:{}".format(rePattern.findall(dataTemp)[0]))

dataTemp = str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell getprop ro.build.expect.baseband''').read()).read())
rePattern = re.compile('[?!\\n]*(.*.)[\\t]*')
print("LTE/CDMA Chipset Ver.:{}".format(rePattern.findall(dataTemp)[0]))

dataTemp = str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell getprop ro.product.cpu.abi''').read()).read())
rePattern = re.compile('[?!\\n]*(.*.)[\\t]*')
print("CPU version Ver.:    {}".format(rePattern.findall(dataTemp)[0]))
