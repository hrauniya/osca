from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('allcoops/', views.AllCoopView.as_view(), name='all-coops'),
    path('allmembers/', views.AllMembersView.as_view(), name='all-members'),
    path('allofficers/', views.AllOfficersView.as_view(), name='all-officers'),
    path('addmemberinfo/',views.MemberCreate.as_view(),name='member-create'),
    path('addofficerinfo/',views.OfficersCreate.as_view(),name='officer-create'),
    path('keepworkchart/', views.WorkChartKeep.as_view(),name='keep-work-chart'),
]