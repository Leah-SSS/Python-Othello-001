board = {}
for x in range(11): 
    for y in range(11):  
        board[(x, y)] = f"・"
        
import random
import time

###>>>Prep. grid gen. function
def display_grid(dict, x, y):
    for x in range(x):
        rows = [str(dict[(x, y)]) for y in range(y)]
        print(" |".join(rows))

	
        
###>>>Prep. modify grid (key:value) value function
###>>>Variables: [grid = dictionary], [x,y = key], [value = key:value]
def update_cell(dict, x, y, value):
	if (x, y) in dict:
		dict[(x, y)] = value
	else:
		print(f"Cell ({x}, {y}) is out of bounds.")
			


###Function to check (a, b) is key in dictionary
def check(dict, a, b):
	if (a, b) in dict:
		print("\nKeyCheck: True")
		return True
	else:
		print("\nKeyChceck: False")
		return False
				
#Function to check all available co-ordinates. 
#Use to check input (x, y) co-ordinates
#If none, returns false. 
#If yes, capture co-ordinate into list, and return co-ordinate list.
def availableW(dict):
	avail = []
	for n in dict:
		if dict[(n[0], n[1])] == 2:
			tnr = [
				(n[0] + 1, n[1]), (n[0] - 1, n[1]), #Verticle
				(n[0], n[1] + 1), (n[0], n[1] - 1),  # Horizontal
				(n[0] + 1, n[1] + 1), (n[0] + 1, n[0] - 1), (n[0] - 1, n[1] + 1), (n[0] - 1, n[1] - 1)  # Diagonal
				]
			for m in tnr:
				if m in dict and dict[m] == 0:
					avail.append(m)
	if len(avail) >= 1:
		return avail
	else:
		return False

#Black available empty co-ordinates around white pieces
def availableB(dict):
	avail = []
	for n in dict:
		if dict[(n[0], n[1])] == 1:
			tnr = [
				(n[0] + 1, n[1]), (n[0] - 1, n[1]), #Verticle
				(n[0], n[1] + 1), (n[0], n[1] - 1),  # Horizontal
				(n[0] + 1, n[1] + 1), (n[0] + 1, n[0] - 1), (n[0] - 1, n[1] + 1), (n[0] - 1, n[1] - 1)  # Diagonal
				]
			for m in tnr:
				if m in dict and dict[m] == 0:
					avail.append(m)
	if len(avail) >= 1:
		return avail
	else:
		return False
			
###Function to check is any empty co-ordinates
#Use with while loop to determine whether game finish or ongoing
def game(dict):
	GameCheck = 0
	for n in dict:
		if dict[(n[0], n[1])] == 0:
			GameCheck = 1
	if GameCheck == 1:
		return False
	elif GameCheck == 0:
		return True
		
		
		
		
		
##Function to store flipping co-ordinates
#1. If the x+n co-ordinate is black, store in fliplist
#2. if x+n	is white and x+n - 1 is black, break for loo
#3. if x+n is empty, white or border, 
def flipstoreW(idDict, a, b, m):
	a = a + 1
	
	if m == 1:
		#fliplist is the check that determines output
		whitefliplist = []
	
		#templist is working store list
		templist = []
		###Check W-Line
		for n in range(11):
			##Shoudn't happen but if code finds invalid co-ordinate, break'
			if (a+n, b) not in idDict:
				break
			
			#Process for if a+n is white need 2 outcomes
			#1. if white at end of black sequence
			#2. if white not at end of black sequence
			elif idDict[(a+n, b)] == 1:
				if len(templist) >= 1:
					whitefliplist.append(templist)
				else:
					break
		
			#Process for if a+n is black
			elif idDict[(a+n, b)] == 2:
				templist.append((a+n, b))
				
			#Process for if a+n is either empty or border
			elif idDict[(a+n, b)] == 0:
				break
			elif idDict[(a+n, b)] == 3:
				break
				
		if len(whitefliplist) >= 1:
			return whitefliplist
		else:
			return False 
			
	
	
	elif m == 2:
		blackfliplist = []
		templist = []
		for n in range(11):
			if (a+n, b) not in idDict:
				break
			
			elif idDict[(a+n, b)] == 2:
				if len(templist) >= 1:
					blackfliplist.append(templist)
				else:
					break
	
			elif idDict[(a+n, b)] == 1:
				templist.append((a+n, b))
				
			elif idDict[(a+n, b)] == 0:
				break
			elif idDict[(a+n, b)] == 3:
				break
				
		if len(blackfliplist) >= 1:
			return blackfliplist
		else:
			return False 

	
	
		
						
