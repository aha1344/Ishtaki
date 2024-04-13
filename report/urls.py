from django.urls import path, include
from . import views

urlpatterns = [
    path('report/', views.report_view, name='report_form'),
    path('ajax/load_sector_names/', views.load_sector_names, name='ajax_load_sector_names'),
    # we wont use the load sector path, its just for ajax purposes.
    path('home/', views.HomePage, name="HomePage"),
    path('statistics/<str:sector_type>/', views.statistics, name='statistics'),
    path('ajax/load_statistics/<str:sector_type>/', views.load_statistics, name='ajax_load_statistics'),
    # we wont use the load sector path, its just for ajax purposes.
]
