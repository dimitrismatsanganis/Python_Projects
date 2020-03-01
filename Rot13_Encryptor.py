print ('ROT13 Encryptor') #UI Message.
input_txt = input("Give text : ") #get user's text.
tl = list(input_txt) #tl is a list of user's text.
c=0 #initialize variable c equals to 0.

#A For-Loop with Rot13 encoding rules.
for ch in tl:
	if (ch>='a' and ch<='m') or (ch>='A' and ch<='M'):
		tl[c] = chr(ord(ch)+13)
	elif (ch>='n' and ch<='z') or (ch>='N' and ch<='Z'):
		tl[c] = chr(ord(ch)-13)
	c=c+1
    
input_txt = "".join(tl)
print ("Your Rot 13 encrypted text: " + input_txt)#Print the encoded output.