def flipstoreSW(idDict, a, b, m):
	a = a + 1
	b = b - 1
	
	if m == 1:
		whitefliplist = []
		templist = []
		for n in range(11):
			if (a+n, b-n) not in idDict:
				break
			
			elif idDict[(a+n, b-n)] == 1:
				if len(templist) >= 1:
					whitefliplist.append(templist)
				else:
					break

			elif idDict[(a+n, b-n)] == 2:
				templist.append((a+n, b-n))
				
			elif idDict[(a+n, b-n)] == 0:
				break
			elif idDict[(a+n, b-n)] == 3:
				break
				
		if len(whitefliplist) >= 1:
			return whitefliplist
		else:
			return False 
	
	elif m == 2:
		blackfliplist = []
		templist = []
		for n in range(11):
			if (a+n, b-n) not in idDict:
				break
			
			elif idDict[(a+n, b-n)] == 2:
				if len(templist) >= 1:
					blackfliplist.append(templist)
				else:
					break

			elif idDict[(a+n, b-n)] == 1:
				templist.append((a+n, b-n))
				
			elif idDict[(a+n, b-n)] == 0:
				break
			elif idDict[(a+n, b-n)] == 3:
				break
				
		if len(blackfliplist) >= 1:
			return blackfliplist
		else:
			return False 
				

def flipstoreS(idDict, a, b, m):
	b = b - 1
	
	if m == 1:
		whitefliplist = []
		templist = []
		for n in range(11):
			if (a, b-n) not in idDict:
				break
			
			elif idDict[(a, b-n)] == 1:
				if len(templist) >= 1:
					whitefliplist.append(templist)
				else:
					break

			elif idDict[(a, b-n)] == 2:
				templist.append((a, b-n))
				
			elif idDict[(a, b-n)] == 0:
				break
			elif idDict[(a, b-n)] == 3:
				break
		
		if len(whitefliplist) >= 1:
			return whitefliplist
		else:
			return False 
			
	
	elif m == 2:
		blackfliplist = []
		templist = []
		for n in range(11):
			if (a, b-n) not in idDict:
				break
			
			elif idDict[(a, b-n)] == 2:
				if len(templist) >= 1:
					blackfliplist.append(templist)
				else:
					break

			elif idDict[(a, b-n)] == 1:
				templist.append((a, b-n))
				
			elif idDict[(a, b-n)] == 0:
				break
			elif idDict[(a, b-n)] == 3:
				break
		
		if len(blackfliplist) >= 1:
			return blackfliplist
		else:
			return False 
		
	


