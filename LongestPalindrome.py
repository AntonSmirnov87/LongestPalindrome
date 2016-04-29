def main():
	print("This will find the longest palindrome in a line of text.\n")
	inpCap = ignore_question("Do you want to ignore capitalization? (y/n) ")
	inpSpa = ignore_question("Do you want to ignore spaces? (y/n) ")
	inpStr = input("Enter a line of text: ")
	longestPalindrome = longest_palindrome(inpStr, inpCap, inpSpa)
	if(longestPalindrome[0] > 1):
		print("\nThe longest palindrome is " + str(longestPalindrome[0]) + " characters long.")
		print("\nThe longest palindromes include:\n")
	print(longestPalindrome[1])
	print("\n\n\n")
	main()

def longest_palindrome(inpStr, inpCap, inpSpa):
	iniStr = inpStr
	if not(inpCap):
		iniStr = iniStr.upper()
		print(iniStr)
	if not(inpSpa):
		iniStr = iniStr.replace(" ", "")
	print("Processing """ + iniStr + "")
	worStr = ""
	for char in iniStr:
		worStr += char + "#"
	strLen = len(worStr)
	curPal = 1
	maxPal = 1
	palindromes = ["There are no palindromes in this line of text."]

	for center in range (1, strLen - 2):
		isBetweenChars = 1 if (center % 2) else 2
		maxPosLen = min(center, strLen - center)
		if(center < strLen / 2):
			maxPosLen += 1
		for edge in range(isBetweenChars, maxPosLen, 2):
			if(worStr[center - edge] == worStr[center + edge]):
				curPal = edge + 1
				if(maxPal > 1 and curPal == maxPal):
					palindromes.append(iniStr[int((center-edge)/2):int((center+edge)/2)+1])
				elif(curPal > maxPal):
					palindromes = [iniStr[int((center-edge)/2):int((center+edge)/2)+1]]
					maxPal = curPal
			else:
				break		

		curPal = 1

	return(maxPal, palindromes)

def ignore_question(question):
	while(True):
		answer = input(question).lower().strip()[0]
		if(answer == "y"):
			return(False)
		elif(answer == "n"):
			return(True)
		else:
			print("Please type ""Yes"" or ""No""")

if __name__ == "__main__":
	main()
	exit()
