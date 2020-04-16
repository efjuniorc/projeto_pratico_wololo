from django.contrib import admin

# Register your models here.
from core.models import *

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('pk', 'url_encurtado', 'contador')
    search_fields = ('pk','url_encurtado',)
    list_filter = ['url_encurtado', ]
