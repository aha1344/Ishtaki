from django.shortcuts import render, redirect
from .choices import hospitals, ministries, institutions, prisons, banks, courts, universities, sector_types
from django.http import JsonResponse
from .forms import ReportForm
from .models import Report
from django.db.models import Count
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .choices import corruption_types, sector_types, cities_coordinates


from .choices import hospitals, ministries, institutions, prisons, banks, courts, universities, sector_types, corruption_types, security_institutions
from django.http import JsonResponse
from .forms import ReportForm
from .models import Report
from django.db.models import Count,F
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
    elif sector_type == 'security_institutions':
        names = security_institutions
    return JsonResponse(names, safe=False)

# function that creates an instance of the form and renders it in the html file, it saves the report into the database if the form is valid.
def report_view(request):
    if request.method == 'POST':
         # validate the form
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    else:
        form = ReportForm() # get an empty form 
    return render(request, 'report/report.html', {'form': form})

# renders the visualization page for every sector type
def statistics(request, sector_type):
    return render(request, 'report/statistics.html', {'sector_type':sector_type, 'corruption_types':corruption_types, 'sector_types':sector_types})

# function that catches an ajax request to send report statistics as a json response to the statistics html page. 
# to add an aggregation just add it inside this function and put in context
def load_statistics(request, sector_type):
    # Get list of corruption types; default to not applying this filter if list is empty
    corruption_types_chosen = request.GET.getlist('corruption_type[]')

    # Aggregate counts by sector type (filtering by a specific sector type)
    temporal_sector_type_count = list(Report.objects
                                    .filter(public_sector_type=sector_type)
                                    .annotate(year=ExtractYear('date_of_incident'))
                                    .values('year')
                                    .annotate(total=Count('id'))
                                    .order_by('year'))
    
    if corruption_types_chosen:
        filtered_query = Report.objects.filter(public_sector_type=sector_type, corruption_type__in=corruption_types_chosen)
    else:
        filtered_query = Report.objects.filter(public_sector_type=sector_type)

    
    temporal_sector_type_ct_count= list(filtered_query.annotate(year=ExtractYear('date_of_incident')).values('year', 'corruption_type').annotate(total=Count('id')).order_by('year', 'corruption_type'))



    # Counting reports per corruption type in a specific public sector
    sector_count_per_corruption_type = list(Report.objects
                                     .filter(public_sector_type=sector_type)
                                     .values('corruption_type')  # Group by corruption type
                                     .annotate(total=Count('id'))  # Count occurrences
                                     )

    sector_data = list(Report.objects.filter(public_sector_type=sector_type)
                                    .values(name=F('public_sector_name'))
                                    .annotate(value=Count('id'))
                                    .order_by('name'))

    context = {
        'temporal_sector_type_count': temporal_sector_type_count,
        'temporal_sector_type_ct_count': temporal_sector_type_ct_count,
        'sector_count_per_corruption_type':sector_count_per_corruption_type,
        'sector_name_data':sector_data,
    }

    return JsonResponse(context)

# function to display home page.
def HomePage(request):
    sectors  = [sector[1] for sector in sector_types]
    return render(request, "report/home.html", {"sectors":sectors})


@require_GET
def corruption_heatmap_data_view(request):
    corruption_type = request.GET.get('corruption_type')
    public_sector_type = request.GET.get('public_sector_type')

    reports = Report.objects.all()
    if corruption_type:
        reports = reports.filter(corruption_type=corruption_type)
    if public_sector_type:
        reports = reports.filter(public_sector_type=public_sector_type)

    data = []
    for report in reports:
        city = report.city
        if city in cities_coordinates:
            latitude, longitude = cities_coordinates[city]
            data.append({
                'latitude': latitude,
                'longitude': longitude,
                'corruption_type': report.corruption_type,
                'public_sector_type': report.public_sector_type,
                'public_sector_name': report.public_sector_name,
                'date_of_incident': report.date_of_incident.isoformat(),
                'street': report.street,
            })

    return JsonResponse(data, safe=False)

def corruption_heatmap_view(request):
    return render(request, 'report/heatmap.html')

def get_choices_view(request):
    return JsonResponse({
        'corruption_types': corruption_types,
        'sector_types': sector_types,
    })
