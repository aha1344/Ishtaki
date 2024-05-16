from django.urls import path, include
from . import views
from .views import corruption_heatmap_view, corruption_heatmap_data_view, get_choices_view

urlpatterns = [
    path('report/', views.report_view, name='report_form'),
    path('ajax/load_sector_names/', views.load_sector_names, name='ajax_load_sector_names'),
    # we wont use the load sector path, its just for ajax purposes.
    path('home/', views.HomePage, name="HomePage"),
    path('heatmap/', corruption_heatmap_view, name='corruption_heatmap'),
    path('corruption-heatmap/', corruption_heatmap_data_view, name='corruption_heatmap_data'),
    path('choices/', get_choices_view, name='get_choices'),
    path('statistics/<str:sector_type>/', views.statistics, name='statistics'),
    path('ajax/load_statistics/<str:sector_type>/', views.load_statistics, name='ajax_load_statistics'),
    path('userdocumentation/', views.user_documentation, name="user_documentation"),
    path('developerdocumentation/', views.developer_documentation, name="developer_documentation"),



    # we wont use the load sector path, its just for ajax purposes.
]
