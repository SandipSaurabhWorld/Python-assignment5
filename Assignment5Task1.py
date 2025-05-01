student_dict = {'Sandeep':85,'Rohit':98,'Gaurav':78,'akhilesh':89}
name = input("Enter the student's name: ")
#print("{}'s Marks: {}".format(name,student_dict.get(name,"Student not found.")))
if name in student_dict:
    print("{}'s Marks: {}".format(name,student_dict[name]))
else:
    print("Student not found")