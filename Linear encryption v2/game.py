from extraFunctions import *

def f(x):
	return abs(coeff*x)	#the abs isn't necessary

def response(s):	#get response from a string
	temp=numToStr(f(strToNum(s)))
	startFlag="<STARTFLAG>"
	endFlag="<ENDFLAG>"
	return temp[temp.find(startFlag)+len(startFlag):temp.find(endFlag):2]	#only use text between start and end flags to allow for randomization and redundancy
	#return temp

answer="Input1"
#Here are the passwords baked into this coeff value:
	#"Input1
	#Second input
	#Dave
	#16273548
	#e

print(response(answer))
