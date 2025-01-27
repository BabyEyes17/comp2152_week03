import random

# Lab 02 - Periodic Table Guessing Game

# Defining elements
elements = ["Hydrogen", "Helium",
            "Lithium", "Beryllium",
            "Boron", "Carbon",
            "Nitrogen", "Oxygen",
            "Fluorine", "Neon"]

# Defining extra element info
elementInfo = ["Hydrogen is the lightest element in the universe.",
               "Helium is commonly used in balloons.",
               "When on fire, Lithium cannot be extinguished by water.",
               "Beryllium Fact.",
               "Boron Fact.",
               "Carbon Fact.",
               "Nitrogen Fact.",
               "Oxygen Fact.",
               "Fluorine Fact.",
               "Neon Fact."]



# Random element selection
randomInt = random.randint(0, 9)
randomElement = elements[randomInt]
print("A random element has been chosen")



attempt = 0
attempts = 3
correct = False

while attempt < attempts and not correct:

    # Listing elements and asking user for input
    print("\nList Of Elements:", elements)
    userGuess = input(f"\nPlease enter your guess ({attempt + 1}/{attempts}): ")

    # Validating user input
    if not userGuess.isalpha():
        print("Error: You must enter a valid element.")

    else:

        if userGuess.lower().strip() == randomElement.lower():
            print(f"Correct! The element was {randomElement}!")
            print(f"You got it in {attempt + 1} tries!")
            correct = True

        else:
            attempt += 1

            if attempt < attempts:
                print(f"Hint: The element starts with \"{randomElement[0]}\"")

            else:
                print(f"Wrong! The correct element was {randomElement}!")

print("\n<<< Game Over >>>")



# Extra element info
print(f"\nDid you know?\n{elementInfo[randomInt]}")