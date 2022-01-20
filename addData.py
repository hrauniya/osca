from csv import Dialect
import os
from re import L
import django
from numpy.random import choice, randint
from datetime import time
from osca.wsgi import *
from catalog.models import Coop, Member, Officer, AllergySeverity, Allergy, Budget, Meal, Menu, Cook, Crew, CookShift, CrewShift

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'osca.settings')
django.setup()

with open('names.txt') as f: #import most of measurement data stored in text file for convenience
        memberNames = f.readlines()

keep = Coop(name = "Keep", building = "Keep Cottage", vegan = False, num_dining = 50, num_housing = 30, hours_needed = 6)
tank = Coop(name = "Tank", building = "Tank House", vegan = False, num_dining = 60, num_housing = 40, hours_needed = 6)
pyle = Coop(name = "Pyle", building = "Asia House", vegan = False, num_dining = 0, num_housing = 70, hours_needed = 5)
harkness = Coop(name = "Harkness", building = "Harkness Hall", vegan = False, num_dining = 70, num_housing = 50, hours_needed = 4)
third_world = Coop(name = "Third World House", building = "Price Hall", vegan = False, num_dining = 30, num_housing = 20, hours_needed = 6)


keep.save()
tank.save()
pyle.save()
harkness.save()
third_world.save()

newBudget = Budget(coop = keep, total_budget = 28000, remaining_budget = 3000)
newBudget.save()
newBudget = Budget(coop = tank, total_budget = 25000, remaining_budget = 4400)
newBudget.save()
newBudget = Budget(coop = pyle, total_budget = 35000, remaining_budget = 6700)
newBudget.save()
newBudget = Budget(coop = harkness, total_budget = 37000, remaining_budget = 7300)
newBudget.save()
newBudget = Budget(coop = third_world, total_budget = 40000, remaining_budget = 8200)
newBudget.save()




tNumber = 0000000
for member in memberNames:
    firstname, lastname = member.split()
    coop = choice([keep, tank, pyle, harkness, third_world], p=(.15, .15, .25, .35, .1))
    pronouns = choice(["she/her/hers", "he/him/his", "they/them/theirs"])
    timeAid = choice([0,1,2,3])
    newMember = Member(first_name = firstname, last_name = lastname, tnumber = tNumber, coop = coop, pronouns = pronouns, time_aid = timeAid)
    newMember.save()

positions = ('DLEC', 3, 'DLEC', 3 , 'Food Safety Coordinator', 'full', 'Food Safety Coordinator', 'full', 'New Member Trainer', 2 , 'KitchCo', 'full' , 'KitchCo', 'full' , 'Membership Coordinator', 3 , 'Membership Coordinator', 3 , 'Accessibility Coordinator', 3,  'Food Buyer and Unpacker', 3, 'Food Buyer and Unpacker', 3, 'Board Representitive', 3, 'Board Representitive', 3, 'Treasurer', 3,  'Pizza Maker', 3, 'Pizza Maker', 3, 'Dough Maker', 2,  'Tasty Things Maker', 3, 'Tasty Things Maker', 3, 'Tasty Things Maker', 3, 'Bread Maker', 'full', 'Bread Maker', 'full',  'Granola Maker', 2, 'Granola Maker', 2, 'Dietary Restrictions Maker', 3, 'Long Range Planning Committee Representitive', 1, 'Environmental Concerns Committee Representitive', 1, 'Programming Committee Representitve', 1, 'OSCA Foundation Representitive', 1, 'Historian', 1)
for coop in  [keep, tank, pyle, harkness, third_world]:
    coop_members = Member.objects.filter(coop = coop)
    i = 0
    num_positions = len(positions)
    for member in coop_members:
        if i == num_positions:
            break
        position = positions[i]
        hours = positions[i+1]
        if hours == 'full':
            hours = coop.hours_needed
        emergencyContact = False
        if position == 'DLEC' or position == 'Food Safety Coordinator' or position == 'KitchCo':
            emergencyContact = True
        newOfficer = Officer(coop = coop, member = member, position_name = positions[i], hours_required = hours, emergency_contact = emergencyContact)
        i += 2
        newOfficer.save()




