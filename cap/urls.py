from django.urls import path, include
from . import views

urlpatterns = [
    path('report/', views.report_view, name='report_form'),
    path('ajax/load_sector_names/', views.load_sector_names, name='ajax_load_sector_names'),
    # we wont use the load sector path, its just for ajax purposes.
]
