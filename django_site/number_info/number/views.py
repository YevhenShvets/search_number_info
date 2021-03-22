from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import F
from django.db.models import Max, Count
from .models import *


def index(request):
    context = {}
    last_view = NumberActivity.objects.order_by('-last_view_date')[:10]
    popular_view = NumberActivity.objects.order_by('-views')[:10]
    popular_comments = Comment.objects.values('id_number__number').annotate(total=Count('id_number')).order_by('-total')

    context['last_view'] = last_view
    context['popular_view'] = popular_view
    context['popular_comments'] = popular_comments
    return render(request, 'number/index.html', context=context)


def search_form(request):
    phone_number = request.POST['number']
    if len(phone_number) > 0:
        return redirect('search_number', phone_number)
    else:
        return redirect('index')


def search(request, number):
    context = {}

    phone_number = number
    if len(phone_number) > 0:
        number = NumberActivity.objects.filter(id_number__number=phone_number).first()
        comments = Comment.objects.filter(id_number=number.id_number)
        context['number'] = number
        context['comments'] = comments

    return render(request, 'number/index.html', context=context)