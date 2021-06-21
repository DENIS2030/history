from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.GalleryCreateView.as_view(), name='add_post'),
    path('electives/', views.ElectiveView.as_view(), name='electives'),
    path("<slug:slug>/",views.ElectiveDetail.as_view(),name="elective_detail"),
    
]