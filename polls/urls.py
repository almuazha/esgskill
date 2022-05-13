from django.urls import path

from .views import index, umfrage_details, vote, results, idee_reg
# , PollDetailView, vote, ResultsDetailView

# app_name = 'polls'
urlpatterns = [
    # hey, wenn eine Anfrage an / reinkommt, dann übergebe das der Funktion
    # index aus der views.py
    path('', index, name='index'),
    path('poll/<str:slug>/', umfrage_details, name = 'umfrage-detail'),
    path('idee_reg>/', idee_reg, name = 'idee_reg'),
    path('poll/<str:slug>/vote/', vote, name='vote'),
    path('poll/<str:slug>/results/', results, name='results'),
    
]