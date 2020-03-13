from django.urls import path
from .views import SingleOfertaView, OfertyView
from kariera import views

urlpatterns = [
    path('oferta/<int:pk>', SingleOfertaView.as_view(), name='oferta'),
    path('oferty', OfertyView.as_view(), name='oferty'),

]