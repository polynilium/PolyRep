# Simple quiz game

print("Hi, welcome to my quiz")
print("try to get as many questions correct as possible")

totalQuestions = 4
score = 0

ans = input("1. What is 1 + 1?")

if ans.lower() == "2":
	print("Correct!")
	score += 1
else:
	print("Incorrect")


ans = input("2. What is 2 + 2?")

if ans == "4":
	print("Correct!")
	score += 1
else:
	print("Incorrect!")


ans = input("3. What is 3 + 3?")

if ans == "6":
	print("Correct!")
	score += 1
else:
	print("Incorrect!")

ans = input("4. What is 4 + 4?")

if ans == "8":
	print("Correct!")
	score += 1
else:
	print("Incorrect!")

print('Thank you for playing, you got', score, "questions correct!")

if score == 1:
	print("25%")
if score == 2:
	print("50%")
if score == 3:
	print("75%")
if score == 4:
	print("100%")