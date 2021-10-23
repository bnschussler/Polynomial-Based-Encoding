from extraFunctions import *

def f(x):
	return abs(coeff*(2*x+1))

def response(s):	#get response from a string
	temp=numToStr(f(strToNum(s)))
	startFlag="<STARTFLAG>"
	endFlag="<ENDFLAG>"
	return temp[temp.find(startFlag)+len(startFlag):temp.find(endFlag):2]	#get text between start and end flags for randomization purposes and to add redundancy
	#return temp

answer="Start"	#use answer="Start" to begin

print(response(answer))