from django.db import migrations


def create_sample_attractions(apps, schema_editor):
    TouristAttraction = apps.get_model('tourism', 'TouristAttraction')
    samples = [
        {
            'name': 'Mount Kenya',
            'location': 'Mount Kenya National Park, Kirinyaga County',
            'category': 'mountain',
            'description': 'Africa\'s second-highest mountain standing at 5,199m (17,057 ft). Mount Kenya offers spectacular hiking trails, diverse ecosystems from rainforest to alpine meadows, and stunning views of the surrounding landscape.',
            'entry_fee': 3500,
            'best_time_to_visit': 'January - February, July - October',
            'latitude': 0.1517,
            'longitude': 37.3039,
        },
        {
            'name': 'Masai Mara National Reserve',
            'location': 'Narok County, Southwest Kenya',
            'category': 'wildlife',
            'description': 'One of the world\'s most spectacular wildlife reserves, home to lions, elephants, giraffes, zebras, and the annual wildebeest migration. Offers exceptional safari experiences and guided wildlife tours.',
            'entry_fee': 5000,
            'best_time_to_visit': 'July - October (Great Migration)',
            'latitude': -1.2921,
            'longitude': 34.8888,
        },
        {
            'name': 'Amboseli National Park',
            'location': 'Kajiado County, Southern Kenya',
            'category': 'wildlife',
            'description': 'Famous for its large elephant herds and stunning views of Mount Kilimanjaro. The park features diverse wildlife and excellent photography opportunities with Kilimanjaro as a backdrop.',
            'entry_fee': 4500,
            'best_time_to_visit': 'June - March',
            'latitude': -2.6558,
            'longitude': 37.2639,
        },
        {
            'name': 'Tsavo National Park',
            'location': 'Taita-Taveta County, Southeast Kenya',
            'category': 'wildlife',
            'description': 'One of the largest national parks in Kenya, divided into Tsavo East and Tsavo West. Home to thousands of elephants, lions, and other wildlife. Features volcanic landscapes, Mzima Springs, and diverse habitats.',
            'entry_fee': 3800,
            'best_time_to_visit': 'June - October',
            'latitude': -2.8000,
            'longitude': 37.7000,
        },
        {
            'name': 'Lake Nakuru National Park',
            'location': 'Nakuru County, Rift Valley',
            'category': 'national_park',
            'description': 'A scenic national park famous for its flamingos, rhinoceros, and lions. The alkaline lake is surrounded by woodland and home to diverse bird species. Great for both wildlife viewing and bird watching.',
            'entry_fee': 3200,
            'best_time_to_visit': 'Year-round',
            'latitude': -0.3610,
            'longitude': 36.0851,
        },
        {
            'name': 'Lake Naivasha',
            'location': 'Nakuru County, Rift Valley',
            'category': 'island',
            'description': 'A freshwater lake in the Rift Valley with beautiful scenery, diverse bird species, and boat tours to Crescent Island. Popular for fishing, water sports, and wildlife viewing.',
            'entry_fee': 2500,
            'best_time_to_visit': 'Year-round',
            'latitude': -0.7242,
            'longitude': 36.4328,
        },
        {
            'name': 'Hell\'s Gate National Park',
            'location': 'Nakuru County, Rift Valley',
            'category': 'national_park',
            'description': 'A unique park where visitors can walk among wildlife and hike through dramatic gorges. Features geothermal hot springs and stunning geological formations. One of the few parks where visitors can explore on foot.',
            'entry_fee': 2800,
            'best_time_to_visit': 'June - October',
            'latitude': -0.5333,
            'longitude': 36.3667,
        },
        {
            'name': 'Great Rift Valley',
            'location': 'Multiple locations across Kenya',
            'category': 'other',
            'description': 'A massive geographic feature stretching over 6000 km across East Africa. Offers breathtaking landscapes, diverse flora and fauna, and numerous viewpoints. A must-see for nature enthusiasts and photographers.',
            'entry_fee': 0,
            'best_time_to_visit': 'Year-round',
            'latitude': 0.0000,
            'longitude': 36.0000,
        },
        {
            'name': 'Mombasa Old Town',
            'location': 'Mombasa, Coastal Region',
            'category': 'cultural',
            'description': 'A historic coastal settlement with Swahili architecture, narrow winding streets, and cultural heritage sites. Features Fort Jesus, ancient mosques, and traditional markets showcasing local Swahili culture.',
            'entry_fee': 1500,
            'best_time_to_visit': 'Year-round',
            'latitude': -4.0434,
            'longitude': 39.6682,
        },
        {
            'name': 'Gedi Ruins',
            'location': 'Kilifi County, Coast Region',
            'category': 'historical',
            'description': 'Ancient Swahili ruins dating back to the 12th century, hidden within a forest. Offers insights into the region\'s historical trading past and features remaining stone structures and artifacts.',
            'entry_fee': 1200,
            'best_time_to_visit': 'Year-round',
            'latitude': -3.4061,
            'longitude': 40.1406,
        },
        {
            'name': 'Thomson\'s Falls',
            'location': 'Nyeri County, Central Highlands',
            'category': 'waterfall',
            'description': 'A scenic waterfall dropping 74 meters into a pristine forested valley. Surrounded by natural vegetation and offers trekking opportunities, picnicking, and beautiful photography spots.',
            'entry_fee': 1000,
            'best_time_to_visit': 'Year-round',
            'latitude': -0.3531,
            'longitude': 36.6322,
        },
        {
            'name': 'Mombasa Marine Park',
            'location': 'Mombasa, Coastal Region',
            'category': 'wildlife',
            'description': 'A protected marine area featuring coral reefs, diverse fish species, and marine life. Popular for snorkeling, diving, and boat tours to view dolphins and sea turtles.',
            'entry_fee': 2000,
            'best_time_to_visit': 'June - September',
            'latitude': -3.9950,
            'longitude': 39.7500,
        },
    ]
    for sample in samples:
        TouristAttraction.objects.get_or_create(name=sample['name'], defaults=sample)


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0003_add_sample_beaches'),
    ]

    operations = [
        migrations.CreateModel(
            name='TouristAttraction',
            fields=[
                ('id', __import__('django.db.models', fromlist=['AutoField']).AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', __import__('django.db.models', fromlist=['CharField']).CharField(max_length=100)),
                ('location', __import__('django.db.models', fromlist=['CharField']).CharField(max_length=100)),
                ('category', __import__('django.db.models', fromlist=['CharField']).CharField(choices=[('national_park', 'National Park'), ('wildlife', 'Wildlife Reserve'), ('cultural', 'Cultural Site'), ('mountain', 'Mountain'), ('waterfall', 'Waterfall'), ('island', 'Island'), ('historical', 'Historical Site'), ('other', 'Other')], max_length=20)),
                ('description', __import__('django.db.models', fromlist=['TextField']).TextField()),
                ('entry_fee', __import__('django.db.models', fromlist=['IntegerField']).IntegerField(default=0)),
                ('best_time_to_visit', __import__('django.db.models', fromlist=['CharField']).CharField(blank=True, max_length=200)),
                ('image', __import__('django.db.models', fromlist=['ImageField']).ImageField(blank=True, null=True, upload_to='attraction_images/')),
                ('latitude', __import__('django.db.models', fromlist=['FloatField']).FloatField(blank=True, null=True)),
                ('longitude', __import__('django.db.models', fromlist=['FloatField']).FloatField(blank=True, null=True)),
                ('created_at', __import__('django.db.models', fromlist=['DateTimeField']).DateTimeField(default=__import__('django.utils.timezone', fromlist=['now']).now)),
            ],
        ),
        migrations.RunPython(create_sample_attractions),
    ]
