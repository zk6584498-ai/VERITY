def welcome():
    print("====================================")
    print("      Welcome to Verity 🚀")
    print("      Evidence Over Influence       ")
    print("====================================")

welcome()

print()

print("Hello Zuhair!")

welcome()

def goodbye():
   
    print("====================================")
    print("      Thank you for using Verity❤️   ")
    print("      See you soon!                ")
    print("====================================")


def get_name():

    name = input("Enter your name: ")
    return name
def show_menu():
    print()
    print("What would you like to analyze today?")
    print("1. Gym💪")
    print("2. Nutrition🥗")
    print("3. Skincare🌟")
    choice = input("Enter your choice (1-3): ")
    return choice

user_name = get_name()
choice = show_menu()

print()

if choice == "1":
    print(f"You have selected Gym💪 for analysis, {user_name}!")
elif choice == "2":
    print(f"You have selected Nutrition🥗 for analysis, {user_name}!")
elif choice == "3":
    print(f"You have selected Skincare🌟 for analysis, {user_name}!")
else:
    print("Invalid choice. Please select 1, 2, or 3.")
claim = input("\nEnter your claim...")

def analyze_claim(claim):

    print("\n===================================")
    print("        VERITY AI ANALYSIS         ")
    print("===================================")

    claim = claim.lower()
    
    if "protein" in claim  or "creatine" in claim :
        print("Category: Nutrition🥗")
        print("Result: Needs scientific evidence.")
        print("Confidence: 75%")

    elif "gym" in claim or "workout" in claim:
        print("Category:Fitness")
        print("Result: This claim may be true depending on the context.")
        print("Confidence: 70%")

    elif "skin" in claim or "facewash" in claim or "serum" in claim:
        print("Category: Skincare🌟")
        print("Result: Consult trusted dermatology sources.")
        print("Confidence: 72%")

    elif "height" in claim:
        print("Category: Fitness💪")
        print("Result: Gym does not stop height growth in healthy individuals.")
        print("Confidence: 88%")
    
    elif "water" in claim:
        print("Category: Health💧")
        print("Result: Staying hydrated supports overall health")
        print("Confidence: 95%")
        
    else:
        print("Category: Unknown")
        print("Result: No analysis available yet.")
        print("Confidence: 0%")

print("====================================")

analyze_claim(claim)
goodbye()

        