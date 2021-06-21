from django.shortcuts import render,redirect
from .forms import ReviewForm
# Create your views here.
from chat.forms import MessageForm
from .models import Lesson,Category,Age,Elective
from django.views.generic import ListView, DetailView,TemplateView,View

class Categories:
    
    def get_categories(self):
        return Category.objects.all()

class Ages:
    
    def get_age(self):
        return Age.objects.all()

class HomePage(ListView):
    model = Category
    query_set = Category.objects.all()
    template_name = "index.html"

class Lessons(ListView,Categories,Ages):
    model = Lesson
    query_set = Lesson.objects.all()
    template_name = "history.html"

class LessonDetail(DetailView):
    model = Lesson
    slug_field = "url"
    template_name = "lesson_detail.html"

class FilterLessonView(ListView,Categories,Ages):
    
    template_name = "history.html"
    
    def get_queryset(self):
        if self.request.GET.getlist("category"):
            queryset = Lesson.objects.filter(category__in=self.request.GET.getlist("category"),age__in=self.request.GET.getlist("age"))
        elif self.request.GET.get("q"): 
            queryset = Lesson.objects.filter(title__icontains=self.request.GET.get("q"))
        else:
            queryset = Lesson.objects.all()
        return queryset


class AddReview(View):
    """Отзыв"""
    def post(self,request,pk):
        form = ReviewForm(request.POST)
        lesson = Lesson.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent",None):
                form.parent_id = int(request.POST.get("parent"))
            form.lesson = lesson
            form.save() 
        return redirect(lesson.get_absolute_url())

class Achivments(TemplateView):
    template_name = "achivments.html"

class SendMessage(View):
    
    def post(self,request):
        form = MessageForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save() 
            return render(request, "index.html", {'form':form})
        return render(request, "index.html", {'form':form})