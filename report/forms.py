from django import forms
from .models import Report
from .choices import corruption_types, sector_types, cities
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

class ReportForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Report
        fields = ['corruption_type', 'public_sector_type', 'public_sector_name', 'date_of_incident', 'city', 'street','captcha']
        widgets = {
            'corruption_type': forms.Select(attrs={'id': 'corruption_type_id'}, choices= corruption_types),
            'public_sector_type': forms.Select(attrs={'id': 'public_sector_type_id'}, choices= sector_types),
            'public_sector_name': forms.Select(attrs={'id': 'public_sector_name_id'}, choices=[('', '')]),  
            'date_of_incident': forms.DateTimeInput(attrs={'type': 'datetime-local', 'id': 'date_of_incident_id'}),
            'city': forms.Select(attrs={'id': 'city_id'}, choices= cities),
            'street': forms.TextInput(attrs={'id': 'street_id'}),
            
        }