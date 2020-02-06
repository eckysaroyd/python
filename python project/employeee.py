extra_hrs = int(input("enter extra hours work  "))
pay= int(input("enter pay rate per hours  "))
hrs =int(input("enter number of hours  "))
ext_pay = int(input("enter extra amount per hours  "))
salary =30*hrs
if(extra_hrs>2):
    salary=salary+extra_hrs*ext_pay
if (extra_hrs >15):
    salary=salary+3000
print("salary of employee is :{} ".format(salary))
