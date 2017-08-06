from django.shortcuts import render
from rest_framework import viewsets
from api.models import *
from api.serializers import *
from django.utils import timezone

# Create your views here.
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()[:20]
    serializer_class = NewsSerializer

class SIGViewSet(viewsets.ModelViewSet):
    queryset = SIG.objects.filter(date__gte=timezone.now().date())
    serializer_class = SIGSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.filter(fromDateTime__gte=timezone.now())
    serializer_class = EventSerializer

class CouncilViewSet(viewsets.ModelViewSet):
    queryset = CouncilMember.objects.all()
    serializer_class = CouncilMemberSerializer