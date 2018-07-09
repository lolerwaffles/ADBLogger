import os,io,re

def DeviceProperties():
    devProp = []
    dataTemp = str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell "service call iphonesubinfo 1 | toybox cut -d \"'\" -f2 | toybox grep -Eo '[0-9]' | toybox xargs | toybox sed 's/\ //g'"''').read()).read())
    rePattern = re.compile('[?!\\n]*(.*.)[\\t]*')
    devProp.append("IMEI:                 {}".format(rePattern.findall(dataTemp)[0]))

    dataTemp = str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell "service call iphonesubinfo 11 | toybox cut -d \"'\" -f2 | toybox grep -Eo '[0-9]' | toybox xargs | toybox sed 's/\ //g'"''').read()).read())
    rePattern = re.compile('[?!\\n]*(.*.)[\\t]*')
    devProp.append("ICCID:                {}".format(rePattern.findall(dataTemp)[0]))

    dataTemp = str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell "service call iphonesubinfo 19 | toybox cut -d \"'\" -f2 | toybox grep -Eo '[0-9]' | toybox xargs | toybox sed 's/\ //g'"''').read()).read())
    rePattern = re.compile('[?!\\n]*(.*.)[\\t]*')
    devProp.append("MDN:                  {}".format(rePattern.findall(dataTemp)[0]))

    dataTemp = str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell "service call iphonesubinfo 8 | toybox cut -d \"'\" -f2 | toybox grep -Eo '[0-9]' | toybox xargs | toybox sed 's/\ //g'"''').read()).read())
    rePattern = re.compile('[?!\\n]*(.*.)[\\t]*')
    devProp.append("IMSI:                 {}".format(rePattern.findall(dataTemp)[0]))

    dataTemp = str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell getprop ro.vendor.product.brand''').read()).read())
    rePattern = re.compile('[?!\\n]*(.*.)[\\t]*')
    devProp.append("Device Brand:         {}".format(rePattern.findall(dataTemp)[0]))

    dataTemp = str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell getprop ro.vendor.product.name''').read()).read())
    rePattern = re.compile('[?!\\n]*(.*.)[\\t]*')
    devProp.append("Device Name:          {}".format(rePattern.findall(dataTemp)[0]))

    dataTemp = str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell getprop ro.build.display.id''').read()).read())
    rePattern = re.compile('[?!\\n]*(.*.)[\\t]*')
    devProp.append("Firmware Version:     {}".format(rePattern.findall(dataTemp)[0]))

    dataTemp = str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell getprop ro.build.version.release''').read()).read())
    rePattern = re.compile('[?!\\n]*(.*.)[\\t]*')
    devProp.append("Android Version:      {}".format(rePattern.findall(dataTemp)[0]))

    dataTemp = str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell getprop ro.boot.hardware.revision''').read()).read())
    rePattern = re.compile('[?!\\n]*(.*.)[\\t]*')
    devProp.append("Hardware Version:     {}".format(rePattern.findall(dataTemp)[0]))

    dataTemp = str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell getprop ro.boot.hardware.ddr''').read()).read())
    rePattern = re.compile('[?!\\n]*(.*.)[\\t]*')
    devProp.append("Memory Type:          {}".format(rePattern.findall(dataTemp)[0]))

    dataTemp = str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell getprop ro.product.board''').read()).read())
    rePattern = re.compile('[?!\\n]*(.*.)[\\t]*')
    devProp.append("LTE/CDMA Chipset type:{}".format(rePattern.findall(dataTemp)[0]))

    dataTemp = str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell getprop ro.build.expect.baseband''').read()).read())
    rePattern = re.compile('[?!\\n]*(.*.)[\\t]*')
    devProp.append("LTE/CDMA Chipset Ver.:{}".format(rePattern.findall(dataTemp)[0]))

    dataTemp = str(io.StringIO(os.popen( r'''.\\platform-tools\\adb shell getprop ro.product.cpu.abi''').read()).read())
    rePattern = re.compile('[?!\\n]*(.*.)[\\t]*')
    devProp.append("CPU version Ver.:    {}".format(rePattern.findall(dataTemp)[0]))

    return devProp
