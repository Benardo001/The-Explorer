from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import BeachForm, BookingForm, ReviewForm, SignupForm, AttractionForm, AccommodationForm, TransportForm
from .models import Beach, Booking, Review, TouristAttraction, Accommodation, Transport


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')


@login_required
def home(request):
    query = request.GET.get('q', '')
    beaches = Beach.objects.all()
    if query:
        beaches = beaches.filter(name__icontains=query) | beaches.filter(location__icontains=query)
    return render(request, 'home.html', {'beaches': beaches, 'query': query})


@login_required
def beach_detail(request, id):
    beach = get_object_or_404(Beach, id=id)
    booking_form = BookingForm()
    review_form = ReviewForm()
    return render(request, 'beach_detail.html', {
        'beach': beach,
        'booking_form': booking_form,
        'review_form': review_form,
    })


@login_required
def create_beach(request):
    form = BeachForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Beach added successfully.')
        return redirect('home')
    return render(request, 'beach_form.html', {'form': form, 'title': 'Add Beach'})


@login_required
def update_beach(request, id):
    beach = get_object_or_404(Beach, id=id)
    form = BeachForm(request.POST or None, request.FILES or None, instance=beach)
    if form.is_valid():
        form.save()
        messages.success(request, 'Beach updated successfully.')
        return redirect('home')
    return render(request, 'beach_form.html', {'form': form, 'title': 'Edit Beach'})


@login_required
def delete_beach(request, id):
    beach = get_object_or_404(Beach, id=id)
    if request.method == 'POST':
        beach.delete()
        messages.success(request, 'Beach deleted successfully.')
        return redirect('home')
    return render(request, 'confirm_delete.html', {'beach': beach})


