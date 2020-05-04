from rest_framework import viewsets
from .serializers import MemberSerializer, ActivityPeriodSerializer
from testsapi.models import Member, ActivityPeriod
from django.http import JsonResponse


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    print(queryset)
    serializer_class = MemberSerializer


class ActivityPeriodViewSet(viewsets.ModelViewSet):
    queryset = ActivityPeriod.objects.all()
    serializer_class = ActivityPeriodSerializer

