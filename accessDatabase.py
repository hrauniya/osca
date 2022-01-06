import os
import django
import random

from osca.wsgi import *
from catalog.models import Coop, Member, Officer, Workchart_slot, AllergySeverity, Allergy, Budget


memberlist = list(Member.objects.all())
for member in memberlist:
    print(member)