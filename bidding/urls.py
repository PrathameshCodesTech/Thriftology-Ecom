from django.urls import path
from . import views

urlpatterns = [
    path('new-arrivals/', views.new_arrivals, name='new_arrivals'),
    path('place-bid/<int:new_arrival_id>/', views.place_bid, name='place_bid'),
]