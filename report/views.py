from django.shortcuts import render, redirect
from .choices import hospitals, ministries, institutions, prisons, banks, courts, universities, military, police, general_security, sector_types
from django.http import JsonResponse
from .forms import ReportForm
from .models import Report
from django.db.models import Count



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