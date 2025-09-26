Pro_active = True
prompt1 = "What is your name?\n"
prompt2 = "If you could visit one place in the would,where would you go?\n"
prompt3 = "\nWould you like to continue (yes/no)?"
Dic = {

}


while Pro_active:

    Name = input(prompt1)
    Place = input(prompt2)
    Dic[Name] = Place

    repeat = input(prompt3)
    if repeat == "no":
        Pro_active = False


print("--- Results ---")
for Name, Place in Dic.items():
    print(f"{Name} want to visit {Place}")