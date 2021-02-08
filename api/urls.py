from django.urls import path
from . import views

urlpatterns=[
    path('home/<int:id>',views.homeView,name="Home"),
    path('flynovoair',views.flynovoairData),
    path('usbair',views.usbairData),
    path('birman',views.birmanData),
    path('allAirlines',views.getAllData)
]