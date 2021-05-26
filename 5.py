names = []
ages = []

# 1. Read name and age using input(). Use .split()
# 2. Ask name, age to names, ages
# 3. Ask user whether he/she wants to input one more user

while True:
    user_data = input("Enter name, age separated by comma:").split(",")
    names.append(user_data[0])
    ages.append(int(user_data[1]))

status = input("One more? Press Y to continue. Otherwise press N:")
if status == "N":
    break

for idx, val in enumerate(names):
    print(f"User {idx}: {val}, {ages[idx]}")