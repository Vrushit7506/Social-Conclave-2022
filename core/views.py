from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from .models import Member, Agenda
import json
app_name = "core"


def agendas(request):
    return render(request, 'core/agendas.html')


def overTheYears(request):
    return render(request, 'core/overTheYears.html')
