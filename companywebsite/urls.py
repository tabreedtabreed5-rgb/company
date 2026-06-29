
from django.urls import path
from companywebsite.views import home, about, services, ContactView,SuccesView

urlpatterns = [

    path('', home, name='home'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('contact/', ContactView.as_view(), name='contact'),
    path("success/", SuccesView.as_view(), name="success"),
    
]
