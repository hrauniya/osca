from csv import Dialect
import os
import django
from numpy.random import choice, randint
from datetime import time
from osca.wsgi import *
from catalog.models import Coop, Member, Officer, AllergySeverity, Allergy, Budget, Meal, Menu, Shift, WorkChartRow

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
# PIZZA_NIGHT = 4
# SATURDAY_DINNER = 5
# SUNDAY_LUNCH = 6
COMMANDO_CREW = 4


MONDAY = 1
TUESDAY = 2
WEDNESDAY = 3
THURSDAY = 4
FRIDAY = 5
SATURDAY = 6
SUNDAY = 7



meals = [BREAKFAST, LUNCH, DINNER, COMMANDO_CREW]

days = [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY]

breakFastTimes = ["9:20-10:20"]

lunchCookTimes = ["10:20-12:20", "10:20-12:20", "10:20-11:20", "10:20-11:20", "11:20-12:20", "11:20-12:20"]

lunchCrewTimes = ["1:00-2:00", "1:00-2:00", "1:00-2:00", "1:00-2:00", "1:00-2:00"]

dinnerCooktimes = ["4:20-6:20", "4:20-6:20", "4:20-5:20", "4:20-5:20", "5:20-6:20", "5:20-6:20"]

dinnerCrewTimes = ["7:00-8:00", "7:00-8:00", "7:00-8:00", "7:00-8:00", "7:00-8:00"]

commandoCrewTimes = ["8:30-9:30", "8:30-9:30", "8:30-9:30"]


