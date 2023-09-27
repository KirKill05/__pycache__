import random
Ecl = False
print("Welcome, to the *Quest to the Balance* game!")
print("Balance in the world has been disturbanced and forces from above try to restore or destroy it completly.")
print("To start the game chose your character(Type their name down to choose them):")
print("The Life")
print("The Death")
if Ecl is False:
    print("Not yet Unlocked")
else:
    print("The Eclipse =)")
chs = input()
if chs == "The Life":
    print("Life starts her journey to restore balance.")
elif chs == "The Death":
    print("Death starts his journey restore the balance.")
elif (chs == "The Eclipse" or  chs == "The Eclipse =)") and Ecl is True:
    print("The opposing forces join the play =).")
elif (chs == "The Eclipse" or  chs == "The Eclipse =)") and Ecl is False:
    print("The time...has't come...yet =). Restart the game and choose avaliable options.")
else:
    print("Ops! It seems like something went wrong! Please restart the game.")