@login_required
def book_beach(request, id):
    beach = get_object_or_404(Beach, id=id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.beach = beach
            booking.save()
            messages.success(request, 'Booking created successfully.')
            return redirect('my_bookings')
    else:
        form = BookingForm()
    return render(request, 'book_beach.html', {'form': form, 'beach': beach})


@login_required
def add_review(request, id):
    beach = get_object_or_404(Beach, id=id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.beach = beach
            review.save()
            messages.success(request, 'Review added successfully.')
            return redirect('beach_detail', id=beach.id)
    else:
        form = ReviewForm()
    return render(request, 'review.html', {'form': form, 'beach': beach})


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).select_related('beach')
    return render(request, 'my_bookings.html', {'bookings': bookings})


@login_required
def attractions(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')
    attractions_list = TouristAttraction.objects.all()
    
    if query:
        attractions_list = attractions_list.filter(name__icontains=query) | attractions_list.filter(location__icontains=query)
    
    if category:
        attractions_list = attractions_list.filter(category=category)
    
    categories = TouristAttraction.CATEGORY_CHOICES
    return render(request, 'attractions.html', {
        'attractions': attractions_list,
        'categories': categories,
        'query': query,
        'selected_category': category,
    })


@login_required
def attraction_detail(request, id):
    attraction = get_object_or_404(TouristAttraction, id=id)
    return render(request, 'attraction_detail.html', {'attraction': attraction})


@login_required
def create_attraction(request):
    form = AttractionForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Tourist attraction added successfully.')
        return redirect('attractions')
    return render(request, 'attraction_form.html', {'form': form, 'title': 'Add Tourist Attraction'})


@login_required
def update_attraction(request, id):
    attraction = get_object_or_404(TouristAttraction, id=id)
    form = AttractionForm(request.POST or None, request.FILES or None, instance=attraction)
    if form.is_valid():
        form.save()
        messages.success(request, 'Tourist attraction updated successfully.')
        return redirect('attraction_detail', id=attraction.id)
    return render(request, 'attraction_form.html', {'form': form, 'title': 'Edit Tourist Attraction'})


@login_required
def delete_attraction(request, id):
    attraction = get_object_or_404(TouristAttraction, id=id)
    if request.method == 'POST':
        attraction.delete()
        messages.success(request, 'Tourist attraction deleted successfully.')
        return redirect('attractions')
    return render(request, 'confirm_delete.html', {'object': attraction, 'type': 'attraction'})


@login_required
def accommodations(request):
    query = request.GET.get('q', '')
    accommodation_type = request.GET.get('type', '')
    accommodations_list = Accommodation.objects.all()
    
    if query:
        accommodations_list = accommodations_list.filter(name__icontains=query) | accommodations_list.filter(location__icontains=query)
    
    if accommodation_type:
        accommodations_list = accommodations_list.filter(accommodation_type=accommodation_type)
    
    types = Accommodation.ACCOMMODATION_TYPE_CHOICES
    return render(request, 'accommodations.html', {
        'accommodations': accommodations_list,
        'types': types,
        'query': query,
        'selected_type': accommodation_type,
    })


@login_required
def accommodation_detail(request, id):
    accommodation = get_object_or_404(Accommodation, id=id)
    return render(request, 'accommodation_detail.html', {'accommodation': accommodation})


@login_required
def create_accommodation(request):
    form = AccommodationForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Accommodation added successfully.')
        return redirect('accommodations')
    return render(request, 'accommodation_form.html', {'form': form, 'title': 'Add Accommodation'})


@login_required
def update_accommodation(request, id):
    accommodation = get_object_or_404(Accommodation, id=id)
    form = AccommodationForm(request.POST or None, request.FILES or None, instance=accommodation)
    if form.is_valid():
        form.save()
        messages.success(request, 'Accommodation updated successfully.')
        return redirect('accommodation_detail', id=accommodation.id)
    return render(request, 'accommodation_form.html', {'form': form, 'title': 'Edit Accommodation'})


@login_required
def delete_accommodation(request, id):
    accommodation = get_object_or_404(Accommodation, id=id)
    if request.method == 'POST':
        accommodation.delete()
        messages.success(request, 'Accommodation deleted successfully.')
        return redirect('accommodations')
    return render(request, 'confirm_delete.html', {'object': accommodation, 'type': 'accommodation'})


@login_required
def transports(request):
    query = request.GET.get('q', '')
    transport_type = request.GET.get('type', '')
    transports_list = Transport.objects.all()

    if query:
        transports_list = transports_list.filter(name__icontains=query) | transports_list.filter(location__icontains=query)

    if transport_type:
        transports_list = transports_list.filter(transport_type=transport_type)

    types = Transport.TRANSPORT_TYPE_CHOICES
    return render(request, 'transports.html', {
        'transports': transports_list,
        'types': types,
        'query': query,
        'selected_type': transport_type,
    })


@login_required
def transport_detail(request, id):
    transport = get_object_or_404(Transport, id=id)
    return render(request, 'transport_detail.html', {'transport': transport})


@login_required
def create_transport(request):
    form = TransportForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Transport service added successfully.')
        return redirect('transports')
    return render(request, 'transport_form.html', {'form': form, 'title': 'Add Transport Service'})


@login_required
def update_transport(request, id):
    transport = get_object_or_404(Transport, id=id)
    form = TransportForm(request.POST or None, request.FILES or None, instance=transport)
    if form.is_valid():
        form.save()
        messages.success(request, 'Transport service updated successfully.')
        return redirect('transport_detail', id=transport.id)
    return render(request, 'transport_form.html', {'form': form, 'title': 'Edit Transport Service'})


@login_required
def delete_transport(request, id):
    transport = get_object_or_404(Transport, id=id)
    if request.method == 'POST':
        transport.delete()
        messages.success(request, 'Transport service deleted successfully.')
        return redirect('transports')
    return render(request, 'confirm_delete.html', {'object': transport, 'type': 'transport'})


def logout_view(request):
    logout(request)
    return redirect('login')
