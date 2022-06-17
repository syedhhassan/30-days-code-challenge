import string

all= string.ascii_letters

d1 = {}
key = 4

for i in range(len(all)):
	d1[all[i]] = all[(i+key)%len(all)]


pt=input("Enter Plain Text: ")
ct=[]

for char in pt:
	if char in all:
		temp = d1[char]
		ct.append(temp)
	else:
		temp =char
		ct.append(temp)
		
ct= "".join(ct)
print("Cipher Text is: ",ct)
