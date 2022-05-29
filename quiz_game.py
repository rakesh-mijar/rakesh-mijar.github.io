print("Welcome to my quiz!!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0
answer = input("What does CPU stand for ? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print('Correct answer is: ',"Central processing unit")

answer = input("What does GPU stand for ? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print('Correct answer is: ',"Graphics processing unit")

answer = input("What does RAM stand for ? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print('Correct answer is: ',"random access memory")

answer = input("What does PSU stand for ? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print('Correct answer is: ',"Power supply unit")

answer = input("What does ROM stand for ? ")
if answer.lower() == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print('Correct answer is: ',"Read only memory")

print("You got " + str(score) + " questions correct!!")
print("You got " + str((score / 5) * 100) + "%.")
    
if score >= 4:
    print("HURRAY!!,Very good")
elif score == 3:
    print("Try hard and get 100%!!")
else:
    print("Better luck next time")
