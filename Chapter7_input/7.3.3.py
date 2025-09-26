reponses = {}

active = True

while active:
    name = input("\nWhat is your name? ")
    reponse = input("\nWhich mountain would you like to climb today? ")

    reponses[name] = reponse

    repeat = input("\nWould you like to continue (yes/no)? ")
    if repeat == "no":
        active = False


print("\n--- Poll Results ---")
for name, response in reponses.items():
    print(f"\n{name.title()} would like to 111climb {response.title()}")