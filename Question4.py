Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
student_1marks=int(input("Enter student 1 marks: "))
student_2marks=int(input("Enter student 2 marks: "))
student_3marks=int(input("Enter student 3 marks: "))
student_4marks=int(input("Enter student 4 marks: "))
student_5marks=int(input("Enter student 5 marks: "))

my_list=[student_1marks,student_2marks,student_3marks,student_4marks,student_5marks]
print("List: ")
print(my_list)
print("Sorted List(decreasing order): ")
my_list.sort(reverse=True)
print(my_list)
 