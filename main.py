import random
#strength
#intelligence
#dexterity
#wisdom
#charisma

points = 250

print("Welcome, adventruer! Skill point time! (250 points available)")

strength = int(input ("How strong are you? (0-100)\n>"))
if strength > 100 or strength < 0 or strength > points:
    print("You can't do that! You LOSE!")
    exit()
points = points - strength
print("Wow such stronk! STRENGHT SET TO " + str(strength))
print("You have " + str(points) + " skill points remaining.")

intelligence = int(input ("How intelligent are you? (0-100)\n>"))
if intelligence > 100 or intelligence < 0 or intelligence > points:
    print("You can't do that! You LOSE!")
    exit()
points = points - intelligence
print("Wow such smarts! INTELLIGENCE SET TO " + str(intelligence))
print("You have " + str(points) + " skill points remaining.")

speed = int(input ("How fast are you? (0-100)\n>"))
if speed > 100 or speed < 0 or speed > points:
    print("You can't do that! You LOSE!")
    exit()
points = points - speed
print("Wow such speed! Speed SET TO " + str(speed))
print("You have " + str(points) + " skill points remaining.")

problemSolving = int(input ("How good are you at problem solving? (0-100)\n>"))
if problemSolving > 100 or problemSolving < 0 or problemSolving > points:
    print("You can't do that! You LOSE!")
    exit()
points = points - problemSolving
print("Wow such problem solving! PROBLEM SOLVING SET TO " + str(problemSolving))
print("You have " + str(points) + " skill points remaining.")

magic = int(input ("How good are you at magic? (0-100)\n>"))
if magic > 100 or magic < 0 or magic > points:
    print("You can't do that! You LOSE!")
    exit()
points = points - magic
print("Wow such problem solving! PROBLEM SOLVING SET TO " + str(magic))
print("You have " + str(points) + " skill points remaining.")

#FIRST ENCOUNTER
print("You encounter a menacing wall. What do you want to do?")
print("1. puch wall")
print("2. reason with wall")
print("3. climb wall ")
print("4. magic wall")
choice = input(">")

if choice == "1":
    roll = random.randrange(0, strength)
    if roll > 20:
        print("The wall shaters in awe of your divine strength")

    else:
        print("Your fist shatters in awe of the wall's divine strength")
        exit()

elif choice == "2":
    roll = random.randrange(0, problemSolving)
    if roll < 10:
        print("Thanks to your reasioning skills the wall has decided to let you pass")

    else:
        print("You could not reason with wall")
        exit()

elif choice == "3":
    roll = random.randrange(0, strength)
    if roll > 30:
        print("You have climbed the wall with your crazy climbing skills")

    else:
        print("Your crazy climbing skills were not enough to conquer the wall")
        exit()

elif choice == "4":
    roll = random.randrange(0, magic)
    if roll > 20:
        print("Your soucery destroyed the wall")

    else:
        print("Your magic could not defeat the wall")
        exit()

else:
    print("You can't do that! You LOSE!")
    exit() 

#SECOND ENCOUNTER
print("You encounter a dragon. What do you want to do?")
print("1. fight the dragon")
print("2. talk it out with the dragon")
print("3. run ")
print("4. challenge the dragon to a game of chess")
choice = input(">")

if choice == "1":
    roll = random.randrange(0, strength)
    if roll > 30:
        print("Your massive muscles have defeated the dragon")

    else:
        print("The dragon destroyed you")
        exit()

elif choice == "2":
    roll = random.randrange(0, problemSolving)
    if roll > 25:
        print("You and the dragon worked out your problems and he is allowing you to continue your journey")

    else:
        print("The dragon was not willing to reason with you")
        exit()

elif choice == "3":
    roll = random.randrange(0, speed)
    if roll > 30:
        print("You have outrun the dragon with your mighty speed")

    else:
        print("The dragon caught you")
        exit()

elif choice == "4":
    roll = random.randrange(0, intelligence)
    if roll > 15:
        print("You are a chess master so the dragon let you go ")

    else:
        print("YOU LOST")
        exit()

else:
    print("You can't do that! You LOSE!")
    exit() 