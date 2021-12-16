from django.db import models
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

    position_description = models.CharField(max_length=500)

    hours_required = models.IntegerField()

    emergency_contact = models.BooleanField()

    all_osca = models.BooleanField()

    def __str__(self):
        """String for representing the Model object."""
        return self.position_name



class Member(models.Model):
    id = models.AutoField(primary_key=True)

    first_name = models.CharField(max_length=30)

    last_name = models.CharField(max_length=50)

    preferred_name = models.CharField(max_length=100)

    tnumber = models.IntegerField()

    coop = models.ForeignKey('Coop', on_delete=models.SET_NULL, null=True)

    email = models.EmailField()

    pronouns = models.CharField(max_length=20)

    time_aid = models.IntegerField()

    missed_jobes = models.IntegerField()

    def __str__(self):
        """String for representing the Model object."""
        return self.preferred_name


class Workchart_slot(models.Model):
    id = models.AutoField(primary_key=True)

    day_of_week = models.CharField(max_length=10)

    meal = models.CharField(max_length=20)

    crew = models.BooleanField()

    required_members = models.IntegerField()

    pic = models.BooleanField()

    def __str__(self):
        """String for representing the Model object."""
        return self.meal


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