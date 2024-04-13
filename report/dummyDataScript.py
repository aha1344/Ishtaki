import random
from faker import Faker
from datetime import datetime, timedelta
from report.models import Report
from report import choices

# this file is a script that can be used to populat the database with dummy data. To do so, go to terminal:
# python manage.py shell
# copy this whole page and paste it there and press enter.

fake = Faker()


sector_names_mapping = {
    'hospitals': choices.hospitals,
    'ministries': choices.ministries,
    'institutions': choices.institutions,
    'banks': choices.banks,
    'prisons': choices.prisons,
    'courts': choices.courts,
    'universities': choices.universities,
    'military': choices.military,
    'police': choices.police,
    'general_security': choices.general_security,
}

corruption_types = [choice[0] for choice in choices.corruption_types]
sector_types = [choice[0] for choice in choices.sector_types]
city_choices = [choice[0] for choice in choices.cities]

for _ in range(10000):
    ct = random.choice(corruption_types)
    sector_type = random.choice(sector_types)
    sector_name = random.choice(sector_names_mapping[sector_type])
    city = random.choice(city_choices)
    street = fake.street_name()
    date_of_incident = datetime.now() - timedelta(days=random.randint(0, 7650))
    Report.objects.create(
        corruption_type=ct,
        public_sector_type=sector_type,
        public_sector_name=sector_name,
        date_of_incident=date_of_incident,
        city=city,
        street=street
    )
