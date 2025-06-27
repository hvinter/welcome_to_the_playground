#
#
#
#           pers_w_age:
#
#
pers_w_age = {
    "rebecca": 42,
    "hella": 41,
    "mathias": 49,
    "stefan": 56,
    "patrik": 48
}

# != (inte lika med)
print("\n!=")
print("rebecca != hella = true\n",
      pers_w_age["rebecca"] != pers_w_age["hella"])  # true
print("hella != hella? = false\n",
      pers_w_age["hella"] != pers_w_age["hella"])  # false

# == (lika med)
print("\n==")
print("mathias == mathias = true\n",
      pers_w_age["mathias"] == pers_w_age["mathias"])  # true
print("Mathias == Stefans = false\n",
      pers_w_age["mathias"] == pers_w_age["stefan"]) # false

# > (större än)
print("\n>=")
print("mathias >= hella = true\n",
      pers_w_age["mathias"] >= pers_w_age["hella"])  # true
print("patrik >= stefan = false\n",
      pers_w_age["patrik"] >= pers_w_age["stefan"])  # false

# < (mindre än)
print("\n<=")
print("Hella <= rebecca = true\n",
      pers_w_age["hella"] <= pers_w_age["rebecca"])  # true
print("mathias <= patrik = false\n",
      pers_w_age["mathias"] <= pers_w_age["patrik"])  # false

# använder 'and'  - båda påståenden måste vara sanna:
print("\nConditional testing using 'and':"),
print("hella <= rebecca 'and' mathias >= hella = true\n",
      pers_w_age["hella"] <= pers_w_age["rebecca"] and  # true
      pers_w_age["mathias"] >= pers_w_age["hella"]) # true  / true

print("2.patrik >= mathias 'and' mathias >= rebecca = false\n",
      pers_w_age["patrik"] >= pers_w_age["mathias"] and  # false
      pers_w_age["mathias"] >= pers_w_age["rebecca"]) # false   / false

print("mathias <= stefan 'and' hella != rebecca = true\n",
      pers_w_age["mathias"] <= pers_w_age["stefan"] and  # true
      pers_w_age["hella"] != pers_w_age["rebecca"]) # true  / true

print("4.mathias >= patrik 'and' stefan <= hella  = false\n",
      pers_w_age["mathias"] >= pers_w_age["patrik"] and  # true
      pers_w_age["stefan"] <= pers_w_age["hella"]) # false  / false

print("5.mathias == mathias 'and' patrik != stefan = true\n",
      pers_w_age["mathias"] == pers_w_age["mathias"] and  #true
      pers_w_age["patrik"] != pers_w_age["stefan"]) # true  / true

print("6.mathias <= hella 'and' hella <= rebecca = false\n",
      pers_w_age["mathias"] <= pers_w_age["hella"] and  # false
      pers_w_age["hella"] <= pers_w_age["rebecca"]) # true  / false

print("7.stefan >= hella 'and' mathias >= rebecca = true\n",
      pers_w_age["stefan"] >= pers_w_age["hella"] and  # true
      pers_w_age["mathias"] >= pers_w_age["rebecca"]) # true    / true

print("8.mathias == stefan 'and' mathias >= rebecca = false\n",
      pers_w_age["mathias"] == pers_w_age["stefan"] and  # false
      pers_w_age["mathias"] >= pers_w_age["rebecca"]) # true    / false

print("9.mathias != rebecca 'and' mathias >= rebecca = true\n",
      pers_w_age["mathias"] != pers_w_age["rebecca"] and  # true
      pers_w_age["mathias"] > pers_w_age["rebecca"]) # true / true

print("\nHär använder vi 'or':")
print("1.mathias == mathias 'or' mathias =< rebecca = true\n",
      pers_w_age["mathias"] == pers_w_age["mathias"] or  # true
      pers_w_age["mathias"] <= pers_w_age["rebecca"]) # false   / true

print("2.patrik != patrik 'or' mathias == rebecca = false\n",
      pers_w_age["patrik"] != pers_w_age["patrik"] or  # false
      pers_w_age["mathias"] == pers_w_age["rebecca"]) # false   / false

print("3.rebecca >= hella 'or' mathias >= rebecca = true\n",
      pers_w_age["rebecca"] > pers_w_age["hella"] or  # true
      pers_w_age["mathias"] > pers_w_age["rebecca"]) # true / true

print("4.patrik != patrik 'or' mathias <= rebecca = false\n",
      pers_w_age["patrik"] != pers_w_age["patrik"] or  # false
      pers_w_age["mathias"] <= pers_w_age["rebecca"]) # false   / false

