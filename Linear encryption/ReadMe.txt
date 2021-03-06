The idea behind this project:
Given n points, there is a polynomial of at least degree n that goes through every point. Since strings can be represented as integers, we can make a degree-n polynomial that converts n input strings to n specific output strings. You could, for instance, make several private pieces of information that are only accessible by inputting a passphrase.

The best part of all this is that the actual coefficients of the polynomial don't directly give you any information about what the original input and output strings are, especially if you introduce some redundancy to the outputs.

This makes this method better than conventional securely stored information in some ways. For instance, when someone accesses their email, they send a (encrypted) password, which is checked against a database. If they match, the data (in this case your emails) is retrieved from a database and sent to you. This makes the exchange of information secure, but doesn't protect against someone physically going to Google's servers and downloading your emails directly (though this isn't really much of a concern unless Google itself wants to spy on you).
In this program, there is no checking against a database, and in fact none of your information is ever stored directly in a server in the first place! 

That isn't a very fair comparison, since in this program the information itself can't be changed once the coefficients of the polynomial are created, so you couldn't actually use this to log into your email account. But, I thought it would be an interesting and quick project to play around with. 

There is one catch... the values of the polynomial vary so wildly around the points of interest (i.e. Runge's phenomenon) that just finding for the roots of the polynomial gives you near-misses of almost every input/output pair, from which the actual passwords can be guessed. So, I made this version, which is simpler and possibly more secure (though I might end up poking holes in it later). It uses a line instead of a polynomial, so there are no zeros to find.

The files game.py and extraFunctions.py hold the entire program, and are about 40 lines in total; I encourage you to look at it, since the program isn't doing anything complicated. coeffGenerator.py allows you to make your own coefficients to replace the one at the end of extraFunctions.py, so feel free to make your own versions of this to do whatever you want with (though if you do I'd appreciate it if you gave me credit).
