from django.contrib import admin
from .models import Coops, Members, Workchart_slots, Officers, Budget, Allergies

admin.site.register(Coops)
admin.site.register(Members)
admin.site.register(Workchart_slots)
admin.site.register(Officers)
admin.site.register(Budget)
admin.site.register(Allergies)

