print("Where should I look (In the bedroom/ In the bathroom or in the lab)?")
search= input()
if search == "in the bedroom":
    print("Where in the bedroom should I look(Under the bed / in the cupboard)?")
    bedroom = input()
    if bedroom == "under the bed":
        print("Found some shoes but no battery")
    elif bedroom == "in the cupboard":
        print("Found some mess but no battery")
    else:
        print("Found nothing")
elif search == "in the bathroom":
    print("Where in the bathroom should I look (In the bathtub/ under the washbowl)?")
    bathroom = input()
    if bathroom == "in the bathtub?":
        print("Found a rubber duck but no battery")
    elif bathroom == "under the wash bowl":
        print("Found a wet surface but no battery")
    else:
        print("Found nothing")
elif search == "in the lab":
    print("Where in the lab should I look (on the table/ under the table)?")
    lab= input()
    if lab == "on the table":
        print("Yes! I found my battery")
    elif lab == "under the table":
        print("Found some tools but no battery")
    else:
        print("Found nothing")
else:
    print("I do not know where that is but I will keep looking")