def flipstoreSE(idDict, a, b, m):
	a = a - 1
	b = b - 1
	
	if m == 1:
		whitefliplist = []
		templist = []
		for n in range(11):
			if (a-n, b-n) not in idDict:
				break
			
			elif idDict[(a-n, b-n)] == 1:
				if len(templist) >= 1:
					whitefliplist.append(templist)
				else:
					break

			elif idDict[(a-n, b-n)] == 2:
				templist.append((a-n, b-n))
				
			elif idDict[(a-n, b-n)] == 0:
				break
			elif idDict[(a-n, b-n)] == 3:
				break
		
		if len(whitefliplist) >= 1:
			return whitefliplist
		else:
			return False 
			
	
	elif m == 2:
		blackfliplist = []
		templist = []
		for n in range(11):
			if (a-n, b-n) not in idDict:
				break
			
			elif idDict[(a-n, b-n)] == 2:
				if len(templist) >= 1:
					blackfliplist.append(templist)
				else:
					break

			elif idDict[(a-n, b-n)] == 1:
				templist.append((a-n, b-n))
				
			elif idDict[(a-n, b-n)] == 0:
				break
			elif idDict[(a-n, b-n)] == 3:
				break
		
		if len(blackfliplist) >= 1:
			return blackfliplist
		else:
			return False 
	
	


#>
def flipstoreE(idDict, a, b, m):
	a = a - 1
	
	if m == 1:
		whitefliplist = []
		templist = []
		for n in range(11):
			if (a-n, b) not in idDict:
				break
			
			elif idDict[(a-n, b)] == 1:
				if len(templist) >= 1:
					whitefliplist.append(templist)
				else:
					break

			elif idDict[(a-n, b)] == 2:
				templist.append((a-n, b))
					
			elif idDict[(a-n, b)] == 0:
				break
			elif idDict[(a-n, b)] == 3:
				break
		
		if len(whitefliplist) >= 1:
			return whitefliplist
		else:
			return False 
	
	elif m == 2:
		blackfliplist = []
		templist = []
		for n in range(11):
			if (a-n, b) not in idDict:
				break
			
			elif idDict[(a-n, b)] == 2:
				if len(templist) >= 1:
					blackfliplist.append(templist)
				else:
					break

			elif idDict[(a-n, b)] == 1:
				templist.append((a-n, b))
				
			elif idDict[(a-n, b)] == 0:
				break
			elif idDict[(a-n, b)] == 3:
				break
				
		if len(blackfliplist) >= 1:
			return blackfliplist
		else:
			return False 


def flipstoreNE(idDict, a, b, m):
	a = a - 1
	b = b + 1
	
	if m == 1:
		whitefliplist = []
		templist = []
		for n in range(11):
			if (a-n, b+n) not in idDict:
				break
			
			elif idDict[(a-n, b+n)] == 1:
				if len(templist) >= 1:
					whitefliplist.append(templist)
				else:
					break

			elif idDict[(a-n, b+n)] == 2:
				templist.append((a-n, b+n))
				
			elif idDict[(a-n, b+n)] == 0:
				break
			elif idDict[(a-n, b+n)] == 3:
				break
		
		if len(whitefliplist) >= 1:
			return whitefliplist
		else:
			return False 
	
	elif m == 2:		
		blackfliplist = []
		templist = []
		for n in range(11):
			if (a-n, b+n) not in idDict:
				break
			
			elif idDict[(a-n, b+n)] == 2:
				if len(templist) >= 1:
					blackfliplist.append(templist)
				else:
					break

			elif idDict[(a-n, b+n)] == 1:
				templist.append((a-n, b+n))
				
			elif idDict[(a-n, b+n)] == 0:
				break
			elif idDict[(a-n, b+n)] == 3:
				break
		
		if len(blackfliplist) >= 1:
			return blackfliplist
		else:
			return False 
	



def flipstoreN(idDict, a, b, m):
	b = b + 1
	
	if m == 1:
		whitefliplist = []
		templist = []
		for n in range(11):
			if (a, b+n) not in idDict:
				break
			
			elif idDict[(a, b+n)] == 1:
				if len(templist) >= 1:
					whitefliplist.append(templist)
				else:
					break

			elif idDict[(a, b+n)] == 2:
				templist.append((a, b+n))
				
			elif idDict[(a, b+n)] == 0:
				break
			elif idDict[(a, b+n)] == 3:
				break
		
		if len(whitefliplist) >= 1:
			return whitefliplist
		else:
			return False 
	
	elif m == 2:
		blackfliplist = []
		templist = []
		for n in range(11):
			if (a, b+n) not in idDict:
				break
			
			elif idDict[(a, b+n)] == 2:
				if len(templist) >= 1:
					blackfliplist.append(templist)
				else:
					break

			elif idDict[(a, b+n)] == 1:
				templist.append((a, b+n))
				
			elif idDict[(a, b+n)] == 0:
				break
			elif idDict[(a, b+n)] == 3:
				break
		
		if len(blackfliplist) >= 1:
			return blackfliplist
		else:
			return False 
			
		
	


