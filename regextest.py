import os, io, re

ADBrawInput = str(io.StringIO(os.popen(".\\platform-tools\\adb devices").read()).read())
pattern = re.compile('\\n.*?\\t')

DUTaddresses = pattern.findall(ADBrawInput)

for i in range(len(DUTaddresses)):
    DUTaddresses[i] = DUTaddresses[i][1:-1]
    print(DUTaddresses[i])
