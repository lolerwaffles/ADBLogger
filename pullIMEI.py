import os,io,re

def pullIMEI(DUTadd, i):

    IMEIraw = str(io.StringIO(os.popen( r'''.\\platform-tools\\adb -s {} shell "service call iphonesubinfo 1 | toybox cut -d \"'\" -f2 | toybox grep -Eo '[0-9]' | toybox xargs | toybox sed 's/\ //g'"'''.format(DUTadd[i])).read()).read())
    IMEIPattern = re.compile('[?!\\n]*(.*.)[\\t]*')
    return IMEIPattern.findall(IMEIraw)[0]