def flipstoreNW(idDict, a, b, m):
	a = a + 1
	b = b + 1
	
	###white
	if m == 1:
		whitefliplist = []
		templist = []
		for n in range(11):
			if (a+n, b+n) not in idDict:
				break
			
			elif idDict[(a+n, b+n)] == 1:
				if len(templist) >= 1:
					whitefliplist.append(templist)
				else:
					break

			elif idDict[(a+n, b+n)] == 2:
				templist.append((a, b+n))
				
			elif idDict[(a+n, b+n)] == 0:
				break
			elif idDict[(a+n, b+n)] == 3:
				break
				
		if len(whitefliplist) >= 1:
			return whitefliplist
		else:
			return False 
	
	###black
	if m == 2:
		blackfliplist = []
		templist = []
		for n in range(11):
			if (a+n, b+n) not in idDict:
				break
			
			elif idDict[(a+n, b+n)] == 2:
				if len(templist) >= 1:
					blackfliplist.append(templist)
				else:
					break

			elif idDict[(a+n, b+n)] == 1:
				templist.append((a, b+n))
				
			elif idDict[(a+n, b+n)] == 0:
				break
			elif idDict[(a+n, b+n)] == 3:
				break
				
		if len(blackfliplist) >= 1:
			return blackfliplist
		else:
			return False
	
	###if player1 turn(1), return the whitelist, if com turn(2), return blacklist



###Compile fliplists
def allflipstore(idDict, a, b, m):
	if m == 1:
		whiteallfliplist = []
		
		if flipstoreN(idDict, a, b, 1) == False:
			pass
		else:
			WhiteN = flipstoreN(idDict, a, b, 1)
			whiteallfliplist.extend(WhiteN)
	 
		if flipstoreNW(idDict, a, b, 1) == False:
			pass
		else:
			WhiteNW = flipstoreNW(idDict, a, b, 1)
			whiteallfliplist.extend(WhiteNW)
			
	
		if flipstoreW(idDict, a, b, 1) == False:
			pass
		else:
			WhiteW = flipstoreW(idDict, a, b, 1)
			whiteallfliplist.extend(WhiteW)
			
		if flipstoreSW(idDict, a, b, 1) == False:
			pass
		else:
			WhiteSW = flipstoreSW(idDict, a, b, 1)
			whiteallfliplist.extend(WhiteSW)
			
		if flipstoreS(idDict, a, b, 1) == False:
			pass
		else:
			WhiteS = flipstoreS(idDict, a, b, 1)
			whiteallfliplist.extend(WhiteS)
		
		if flipstoreSE(idDict, a, b, 1) == False:
			pass
		else:
			WhiteSE = flipstoreSE(idDict, a, b, 1)
			whiteallfliplist.extend(WhiteSE)
			
		if flipstoreE(idDict, a, b, 1) == False:
			pass
		else:
			WhiteE = flipstoreE(idDict, a, b, 1)
			whiteallfliplist.extend(WhiteE)
		
		if flipstoreNE(idDict, a, b, 1) == False:
			pass
		else:
			WhiteNE = flipstoreNE(idDict, a, b, 1)
			whiteallfliplist.extend(WhiteNE)
		
		if len(whiteallfliplist) >= 1:
			return whiteallfliplist
		else:
			return False
			
	elif m == 2:
		blackallfliplist = []
		
		if flipstoreN(idDict, a, b, 2) == False:
			pass
		else:
			BlackN = flipstoreN(idDict, a, b, 2)
			blackallfliplist.extend(BlackN)
		
		if flipstoreNW(idDict, a, b, 2) == False:
			pass
		else:
			BlackNW = flipstoreNW(idDict, a, b, 2)
			blackallfliplist.extend(BlackNW)
		
		if flipstoreW(idDict, a, b, 2) == False:
			pass
		else:
			BlackW = flipstoreW(idDict, a, b, 2)
			blackallfliplist.extend(BlackW)
			
		if flipstoreSW(idDict, a, b, 2) == False:
			pass
		else:
			BlackSW = flipstoreSW(idDict, a, b, 2)
			blackallfliplist.extend(BlackSW)
			
		if flipstoreS(idDict, a, b, 2) == False:
			pass
		else:
			BlackS = flipstoreS(idDict, a, b, 2)
			blackallfliplist.extend(BlackS)
		
		if flipstoreSE(idDict, a, b, 2) == False:
			pass
		else:
			BlackSE = flipstoreSE(idDict, a, b, 2)
			blackallfliplist.extend(BlackSE)
						
		if flipstoreE(idDict, a, b, 2) == False:
			pass
		else:
			BlackE = flipstoreE(idDict, a, b, 2)
			blackallfliplist.extend(BlackE)
		
		if flipstoreNE(idDict, a, b, 2) == False:
			pass
		else:
			BlackNE = flipstoreNE(idDict, a, b, 2)
			blackallfliplist.extend(BlackNE)
		
		if len(blackallfliplist) >= 1:
			return blackallfliplist
		else:
			return False
		

