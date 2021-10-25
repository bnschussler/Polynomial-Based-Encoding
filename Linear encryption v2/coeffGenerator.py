# the values retuned from this program are meant to be used as the value of 'coeff' in extraFunctions.py
from random import randint
from extraFunctions import *

def m(x,mod):
	return (x%mod+mod)%mod

def randomtext(l):
	return "".join(chr(randint(0,255)) for i in range(l))

def pad(s,frontpad=0,endpad=0,startflag="",endflag=""):
	return randomtext(frontpad)+startflag+"".join(i + chr(randint(0,255)) for i in s)+endflag+randomtext(endpad)

def getCoeff(points,frontpadrange=[0,0],endpadrange=[0,0],startflag="",endflag=""):
	
	if "" in [i[0] for i in points]:	#0 times anything is still 0, so the emtpy string doesnt work
		return "the empty string cannot be an input"

	points=[[i[0],pad(i[1],
						randint(frontpadrange[0],frontpadrange[1]),
						randint(endpadrange[0],endpadrange[1]),
						startflag,
						endflag)] for i in points]
	coeff=0
	place=0
	for point in points:
		val=strToNum(point[0])
		goal=strToNum(point[1])

		###Stuff to make even numbers work###
		temp=0
		while val%2==0:
			val=val//2
			temp=(temp-2)%8+1
		goal*=2**temp
		goal+=randint(0,2**temp-1)
		###                               ###

		inputsize=2*256**len(point[0])
		goalsize=256**(1+len(point[1]))	#+1 to account for the extra pad character
		current=((coeff*val)//(256**place))%goalsize
		additional=(pow(val,-1,goalsize)*m(goal-current,goalsize))%goalsize #pow(x,-1,m) gives the modular multiplicative inverse of x in mod m
			#(m is a power of two and x is odd so gcd(x,m)=1)
		coeff+=additional*256**place
		place+=len(point[1])
	return(coeff)

a=getCoeff([["Input1","output number 1"],
			["Second input","the next output"],
			["Dave","Davidson"],
			["16273548","Supposedly, this is a number. Why? Explain your answer."],
			["e","eeeeeeeeeeeeeeeeee"]],
			[0,10],[0,10],"<STARTFLAG>","<ENDFLAG>")
print(a)
