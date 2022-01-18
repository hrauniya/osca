from django.forms import ModelForm


from catalog.models import Member 
from catalog.models import Workchart_slot
from catalog.models import Allergy
from catalog.models import Budget
from catalog.models import Officer

class addMemberInfo(ModelForm):
   

    class Meta:
        model=Member
        fields=['id','first_name','last_name','preferred_name','tnumber','coop','email','pronouns','time_aid','missed_jobes']

class addOfficerInfo(ModelForm):
    
    class Meta:
        model= Officer
        fields=['id','coop','member','position_name','position_description','hours_required','emergency_contact','all_osca']

