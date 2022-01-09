import os
import django
from numpy.random import choice

from osca.wsgi import *
from catalog.models import Coop, Member, Officer, Workchart_slot, AllergySeverity, Allergy, Budget

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