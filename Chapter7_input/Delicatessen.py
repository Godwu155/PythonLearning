sandwich_orders = ['American Sandwich','BLT Sandwich','Bologna Sandwich','Cheese Sandwich','pastrami','pastrami','pastrami']
finished_sandwithes = []

"""
for sandwich in sandwich_orders:
    print(f"I made your {sandwich}")
    finished_sandwithes.append(sandwich)
    sandwich_orders.remove(sandwich)

    if len(sandwich_orders) < 0:
        break
        print(f"Your sandwithed is finished!"+"Ther are ")
        for sandwich__ in finished_sandwithes:
            print(sandwich__)
            break
"""
# if sandwich == []:
print("pastrami has sold out!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')



while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwithes.append(sandwich)
    print(f"Your {sandwich} is finished!")

    if len(sandwich_orders) < 1:
        print(f" finished.")
        for sandwich in finished_sandwithes:
            print(sandwich)

        break




