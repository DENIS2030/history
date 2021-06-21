from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Message(models.Model):
    
    message = models.TextField(verbose_name="Текст сообщения")
    fromuser = models.ForeignKey(User,on_delete=models.CASCADE,related_name = "ffromuser")
    touser = models.ForeignKey(User,on_delete=models.CASCADE,related_name="ttouser")
    date = models.DateField(auto_now_add=True,verbose_name="Дата сообщения")

    def __str__(self):
        return "От " + self.fromuser.username + " к " + self.touser.username
    
    class Meta:
        verbose_name="Сообщение"
        verbose_name_plural = "Сообщения"