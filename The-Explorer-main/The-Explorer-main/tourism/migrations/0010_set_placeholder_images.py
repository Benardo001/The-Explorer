from django.db import migrations


def set_placeholders(apps, schema_editor):
    Beach = apps.get_model('tourism', 'Beach')
    Transport = apps.get_model('tourism', 'Transport')
    Accommodation = apps.get_model('tourism', 'Accommodation')
    TouristAttraction = apps.get_model('tourism', 'TouristAttraction')

    mapping = [
        (Beach, 'beach_images/beach_placeholder.svg'),
        (Transport, 'transport_images/transport_placeholder.svg'),
        (Accommodation, 'accommodation_images/accommodation_placeholder.svg'),
        (TouristAttraction, 'attraction_images/attraction_placeholder.svg'),
    ]

    for Model, path in mapping:
        try:
            for obj in Model.objects.all():
                img = getattr(obj, 'image', None)
                # Django ImageField truthiness: check name
                if not img or not getattr(img, 'name', None):
                    obj.image = path
                    obj.save()
        except Exception:
            # be tolerant during migration
            continue


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0009_add_contact_feedback'),
    ]

    operations = [
        migrations.RunPython(set_placeholders),
    ]
