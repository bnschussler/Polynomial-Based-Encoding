#https://en.wikipedia.org/wiki/Polynomial_interpolation
from fractions import Fraction
import numpy as np
from extraFunctions import *
import random

def padNum(x,startpadlen,endpadlen): #pads a number with a random endstring so the coefficients can be rounded to integers
	out=toBase(256,x)
	out=[random.randint(0,255) for i in range(startpadlen)]+out+[random.randint(0,255) for i in range(endpadlen)]
	return arrToNum(256,out)

def pointToNums(point,startFlag="",endFlag="",startpadlen=0,endpadlen=0): #in-->out pair to pair of ints
	return [[strToNum(i[0]),padNum(strToNum(startFlag+i[1]+endFlag),startpadlen,endpadlen)] for i in point]

#points=[[i[0],i[1]+"<END CODED MESSAGE>"] for i in points]
#points=[[strToNum(j) for j in i] for i in points]
#points=[[i[0],padNum(i[1])] for i in points]

def inv(mat): #couldn't get numpy to work with arbitrary precision so I decided to do it myself
	l=len(mat) #assume mat is square
	if l==1:
		return np.array([[1/mat[0][0]]])
	h=int(l/2)
	a,b,c,d=mat[:h,:h],mat[:h,h:],mat[h:,:h],mat[h:,h:]
	ia=inv(a)
	schur=inv(d-c@ia@b)
	a1=ia+ia@b@schur@c@ia
	b1=-ia@b@schur
	c1=-schur@c@ia
	d1=schur
	return np.block([[a1,b1],[c1,d1]])

def getCoeffs(points,startFlag="",endFlag="",startpadlenrange=[0,0],endpadlenrange=[0,0]):
	points=pointToNums(points,
						startFlag,
						endFlag,
						random.randint(startpadlenrange[0],startpadlenrange[1]),
						random.randint(endpadlenrange[0],endpadlenrange[1]))	#convert strings into 2d vectors for math

	vandermonde=np.array([[Fraction(i[0])**n for n in range(len(points))] for i in points])
	ys=np.array([Fraction(i[1]) for i in points])

	coeffs=inv(vandermonde)@ys		#exact coefficients for in-->out
	coeffs=[int(i) for i in coeffs]	#rounding doesn't change the output because of the redundant garbage characters
	return coeffs

print(getCoeffs([["Example input 1","Example output 1"],
				 ["Top text","Bottom Text"],
				 ["password:pyhonRocks1234","Your social security number is:7489A1273412"],
				 ["This should work for any number of inputs/responses","just add more/remove some entries"],
				 ["If the outputs don't work, you might need to increase the values that say \"[200,300]\"","especially if your inputs are long"]],	#change this part to change the input/output text
				 "<START FLAG>","<END FLAG>",[5,10],[200,300]))
#print(np.linalg.inv(vandermonde))
