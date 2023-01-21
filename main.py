whfile = open("whrandom.py")
exec(whfile.read())
whfile.close()

random = whrandom()

lives = 3
guess = -1
answer = random.randint(1, 10)

while lives > 0:
	print"You have " + str(lives) + " lives left"

	guess = int(input("? "))

	if guess > answer:
		print"Too high!"

	if guess < answer:
		print"Too low!"
	
	if guess == answer:
		print"You win!"
		break

	lives = lives - 1

if lives == 0:
	print"Game over! The answer was " + str(answer)