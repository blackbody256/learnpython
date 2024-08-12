print("Hello world !!!!!!\nI am Iron Man\nNo, I am Tony stark\nNo, I am poppy")
#single line string
print("""I am ironman
      No, I am Tony Stark
      No, I am poppy""")
#this is a multiline string
#This is a commment by the way


print("I am Andrew\n"*3)

print("hello,", end="")
print(" world")
#The end property of the print function is a new line by default
#but i change it to a nothing so that the next print statement will be on the same line


name=input("What is your name?\n").strip().title()
#.stip() is used to remove any white space in the input
#.title() is used to capitalize teh first letter of every word in the input
print("hello", name, sep="@@@@@")
#here i changed the separate property of the print function so that every parameter is separated by @@@@@@
#and not a space