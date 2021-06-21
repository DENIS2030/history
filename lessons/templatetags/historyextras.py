from django import template
from ..models import Gallery
from chat.models import Message
from chat.forms import MessageForm
from django.contrib.auth.models import User
register = template.Library()

@register.inclusion_tag('include/slider.html')
def slider_list():
    slider = Gallery.objects.filter(check=True)
    return{
	    'slider_list': slider
	}
@register.inclusion_tag('include/gallery.html')
def gallery_list():
    gallery = Gallery.objects.filter(check=True)
    return{
	    'gallery_list': gallery
	}

@register.inclusion_tag('messages.html')
def message_list(user):
    message = Message.objects.all()
    return{
        'message_list':message,
        'user':user
    }