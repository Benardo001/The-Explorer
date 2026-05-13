from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import BeachForm, BookingForm, ReviewForm, SignupForm
from .models import Beach, Booking, Review


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


def logout_view(request):
    logout(request)
    return redirect('login')
