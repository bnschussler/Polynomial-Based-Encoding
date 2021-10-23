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
	points=[[i[0],pad(i[1],
						randint(frontpadrange[0],frontpadrange[1]),
						randint(endpadrange[0],endpadrange[1]),
						startflag,
						endflag)] for i in points]
	coeff=0
	place=0
	for point in points:
		val=strToNum(point[0])*2+1
		goal=strToNum(point[1])
		inputsize=2*256**len(point[0])
		goalsize=256**len(point[1])
		current=((coeff*val)//(256**place))%goalsize
		additional=(pow(val,-1,goalsize)*m(goal-current,goalsize))%goalsize #pow(x,-1,m) gives the modular multiplicative inverse of x in mod m 
			#(m is a power of two and x is odd so gcd(x,m)=1)
		coeff+=additional*256**place
		place+=len(point[1])
	return(coeff)

a=getCoeff([["Example input 1","output 1"],	#here are some preset answers. just press enter to get the value of coeff for these answer/response pairs.
				 ["Top text","Bottom Text"],
				 ["password:pyhonRocks1234","Your social security number is:7489A1273412"],
				 ["This should work for any number of inputs/responses; just add/revome some entries.","One thing to note is that an input can't be longer than its output's position in the unfiltered output string, or some of the input key will be redundant and not affect the output message."], 
				 																																				# not sure if that makes sense; a good example of this with these presets is inputting "qWeRtYu input 1" with the the end padding set to zero,
				 																																				# which should give the same result as "Example input 1", because the extra characters are too large to affect values in the spot of the output string where "output 1" is.
				 ["You can always increase the end padding though","which should fix the issue."]],[0,10],[0,10],"<STARTFLAG>","<ENDFLAG>")
print(a)
