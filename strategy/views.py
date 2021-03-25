import logging
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from strategy.serializers import *
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from strategy.permissions import IsOwnerOrReadOnly
# Create your views here.
logging = logging.getLogger('message')


class ReceptorViewSet(viewsets.ModelViewSet):

    queryset = Receptor.objects.all()
    serializer_class = ReceptorSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly,)


class RelationViewSet(viewsets.ModelViewSet):
    queryset = Relation.objects.all()
    serializer_class = RelationSerializer


class StrategyViewSet(viewsets.ModelViewSet):
    queryset = Strategy.objects.all()
    serializer_class = StrategySerializer


class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer


def vue_practise(request):

    return render(request, 'temp_one.html')


def test(request):
    return render(request, 'index.html')



def two(request):
    return render(request, 'temp_one.html')
