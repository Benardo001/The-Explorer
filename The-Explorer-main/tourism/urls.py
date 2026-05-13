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
]