BREAKFAST = 1
LUNCH = 2
DINNER = 3
PIZZA_NIGHT = 4
SATURDAY_DINNER = 5
SUNDAY_LUNCH = 6
COMMANDO_CREW = 7


MONDAY = 1
TUESDAY = 2
WEDNESDAY = 3
THURSDAY = 4
FRIDAY = 5
SATURDAY = 6
SUNDAY = 7

FULL = 1
FIRST = 2
SECOND = 3

def addMeal(mealOfDay, members, numCook, numCrew, mealObj):
    shiftOptions = [FULL, FIRST, SECOND, FIRST, SECOND, FULL]
    if mealOfDay == BREAKFAST:
        crewStart = time(hour = 9, minute=  20)
        crewEnd = time(hour = 10, minute=  20)
        numCrew = 1
        numCook = 0
    elif mealOfDay == LUNCH:
        CookStart = time(hour = 10, minute=  20)
        CookMid = time(hour = 11, minute=  20)
        CookEnd = time(hour = 12, minute=  20)
        crewStart = time(hour = 13)
        crewEnd = time(hour = 14)
    elif mealOfDay == DINNER:
        CookStart = time(hour = 16, minute=  20)
        CookMid = time(hour = 17, minute=  20)
        CookEnd = time(hour = 18, minute=  20)
        crewStart = time(hour = 19)
        crewEnd = time(hour = 20)
    elif mealOfDay == PIZZA_NIGHT:
        CookStart = time(hour = 16, minute=  20)
        CookMid = time(hour = 17, minute=  20)
        CookEnd = time(hour = 18, minute=  20)
        crewStart = time(hour = 19)
        crewEnd = time(hour = 20, minute=  30) #until finished
        numCrew += 1
    elif mealOfDay == SATURDAY_DINNER:
        CookStart = time(hour = 16, minute=  20)
        CookMid = time(hour = 17, minute=  20)
        CookEnd = time(hour = 18, minute=  20)
        crewStart = time(hour = 19)
        crewEnd = time(hour = 20, minute=  30) #until finished
        numCrew += 1
    elif mealOfDay == SUNDAY_LUNCH:
        CookStart = time(hour = 10, minute=  20)
        CookMid = time(hour = 11, minute=  20)
        CookEnd = time(hour = 12, minute=  20)
        crewStart = time(hour = 13)
        crewEnd = time(hour = 14, minute = 30) #until finished
        numCrew += 1
    elif mealOfDay == COMMANDO_CREW:
        crewStart = time(hour = 20, minute=  30)
        crewEnd = time(hour = 21, minute=  30)
        numCrew = 3
        numCook = 0

    if mealOfDay in [BREAKFAST, COMMANDO_CREW]:
        newCrew = Crew(start_time = crewStart, end_time = crewEnd)
        newCrew.save()
        for i in range(numCrew):
            index = randint(len(members), size=1)
            index = int(index[0])
            pic = i == 0
            newCrewShift = CrewShift(crew_obj = newCrew, member = members[index], is_pic = pic)
            newCrewShift.save()
            if pic:
                newCrew.pic = newCrewShift
                newCrew.save()
        mealObj.crew = newCrew
        newCrew.save()
    else:
        newCook = Cook(start_time = crewStart, mid_time = CookMid, end_time = crewEnd)
        newCrew = Crew(start_time = crewStart, end_time = crewEnd)
        newCook.save()
        newCrew.save()
        for i in range(numCook): #fill new cook shift with members
            index = randint(len(members), size=1)
            index = int(index[0])
            headCook = i == 0
            newCookShift = CookShift(cook_obj = newCook, member = members[index], shift_selection = shiftOptions[i], is_head_cook = headCook)
            newCookShift.save()
            if headCook:
                newCrew.head_cook = newCookShift
                newCook.save()
        for i in range(numCrew): #fill new crew shift with members
            index = randint(len(members), size=1)
            index = int(index[0])
            pic = i == 0
            newCrewShift = CrewShift(crew_obj = newCrew, member = members[index], is_pic = pic)
            newCrewShift.save()
            if pic:
                newCrew.pic = newCrewShift
                newCrew.save()
        mealObj.cook = newCook
        mealObj.crew = newCrew
        newCook.save()
        newCrew.save()


normal_meals = [BREAKFAST, LUNCH, DINNER]

