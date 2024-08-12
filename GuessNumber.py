import random
print("1.Scisors\n2.Paper\n3.Rock\n4.Exit\nNote:The answer should be either 1,2 or 3 only")
choice =int(input("What is your choice:"))
comp= random.randrange(1,3)
while choice != 4:
    if choice==comp :
        print('It\'s a draw')
    elif choice == 1 and comp == 2 :
        print('You win\nScisors cut paper')
    elif choice == 2 and comp == 1 :
        print('Computer wins\nScissors cut paper')
    elif choice == 2 and comp == 3 :
        print('You win\nPaper wraps rock')
    elif choice == 3 and comp == 2 :
        print('Computer wins\nPaper wraps rock')
    elif choice == 3 and comp == 1 :
        print('You win\n Rock bangs scissors')
    elif choice == 1 and comp == 3 :
        print('Computer wins\nRock bangs scissors')
    else:
        print('Not be a fool\nRead instruction')

    
    print("1.Scisors\n2.Paper\n3.Rock\n4.Exit\nNote:The answer should be either 1,2 or 3 only")
    choice = int(input('What is your choice:'))



print("Thanks for playing")