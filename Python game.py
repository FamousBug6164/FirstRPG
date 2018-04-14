from random import*
import random, math

def changelog():
    print("")
    print("The current version is 1.1")
    print("1.0 Introduced the game,")
    print("""1.1 Introduced health. Changed certain scripts. Added some art.
    Also added an extra enemy to fight, The Boss!""")
    print("")

def copyright():
    print("""
IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
IOI   _____                       _       _     _    IOI
IOI  / ____|                     (_)     | |   | |   IOI
IOI | |     ___  _ __  _   _ _ __ _  __ _| |__ | |_  IOI
IOI | |    / _ \| '_ \| | | | '__| |/ _` | '_ \| __| IOI
IOI | |___| (_) | |_) | |_| | |  | | (_| | | | | |_  IOI
IOI  \_____\___/| .__/ \__, |_|  |_|\__, |_| |_|\__| IOI
IOI            | |     __/ |        __/ |            IOI
IOI            |_|    |___/        |___/             IOI
IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
IIIII                                              IIIII
IIIII             Copyright 2018 ©                 IIIII
IIIII                                              IIIII
IIIII               Bugged Co. ©                   IIIII
IIIII                                              IIIII
IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
""")

    
def victory():
    redo = int(input("You win, would you like to play again, 1 for yes, 2 for no. "))
    if redo == 2:
        leaveGame()
    if redo == 1:
        explore()
    if redo < 1 or redo > 2:
        leavegame()

def loss():
    redo = int(input("You died, but would you like to be ressurected, 1 for yes, 2 for no. "))
    if redo == 2:
        leavegame()
    if redo == 1:
        explore()
    if redo < 1 or redo > 2:
        leavegame()

def draw():
    print("You didn't do anything. ")
    redo = int(input("Would you like to carry on, 1 for yes, 2 for no. "))
    if redo == 2:
        leavegame()
    if redo == 1:
        explore()
    if redo < 1 or redo > 2:
        leavegame()


def leaveGame():
    print("Come back anytime.")
    input("Press enter to quit.")

def run():
    runningAway = random.randint(1,2)
    if runningAway == 1:
        print("You escaped, barely. You have to leave!")
        runningAnswer = int(input("Would you like to continue on your adventure. 1 for yes, 2 for no. "))
        if runningAnswer == 1:
            explore()
        elif runningAnswer == 2:
            leaveGame()
        else:
            leaveGame()
    if runningAway == 2:
        print("You died while running.")
        input("Press enter to leave the game.")

def skeleton():
    skeletonHealth = random.randint(1,20)
    skeletonAttack = random.randint(1,6)
    skeletonDefence = random.randint(1,1)
    print("You encountered a skeleton!")
    print("It has", skeletonHealth,"health")
    print("It has", skeletonAttack,"attack")
    print("It has", skeletonDefence,"defence")
    skeletonFight = int(input("Would you like to fight, 1 for yes, 2 to run. "))
    if skeletonFight > 2 or skeletonFight < 1:
        leaveGame()
    if skeletonFight == 2:
        run()
    if skeletonFight == 1:
        fightType = int(input("What do you want to do, 1 to attack or 2 to defend. "))
        if fightType > 2 or fightType < 1:
            leaveGame()
        if fightType == 1:
            if attack > skeletonDefence:
                damage = attack - skeletonDefence
                while skeletonHealth > 0:
                    skeletonHealth = skeletonHealth - damage
                    print("The skeleton has", skeletonHealth,"health left.")
                if skeletonHealth <= 0:
                    victory()
            elif attack == skeletonDefence:
                draw()
            else:
                loss()
        if fightType == 2:
            if defence > skeletonAttack:
                damage = defence - skeletonAttack
                while skeletonHealth > 0:
                    skeletonHealth = skeletonHealth - damage
                    print("The skeleton has", skeletonHealth,"health left.")
                if skeletonHealth <= 0:
                    victory
            elif defence == skeletonAttack:
                draw()
            else:
                loss()
            
def goblin():
    goblinHealth = random.randint(1,20)
    goblinAttack = random.randint(1,6)
    goblinDefence = random.randint(1,6)
    print("You encountered a goblin!")
    print("It has", goblinHealth,"health")
    print("It has", goblinAttack,"attack")
    print("It has", goblinDefence,"defence")
    goblinFight = int(input("Would you like to fight, 1 for yes, 2 to run. "))
    if goblinFight == 2:
        run()
    if goblinFight == 1:
        fightType = int(input("What do you want to do, 1 to attack or 2 to defend. "))
        if fightType == 1:
            if attack > goblinDefence:
                damage = attack - goblinDefence
                while goblinHealth > 0:
                    goblinHealth = goblinHealth - damage
                    print("The goblin has", goblinHealth,"health left.")
                if goblinHealth <= 0:
                    victory()
            elif attack == goblinDefence:
                draw()
            else:
                loss()
        if fightType == 2:
            if defence > goblinAttack:
                damage = defence - goblinAttack
                while goblinHealth > 0:
                    goblinHealth = goblinHealth - damage
                    print("The goblin has", goblinHealth,"health left.")
                if goblinHealth <= 0:
                    victory()
            elif defence == goblinAttack:
                draw()
            else:
                loss()
    else:
        leaveGame()

def boss():
    bossHealth = random.randint(1,30)
    bossAttack = random.randint(1,8)
    bossDefence = random.randint(1,8)
    print("You encountered the boss!")
    print("It has", bossHealth,"health")
    print("It has", bossAttack,"attack")
    print("It has", bossDefence,"defence")
    bossFight = int(input("Would you like to fight, 1 for yes, 2 to run. "))
    if bossFight == 2:
        run()
    if bossFight == 1:
        fightType = int(input("What do you want to do, 1 to attack or 2 to defend. "))
        if fightType == 1:
            if attack > bossDefence:
                damage = attack - bossDefence
                while bossHealth > 0:
                    bossHealth = bossHealth - damage
                    print("The boss has", bossHealth,"health left.")
                if bossHealth <= 0:
                    victory()
            elif attack == bossHealth:
                draw()
            else:
                loss()
        if fightType == 2:
            if defence > bossAttack:
                damage = defence - bossAttack
                while goblinHealth > 0:
                    bossHealth = bossHealth - damage
                    print("The goblin has", bossHealth,"health left.")
                if bossHealth <= 0:
                    victory()
            elif defence == bossHealth:
                draw()
            else:
                loss()
    else:
        leaveGame()


def explore():
    enemy = random.randint(1,3)
    if enemy == 1:
        skeleton()
    if enemy == 2:
        goblin()
    if enemy == 3:
        boss()

copyright()
changelog()

name = input("Hello adventurer, I am the grand wizard, ehhh, I cant remember your name, could you tell me please ")
print("""So""", name,"""the classes are:""")
print("")
print("Warrior, high attack, low defence,")
print("")
print("Guardian, low attack, high defence,")
print("")
print("Mage, medium attack, medium defence,")
print("")
print("Enter 1 for warrior, 2 for guardian and 3 for mage.")

playerClass = int(input("So, what class are you? "))

if playerClass == 1:
    health = 20
    attack = 5
    defence = 3

if playerClass == 2:
    attack = 3
    defence = 5

if playerClass == 3:
    attack = 3
    defence = 3

print("Your attack is", attack,"")
print("Your defence is", defence,"")

answer = int(input("Would you like to go exploring? 1 for yes, 2 for no. "))

if answer == 2:
    leaveGame()
elif answer == 1:
    explore()
else:
    leavegame()



