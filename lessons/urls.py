from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('lessons/', views.Lessons.as_view(), name='lessons'),
    path('achivments/', views.Achivments.as_view(), name='achivments'),
    path("sendmessage/",views.SendMessage.as_view(),name="sendmessage"),
    path('filter/', views.FilterLessonView.as_view(), name='filter'),
    path("<slug:slug>/",views.LessonDetail.as_view(),name="lesson_detail"),
    path("review/<int:pk>/",views.AddReview.as_view(),name="add_review"),
]
