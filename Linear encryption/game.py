from extraFunctions import *

def f(x):
	return abs(coeff*(2*x+1))

def response(s):	#get response from a string
	temp=numToStr(f(strToNum(s)))
	startFlag="<STARTFLAG>"
	endFlag="<ENDFLAG>"
	return temp[temp.find(startFlag)+len(startFlag):temp.find(endFlag):2]	#only use text between start and end flags to allow for randomization and redundancy
	#return temp

answer="Start"	#use answer="Start" to begin

print(response(answer))
