from extraFunctions import *

def f(x):			#plug x into a polynomial with coefficients "coeffs"
	return abs(sum([v*x**i for i,v in enumerate(coeffs)])) #coeffs[0]+coeffs[1]x+coeffs[2]x^2+coeffs[3]x^3...

def response(s):	#get response from a string
	temp=numToStr(f(strToNum(s)))
	startFlag="<START FLAG>"
	endFlag="<END FLAG>"
	return temp[temp.find(startFlag)+len(startFlag):temp.find(endFlag)]	#get text between start and end flags for randomization purposes and to add redundancy
	#return temp	#the extra end text also allows the coefficients to be integers (they could've just been rational numbers, but I wanted integer coefficients)

answer="Start"	#use answer="Start" to begin

print(response(answer))