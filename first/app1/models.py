from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.



class Common_Class(models.Model):
    """This is Common class"""

    def __str__(self):
        if type(self) == Employee:
            return f"{self.id} --- {self.name}"
        elif type(self) == License:
            return f"{self.license_no} --- {self.expiry_date}"    

        elif type(self) == Task:
            # return f"{self.task_id} --- {self.name}"
            return f"{self.__dict__}"
        
        elif type(self) == Project:
            return f"{self.project_id} --- {self.name}"
            # return f"{self.__dict__}"


    def __repr__(self):
        return str(self)

    class Meta:
        abstract = True


class Employee(Common_Class):    # table name --- app1_Employee
    name = models.CharField(max_length=100)
    salary = models.FloatField()
    address = models.CharField(max_length=500)
    company = models.CharField(max_length=100, default="Capegemini")


    class Meta:
        db_table = "emp"


    def get_name_with_salary(self):
        return f"Name:- {self.name} Salary:- {self.salary}"


    def get_task_count(self):
        return len(self.task_set.all())


class License(Common_Class):
    license_no = models.CharField(primary_key=True, max_length=16)
    expiry_date = models.DateField()
    dl_type = models.CharField(max_length=10)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)


    class Meta:
        db_table = "license"


    def get_employee(self):
        return self.employee


    def change_address(self, new_adr):
        self.employee.adr = new_adr
        self.employee.save()
        # print("Address updated Successfully...!")

# @staticmethod
@classmethod
def get_license_obj(cls,license_no):
    return cls.objects.get(license_no=license_no)




class Task(Common_Class):
    task_id = models.AutoField(primary_key=True) # autogenerate
    name = models.CharField(max_length=100) # mandatory
    timeline = models.DateTimeField(null=True)
    task_created_date = models.DateTimeField(auto_now_add=True)
    employee = models.ForeignKey(Employee,null=True, on_delete=models.SET_NULL, related_name="tasks")   # One To Many Relationship


    class Meta:
        db_table = "task"


    def get_employee(self):
        return self.employee


class Project(Common_Class):
    project_id = models.AutoField(primary_key=True)
    description = models.TextField(null=True)
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=15)
    client = models.CharField(max_length=16)
    employee = models.ManyToManyField(Employee, db_column="emp_project") 

    class Meta:
        db_table = "emp_project"


#---------------------------------------------------



class Common_Pizza(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Topping(Common_Pizza):
    pass


class Pizza(Common_Pizza):
    toppings = models.ManyToManyField('Topping', related_name='pizzas')


















# id, name, salary --- as creating table for given fields in models 

# create table Employee (id int auto increment, name varchar(50), salary float, primary key(id))

# CREATE TABLE "app1_employee" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "salary" real NOT NULL, "address" varchar(500) NOT NULL);

















