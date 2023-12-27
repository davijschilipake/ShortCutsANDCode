#Save the shortcut via https://www.icloud.com/shortcuts/781abcfd94d84560b570f0c4dbfece86
#Make sure to update the route of the python script on the shortcut to where you save this file
#Author: Davi Schilipake

import sys
import webbrowser
import urllib.parse
import clipboard

dateNTime = urllib.parse.unquote(sys.argv[1])
time = ""
for x in dateNTime:
     if x != ":":
     	time = time + x
     else:
     	break

def announceOrNot(time):
#The following line will be where you set what time frame you would like for it not to run
	if time >= 23 or time <= 9:
		clipboard.set("False")
	else:
		clipboard.set("True")
		
announceOrNot(int(time))


