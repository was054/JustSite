from django.shortcuts import render
from .models import ModelNews

from .models import Rubric
from django.views.generic.edit import CreateView
from .forms import ModelNewsForm
from django.contrib.auth.models import User
import csv
FILE='info.csv'


def index(request):
    return render(request, 'news/index.html')

def index_count(request):

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    if User.is_authenticated:
        if User.is_active:
            visits = num_visits
            pkey = request.user.pk
            users = User.objects.get(pk=pkey)
            dates = User.objects.filter(is_active=True).values('last_login').get(pk=pkey)
            emails = User.objects.filter(is_active=True).values('email').get(pk=pkey)
            info = User.objects.filter(is_active=True).values('username', 'pk', 'last_login', 'email').get(pk=pkey)
    return render(request, 'news/NewsIndex.html', context={'num_visits':num_visits,'info': info,'dates': dates,'emails': emails,'users': users,'visits':visits,'pkey':pkey})

def new(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    if User.is_authenticated:
        if User.is_active:
            visits=num_visits
            pkey = request.user.pk
            users =User.objects.get(pk=pkey)
            dates = User.objects.filter(is_active=True).values('last_login').get(pk=pkey)
            emails = User.objects.filter(is_active=True).values('email').get(pk=pkey)
            info = User.objects.filter(is_active=True).values('pk','username','last_login','email').get(pk=pkey)
            data = [[info],[visits]]
            data_all=data
            data_all.append(data)
            with open('info.csv','a') as f:
                writer =csv.writer(f)
                for row in data_all:
                    writer.writerow(row)

    bbs = ModelNews.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics,'num_visits': num_visits,'info': info,'dates': dates,'emails': emails,'users': users,'visits':visits,'pkey':pkey}
    return render(request, 'news/NewsIndex.html', context)

def by_rubric(request,rubric_id):
    bbs = ModelNews.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'news/by_rubric.html', context)

class ModelNewsCreateView(CreateView):
    template_name = 'news/create.html'
    form_class = ModelNewsForm
    success_url = '/news/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