##Function to flip action stored flipping co-ordinates
def flipactionW(idDict, fliplist, display): 
	#in list, get first 
	for coord in fliplist:
		for n in coord:
			idDict[(n[0], n[1])] = 1
			display[(n[0], n[1])] = '🐦‍'

##########^^^^^Finish All flipfunction - white
##########>>>>>Start All flipfunction - black 




def flipactionB(idDict, fliplist, display):
	for coord in fliplist:
		for n in coord:
			idDict[(n[0], n[1])] = 2
			display[(n[0], n[1])] = '🐦‍⬛'
		







	
				###>>>AXIS labeling
for y in range (11):
	board[(0, y)] = f"{y}X"
	 
for x in range(11):
	board[(x, 0)] = f"{x}Y"
for y in range(1):
	board[(0,y)] = f"XY"

		
hb = {}
for x in range(12): 
    for y in range(12):  
        hb[(x, y)] = 0

###>>> Giving boarder id=3
for y in range(12):  
	hb[(0, y)] = 3
	hb[(11, y)] = 3
for x in range(12):
	hb[(x, 0)] = 3	
	hb[(x, 11)] = 3

###>>> starting co-ordinate
for x in range(11):
	hb[(5, 6)] = 1
	hb[(6, 5)] = 1
	hb[(5, 5)] = 2
	hb[(6, 6)] = 2


###>>> Give display id=1'白' id=2'黒'
for x in range(11):
	for y in range(11):
		if hb[(x, y)] == 1:
			update_cell(board, x, y, '🐦‍')
		elif hb[(x, y)] == 2:
			update_cell(board, x, y, '🐦‍⬛')

white = 0
black = 0

print("\n")
display_grid(board, 11, 11)

print("\n")
display_grid(hb, 12, 12)

screen = "__________________"








