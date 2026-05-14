from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('create/', views.create_beach, name='create_beach'),
    path('update/<int:id>/', views.update_beach, name='update_beach'),
    path('delete/<int:id>/', views.delete_beach, name='delete_beach'),
    path('beach/<int:id>/', views.beach_detail, name='beach_detail'),
    path('book/<int:id>/', views.book_beach, name='book_beach'),
    path('review/<int:id>/', views.add_review, name='add_review'),
    path('bookings/', views.my_bookings, name='my_bookings'),
    path('attractions/', views.attractions, name='attractions'),
    path('attraction/<int:id>/', views.attraction_detail, name='attraction_detail'),
    path('attraction/create/', views.create_attraction, name='create_attraction'),
    path('attraction/update/<int:id>/', views.update_attraction, name='update_attraction'),
    path('attraction/delete/<int:id>/', views.delete_attraction, name='delete_attraction'),
    path('accommodations/', views.accommodations, name='accommodations'),
    path('accommodation/<int:id>/', views.accommodation_detail, name='accommodation_detail'),
    path('accommodation/create/', views.create_accommodation, name='create_accommodation'),
    path('accommodation/update/<int:id>/', views.update_accommodation, name='update_accommodation'),
    path('accommodation/delete/<int:id>/', views.delete_accommodation, name='delete_accommodation'),
]