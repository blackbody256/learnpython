# Let's start a coffee shop together!! We're going to uild a coffee shop using some new 
#python concepts specially input function
print("Hello, welcome to NetworkChuck Coffee!!!!")
name=input("What is your Name?\n")
print("Hello "+name+" Welcome to Networkchuck coffee shop")

#menu
Item1="1.Brown coffee\t\t10$"
Item2="2.Cupiccino\t\t12$"
Item3="3.African Tea\t'\t12$"
Item4="4.Chocolate milk\t\t14"

print("Here is our menu\n")
print(Item1+"\n"+Item2+'\n'+Item3+'\n'+Item4+'\n\n\n')
choice=int(input(name+'\nChoose your order:\nchoice is either 1,2,3 or 4 only\n'))
if choice==1:
    print("Your Brown coffee is being prepared please wait")
elif  choice==2:
    print("Your Cupiccino is being prepared please wait")
elif choice==3:
    print("Your african Tea is being prepared please wait")
elif choice==4:
    print('Your chocolate milk is being prepared please wait')
else :
    print('Sorry we don\'t have that order')



