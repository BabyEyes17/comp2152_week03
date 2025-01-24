import random

# Dice options created using list() and range()
diceOptions = list(range(1, 7))

# Weapons list
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

print("Available weapons are:", ', '.join(weapons))

def getCombatStrength(prompt):

    while True:

        value = int(input(prompt))

        if 1 <= value <= 6:
            return value

        else:
            print("Invalid input. Please enter a number between 1-6.")

# Prompting user for Player and Monster combat strength input
playerCombatStrength = getCombatStrength("Please enter a number between 1-6 for Player: ")
monsterCombatStrength = getCombatStrength("Please enter a number between 1-6 for Monster: ")

for j in range(1, 21, 2):
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

    heroWeapon = weapons[heroRoll - 1]
    monsterWeapon = weapons[monsterRoll - 1]

    heroTotal = playerCombatStrength + heroRoll
    monsterTotal = monsterCombatStrength + monsterRoll

    print(f"\nBattle {j}")
    print(f"Hero rolled {heroRoll}, Monster rolled {monsterRoll}")
    print(f"Hero selected {heroWeapon}, Monster selected {monsterWeapon}")
    print(f"Hero total was {heroTotal}, Monster total was {monsterTotal}")

    if heroTotal > monsterTotal:
        print("Player wins!")

    elif heroTotal < monsterTotal:
        print("Monster wins!")

    else:
        print("It's a tie!")

if j != 11:
    print("\nBattle concluded after 20 rounds.")