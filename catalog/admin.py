from django.contrib import admin
from .models import Coop, Member, Officer, Budget, Allergy

admin.site.register(Coop)
admin.site.register(Member)
#admin.site.register(Workchart_slot)
admin.site.register(Officer)
admin.site.register(Budget)
admin.site.register(Allergy)

