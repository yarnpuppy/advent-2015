
accumulator = 0
counter = 0
with open("basic2.txt") as f:
	for line in f:
		l, w, h = line.split('x')
		#print (l,w,h)

		l = int(l)
		w = int (w)
		h = int (h)

		#print l
		#print w
		#print h

		list2= (l,w,h)
		#print list 

		list3 = sorted(list2)

		#print list3


		#what is surface area of one box?

		sabox1= 2*((l*w)+ (w*h) + (h*l))

	

		#print ('Surface area of box is', sabox1)

		#what is the smallest number in dimenisons


		smallestside= list3[0]
		nextsmallestside = list3[1]

		feetofribbon = smallestside + smallestside + nextsmallestside + nextsmallestside 

		feetofbow = l*w*h


		saslack = (smallestside * nextsmallestside)

		#print ('Surface area of slack is', saslack)


		sabox2 = sabox1 + saslack
		#print ('Total surface area is', sabox2)

		totalfeetofribbon= feetofribbon + feetofbow
	

		accumulator = accumulator + sabox2
		counter = counter + totalfeetofribbon
	print accumulator
	print counter


