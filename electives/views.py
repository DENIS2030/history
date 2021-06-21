from django.shortcuts import render
from lessons.models import Elective,Gallery
# Create your views here.
from django.views.generic import ListView, DetailView,TemplateView,CreateView
from .forms import GalleryForm
from django.urls import reverse_lazy


class ElectiveView(ListView):
    model = Elective
    queryset = Elective.objects.all()
    template_name = "elective_list.html"

class ElectiveDetail(DetailView):
    model = Elective
    template_name = "elective_detail.html"
    slug_field = "url"


class GalleryCreateView(CreateView):
    model = Gallery
    form_class = GalleryForm
    template_name = "upload_file.html"
    success_url = reverse_lazy('home')





