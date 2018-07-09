import easygui
from GUIdeviceProperties import DeviceProperties

devProp = DeviceProperties()

title = "Connected Device Properties"
easygui.msgbox("{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n"
				.format(devProp[0],devProp[1],devProp[2],devProp[3],devProp[4],devProp[5],devProp[6],devProp[7],devProp[8],devProp[9],devProp[10],devProp[11],devProp[12]), title)

