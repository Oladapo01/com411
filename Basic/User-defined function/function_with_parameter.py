def escape_by(plan):
    if plan == "Jumping over":
        print("We can not escape that way! The boulder is too big!")
    elif plan == "Running over":
        print("We can not escape that way! The boulder is too fast!")
    elif plan == "Going deeper":
        print("That might just work let's go deeper")
    else:
        print("We can not escape that way")
escape_by("Jumping over")
escape_by("Running over")
escape_by("Going deeper")