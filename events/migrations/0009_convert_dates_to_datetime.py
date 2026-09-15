# events/migrations/0009_convert_dates_to_datetime.py

from django.db import migrations, models  # <-- models import add kiya
from datetime import datetime, time

def convert_dates_to_datetime(apps, schema_editor):
    """Convert date fields to datetime with default time"""
    Event = apps.get_model('events', 'Event')
    
    # Saare events ko update karein
    for event in Event.objects.all():
        # Date ko datetime mein convert karein (12:00 PM default time)
        event.start_date = datetime.combine(event.start_date, time(12, 0))
        event.end_date = datetime.combine(event.end_date, time(14, 0))
        event.save()
        print(f"Updated: {event.event_name}")

def reverse_conversion(apps, schema_editor):
    """Reverse conversion (if needed)"""
    Event = apps.get_model('events', 'Event')
    
    for event in Event.objects.all():
        # DateTime se sirf date part lein
        event.start_date = event.start_date.date()
        event.end_date = event.end_date.date()
        event.save()

class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_budgetfinance'),
    ]

    operations = [
        # Pehle data convert karein
        migrations.RunPython(convert_dates_to_datetime, reverse_conversion),
        
        # Phir field type change karein
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(),
        ),
    ]