normal_days = [MONDAY, TUESDAY, WEDNESDAY, THURSDAY]


for coop in [keep, tank, pyle, harkness, third_world]:
    members = Member.objects.filter(coop = coop)
    if coop == keep:
        crew_required_members = 4
        cook_required_members = 5
    elif coop == tank:
        crew_required_members = 4
        cook_required_members = 5
    elif coop == pyle:
        crew_required_members = 5
        cook_required_members = 6
    elif coop == harkness:
        crew_required_members = 5
        cook_required_members = 6
    elif coop == third_world:
        crew_required_members = 4
        cook_required_members = 5
    for day in normal_days:
        for meal in normal_meals:
            newMeal = Meal(coop = coop, meal_of_the_day = meal, day_of_week = day)
            addMeal(meal, members, cook_required_members, crew_required_members, newMeal)
            newMeal.save()
    for day in [FRIDAY, SATURDAY, SUNDAY]:
        meal = BREAKFAST
        newMeal = Meal(coop = coop, meal_of_the_day = meal, day_of_week = day)
        addMeal(meal, members, cook_required_members, crew_required_members, newMeal)
        newMeal.save()

    meal = LUNCH
    day = FRIDAY
    newMeal = Meal(coop = coop, meal_of_the_day = meal, day_of_week = day)
    addMeal(meal, members, cook_required_members, crew_required_members, newMeal)
    newMeal.save()
    day = SATURDAY
    newMeal = Meal(coop = coop, meal_of_the_day = meal, day_of_week = day)
    addMeal(meal, members, cook_required_members, crew_required_members, newMeal)
    newMeal.save()

    meal = DINNER
    day = SUNDAY
    newMeal = Meal(coop = coop, meal_of_the_day = meal, day_of_week = day)
    addMeal(meal, members, cook_required_members, crew_required_members, newMeal)
    newMeal.save()

    meal = PIZZA_NIGHT
    day = FRIDAY
    newMeal = Meal(coop = coop, meal_of_the_day = meal, day_of_week = day)
    addMeal(meal, members, cook_required_members, crew_required_members, newMeal)
    newMeal.save()

    meal = SATURDAY_DINNER
    day = SATURDAY
    newMeal = Meal(coop = coop, meal_of_the_day = meal, day_of_week = day)
    addMeal(meal, members, cook_required_members, crew_required_members, newMeal)
    newMeal.save()

    meal = SUNDAY_LUNCH
    day = SUNDAY
    newMeal = Meal(coop = coop, meal_of_the_day = meal, day_of_week = day)
    addMeal(meal, members, cook_required_members, crew_required_members, newMeal)
    newMeal.save()

    meal = COMMANDO_CREW
    day = WEDNESDAY
    newMeal = Meal(coop = coop, meal_of_the_day = meal, day_of_week = day)
    addMeal(meal, members, cook_required_members, crew_required_members, newMeal)
    newMeal.save()
    day = SUNDAY
    newMeal = Meal(coop = coop, meal_of_the_day = meal, day_of_week = day)
    addMeal(meal, members, cook_required_members, crew_required_members, newMeal)
    newMeal.save()


    





#officer positions:
#iDLEC, DLEC, Food Safety Coordinator, New Member Trainer, KitchCo, Membership Coordinator, DLEC, Accessibility Coordinator, Food Buyer and Unpacker, Board Representitive, Treasurer, Head Cook, Pizza Maker, Dough Maker, Tasty Things Maker, Bread Maker, Granola Maker, Dietary Restrictions Maker, Long Range Planning Committee Representitive, Environmental Concerns Committee Representitive, Programming COmmittee Representitve, OSCA Foundation Representitive, Historian, Cheese Slicer, 

# # Create a new record using the model's constructor.
# record = MyModelName(my_field_name="Instance #1")

# # Save the object into the database.
# record.save()

# # Access model field values using Python attributes.
# print(record.id) # should return 1 for the first record.
# print(record.my_field_name) # should print 'Instance #1'

# # Change record by modifying the fields, then calling save().
# record.my_field_name = "New Instance Name"
# record.save()


# all_books = Book.objects.all()

# wild_books = Book.objects.filter(title__contains='wild')
# number_wild_books = wild_books.count()