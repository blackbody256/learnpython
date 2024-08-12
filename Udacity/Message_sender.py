names = input("Enter names separated by commas: ") # get and process input for a list of names
assignments = input("Enter assignment counts separated by commas: ") # get and process input for a list of the number of assignments
grades = input("Enter grades separated by commas: ") #get and process input for a list of grades
name_list= list(names.split(','))
assignment_list = list(assignments.split(','))
grade_list = list(grades.split(','))
# message string to be used for each student
#HINT: use .format() with this string in your for loop
for i in range(len(name_list)):
    message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
    submit before you can graduate. Your current grade is {} and can increase \
    to {} if you submit all assignments before the due date.\n\n".format(name_list[i], assignment_list[i], int(grade_list[i])+ int(assignment_list[i]))
    print(message)

## write a for loop that iterates through each set of names, assignments, and grades to print each student's messagenames = input("Enter names separated by commas: ").title().split(",")

#Another version
names = input("Enter names separated by commas: ").title().split(",")
assignments = input("Enter assignment counts separated by commas: ").split(",")
grades = input("Enter grades separated by commas: ").split(",")

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))