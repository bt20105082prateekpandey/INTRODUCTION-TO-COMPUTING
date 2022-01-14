Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
my_list=['Red','Green','White','Black','Pink','Yellow']
#(a) part
print('(a)')
print(my_list)
# remove 4th term that is black
my_list.remove('Black')
print(my_list)

my_list=['Red','Green','White','Black','Pink','Yellow']
#(b) part
print('(b)')
print(my_list)
#replace black and pink with purple
# to replace nth term we write {my_list[n-1]='new value'}
my_list[3:5]=['Purple']
print(my_list)
