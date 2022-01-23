#from calendar import FRIDAY, MONDAY, SATURDAY, SUNDAY, THURSDAY, TUESDAY, WEDNESDAY
from django.db import models
from django import forms
import uuid

# Create your models here.

class Coop(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100, help_text='What is the name of this coop')

    address = models.CharField(max_length=500, null=True, blank=True, help_text='what is the address of this coop')

    building = models.CharField(max_length=100, help_text='What building is this coop in')

    vegan = models.BooleanField(help_text='is this a vegan coop')

    num_dining = models.IntegerField(help_text='how many dining members does this coop have')

    num_housing = models.IntegerField(help_text='how many housing members does this coop have')

    hours_needed = models.IntegerField(help_text='how many hours a week do members have to work')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Officer(models.Model):
    id = models.AutoField(primary_key=True)

    coop = models.ForeignKey('Coop', on_delete=models.SET_NULL, null=True)

    member = models.ForeignKey('Member', on_delete=models.SET_NULL, null=True)

    position_name = models.CharField(max_length=100)

    position_description = models.CharField(max_length=500, null=True, blank=True)

    hours_required = models.IntegerField()

    emergency_contact = models.BooleanField(default=False)

    all_osca = models.BooleanField(default=False)

    class Meta:
        permissions = (("is_officer", "Gives user the officer permissions"),)

    def __str__(self):
        """String for representing the Model object."""
        return self.position_name



class Member(models.Model):
    id = models.AutoField(primary_key=True)

    first_name = models.CharField(max_length=30)

    last_name = models.CharField(max_length=50)

    preferred_name = models.CharField(max_length=100, null=True, blank = True)

    tnumber = models.IntegerField()

    coop = models.ForeignKey('Coop', on_delete=models.SET_NULL, null=True)

    email = models.EmailField(null = True, blank = True)

    pronouns = models.CharField(max_length=20)

    time_aid = models.IntegerField()

    missed_jobes = models.IntegerField(null = True, blank = True)



    def __str__(self):
        """String for representing the Model object."""
        returnString = self.first_name + " " + self.last_name
        return returnString



class Menu(models.Model):
    id = models.AutoField(primary_key=True)

    headCook = models.ForeignKey('Member', on_delete=models.SET_NULL, null = True)

    protein = models.CharField(max_length=300)

    vegetable = models.CharField(max_length=300)

    starch = models.CharField(max_length=300)

    dr_protein = models.CharField(max_length=300, null=True, blank = True)

    dr_vegetable = models.CharField(max_length=300, null=True, blank = True)

    dr_starch = models.CharField(max_length=300, null=True, blank = True)

    meat = models.BooleanField(null = True, default = False)

    comments = models.CharField(max_length=500, null=True, blank = True)

class Meal(models.Model):
    class Meal_Choices(models.IntegerChoices):
        BREAKFAST = 1, ("Breakfast")
        LUNCH = 2, ("Lunch")
        DINNER = 3, ("Dinner")
        PIZZA_NIGHT = 4, ("Pizza Night")
        SPECIAL_MEAL = 5, ("Specail Meal")
        COMMANDO_CREW = 6, ("Commando Crew")

    class Day_Choices(models.IntegerChoices):
        MONDAY = 1, ("Monday")
        TUESDAY = 2, ("Tuesday")
        WEDNESDAY = 3, ("Wednesday")
        THURSDAY = 4, ("Thursday")
        FRIDAY = 5, ("Friday")
        SATURDAY = 6, ("Saturday")
        SUNDAY = 7, ("Sunday")

    id = models.AutoField(primary_key=True)

    coop = models.ForeignKey('Coop', on_delete=models.SET_NULL, null=True)

    menu = models.ForeignKey('Menu', on_delete=models.SET_NULL, null=True, blank=True)

    meal_of_the_day = models.IntegerField('Meal_Choices', choices = Meal_Choices.choices, default=2)

    day_of_week = models.IntegerField('Day_Choices', choices=Day_Choices.choices, default=1)

    
class Shift(models.Model):

    id = models.AutoField(primary_key=True)

    cook = models.BooleanField()

    member = models.ForeignKey('Member', on_delete=models.SET_NULL, null=True)

    is_pic = models.BooleanField()

    meal = models.ForeignKey('Meal', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return str(self.member)


class WorkChartRow(models.Model):
    id = models.AutoField(primary_key=True)

    coop = models.ForeignKey('Coop', on_delete=models.SET_NULL, null=True)

    time = models.CharField(max_length=20, null=True, blank = True)

    cook = models.BooleanField()

    pic = models.BooleanField()

    monday = models.ForeignKey('Shift', on_delete=models.SET_NULL, null=True, related_name='monday')
    
    tuesday = models.ForeignKey('Shift', on_delete=models.SET_NULL, null=True, related_name='tuesday')

    wednesday = models.ForeignKey('Shift', on_delete=models.SET_NULL, null=True, related_name='wednesday')

    thursday = models.ForeignKey('Shift', on_delete=models.SET_NULL, null=True, related_name='thursday')

    friday = models.ForeignKey('Shift', on_delete=models.SET_NULL, null=True, related_name='friday')

    saturday = models.ForeignKey('Shift', on_delete=models.SET_NULL, null=True, related_name='saturday')

    sunday = models.ForeignKey('Shift', on_delete=models.SET_NULL, null=True, related_name='sunday')




# class Workchart_slot(models.Model):
#     id = models.AutoField(primary_key=True)

#     coop = models.ForeignKey('Coop', on_delete=models.SET_NULL, null=True)

#     meal = models.ForeignKey('Meal', on_delete=models.SET_NULL, null=True)

#     member = models.ForeignKey('Member', on_delete=models.SET_NULL, null=True)

#     crew = models.BooleanField()

#     start_time = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)

#     end_time = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)

#     pic = models.BooleanField()



#     def __str__(self):
#         """String for representing the Model object."""
#         return str(self.start_time)


class AllergySeverity(models.IntegerChoices):
    LOW = 0, ('Low')
    MED_LOW = 1, ('Medium-Low')
    MED = 2, ('Medium')
    MED_HIGH= 3, ('Medium-High')
    HIGH = 4, ('High')

class Allergy(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=50)

    severity = models.IntegerField(default=AllergySeverity.LOW, choices=AllergySeverity.choices)

    member = models.ForeignKey('Member', on_delete=models.SET_NULL, null=True)

    coop = models.ForeignKey('Coop', on_delete=models.SET_NULL, null=True)

    allowed_in_coop = models.BooleanField()
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name



class Budget(models.Model):
    id = models.AutoField(primary_key=True)

    coop = models.ForeignKey('Coop', on_delete=models.SET_NULL, null=True)

    total_budget = models.IntegerField()

    remaining_budget = models.IntegerField()
    
    def __str__(self):
        """String for representing the Model object."""
        return self.coop