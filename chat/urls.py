from django.urls import path


from . import views


urlpatterns =[  
    
    path("adminmessage/",views.AdminMessage.as_view(),name="adminmessage"),
    
]