from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    # return HttpResponse('salam kora salam :) ')
    return render(request , 'about.html')

def home(request):
    # return HttpResponse('salam inja home hast :) ')
    return render(request , 'home.html')