print("5.hella >= mathias 'or' mathias != rebecca = true\n",
      pers_w_age["hella"] >= pers_w_age["mathias"] or  # false
      pers_w_age["mathias"] != pers_w_age["rebecca"]) # true    / true

print("\nname :\n" + "\n".join([f"{namn}" for
                                namn, ålder in pers_w_age.items()]))
print("\nage :\n" + "\n".join([f"{ålder}" for
                               namn, ålder in pers_w_age.items()]))
print("\nname / age :\n".join([f"{namn} {age}" for
                               namn, age in pers_w_age.items()]))
#
#
#
#             co-workers:
#
#
print("\n\n\nLet's continue with co-workers:")

kollega_npt = ["EMil", "JeSpEr", "siMon"]
(print("\nThe original list 'koll_npt' prior to any alterations :"),
 print(kollega_npt))

kollega_npt = [name.lower() for name in kollega_npt]
print("\nThe list we use from now on :"), print(kollega_npt)

print("\nMade a functon to print kollega.title -")
def kollegorna():
    for koll in kollega_npt:
        print(koll.title())
print("and this is what it looks like when used :"), kollegorna()

print("\nMade a func.to write co-worker.title, .upper och .lower : ")
def kollega_tit_up_low():
    for kollega in kollega_npt:
        print(kollega.title())
        print(kollega.upper())
        print(kollega.lower())
kollega_tit_up_low()

print("\nAdding a few more w. '.extend' :")
kollega_npt.extend(["miKA".lower()])
kollega_npt.extend(["marTA".lower(), "TUre".lower(), "zaCKe".lower()])

kollega_npt[0] = ("jÖrgen".lower())
kollega_npt[3] = ("chrIStian".lower())

kollega_npt.append("jOnAS".lower())
kollega_npt.append("arne".lower())

print("och nu är listan : ", kollegorna())

# remove
print("\nGetting rid of zacke med '.remove'"
      "- must have the exact value in index.")
kollega_npt.remove("zacke")
print("Removal succesful and the list is now : "), kollegorna()

# delete (del)
print("\nIf we want to use '.del' we must have the numerical value -")
print("I'm deleting the last one on the list "
      "w. '[-1]' and i ought to be arne :")
del kollega_npt[-1]
kollegorna()

#pop
print("\nIf you WANT to use numerical value from index = 'pop'.")
popped = kollega_npt.pop(0)
print("Jörgen should have disappeared\nthere is no-one who can stand him...")
print(f"The one who got popped is : {popped.title()}.")
print("\nThe list is now the following : "), kollegorna()

print("\nAdding popped back to the list :")
kollega_npt.append(popped.title()), kollegorna()
print(f"And here's {popped.title()} again.\n")
print("For reals yo - he truly is an idiot!")
print("Let's go 'del' on his arse:\nAdios maddafakka!!!!!")

del kollega_npt[-1]

print("Vi kollar :\n"), kollegorna()
print("Whoop - whoop! :p")

print("\nThree in from the start '0:3' :")
for kollega in kollega_npt[0:3]: print(kollega.title())

print("Three from the back '-3:' :")
for kollega in kollega_npt[-3:]: print(kollega.title())

print("The three in the middle '2:5' :")
for kollega in kollega_npt[2:5]: print(kollega.title())

print("\nTotal number of co-workers :")
print(len(kollega_npt))

def kolla_fredde():
    if "fredde" not in kollega_npt:print("\nYou're not on the list.")
    else: print(f"\nWelcome to the crew, Fredde!")

print("\nLet's check on Fredde :"), kolla_fredde()

print("\nHe's not on the list.")
print("Using .append to add 'fredde'"), kollega_npt.append("fredde")

print(kollega_npt.sort)
#
#
#
#                      user:
#
#
print("\nThe last part of the assignment was to 'check for a user' -")
user = "SIguRd".lower()
print(f"and now I have created one named {user}.")

print("\n'User' is : "), print(user)

print("\nCreating a func. to check if 'user' is in 'koll_npt'.")
def check():
    if user in kollega_npt:
        print(f"{user} is on the list 'koll_npt'.")
    else:
        print(f"{user} is not in the list 'koll_npt'.")

print("\nFirst check :\nUser not on the list :")
check()
print("\nUsing 'append' to add user to list :")
kollega_npt.append(user)
print("\nLet's 'check':")
check()
print("\nthe list of users is :")
kollegorna()
#
#
#   / gurudev 2025-05-31
#               the first.