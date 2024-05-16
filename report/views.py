from django.shortcuts import render, redirect
from .choices import hospitals, ministries, institutions, prisons, banks, courts, universities, sector_types
from django.http import JsonResponse
from .forms import ReportForm
from .models import Report
from django.db.models import Count
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .choices import corruption_types, sector_types, cities_coordinates



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
    elif sector_type == 'general_security':
        names = general_security
    return JsonResponse(names, safe=False)

# function that creates an instance of the form and renders it in the html file, it saves the report into the database if the form is valid.
def report_view(request):
    if request.method == 'POST': # validate the form
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin/')
    else:
        form = ReportForm() # get an empty form 
    return render(request, 'report/report.html', {'form': form})
# different queries that can be used for visualization. Temporary function that will change according to visualization needs.
def statistics_view(request):
    corruption_type_count = Report.objects.values('corruption_type').annotate(total=Count('corruption_type'))

    # Count reports by public sector type
    public_sector_type_count = Report.objects.values('public_sector_type').annotate(total=Count('public_sector_type'))

    # Count reports by city
    city_count = Report.objects.values('city').annotate(total=Count('city'))

    latest_report = Report.objects.latest('date_of_incident')

    context = {
        'corruption_type_count': corruption_type_count,
        'public_sector_type_count': public_sector_type_count,
        'city_count': city_count,
        'latest_report': latest_report,
    }
    
    return render(request, 'report/visualization.html', context)

# view to display home page.
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