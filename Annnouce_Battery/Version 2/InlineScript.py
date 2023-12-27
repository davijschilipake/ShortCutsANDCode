#Save the shortcut via https://www.icloud.com/shortcuts/37a77c511bf94dbba5b77ccebe6c1921
#This code snippet should be used in the shortcut itself. The pythonista app provides inline script run
#Make sure to update the route of the python script on the shortcut to where you save this file
#Author: Davi Schilipake

time = ""
for x in "Formatted Date":
     if x != ":":
     	time = time + x
     else:
     	break

def announceOrNot(time):
#The following line will be where you set what time frame you would like for it not to run
	if time >= 23 or time <= 9:
		return False
	else:
		return True
		
announceOrNot(int(time))}