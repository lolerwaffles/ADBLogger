import os,io,re

def pullDUTADD():
    ADBrawInput = str(io.StringIO(os.popen(".\\platform-tools\\adb devices").read()).read())
    pattern = re.compile('\\n((?!\\n|\\t).*?)\\t')
    return pattern.findall(ADBrawInput)
