from django.shortcuts import render
from .models import smartphone


def homelistview(request):
    phoneinfoall = [1, 2, 3, 4]
    context = {
        'phoneinfo':phoneinfoall
    }
    return render(request,'dealsnepalapp/home.html')