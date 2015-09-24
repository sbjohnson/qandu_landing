from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.core.urlresolvers import reverse_lazy
from .models import *

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"
    
class QuestionCreateView(CreateView):
    model = Question
    template_name = "question/question_form.html"
    fields = ['title', 'description']
    success_url = reverse_lazy('home')
    