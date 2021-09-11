

#-----------------------------Session:- 03: Migrations-----------------------------------------------------

from django.db.models import*
from itertools import count
from django.db.models import query
from app1.models import*


# exec(open("E:\\B5_Python Learnings\\B5_Batch\\B5_Django Projects\\first\\db_shell.py").read())

# 1st way ---

# e = Employee(name="A", salary=455.50, address="Pune")
# e.save()

#---------------


# 2nd way --- 

# objects - model manager


# Employee.objects.create(name="PQR", salary=2555.50, address="Kolkata")

#------------------------------------------------


# all_data = list(Employee.objects.all())[-1]
# print(all_data)



# all_data = Employee.objects.all()
# print(all_data.query) # getting  sql query 


# SELECT "app1_employee"."id", "app1_employee"."name", "app1_employee"."salary", "app1_employee"."address" FROM "app1_employee"

#--------------------------------------------------


# all_data = Employee.objects.all()[3]
# print(all_data)


# emp = Employee.objects.filter(name="A")
# print(emp)


#-------------------------Session:- 4: Django_Models_ORM Queries--------------------------------------------


#--- databse change
#--- models
#--- relationship

# ----------------------------------------------------------------------

# e = Employee(name="ABC", salary=52550, address="Pune")
# e.save()

# import random

# ad_list = ["Pune", "Mumbai", "Bangalore", "Kolkata", "hyderabad"]
# for i in range(1, 21):
#     Employee.objects.create(name=chr(65+i), salary=random.randint(35000, 85000), address=random.choices(ad_list))


#----------------------------------------------


# to get all records ---

# emp = Employee.objects.all()
# print(emp)

#--------------------------------------

# get records by id ---


# emp = Employee.objects.get(id=5)
# print(emp)

#---------------------------------------

# filtered records ---

# emp = Employee.objects.filter(name="A")
# print(emp[1].salary)


# emp = Employee.objects.get(name="A")  
# print(emp) #    raise self.model.MultipleObjectsReturned -- app1.models.Employee.MultipleObjectsReturned: get() returned more than one Employee -- it returned 2!



# e = Employee.objects.filter(name="B").count()
# print(e)



# e = Employee.objects.filter(salary=73852).count()
# print(e)



# e = Employee.objects.all().exclude(name="A")
# print(e)


# e = Employee.objects.annotate(first_name="name")
# print(e)



# format1 = """

# ------------- ID:- {} -----------
# Name:- {}
# Salary:- {}
# Address{}

# """


# def get_emp_dict():
#     emp_list = []
#     for i in Employee.objects.all():
#         # print(format1.format(i.id, i.name, i.salary, i.address))
#         emp_list.append({"ID": i.id, "Name": i.name, "Salary": i.salary, "Address": i.address})
#     return emp_list    


# print(get_emp_dict())

# -------------------------------------------------

# e1 = Employee.objects.first()
# print(hasattr(e1,"get_name_with_salary"))


#--------------------------------------------------

# total sum of salaries

# total_payout = 0
# for i in Employee.objects.all():
#     total_payout += i.salary

# print(total_payout)    


# using Lambda with reduce function ---

# from functools import reduce

# t = reduce(lambda x,y: x["salary"]+y["salary"], [{'salary': 58656.0}, {'salary': 58656.0}])
# print(t)  # int --- o/p -- 117312.0


# # above same e.g. for nested lambda ---


# l = [{'salary': 45.0}, {'salary': 555.0}, {'salary': 745.01}]

# t = reduce(lambda x,y: x+y, list(map(lambda j: j["salary"], l)))
# # print(t)  # int


#-----------------------------------------------------------------------------------------------------------


#---------------------------------Session:-5 : ORM_Queries-----------------------------------------------------

# exec(open("E:\\B5_Python Learnings\\B5_Batch\\B5_Django Projects\\first\\db_shell.py").read())

# from django.db.models import Avg, Max

# emps = Employee.objects.all().aggregate(Avg("salary"))
# print(emps) # {'salary__avg': 64215.90476190476}



# emps = Employee.objects.all().aggregate(Max("salary"))
# print(emps) #  {'salary__max': 80242.0}


#-------------------------------------------------------------------

# CRUD Operations -----


# def update_emp(eid, first_name):
#     emp_obj = Employee.objects.get(id=eid)
#     emp_obj.name = first_name
#     emp_obj.save()
#     print("Employee object updated Successfully..!")


# update_emp(3, "ABC")  # Update operation done 


#-------------------------------------


# incrementing salary by 5% ---


# def increment_sal(increment_value):
#     emps = Employee.objects.all()
#     for e in emps:
#         e.salary = e.salary + (e.salary*(increment_value/100))
#         e.save()
#     print("salary incremented by 5 percent for every employee...!")


# increment_sal(5)  # incremented by 5% for salary of every employee


#-----------------------------------------


# Employee.objects.all().update(company="Barkleys")

# Employee.objects.filter(name="ABC").update(company="Cybage")

#-----------------------------------------


# emps = Employee.objects.filter(id__lt=5) # will provide id less_than 5 / same for __gt = greater_than
# print(emps)


# emp = Employee.objects.filter(name__startswith="N") # we can get also for -- name__endswith
# print(emp)

#--------------------------------------------------


# Relationaship ---


# Delete data-----


# def delete_emp_by_id(eid):
#     emp = Employee.objects.get(id=eid)
#     emp.delete()


