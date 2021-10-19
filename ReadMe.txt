The idea behind this project:
Given n points, there is a polynomial of at least degree n that goes through every point. Since strings can be represented as integers, we can make a degree-n polynomial that converts n input strings to n specific output strings. You could, for instance, make several private pieces of information that are only accessible by inputting a passphrase.

The best part of all this is that the actual coefficients of the polynomial don't gave you any information about what the original input and output strings were (at least as far as I can tell), especially if you introduce some redundancy to the outputs.

This makes this method better than conventional securely stored information in some ways. For instance, when someone accesses their email, they send a (encrypted) password, which is checked against a database. If they match, the data (in this case your emails) is retrieved from a database and sent to you. 
In this program, there is no checking against a database, and in fact none of your sensitive information is every stored directly in a server in the first place! 

That isn't a very fair comparison, since in this program the information itself can't be changed once the coefficients of the polynomial are created, so you couldn't actually use this log into your email account. But, I thought it would be an interesting and quick project to play around with. 

The files game.py and extraFunctions.py hold the entire program, and is about 40 lines in total; I encourage you to look at it, since the program isn't doing anything complicated. coeffGenerator.py allows you to make your own coefficients to replace the ones at the end of extraFunctions.py, so feel free to make your own versions of this to do whatever you want with (just give me credit I guess).