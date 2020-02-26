#names = input("Enter names separated by commas: ")
#assignments = input("Enter assignment counts separated by commas: ")
#grades = input("Enter grades separated by commas: ")

#name_list = names.split(',')
#assignment_list = assignments.split(',')
#grade_list = grades.split(',')

#for i,name in enumerate(name_list):
#	protential_grade = int(grade_list[i]) + 2 * int(assignment_list[i])
#	print("Hi {},\n\nThis is a reminder that you have {} assignments left to submit \
#	before you can graduate. Your current grade is {} and can increase to {} if you \
#	submit all assignments before the due date.\n".format(name,assignment_list[i],grade_list[i],protential_grade))
	
names = input("Enter names separated by commas: ").title().split(',')
assignments = input("Enter assignment counts separated by commas: ").split(',')
grades = input("Enter grades separated by commas: ").split(',')

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to submit \
	before you can graduate. Your current grade is {} and can increase to {} if you \
	submit all assignments before the due date.\n"

for name, assignment, grade in zip(names,assignments,grades):
	print(message.format(name, assignment, grade, int(grade) + 2 * int(assignment)))