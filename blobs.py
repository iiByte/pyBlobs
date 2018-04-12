from colorama import Fore, Style
from libapple import iDevice

device = iDevice(input("Device Identifier: "))
firmwareList = list(device.signed.keys())

for i in firmwareList:
	if device.signed[i] == True:
		print(Fore.GREEN + i)
	else:
		print(Fore.RED + i)

print(Style.RESET_ALL)
print(device)