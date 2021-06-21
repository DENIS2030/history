from django.contrib import admin

# Register your models here.
from .models import Category, Age, Lesson, Pharagraph, AdditionalInfo, Books, PharagraphImage, AdditionalInfo, LearnApps, Elective, Gallery, Reviews,ElectiveCategory,Multimedia

admin.site.register(Category)
admin.site.register(Age)
admin.site.register(Lesson)
admin.site.register(Pharagraph)
admin.site.register(AdditionalInfo)
admin.site.register(Books)
admin.site.register(PharagraphImage)
admin.site.register(LearnApps)
admin.site.register(Elective)
admin.site.register(Gallery)
admin.site.register(Reviews)
admin.site.register(ElectiveCategory)
admin.site.register(Multimedia)
