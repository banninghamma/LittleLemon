from django.shortcuts import render

from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer

# Create your views here.
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all().order_by('id')
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all().order_by('id')
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by('id')
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

def index(request):
    return render(request, 'index.html', {})