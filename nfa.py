'''
Input Format: 
The input needs to be a valid x-path expression. Each of the nodes in the path needs to be separated by space. 

For eg: /toc /student /name[text()='sona'] (Note the space between two location steps)

Invalid expression: /toc/student/name[text()='sona'] (Invalid because incorrect input format. The nodes need to be separated by a space.]
'''
def nfa(txt, name, phone, address):
	nfa = 0
	x = txt.split(" ")
	# print (x)
	count = len(x)
	n = 0
	b = 0
#for all the path expressions of the form /
	if (x[0][1] != "/" and x[0][1] != "*"): #/toc
		y0 = x[0].split("/")
		if (len(y0) == 2 and "toc" == y0[1]):
			nfa = 1
			# print ("/toc", len(y0[1]))
			n = 1 
		else:
			nfa = 0
			n = 0
		
	if (x[0][1] == "/"): 
		y0 = x[0].split("//")
		if (len(y0) == 2 and "toc" == y0[1]): #//toc
			nfa = 11
			return nfa
			# n = 1
		elif (len(y0) == 2 and "student" == y0[1]): #//student
			nfa = 21
			n = 1
			b = 21
		elif (len(y0) == 2 and "name" == y0[1]): #//name
			nfa = 32
		elif (len(y0) == 2 and "phone" == y0[1]): #//phone
			nfa = 42
		elif (len(y0) == 2 and "address" == y0[1]): #//address
			nfa = 52
		else:
			nfa = 0
			n = 0

	if (n < count and n == 1 and b == 21):
		nfa = 0
		if (x[1][1] != "/" and x[1][1] != "*"): #//student/text()
			y1 = x[1].split("/")
			if (len(y1) == 2 and "text()" == y1[1]):
				nfa = 22
				n = 2
			else:
				nfa = 0
				n = 0
	

	if (n < count and n == 1):
		nfa = 0
		if (x[1][1] != "/" and x[1][1] != "*"): #/toc/student
			y1 = x[1].split("/")
			if (len(y1) == 2 and "student" == y1[1]):
				nfa = 2
				n = 2
			if (len(y1) == 2 and "student[1]" == y1[1]):
				nfa = 2222
				n = 2
			if (len(y1) == 2 and "student[2]" == y1[1]):
				nfa = 2221
				n = 2
		elif (x[1][1] == "/"): #/toc//student
			y1 = x[1].split("//")
			if (len(y1) == 2 and "student" == y1[1]):
				nfa = 21
				n = 2
				b = 21
		elif (x[1][1] == "*"): #/toc/*
			y1 = x[1].split("/*")
			if (len(y1) == 2 and "" == y1[1]):
				nfa = 222
		else:
			nfa = 0
			

	if (n < count and n == 2 and b == 21):
		nfa = 0
		if (x[2][1] != "/" and x[2][1] != "*"): #/toc//student/text()
			y2 = x[2].split("/")
			if (len(y2) == 2 and "text()" == y2[1]):
				nfa = 22
				n = 3
		else:
			nfa = 0
			

	if (n < count and n == 2):
		nfa = 0
		if (x[2][1] != "/" and x[2][1] != "*"):
			y2 = x[2].split("/")
			# print (len(y2[1]))
			if (len(y2[1]) == 4 and y2[1] == "name"):#/toc/student/name
				nfa = 3
			elif (len(y2[1]) == 5 and y2[1] == "phone"):#/toc/student/phone
				nfa = 4
			elif (len(y2[1]) == 7 and y2[1] == "address"):#/toc/student/address
				nfa = 5
			else:
				for i in range(len(name)):
					nam = "name[text()='"+ str(name[i])+"']"
					if (nam == y2[1]): #/toc/student/name[text()='sona']
						nfa = 33
						# print ("done name")
						return nfa

				for i in range(len(phone)):
					phn = "phone[text()='"+ str(phone[i])+"']"
					if (phn == y2[1]): #/toc/student/phone[text()=phone[i]]
						nfa = 44
						return nfa
			
				for i in range(len(address)):
					addr = "address[text()='"+ str(address[i])+"']"
					if (addr == y2[1]): #/toc/student/address[text()='nepal']
						nfa = 55
						# print ("done address")
						return nfa

			

		if (x[2][1] == "/"): #/toc/student//name
			y2 = x[2].split("//")
			if (len(y2[1]) == 4 and "name" == y2[1]):
				nfa = 31
				n = 3 
				b = 31
			elif (len(y2[1]) == 5 and "phone" == y2[1]): #/toc/student//phone
				nfa = 41
				n = 3 
				b = 41
			elif (len(y2[1]) == 7 and "address" == y2[1]): #/toc/student//address
				nfa = 51
				n = 3 
				b = 51
	
	if (n < count and n == 3 and b == 31):
		nfa = 0
		if (x[3][1] != "/" and x[3][1] != "*"): #/toc/student//name/text()
			y3 = x[3].split("/")
			if ("text()" == y3[1]):
				nfa = 32
				n = 4
			else:
				nfa = 0

	if (n < count and n == 3 and b == 41):
		nfa = 0
		if (x[3][1] != "/" and x[3][1] != "*"): #/toc/student//phone/text()
			y3 = x[3].split("/")
			if ("text()" == y3[1]):
				nfa = 42
				n = 4
			else:
				nfa = 0

	if (n < count and n == 3 and b == 51):
		nfa = 0
		if (x[3][1] != "/" and x[3][1] != "*"): #/toc/student//address/text()
			y3 = x[3].split("/")
			if ("text()" == y3[1]):
				nfa = 52
				n = 4
			else:
				nfa = 0	
		
	return nfa

txt = raw_input("Enter path expression\n")
name = ['sona', 'xyz']
phone = ['9999999999', '8888888888']
address = ['nepal', 'india']
answer= nfa(txt, name, phone, address)
print (answer)
if (answer == 33 or answer == 44 or answer == 55):
	print("The text you're searching for is found in the document.")
elif (answer == 1 or answer == 2 or answer == 3 or answer == 4 or answer == 5):
	print ("Valid path")
elif (answer == 11):
	print ("Valid path. Selecting all the elements of toc")
elif (answer == 21 ):
	print ("Valid path. Selecting all the elements of student")
elif (answer == 31 ):
	print ("Valid path. Selecting all the names")
elif (answer == 41 ):
	print ("Valid path. Selecting all the phone numbers")
elif (answer == 51 ):
	print ("Valid path. Selecting all the addresses")
elif (answer == 22):
	for i in range(len(name)):
		print (name[i], phone[i], address[i])
elif (answer == 32):
	for i in range(len(name)):
		print (name[i])
elif (answer == 42):
	for i in range(len(phone)):
		print (phone[i])
elif (answer == 52):
	for i in range(len(address)):
		print (address[i])
elif (answer == 222):
	print ("Valid path. Accessing all the child element nodes of TOC")
elif (answer == 2222):
	print (name[0], phone[0], address[0])
elif (answer == 2221):
	print (name[1], phone[1], address[1])
else:
	print("Reject")



