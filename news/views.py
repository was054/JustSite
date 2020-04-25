from django.shortcuts import render
from .models import ModelNews

from .models import Rubric
from django.views.generic.edit import CreateView
from .forms import ModelNewsForm
from django.contrib.auth.models import User



def index(request):
    return render(request, 'news/index.html')

def index_count(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    if User.is_active:
        if User.is_authenticated:
            dates = User.objects.values_list('pk','email')
            users = User.objects.filter(is_active=True).exclude(email='')
            emails = User.objects.filter(is_active=True).exclude(email='').values_list('email', flat=True)
    return render(request, 'news/NewsIndex.html', context={'num_visits': num_visits,'dates': dates,'emails': emails,'users': users})

def new(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    if User.is_authenticated:
        if User.is_active:
            visits=num_visits
            users =User.objects.get(pk=3)
            dates = User.objects.filter(is_active=True).values('last_login').get(pk=3)
            emails = User.objects.filter(is_active=True).values('email').get(pk=3)
            info = User.objects.filter(is_active=True).values('username','pk','last_login','email').get(pk=3)



    bbs = ModelNews.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics,'num_visits':num_visits,'info': info,'dates': dates,'emails': emails,'users': users,'visits':visits}
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

