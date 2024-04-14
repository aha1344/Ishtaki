from django.shortcuts import render, redirect
from .choices import hospitals, ministries, institutions, prisons, banks, courts, universities, military, police, general_security, sector_types, corruption_types
from django.http import JsonResponse
from .forms import ReportForm
from .models import Report
from django.db.models import Count
from django.db.models.functions import ExtractYear




# function that accepts a get request to the server in order to retrieve the sector names associated with the sector type chosen in the form, return the sector names as JSON.
def load_sector_names(request):
    sector_type = request.GET.get('sector_type')
    names = []
    if sector_type == 'hospitals':
        names = hospitals
    elif sector_type == 'ministries':
        names = ministries
    elif sector_type == 'institutions':
        names = institutions
    elif sector_type == 'banks':
        names = banks
    elif sector_type == 'prisons':
        names = prisons
    elif sector_type == 'courts':
        names = courts
    elif sector_type == 'universities':
        names = universities
    elif sector_type == 'military':
        names = military
    elif sector_type == 'police':
        names = police
    elif sector_type == 'general_security':
        names = general_security
    return JsonResponse(names, safe=False)

# function that creates an instance of the form and renders it in the html file, it saves the report into the database if the form is valid.
def report_view(request):
    if request.method == 'POST':
         # validate the form
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin/')
    else:
        form = ReportForm() # get an empty form 
    return render(request, 'report/report.html', {'form': form})

# renders the visualization page for every sector type
def statistics(request, sector_type):
    return render(request, 'report/statistics.html', {'sector_type':sector_type, 'corruption_types':corruption_types, 'sector_types':sector_types})

# function that catches an ajax request to send report statistics as a json response to the statistics html page. 
# to add an aggregation just add it inside this function and put in context
def load_statistics(request, sector_type):

    corruption_type_chosen = request.GET.get('corruption_type', 'none')

    # Aggregate counts by sector type (filtering by a specific sector type)
    temporal_sector_type_count = list(Report.objects
                                    .filter(public_sector_type=sector_type)
                                    .annotate(year=ExtractYear('date_of_incident'))
                                    .values('year')
                                    .annotate(total=Count('id'))
                                    .order_by('year'))
    
    temporal_sector_type_ct_count= list(Report.objects
                                    .filter(public_sector_type=sector_type, corruption_type=corruption_type_chosen)
                                    .annotate(year=ExtractYear('date_of_incident'))
                                    .values('year')
                                    .annotate(total=Count('id'))
                                    .order_by('year'))

# Counting reports per corruption type in a specific public sector
    sector_count_per_corruption_type = list(Report.objects
                                     .filter(public_sector_type=sector_type)
                                     .values('corruption_type')  # Group by corruption type
                                     .annotate(total=Count('id'))  # Count occurrences
                                     )
    

        

    context = {
        'temporal_sector_type_count': temporal_sector_type_count,
        'temporal_sector_type_ct_count': temporal_sector_type_ct_count,
        'sector_count_per_corruption_type':sector_count_per_corruption_type,
    }

    return JsonResponse(context)

# function to display home page.
def HomePage(request):
    sectors  = [sector[1] for sector in sector_types]
    return render(request, "report/home.html", {"sectors":sectors})