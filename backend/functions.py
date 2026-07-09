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
print("Claim:",claim)
print("Status: AI Analysis Coming soon...")
goodbye()


   
    