name = input("what is your name?")
print "hi " + name
skill = input("would you like to use magic or a weapon?")
if skill == "magic":
    print ("you obtained a wand!")
if skill == "weapon":
    print ("you obtained a sword!")
print("the forest is to your left and a mountain to your right.")
dest = input("do you go left or right?")
if dest == "left":
    print ("you go into the forest.")
if dest == "right":
    print ("you go to the mountain.")
print("a low level monster attacks you!")
choice = input("do you attack or flee?")
if choice == "attack":
    print("the monster is defeated!")
if choice == "flee":
    print ("you got away.")

alive = True
while alive == True:
    if dest == "left":
        print ("you go further into the forest.")
        print ("you see a small house.")
        greet = input("do you go in?")
        if greet == "yes":
            print("a witch is inside! she locks you inside her cellar.")
            fate = input("do you try to get out?")
            if fate == "no":
                print ("you never escape from the cellar and die from starvation.")
                break
            if fate == "yes":
                print ("the witch attacks you!")
                choice = input("do you attack or flee?")
                if choice == "flee":
                    print ("you go back into the cellar.")
                    print ("you never escape from the cellar and die from starvation.")
                    break
                if choice == "attack":
                    if skill == "magic":
                        print("the witch is still able to fight!")
                        battle = input("do you continue fighting?")
                        if battle == "yes":
                            print ("the witch is defeated! you escape from her cellar.")
                            print ("you obtained a lot of gold!")
                            if battle == "no":
                                print ("you go back into the cellar.")
                                print ("you never escape from the cellar and die from starvation.")
                                break
                    home = input("do you want to go home?")
                    if home == "yes":
                        print ("on the way home, the forest boss finds you and kills you.")
                        break
                    if home == "no":
                        print("you continue walking.")
                    if skill == "weapon":
                        print ("the witch is defeated! you escape from her cellar.")
                        print ("you obtained a lot of gold!")
                        home = input("do you want to go home?")
                        if home == "yes":
                            print ("on the way home, the forest boss finds you and kills you.")
                            break
                        if home == "no":
                            print("you continue walking.")
        if greet == "no":
            print("you continue walking.")
        print("the forest boss comes out of the ground before you!")
        forbos = input("do you fight or flee?")
        if forbos == "flee":
            print("it caught you and ate you whole!")
            break
        if forbos == "fight":
            print("you attacked the forest boss!")
            print("the forest boss is still able to fight!")
            forebos = input("do you continue fighting?")
            if forebos == "yes":
                print("the forest boss attacks you and you pass out.")
                print("it cooks you over a fire and eats you!")
                break
            if forebos == "no":
                print("it caught you and ate you whole!")
                break

    if dest == "right":
        print ("you go up the mountain.")
        print ("you see a cave.")
        faate = input("do you go in?")
        if faate == "yes":
            print("there is a yeti sleeping inside.")
            yeti = input("do you wake up the yeti?")
            if yeti == "yes":
                print("the yeti attacks you!")
                batttle = input("do you fight or flee?")
                if batttle == "flee":
                    print("the yeti steps on you.")
                    break
                if batttle == "fight":
                    if skill == "magic":
                        print("the yeti is defeated!")
                        print("you obtained a lot of gold!")
                        homee = input("do you want to go home?")
                        if homee == "yes":
                            print("on the way home, the mountain boss finds you and kills you.")
                            break
                        if homee == "no":
                            print ("you continue up the mountain.")
                    if skill == "weapon":
                        print ("the yeti is still able to fight!")
                        baatttle = input("do you continue fighting?")
                        if baatttle == "yes":
                            print ("you defeated the yeti!")
                            print ("you obtained a lot of gold!")
                            hoome = input("do you want to go home?")
                            if hoome == "yes" or "y":
                                print("on the way home, the mountain boss swoops down and picks you up.")
                                print("it eats you whole!")
                                break
                            if hoome == "no" or "n":
                                print ("you continue going up the mountain.")
                        if baatttle == "no":
                            print ("the yeti caught you!")
                            print ("he eats you alive")
                            break
            if yeti == "no":
                print ("you exit the cave and continue going up the mountain.")
        if faate == "no":
            print("you continue going up the mountain.")
        print("the mountain boss comes flying towards you!")
        mobo = input("do you fight or flee?")
        if mobo == "flee":
            print ("it swooped down and grabbed you!")
            print("it tosses you into its mouth!")
            break
        if mobo == "fight":
            print("you attacked the mountain boss!")
            print("the mountain boss is still able to fight.")
            moubo = input("do you continue to fight?")
            if moubo == "yes":
                print ("the mountain boss attacks you!")
                print ("you faint from lack of oxygen!")
                print ("you get ripped to shreds by the mountain boss.")
                break
            if moubo == "no":
                print ("it swooped down and grabbed you!")
                print("it tosses you into its mouth!")
                break

print (name + " died! game over.")