for coop in [keep, tank, pyle, harkness, third_world]:
    members = Member.objects.filter(coop = coop)
    for meal in meals:
        mondayMeal = Meal(coop = coop, meal_of_the_day = meal, day_of_week = MONDAY)
        mondayMeal.save()

        tuesdayMeal = Meal(coop = coop, meal_of_the_day = meal, day_of_week = TUESDAY)
        tuesdayMeal.save()

        wednesdayMeal = Meal(coop = coop, meal_of_the_day = meal, day_of_week = WEDNESDAY)
        wednesdayMeal.save()

        thursdayMeal = Meal(coop = coop, meal_of_the_day = meal, day_of_week = THURSDAY)
        thursdayMeal.save()

        fridayMeal = Meal(coop = coop, meal_of_the_day = meal, day_of_week = FRIDAY)
        fridayMeal.save()

        saturdayMeal = Meal(coop = coop, meal_of_the_day = meal, day_of_week = SATURDAY)
        saturdayMeal.save()

        sundayMeal = Meal(coop = coop, meal_of_the_day = meal, day_of_week = SUNDAY)
        sundayMeal.save()
        if meal == BREAKFAST:
            for shiftTime in breakFastTimes:
                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                monday = Shift(cook = False, is_pic = True, meal = mondayMeal, member = memberForShift)
                monday.save()

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                tuesday = Shift(cook = False, is_pic = True, meal = tuesdayMeal, member = memberForShift)
                tuesday.save()

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                wednesday = Shift(cook = False, is_pic = True, meal = wednesdayMeal, member = memberForShift)
                wednesday.save()

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                thursday = Shift(cook = False, is_pic = True, meal = thursdayMeal, member = memberForShift)
                thursday.save()

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                friday = Shift(cook = False, is_pic = True, meal = fridayMeal, member = memberForShift)
                friday.save()

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                saturday = Shift(cook = False, is_pic = True, meal = saturdayMeal, member = memberForShift)
                saturday.save()

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                sunday = Shift(cook = False, is_pic = True, meal = sundayMeal, member = memberForShift)
                sunday.save()
                newWorkChartRow = WorkChartRow(coop = coop, time = shiftTime, cook = False, pic = True, monday = monday, tuesday = tuesday, wednesday = wednesday, thursday = thursday, friday = friday, saturday = saturday, sunday = sunday)
                newWorkChartRow.save()
        if meal == LUNCH:
            i = 0
            for shiftTime in lunchCookTimes:
                pic = i==0
                cook = True

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                monday = Shift(cook = cook, is_pic = pic, meal = mondayMeal, member = memberForShift)
                monday.save()

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                tuesday = Shift(cook = False, is_pic = True, meal = tuesdayMeal, member = memberForShift)
                tuesday.save()

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                wednesday = Shift(cook = cook, is_pic = pic, meal = wednesdayMeal, member = memberForShift)
                wednesday.save()

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                thursday = Shift(cook = cook, is_pic = pic, meal = thursdayMeal, member = memberForShift)
                thursday.save()

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                friday = Shift(cook = cook, is_pic = pic, meal = fridayMeal, member = memberForShift)
                friday.save()

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                saturday = Shift(cook = cook, is_pic = pic, meal = saturdayMeal, member = memberForShift)
                saturday.save()

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                sunday = Shift(cook = cook, is_pic = pic, meal = sundayMeal, member = memberForShift)
                sunday.save()
                i+=1
                newWorkChartRow = WorkChartRow(coop = coop, time = shiftTime, cook = cook, pic = pic, monday = monday, tuesday = tuesday, wednesday = wednesday, thursday = thursday, friday = friday, saturday = saturday, sunday = sunday)
                newWorkChartRow.save()
            i = 0
            for shiftTime in lunchCrewTimes:
                pic = i==0
                cook = False

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                monday = Shift(cook = cook, is_pic = pic, meal = mondayMeal, member = memberForShift)
                monday.save()

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                tuesday = Shift(cook = False, is_pic = True, meal = tuesdayMeal, member = memberForShift)
                tuesday.save()

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                wednesday = Shift(cook = cook, is_pic = pic, meal = wednesdayMeal, member = memberForShift)
                wednesday.save()

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                thursday = Shift(cook = cook, is_pic = pic, meal = thursdayMeal, member = memberForShift)
                thursday.save()

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                friday = Shift(cook = cook, is_pic = pic, meal = fridayMeal, member = memberForShift)
                friday.save()

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                saturday = Shift(cook = cook, is_pic = pic, meal = saturdayMeal, member = memberForShift)
                saturday.save()

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                sunday = Shift(cook = cook, is_pic = pic, meal = sundayMeal, member = memberForShift)
                sunday.save()
                i+=1
                newWorkChartRow = WorkChartRow(coop = coop, time = shiftTime, cook = cook, pic = pic, monday = monday, tuesday = tuesday, wednesday = wednesday, thursday = thursday, friday = friday, saturday = saturday, sunday = sunday)
                newWorkChartRow.save()
        if meal == DINNER:
            i = 0            
            for shiftTime in dinnerCooktimes:
                pic = i==0
                cook = True

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                monday = Shift(cook = cook, is_pic = pic, meal = mondayMeal, member = memberForShift)
                monday.save()

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                tuesday = Shift(cook = False, is_pic = True, meal = tuesdayMeal, member = memberForShift)
                tuesday.save()

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                wednesday = Shift(cook = cook, is_pic = pic, meal = wednesdayMeal, member = memberForShift)
                wednesday.save()

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                thursday = Shift(cook = cook, is_pic = pic, meal = thursdayMeal, member = memberForShift)
                thursday.save()

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                friday = Shift(cook = cook, is_pic = pic, meal = fridayMeal, member = memberForShift)
                friday.save()

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                saturday = Shift(cook = cook, is_pic = pic, meal = saturdayMeal, member = memberForShift)
                saturday.save()

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                sunday = Shift(cook = cook, is_pic = pic, meal = sundayMeal, member = memberForShift)
                sunday.save()
                i+=1
                newWorkChartRow = WorkChartRow(coop = coop, time = shiftTime, cook = cook, pic = pic, monday = monday, tuesday = tuesday, wednesday = wednesday, thursday = thursday, friday = friday, saturday = saturday, sunday = sunday)
                newWorkChartRow.save()
            i = 0
            for shiftTime in dinnerCrewTimes:
                pic = i==0
                cook = False

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                monday = Shift(cook = cook, is_pic = pic, meal = mondayMeal, member = memberForShift)
                monday.save()

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                tuesday = Shift(cook = False, is_pic = True, meal = tuesdayMeal, member = memberForShift)
                tuesday.save()

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                wednesday = Shift(cook = cook, is_pic = pic, meal = wednesdayMeal, member = memberForShift)
                wednesday.save()

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                thursday = Shift(cook = cook, is_pic = pic, meal = thursdayMeal, member = memberForShift)
                thursday.save()

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                friday = Shift(cook = cook, is_pic = pic, meal = fridayMeal, member = memberForShift)
                friday.save()

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                saturday = Shift(cook = cook, is_pic = pic, meal = saturdayMeal, member = memberForShift)
                saturday.save()

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                sunday = Shift(cook = cook, is_pic = pic, meal = sundayMeal, member = memberForShift)
                sunday.save()
                i+=1
                newWorkChartRow = WorkChartRow(coop = coop, time = shiftTime, cook = cook, pic = pic, monday = monday, tuesday = tuesday, wednesday = wednesday, thursday = thursday, friday = friday, saturday = saturday, sunday = sunday)
                newWorkChartRow.save()
        if meal == COMMANDO_CREW:
            i = 0
            for shiftTime in commandoCrewTimes:
                pic = i==0
                cook = False

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                wednesday = Shift(cook = cook, is_pic = pic, meal = wednesdayMeal, member = memberForShift)
                wednesday.save()

                index = randint(len(members), size=1)
                index = int(index[0])
                memberForShift = members[index]
                saturday = Shift(cook = cook, is_pic = pic, meal = saturdayMeal, member = memberForShift)
                saturday.save()
                i+=1
                newWorkChartRow = WorkChartRow(coop = coop, time = shiftTime, cook = cook, pic = pic, wednesday = wednesday, saturday = saturday)
                newWorkChartRow.save()    





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