print(screen * 5)
print("\n\nThis is Othello!")
print("Your goal is to as many spaces as possible.")
print("You are white, and you get to go first.")


			
###Game Start
while game(hb) == False:
	forfeit = 0
	print("\n New Turn! ")
	###avail gets empty around enermy.
	###allflipstore == false, condition to removes invalid empty
	###so if avail == false: pass
	###elif, allflipstore == false to remove.
	###if allflipstore == empty: pass
	###else continue game

	#
	###>>>>White's Code'
	###IF condition1: availablity
	if availableW(hb) == False:
		print("\nOh no! There are not available places you can choose...")
		print("It will be Black's turn'")
		forefeit += 1
		pass
	else:
		WhitePossible = availableW(hb)
	###Checks if co-ordinates have valid flip sequences. If not, removes from sequence.
		for n in WhitePossible[:]:
			if allflipstore(hb, n[0], n[1], 1) == False:
				WhitePossible.remove(n)
			else:
				pass
		
		###IF condition2: possiblity
		if len(WhitePossible) == 0:
			print("\nOh no! There are not available places you can choose...")
			print("It will be Black's turn'")
			forfeit += 1
			pass
		else:
			###Starts input
			print("\n Its your Turn! \nThese are available co-ordinates: \n" , WhitePossible, "\n Please choose a co-ordinate in the list.")	
			px = 0 
			py = 0 
			while (px, py) not in WhitePossible:
				px = input("\nChoose a X-Coordinate of an available (x, y): ")
				try:
					px = int(px)
				except:
					px = 0
						
				py = input("Choose a Y-Coordinate of an available (x, y: ")
				try:
					py = int(py)
				except:
					py = 0
	

			print("\n You chose: ", (px, py))
			###This updates chosen co-ordinates
			update_cell(hb, px, py, 1)
			update_cell(board, px, py, '🐦‍')

			###This retrieves all black co-ordinates to flip
			whiteflipper = allflipstore(hb, px, py, 1)
			
			print("\n Calculating flips...")
			time.sleep(2)
	
			###This flips all co-ordinates in whiteflipper
			flipactionW(hb, whiteflipper, board)
	
			display_grid(board, 11, 11)
			time.sleep(2)
	
	print("Now is Black's turn!")
	#IF condition1: availability
	if availableB(hb) == False:
		print("\nOh no! There are not available places for Black to choose...")
		print("It will be Your turn'")
		time.sleep(2)
		forefeit += 1
		pass
	
	else:	
		###BLacks turn, using randint.

		coblack = availableB(hb)
		for n in coblack[:]:
			if allflipstore(hb, n[0], n[1], 2) == False:
				coblack.remove(n)
			else:
				pass
		#If condition2: possiblity
		if len(coblack) == 0:
			print("\nOh no! There are not available places for Black to choose...")
			print("It will be Your turn'")
			time.sleep(2)
			forefeit += 1
			pass
		
		else:
			ranblack = len(coblack)
			choiceblack = random.randint(0, ranblack - 1)
			qx = coblack[choiceblack][0]
			qy = coblack[choiceblack][1]
	
			print("\n Black player chose co-ordinate: ", (qx, qy))
			print("\n Calculating flips...")
			time.sleep(2)
	
			update_cell(hb, qx, qy, 2)
			update_cell(board, qx, qy, '🐦‍⬛' )
			blackflipper = allflipstore(hb, qx, qy, 2)
	
			flipactionB(hb, blackflipper, board)
	
	
			display_grid(board, 11, 11)
	
	###>>> This is counting [白:黒] score
	WScore = 0
	BScore = 0
 
	for key, value in board.items():
			if value == '🐦‍':
				WScore += 1
			elif value == '🐦‍⬛':
				BScore += 1
	time.sleep(2)
	print("\n These are the current scores: \nWhite Points: ", WScore, "\nBlack Points: ", BScore)
	
	time.sleep(2)
	if forfeit == 2:
		break
	else:
		forfeit == 0

time.sleep(2)
print("\n\nThats the end of the Game!")
print("\nLets see who won!")
time.sleep(2)

print("\n These are the final scores: \nWhite Points: ", WScore, "\nBlack Points: ", BScore)
time.sleep(2)
if WScore > BScore:
	print("You Won!")

elif WScore < BScore:
	print("You lost...")
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		
			
