from django.shortcuts import render

from app01 import models
from app01.utils.pagination import Pagination


def index(request):
    return render(request, 'index.html')
