#This simulates rolling to hit in Warhammer 40,000
#Prompt the user how many dice are being rolled, and what the hit target is
#Roll the correct number of dice, then display the results
#This is a guided practice. Either follow with the video or your instructor will
#go over this in class.
#Video Link: https://youtu.be/89G5DN0-O3k

import random

random.seed()

print("Enter the number of dice and the hit target: ")

DiceCount = int(input("Number of dice: "))
HitTarget = int(input("Enter the hit target: "))

HitCount = 0
DiceRoll = 0

for i in range(DiceCount):
    DiceRoll = random.randint(1,6)
    #print(f"DiceRoll: {DiceRoll}")
    if DiceRoll >= HitTarget:
        HitCount += 1

print(f"You rolled {DiceCount} dice with a hit target of {HitTarget} and hit {HitCount} times.")