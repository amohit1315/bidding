from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate


def index(request):
    return render(request, "landingpage.html")