from django.db import migrations


def create_more_sample_data(apps, schema_editor):
    Beach = apps.get_model('tourism', 'Beach')
    TouristAttraction = apps.get_model('tourism', 'TouristAttraction')
    Accommodation = apps.get_model('tourism', 'Accommodation')
    Transport = apps.get_model('tourism', 'Transport')

    beaches = [
        {
            'name': 'Watamu Beach',
            'location': 'Watamu, Kilifi County',
            'description': 'A protected marine area with soft white sand, crystal-clear waters, and some of the best snorkeling in Kenya.',
            'activities': 'Snorkeling, kite surfing, turtle watching, dhow sailing',
            'price': 4200,
            'latitude': -3.3497,
            'longitude': 40.0145,
        },
        {
            'name': 'Malindi Beach',
            'location': 'Malindi, Kilifi County',
            'description': 'A historic beach town with golden sands, vibrant markets, and easy access to marine national parks and coral reefs.',
            'activities': 'Swimming, marine safaris, beach dining, snorkeling',
            'price': 3900,
            'latitude': -3.2175,
            'longitude': 40.1166,
        },
        {
            'name': 'Shimoni Beach',
            'location': 'Shimoni, Kwale County',
            'description': 'A quieter, scenic beach south of Mombasa popular for fishing, boat trips, and exploring nearby caves.',
            'activities': 'Fishing, boat trips, cave tours, beach walks',
            'price': 2800,
            'latitude': -4.6358,
            'longitude': 39.2727,
        },
        {
            'name': 'Tiwi Beach',
            'location': 'Tiwi, Kwale County',
            'description': 'A beautiful, less crowded beach with limestone cliffs, natural pools, and excellent snorkeling over coral gardens.',
            'activities': 'Snorkeling, kayaking, beach picnics, bird watching',
            'price': 3500,
            'latitude': -4.5644,
            'longitude': 39.3758,
        },
    ]

    attractions = [
        {
            'name': 'Sheldrick Wildlife Trust',
            'location': 'Nairobi National Park',
            'category': 'wildlife',
            'description': 'A sanctuary dedicated to rescuing and rehabilitating orphaned elephants and rhinos. Visitors can watch feeding sessions and learn about wildlife conservation.',
            'entry_fee': 2000,
            'best_time_to_visit': 'Year-round, morning visits preferred',
            'latitude': -1.3634,
            'longitude': 36.8935,
        },
        {
            'name': 'Giraffe Centre',
            'location': 'Langata, Nairobi',
            'category': 'wildlife',
            'description': 'A conservation centre focused on the endangered Rothschild giraffe. Guests can feed giraffes by hand and tour the surrounding nature trails.',
            'entry_fee': 1250,
            'best_time_to_visit': 'Year-round',
            'latitude': -1.3660,
            'longitude': 36.7400,
        },
        {
            'name': 'Lamu Old Town',
            'location': 'Lamu Island, Lamu County',
            'category': 'cultural',
            'description': 'A UNESCO World Heritage Site with narrow alleys, ancient Swahili architecture, and a relaxed island atmosphere where people travel on foot or by donkey.',
            'entry_fee': 0,
            'best_time_to_visit': 'November - March',
            'latitude': -2.2686,
            'longitude': 40.9026,
        },
        {
            'name': 'Kakamega Forest',
            'location': 'Kakamega County',
            'category': 'other',
            'description': 'A tropical rainforest and biodiversity hotspot in western Kenya, home to rare butterflies, birds, primates, and tranquil hiking trails.',
            'entry_fee': 1200,
            'best_time_to_visit': 'May - October',
            'latitude': 0.2833,
            'longitude': 34.7500,
        },
    ]

    accommodations = [
        {
            'name': 'Watamu Beach Resort',
            'location': 'Watamu, Kilifi County',
            'accommodation_type': 'resort',
            'description': 'A beachfront resort offering family-friendly rooms, pools, and easy access to marine activities and cultural tours.',
            'price_per_night': 8500,
            'max_guests': 4,
            'amenities': 'Pool, Restaurant, WiFi, Beach access, Tour desk',
            'contact_info': '+254 700 123 456',
            'website': 'https://watamubeachresort.example.com',
            'latitude': -3.3497,
            'longitude': 40.0145,
        },
        {
            'name': 'Malindi Seaside Hotel',
            'location': 'Malindi, Kilifi County',
            'accommodation_type': 'hotel',
            'description': 'A comfortable beachfront hotel ideal for couples and families, with easy access to Malindi town and the marine park.',
            'price_per_night': 6200,
            'max_guests': 3,
            'amenities': 'Free breakfast, WiFi, Airport shuttle, Swimming pool',
            'contact_info': '+254 702 234 567',
            'website': 'https://malindiseasidehotel.example.com',
            'latitude': -3.2175,
            'longitude': 40.1166,
        },
        {
            'name': 'Shimoni Cliff Cottage',
            'location': 'Shimoni, Kwale County',
            'accommodation_type': 'cottage',
            'description': 'A secluded cliffside cottage with ocean views, perfect for a quiet coastal getaway and relaxing sunsets.',
            'price_per_night': 5400,
            'max_guests': 4,
            'amenities': 'Sea view, Kitchenette, Private terrace, Free parking',
            'contact_info': '+254 703 345 678',
            'website': 'https://shimonicottage.example.com',
            'latitude': -4.6358,
            'longitude': 39.2727,
        },
        {
            'name': 'Nairobi City Guesthouse',
            'location': 'Nairobi, Nairobi County',
            'accommodation_type': 'guesthouse',
            'description': 'A cozy guesthouse in the city offering affordable rooms, easy access to Nairobi attractions, and a friendly local experience.',
            'price_per_night': 4200,
            'max_guests': 2,
            'amenities': 'Breakfast, WiFi, Laundry service, Airport transfer',
            'contact_info': '+254 704 456 789',
            'website': 'https://nairobiguesthouse.example.com',
            'latitude': -1.2921,
            'longitude': 36.8219,
        },
    ]

    transports = [
        {
            'name': 'Watamu Shuttle Service',
            'transport_type': 'bus',
            'description': 'Daily shuttle service between Malindi, Watamu and Kilifi with comfortable seats and reliable schedules.',
            'location': 'Watamu',
            'destination': 'Malindi',
            'price_per_trip': 650,
            'price_unit': 'trip',
            'capacity': 40,
            'amenities': 'AC, WiFi, Luggage rack',
            'contact_info': '+254 711 888 999',
            'available_24_7': False,
            'latitude': -3.3497,
            'longitude': 40.0145,
        },
        {
            'name': 'Lamu Island Boat Taxi',
            'transport_type': 'boat',
            'description': 'Fast and safe boat transfers between Lamu town and surrounding islands with scenic coastal views.',
            'location': 'Lamu Island',
            'destination': 'Manda Island',
            'price_per_trip': 1200,
            'price_unit': 'trip',
            'capacity': 10,
            'amenities': 'Life jackets, Shade cover, Cold drinks',
            'contact_info': '+254 729 123 000',
            'available_24_7': False,
            'latitude': -2.2686,
            'longitude': 40.9026,
        },
        {
            'name': 'Nairobi Airport Shuttle',
            'transport_type': 'bus',
            'description': 'Regular shuttle transfers between Jomo Kenyatta International Airport and Nairobi city hotels. Comfortable buses with luggage storage.',
            'location': 'JKIA',
            'destination': 'Nairobi city',
            'price_per_trip': 1200,
            'price_unit': 'trip',
            'capacity': 40,
            'amenities': 'WiFi, Air conditioning, Luggage handling',
            'contact_info': '+254 722 234 567',
            'available_24_7': True,
            'latitude': -1.3192,
            'longitude': 36.9278,
        },
        {
            'name': 'Mombasa Train Express',
            'transport_type': 'train',
            'description': 'Scenic train service linking Nairobi and Mombasa with comfortable seating and panoramic views through the Kenyan countryside.',
            'location': 'Nairobi Terminus',
            'destination': 'Mombasa Terminus',
            'price_per_trip': 2500,
            'price_unit': 'trip',
            'capacity': 60,
            'amenities': 'Dining car, WiFi, Power outlets',
            'contact_info': '+254 733 111 222',
            'available_24_7': False,
            'latitude': -1.3230,
            'longitude': 36.8219,
        },
    ]

    for sample in beaches:
        Beach.objects.get_or_create(name=sample['name'], defaults=sample)

    for sample in attractions:
        TouristAttraction.objects.get_or_create(name=sample['name'], defaults=sample)

    for sample in accommodations:
        Accommodation.objects.get_or_create(name=sample['name'], defaults=sample)

    for sample in transports:
        Transport.objects.get_or_create(name=sample['name'], defaults=sample)


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0011_merge_20260515_1527'),
    ]

    operations = [
        migrations.RunPython(create_more_sample_data),
    ]
