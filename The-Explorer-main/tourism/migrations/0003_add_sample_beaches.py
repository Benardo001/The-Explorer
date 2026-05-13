from django.db import migrations


def create_sample_beaches(apps, schema_editor):
    Beach = apps.get_model('tourism', 'Beach')
    samples = [
        {
            'name': 'Diani Beach',
            'location': 'Diani, Kwale',
            'description': 'A white-sand coastal paradise with vibrant resorts, water sports and coral gardens.',
            'activities': 'Snorkeling, kite surfing, beach volleyball, sunset cruises',
            'price': 4500,
            'latitude': -4.3000,
            'longitude': 39.5833,
        },
        {
            'name': 'Nyali Beach',
            'location': 'Nyali, Mombasa',
            'description': 'A lively beach destination near the city with restaurants, nightlife, and marine parks.',
            'activities': 'Swimming, dolphin watching, fishing, seaside dining',
            'price': 3800,
            'latitude': -4.0434,
            'longitude': 39.6525,
        },
        {
            'name': 'Bamburi Beach',
            'location': 'Bamburi, Mombasa',
            'description': 'Perfect for relaxation, family holidays and easy access to theme parks and resorts.',
            'activities': 'Beach lounging, snorkeling, jet skiing, local markets',
            'price': 3200,
            'latitude': -3.9874,
            'longitude': 39.7191,
        },
    ]
    for sample in samples:
        Beach.objects.get_or_create(name=sample['name'], defaults=sample)


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0002_remove_review_user_name_beach_image_beach_latitude_and_more'),
    ]

    operations = [
        migrations.RunPython(create_sample_beaches),
    ]
