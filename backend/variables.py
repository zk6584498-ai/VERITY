app_name = "Verity"
tagline = "Evidence Over Influence"

print("===================================")
print(f"        Welcome to {app_name} 🚀")
print(f"      {tagline}       ")
print("===================================")

user_name = input("Enter your name: ")
print("Hello,", user_name)
print("Welcome to Verity!")
print()
print("What would you like to analyze today?")
print("1. Gym💪")
print("2. Nutrition🥗")
print("3. Skincare🌟")

choice = input("Enter your choice (1-3): ")

print()
if choice == "1":
    print("You chose Gym💪. Let's analyze your workout routine!")
    claim = input("Please enter your fitness claim: ")
    print()
    print("Analyzing your claim:")
    print("claim", claim)
    print("Status: AI Analysis Coming Soon!")
elif choice == "2":
    print("You chose Nutrition🥗. Let's analyze your diet!")
    claim = input("Please enter your nutrition claim: ")
    print()
    print("Analyzing your claim:")
    print("claim", claim)
    print("Status: AI Analysis Coming Soon!")
elif choice == "3":
    print("You chose Skincare🌟. Let's analyze your skincare routine!")
    claim = input("Please enter your skincare claim: ")
    print()
    print("Analyzing your claim:")
    print("claim", claim)
    print("Status: AI Analysis Coming Soon!")