Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
gross_income=input("Please enter gross income: ")
gross_income=float(gross_income)

standard_deduction=10000
dependents=input("Enter the no. of dependents: ")
dependents=int(dependents)
#there is a $3000 deduction for each dependents
dependent_deduction=3000

#tax rate=20%
taxable_income=gross_income-standard_deduction-(dependent_deduction*dependents)
print("taxable income:")
print(taxable_income)
tax=(taxable_income*20)/100
print("tax:")
print(tax)