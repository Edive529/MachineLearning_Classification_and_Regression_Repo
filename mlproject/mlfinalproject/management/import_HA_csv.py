import csv
from datetime import datetime
from django.core.management import BaseCommand
from mlfinalproject.models import classification


class Command(BaseCommand):
    help = 'Import heartproblems data into PostgreSQL'

    def handle(self, *args, **options):
        file_path = 'dataset/heartproblems.csv'
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:

                # Convert empty values to None
                for field in ['age', 'gender', 'impulse', 'pressurehigh', 'pressurelow', 'glucose', 'kcm', 'troponin', 'classification']:
                    row[field] = row[field] if row[field] != '' else None

                classification.objects.create(
                    age=row['age'],
                    gender=row['gender'],
                    impulse=row['impulse'],
                    pressurehigh=row['pressurehigh'],
                    pressurelow=row['pressurelow'],
                    glucose=row['glucose'],
                    kcm=row['kcm'],
                    troponin=row['troponin'],
                    classification=row['classification'],
                )
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))