# delete_emp_by_id(21) # will delete the particular data for id=21


# Employee.objects.all().delete --- # will delete all data


# Employee.objects.filter(salary__gte=50000).delete()


# Employee.objects.create(name="Pawan", salary=45755.50, address="Kolkata") -- data created


# emp = Employee.objects.get(id=22)
# print(emp.name)

#-------------------------------------------
from datetime import date


# l = License(license_no="MH12 39587620983", expiry_date=date(2035, 12, 13), dl_type="MCWG", employee=emp)
# l.save()


# l = License(license_no="MH12 39587620983", expiry_date=date(2035, 12, 13), dl_type="MCWG", employee_id=23)
# l.save() # will throw us integrity Error 

#-------------------------------------------------------------------------------------------------


#----------------------- Session:- 6: Django_models_query_1 to 1_relation-------------------------------------------------  

# exec(open("E:\\B5_Python Learnings\\B5_Batch\\B5_Django Projects\\first\\db_shell.py").read())


# *** One to One Relation ***


# fetching data ---  Employee to License 

#  fetch license by emp object --- employee_obj.classname(small_letters)


# emp = Employee.objects.get(id=22)
# print(emp.license)



# l = License.objects.get(license_no="MH12 39587620983")
# print(l)


# l1 = License.objects.get(employee=e)
# print(l1)

#-------------------------------------------


# fetching data --- License to Employee 


# l1 = License.objects.get(license_no="MH12 39587620983").employee
# l1.name = "Rohan"
# l1.save()


# License.objects.get(employee__name="Rohan")

#-----------------------------------------------

# object create  
# update  
# delete
# read 

#-----------------------------------------------


# print(License.objects.get(employee=22))


#------------------------------------------------


# emp = Employee.objects.create(name="Kapil", salary=35550.55, address="Nagpur")


# l = License.objects.create(license_no="MH20 94873610823", expiry_date=date(2032, 10, 8), dl_type="MCWG", employee=emp)
# l.save()


# deleting ------



# l = License.objects.get(license_no="MH12 39587620983")
# print(l)

# l.delete() # deleted the license no for given ---


# Employee.objects.get(id=23).delete() # deleted for employee table for single employee


# Employee.objects.all().delete()   # all data will be deleted --

#-----------------------------------


# l = License.objects.get(license_no="MH12 39587620985")
# print(l.employee.adr)

# if hasattr(l, "change_address"):
#     l.change_address("Mumbai")


# print(l.get_employee())


# try:
#     print(License.get_license_obj("MH12 39587620985"))
# except AttributeError:
#     print("There is attribute Error, Please check attribuate for same...")    

#------------------------------


# staff --- Particular person can only login if true
# active -- soft delete
# superuser -- all access by default

#---------------------------------------------

#-------------------------------Session:- 07: orm_relaionship-------------------------------------------------------



# emp_list = [Employee(name="Rakesh", salary=34540.45, address="Mumbai"),
# Employee(name="Rakesh", salary=44840.35, address="Hyderabad"),
# Employee(name="Rakesh", salary=30540.25, address="Kolkata"),
# Employee(name="Rakesh", salary=55940.05, address="Pune")]

# print(emp_list)

# for i in emp_list:
#     i.save()



# Employee.objects.bulk_create(emp_list) # created multiple objects with passing iterables -- 


#------------------------------------------------------------


# id in ---


# print(Employee.objects.filter(id__in=[27,28,29]))


#------------------------------------------------------------------------------------


# One To Many Relationship ---

from datetime import date

# first way --

emp = Employee.objects.get(id=27)

# t1 = Task.objects.create(name="Create login page", timeline=str(date(2021, 8, 12)), employee=emp) # contral+G = jump to line no ---
# print(t1)


# second way --

# Task.objects.create(name="Create homepage")


# def assign_task(emp_id, timeline, task_id):
#     emp = Employee.objects.get(id=emp_id)
#     task_obj = Task.objects.get(task_id=task_id)
#     task_obj.employee = emp
#     task_obj.timeline = timeline
#     task_obj.save()


# assign_task(27, date(2021, 8, 21), 3)


#----------------------------------------------------------


# emp = Employee.objects.get(id=27)
# print(emp.get_task_count())  
# print(emp.task_set.all())   # data will fetch for One to Many

# print(emp.tasks.all())

# t = Task.objects.get(task_id=2)
# print(t)
# print(t.get_employee())


#-----------------------------------------------------------------------------


# Many to Many Relation --- e.g. Pizza & Toppings


# hawaiian_pizza = Pizza.objects.create(name="Hawaiian") # 3
 
# pineapple = Topping(name='pineapple') # 3 
# pineapple.save()
# hawaiian_pizza.toppings.add(pineapple)

# pizza = Pizza.objects.get(id=3)
# t1 = Topping(name="Capsicum")
# t1.save()

# pizza.toppings.add(t1)


# pizza1 = Pizza.objects.create(name="Cheese")
# t1 = Topping.objects.get(id=3)
# t2 = Topping.objects.get(id=4)

# pizza1.toppings.add(t1)
# pizza1.toppings.add(t2)



# t1 = Topping.objects.get(id=4)
# print(t1.pizza_set.all())



# Pizza.objects.filter(toppings__name__startswith='p') # to fetch name for pizza---


####################################################################################################################










































































































































