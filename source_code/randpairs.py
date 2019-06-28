from random import randint

the_list = ["1. radek_m", "2. szpajchel", "3. Rivelv", "4. klechu", "5. Ryszard", "6. Koralik", "7. skaarj"]

pentaxians = the_list.copy()

print("\nZdjęciami wymienią się:")
while len(pentaxians) > 1:
    find = randint(0, len(pentaxians)-1)
    user_1 = pentaxians.pop(find)
    find = randint(0, len(pentaxians)-1)
    user_2 = pentaxians.pop(find)
    print("  {:<10}   i   {:<10}".format(user_1, user_2))

if pentaxians != []:
    print("\nBonus:")
    user_1 = pentaxians[0]
    pentaxians = the_list.copy()
    pentaxians.remove(user_1)
    find = randint(0, len(pentaxians))
    user_2 = pentaxians.pop(find)
    print("  {:<10}   i   {:<10}".format(user_1, user_2))
