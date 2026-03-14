# Our massive dictionary of epic Bopl Battle combos
combo_recommender = {
    "The Wrecking Ball": ["Push", "Rock", "Grappling Hook"],
    "The Balloon": ["Mine", "Gust", "Grappling Hook"],
    "Instant Destruction": ["Dash", "Dash", "Meteor"],
    "Map Eater": ["Growth Ray", "Black Hole", "Platform"],
    "Stealth Sniper": ["Smoke", "Time Stop", "Bow"],
    "The Rumbling": ["Growth Ray", "Revival", "Revival"],
    "Demon Core": ["Growth Ray", "Mine", "Duplicator"],
    "Quantum": ["Beam", "Invisibility", "Teleport"],
    "Apocalypse Survivor": ["Push", "Revival", "Teleport"],
    "Assassin": ["Bow", "Time Stop", "Grappling Hook"],
    "Black Hole Cannon": ["Black Hole", "Beam", "Smoke"],
    "Reverse the Polarity": ["Shrink Ray", "Black Hole", "Shrink Ray"],
    "Tele-Mines": ["Teleport", "Mine", "Dash"],
    "Where is the map???": ["Blink Gun", "Blink Gun", "Blink Gun"]
}

abilities = [
    "Beam", "Black Hole", "Blink Gun", "Bow", "Dash", "Drill", 
    "Duplicator", "Engine", "Grappling Hook", "Grenade", "Growth Ray", 
    "Gust", "Invisibility", "Magnet Gun", "Meteor", "Mine", "Missile", 
    "Platform", "Push", "Random", "Revival", "Rock", "Roll", "Shrink Ray", 
    "Smoke", "Spike", "Teleport", "Tesla Coil", "Throw", "Time Stop"
]

def power_match(power1, power2, power3):
    # Group the powers together into a list
    chosen_powers = [power1, power2, power3]
    
    # Loop through our dictionary to see if there is a match
    for combo_name, combo_powers in combo_recommender.items():
        # We sort them so the order the powers are entered doesn't matter!
        if sorted(chosen_powers) == sorted(combo_powers):
            return f"\nAwesome! You created the '{combo_name}' combo!"
            
    # If the loop finishes and finds nothing:
    return "\nNo known combo found for these powers. You might have invented a new one!\nor its just a bad combo ):"

def checkIfAbilityInAbilityList(ability):
    # Python's built-in way to check if an item is in a list
    if ability in abilities:
        return True
    print("please entr an ability wich is in the ability list")
    print(abilities)
    return False

def main():
    print("Give me Bopl powers combos and I'll tell you if it's good!")
    
    abilitie1 = input("enter ability 1: ")
    while not checkIfAbilityInAbilityList(abilitie1):
        print("ability" + abilitie1 + "doesn't exist. Check the ability list!")
        abilitie1 = input("enter ability 1: ")
        
    abilitie2 = input("enter ability 2: ")
    while not checkIfAbilityInAbilityList(abilitie2):
        print("ability" + abilitie2 + "doesn't exist. Check the ability list!")
        abilitie2 = input("enter ability 2: ")
        
    abilitie3 = input("enter ability 3: ")
    while not checkIfAbilityInAbilityList(abilitie3):
        print("ability" + abilitie3 + "doesn't exist. Check the ability list!")
        abilitie3 = input("enter ability 3: ")

    result = power_match(abilitie1, abilitie2, abilitie3)
    print(result)

if __name__ == "__main__":
    main()