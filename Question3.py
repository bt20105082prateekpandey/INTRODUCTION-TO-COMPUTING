Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
name=input("Please enter name: ")
sid= input("Enter student Id: ")
gender=input("Enter gender: ")
course_name=input("Enter your course name: ")
cgpa=input("Enter cgpa: ")
sid=int(sid)
cgpa=float(cgpa)
#our list now name as student_info
data=['Name','SID','Gender','Course name','Cgpa']
print(data)
student_info=[name,sid,gender,course_name,cgpa]
print(student_info)