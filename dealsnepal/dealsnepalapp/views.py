from django.shortcuts import render
from .models import smartphone


def homelistview(request):

    context = {
        'phoneinfo':smartphone.objects.all()
    }
    return render(request,'dealsnepalapp/home.html',context)
