from django.shortcuts import render
from django.views.generic import ListView, DetailView,TemplateView,View
from django.contrib.auth.models import User
from .models import Message
# Create your views here.



class AdminMessage(ListView):

    model = User
    queryset = User.objects.all()
    template_name = "adminchat.html"

    def get_context_data(self, **kwards):
        context = super(AdminMessage, self).get_context_data(**kwards)
        context['message'] = Message.objects.all()
        #context['Category'] = CategoryLesson.objects.all()
        return context