from django.contrib import admin
from .models import Maincont

class MaincontAdmin(admin.ModelAdmin):
    search_fields = ['subject'] #제목으로 검색 하기

admin.site.register(Maincont, MaincontAdmin)

# Register your models here.
