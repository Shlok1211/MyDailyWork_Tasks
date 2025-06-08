print("WELCOME TO QUIZ GAME -")
print("Choose from Options - A,B,C and D\n")

score = 0

print("1) What is the capital of India?")
print("A. Mumbai\nB. Delhi\nC. Kolkata\nD. Chennai")
ans = input("Your answer: ").upper()
if ans == "B":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer is B. Delhi\n")

print("2) What does CPU stand for?")
print("A. Central Process Unit\nB. Central Processing Unit\nC. Computer Personal Unit\nD. Control Processing Unit")
ans = input("Your answer: ").upper()
if ans == "B":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer is B. Central Processing Unit\n")

print("3) Which planet is known as the Red Planet?")
print("A. Earth\nB. Venus\nC. Mars\nD. Jupiter")
ans = input("Your answer: ").upper()
if ans == "C":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer is C. Mars\n")

print(f"You scored {score}")
if score == 3:
    print("Excellent!")
elif score == 2:
    print("Good job!")
else:
    print("Try again!")

playagain = input("Do you want to play again (y/n)? ").lower()

if playagain == "y":
    print("Restart the Code !!")
else:
    print("Thank you for playing!\n")
