#Ask user what to do
activity=input("What should I do (Study/Play)?")

#Decide if beep should study or play
if activity == "play":

    #Ask what to play with
    print("What do you want to play with (Toy/ Friend)?")
    play_with=  input()

    #decide if beep should play with toys or friend
    if play_with == "toy":
        print("I will play with my toys!")

    else:
        print("I will play with my friend!")

else:
    print("I will study")

#Ask for book cover
print("what type of cover does the book have?")
cover= input()
#Soft or hard response
if cover == "soft":
    print("Is the book perfect-bound?")
    book= input()
    if book == "perfect-bound":
        print("Perfect bound books are very popular")
    else:
        print("Soft covers with coils or stitches are great for short breaks")

else:
    print("Books with hard covers can be more expensive.")