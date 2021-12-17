from django.shortcuts import render

# Create your views here.

from .models import Coop, Member, Officer, Workchart_slot, Allergy, AllergySeverity, Budget

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_coops = Coop.objects.all().count()
    num_members = Member.objects.all().count()

    # Available books (status = 'a')
    #num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    #num_authors = Author.objects.count()

    context = {
        'num_coops': num_coops,
        'num_members': num_members,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)